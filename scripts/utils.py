from subprocess import Popen, PIPE
import sys
from typing import List
import time 

def init_progress_bar(toolbar_width=40):
    ''' Initialize progress bar '''
    print("Running ABY unit tests")
    sys.stdout.write("[%s]" % ("." * toolbar_width))
    sys.stdout.flush()
    sys.stdout.write("\b" * (toolbar_width+1)) 

def update_progress_bar():
    ''' Increment progress bar '''
    sys.stdout.write("#")
    sys.stdout.flush()

def end_progress_bar():
    ''' Close progress bar '''
    sys.stdout.write("]\n") # this ends the progress bar

def flatten_args(args: dict) -> list:
    ''' Flatten dictionary into list '''
    flat_args = []
    for k, v in args.items():
        flat_args.append(str(k))
        if type(v) == list:
            flat_args += [str(x) for x in v]
        else:
            flat_args.append(str(v))
    return flat_args

def update_path(path: str, lang: str) -> str:
    '''Append path with language type'''
    return f'{path}_{lang}_test'

def build_server_cmd(exec: str, args: dict) -> List[str]:
    return [exec, "-r", "0", "-i"] + flatten_args(args)

def build_client_cmd(exec: str, args: dict) -> List[str]:
    return [exec, "-r", "1", "-i"] + flatten_args(args)

def run_test(desc: str, expected: str, server_cmd: List[str], client_cmd: List[str]) -> bool:
    assert len(server_cmd) > 3, "server cmd does not have enough arguments"
    assert len(client_cmd) > 3, "client cmd does not have enough arguments"

    assert server_cmd[0] == client_cmd[0], "server and client do not have the same cmd: " + server_cmd[0] + ", " + client_cmd[0]
    
    try:
        # start_time = time.time()
        server_proc = Popen(server_cmd, stdout=PIPE, stderr=PIPE)
        client_proc = Popen(client_cmd, stdout=PIPE, stderr=PIPE)

        server_out, server_err = server_proc.communicate(timeout=300)
        # end_time = time.time()
        client_out, client_err = client_proc.communicate(timeout=300)
        # duration = end_time - start_time

        assert not server_err, "server cmd has an error"
        assert not client_err, "client cmd has an error"

        server_out = server_out.decode('utf-8').strip()
        client_out = client_out.decode('utf-8').strip()

        sout_split = server_out.split()
        cout_split = client_out.split()

        s_exec = float(sout_split[4])
        c_exec = float(cout_split[4])

        s_ret =  sout_split[5]
        c_ret =  cout_split[5]

        duration = (s_exec + c_exec) / 2

        assert s_ret == c_ret, "server out != client out\nserver_out: "+server_out+"\nclient_out: "+client_out
        assert s_ret == expected, "server_out: "+server_out+"\nexpected: "+expected
        return True, duration
    except Exception as e:
        print("Exception: ", e)
        return False, e

def run_tests(lang: str, tests: List[dict]):
    '''
    tests will be a list of all tests to run. each element in the list will be 
    1. description of test case: string
    2. expected output: string
    3. executable path: string
    4. server arguments: dict[name] = value
    5. client arguments: dict[name] = value
    '''
    print("Running tests for frontend", lang)
    failed_test_descs = []
    cost_record = {}
    num_retries = 10
    progress_inc = 5
    init_progress_bar(len(tests) // progress_inc + 1)
    for t, test in enumerate(tests):
        print(test)
        assert len(test) == 5, "test configurations are wrong for test: "+test[0]
        desc = test[0]
        expected = str(test[1])
        path = update_path(test[2], lang)
        server_cmd = build_server_cmd(path, test[3])
        client_cmd = build_client_cmd(path, test[4])

        test_results = []
        for i in range(num_retries):
            test_results.append(run_test(desc, expected, server_cmd, client_cmd))

        count = 0
        cost = 0

        for success, duration in test_results:
            if success:
                count += 1
                cost += duration
        if count == 0:
            cost = 0
        else:
            cost  = cost*1.0/count

        cost_record[test[0]] = cost
        
        if all([not r[0] for r in test_results]):
            failed_test_descs += [(desc, e[1]) for e in test_results]

        if t % progress_inc == 0:
            update_progress_bar()
        print(cost_record)
    end_progress_bar()
    
    if len(failed_test_descs) == 0:
        print("All tests passed ✅")

    failed_test_descs = [f"{r}:\n{e}" for r, e in failed_test_descs]

    assert len(failed_test_descs) == 0, "there were failed test cases:\n======\n" + "\n\n".join(failed_test_descs)

    # print(cost_record)
    return cost_record