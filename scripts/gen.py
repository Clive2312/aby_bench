#!/usr/bin/env python3

import os
from aby_skeleton import *
from utils import run_tests
import argparse

aby_dir = "./third_party/ABY/"

target_dir = "./third_party/ABY/src/examples/ABY_AUTO_GEN"

bin_dir = "./third_party/ABY/build/bin/"

# counts = [1, 11, 101, 1001, 10001, 100001, 1000001]

# counts = [1, 11, 101, 1001, 2001, 3001, 4001, 5001, 6001, 7001, 8001, 9001, 10001]

# counts = [1, 10001]

counts = [1, 101]

test_cases = [
    # [
    #     "add",
    #     counts,
    #     ["a", "b", "y"],
    #     3,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 2},
    # ],
    # [
    #     "and",
    #     counts,
    #     ["b", "y"],
    #     0,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 1},
    # ],
    # [
    #     "eq",
    #     counts,
    #     ["b", "y"],
    #     1,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "ne",
    #     counts,
    #     ["b", "y"],
    #     0,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "ge",
    #     counts,
    #     ["b", "y"],
    #     1,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "gt",
    #     counts,
    #     ["b", "y"],
    #     0,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "le",
    #     counts,
    #     ["b", "y"],
    #     1,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "lt",
    #     counts,
    #     ["b", "y"],
    #     0,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "mul",
    #     counts,
    #     ["a", "y"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 1},
    # ],
    # [
    #     "mux",
    #     counts,
    #     ["b", "y"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 1},
    # ],
    # [
    #     "or",
    #     counts,
    #     ["b", "y"],
    #     1,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 1},
    # ],
    # [
    #     "xor",
    #     counts,
    #     ["b", "y"],
    #     0,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 1},
    # ],
    # [
    #     "sub",
    #     counts,
    #     ["a", "b", "y"],
    #     0,
    #     {"a": 0, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "a2b",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "a2y",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "b2a",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "b2y",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "y2a",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    # [
    #     "y2b",
    #     counts,
    #     ["c"],
    #     1,
    #     {"a": 1, "b": 0},
    #     {"a": 0, "b": 0},
    # ],
    [
        "div",
        counts,
        ["b", "y"],
        1,
        {"a": 1, "b": 0},
        {"a": 0, "b": 1},
    ],
    [
        "rem",
        counts,
        ["b", "y"],
        0,
        {"a": 1, "b": 0},
        {"a": 0, "b": 1},
    ]
]

def create_dirs(path):
    if not os.path.exists(path):
        os.makedirs(path)

def gen_aby_program():
    for case in test_cases:
        op = case[0]
        for t in case[2]:
            for count in case[1]:
                test_name = "auto_cost_" + op + "_" + t + "_" + str(count) + "_c"
                path = os.path.join(target_dir, op, t, test_name)
                common_path = os.path.join(path, "common")
                create_dirs(common_path)
                print("add_subdirectory(" + os.path.join("ABY_AUTO_GEN", op, t, test_name) + ")")
                # common_h
                with open(os.path.join(common_path, test_name + ".cpp"), "w") as f:
                    f.write(get_common_cpp(test_name, count, op, t))

                # common_cpp
                with open(os.path.join(common_path, test_name + ".h"), "w") as f:
                    f.write(get_common_h(test_name))
                    

                # makefile
                with open(os.path.join(path, "CMakeLists.txt"), "w") as f:
                    f.write(get_cmake_list(test_name))

                # cpp
                with open(os.path.join(path, test_name + "_test.cpp"), "w") as f:
                    f.write(get_cpp(test_name))

def gen_test_suite():
    test_suite = []
    for case in test_cases:
        op = case[0]
        for gate_type in case[2]:
            for count in case[1]:
                test_suite.append(
                    [
                        "auto_cost_" + op + "_" + gate_type + "_" + str(count),
                        case[3],
                        bin_dir + "auto_cost_" + op + "_" + gate_type + "_" + str(count),
                        case[4],
                        case[5],
                    ]
                )
    return test_suite



if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-g", "--generate", action="store_true", help="generate all test cases")
    parser.add_argument("-test", "--test", action="store_true", help="run test")
    args = parser.parse_args()

    if args.generate:
        gen_aby_program()
    if args.test:
        test_suite = gen_test_suite()
        print(test_suite)
        run_tests('c', test_suite)