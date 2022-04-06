### gates

# a2b
gate_a2b = "bcirc->PutY2BGate(ycirc->PutA2YGate(s_main_f0_lex0_a_v0))"

# a2y
gate_a2y = "ycirc->PutA2YGate(s_main_f0_lex0_a_v0)"

# add
gate_add = "CIRC->PutADDGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# and
gate_and = "CIRC->PutANDGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# b2a
gate_b2a = "acirc->PutB2AGate(s_main_f0_lex0_a_v0)"

# b2y
gate_b2y = "ycirc->PutB2YGate(s_main_f0_lex0_a_v0)"

# div
gate_div = "signeddivbl(CIRC, s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# eq
gate_eq = "CIRC->PutXORGate(CIRC->PutXORGate(CIRC->PutGTGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0), CIRC->PutGTGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)), CIRC->PutCONSGate((uint64_t)1, (uint32_t)1));"

# ge
gate_ge = "((BooleanCircuit *)CIRC)->PutINVGate(CIRC->PutGTGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0))"

# gt
gate_gt = "CIRC->PutGTGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# le
gate_le = "((BooleanCircuit *)CIRC)->PutINVGate(CIRC->PutGTGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0))"

# lt
gate_lt = "CIRC->PutGTGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)"

# mul
gate_mul = "CIRC->PutMULGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# mux
gate_mux = "CIRC->PutMUXGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)"

# ne
gate_ne = "((BooleanCircuit *)CIRC)->PutINVGate(CIRC->PutXORGate(CIRC->PutXORGate(CIRC->PutGTGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0), CIRC->PutGTGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)), CIRC->PutCONSGate((uint64_t)1, (uint32_t)1)))"

# or
gate_or = "((BooleanCircuit *) CIRC)->PutORGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# rem
gate_rem = "signedmodbl(CIRC, s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# shl
# shr


# sub
gate_sub = "CIRC->PutSUBGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)"

# xor
gate_xor = "((BooleanCircuit *) CIRC)->PutXORGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0)"

# y2a
gate_y2a = "acirc->PutB2AGate(bcirc->PutY2BGate(ss))"

# y2b
gate_y2b = "bcirc->PutY2BGate(ss)"

gate_yao_preset = "share* ss = ycirc->PutA2YGate(s_main_f0_lex0_a_v0);\n"

gate_collection = {
	"a2b": gate_a2b,
	"a2y": gate_a2y,
	"add": gate_add,
	"and": gate_and,
	"b2a": gate_b2a,
	"b2y": gate_b2y,
	"div": gate_div,
	"eq": gate_eq,
	"ge": gate_ge,
	"gt": gate_gt,
	"le": gate_le,
	"lt": gate_lt,
	"mul": gate_mul,
	"mux": gate_mux,
	"ne": gate_ne,
	"or": gate_or,
	"rem": gate_rem,
	"sub": gate_sub,
	"xor": gate_xor,
	"y2a": gate_y2a,
	"y2b": gate_y2b,
}

gate_conv = ["a2b", "a2y", "b2a", "b2y", "y2a", "y2b"]

## common/.h
commmon_h_include = \
"""#include "../../../../../../abycore/circuit/booleancircuits.h"
#include "../../../../../../abycore/circuit/arithmeticcircuits.h"
#include "../../../../../../abycore/circuit/circuit.h"
#include "../../../../../../abycore/aby/abyparty.h"
#include <math.h>
#include <cassert>
#include <chrono>

using namespace std::chrono;
"""

common_h_func_prev = "int32_t test_"

common_h_func_succ = \
"""_circuit(std::map<std::string, std::string> params, e_role role, const std::string& address, 
		uint16_t port, seclvl seclvl, uint32_t bitlen, uint32_t nthreads, e_mt_gen_alg mt_alg, e_sharing sharing);"""


def get_common_h(test_name):
    return commmon_h_include + \
            common_h_func_prev + \
            test_name + \
            common_h_func_succ

## common/.cpp
common_cpp_include = \
"""#include "PLACEHOLDER.h"
#include "../../../../../../abycore/circuit/booleancircuits.h"
#include "../../../../../../abycore/circuit/arithmeticcircuits.h"
#include "../../../../../../abycore/circuit/circuit.h"
#include "../../../../../../../EZPC/ezpc.h"

#include "../../../../../../abycore/sharing/sharing.h"
"""

common_cpp_func_prev = "int32_t test_"

common_cpp_cun_succ = """_circuit(std::map<std::string, std::string> params, e_role role, const std::string& address, 
	uint16_t port, seclvl seclvl, uint32_t bitlen, uint32_t nthreads, e_mt_gen_alg mt_alg, e_sharing sharing) {"""

common_cpp_setup_compile = \
"""	// setup
	ABYParty* party = new ABYParty(role, address, port, seclvl, bitlen, nthreads, mt_alg);
	std::vector<Sharing*>& sharings = party->GetSharings();
	Circuit* acirc = sharings[S_ARITH]->GetCircuitBuildRoutine();
	Circuit* bcirc = sharings[S_BOOL]->GetCircuitBuildRoutine();
	Circuit* ycirc = sharings[S_YAO]->GetCircuitBuildRoutine();
	output_queue out_q;
	
	// compiled circuit
	uint32_t main_f0_lex0_a_v0 = std::atoi(params["a"].c_str());
share* s_main_f0_lex0_a_v0;
uint32_t main_f0_lex0_b_v0 = std::atoi(params["b"].c_str());
share* s_main_f0_lex0_b_v0;
"""

common_cpp_server_original = \
"""if (role == SERVER) {
	s_main_f0_lex0_a_v0 = CIRC->PutINGate(main_f0_lex0_a_v0, bitlen, SERVER);
	s_main_f0_lex0_b_v0 = CIRC->PutDummyINGate(bitlen);
}
if (role == CLIENT) {
	s_main_f0_lex0_b_v0 = CIRC->PutINGate(main_f0_lex0_b_v0, bitlen, CLIENT);
	s_main_f0_lex0_a_v0 = CIRC->PutDummyINGate(bitlen);
}
"""

common_cpp_end = \
"""
	high_resolution_clock::time_point start_exec_time = high_resolution_clock::now();
	party->ExecCircuit();
	high_resolution_clock::time_point end_exec_time = high_resolution_clock::now();
	duration<double> exec_time = duration_cast<duration<double>>(end_exec_time - start_exec_time);
	std::cout << "LOG: " << (role == SERVER ? "Server exec time: " : "Client exec time: ") << exec_time.count() << std::endl;
	flush_output_queue(out_q, role, bitlen);
	return 0;
}
"""

gate_circ = {
	"a": "acirc",
	"b": "bcirc",
	"y": "ycirc",
	"c": "",
}

def get_common_cpp_compute(test_name, count, gate_type):
	output = ""
	for i in range(count):
		output += "share* s_" + \
					str(i) + \
					" = " + \
					gate_collection[gate_type] + \
					";\n"

	output += "add_to_output_queue(out_q, CIRC->PutOUTGate(s_" + str(count - 1) + ", ALL), role, std::cout);\n"
	return output



def get_common_cpp(test_name, count, gate_type, aby):
	if gate_type in gate_conv:
		if gate_type == "a2b":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "acirc") + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "bcirc") + \
				common_cpp_end
		if gate_type == "a2y":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "acirc") + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "ycirc") + \
				common_cpp_end
		if gate_type == "b2a":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "bcirc") + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "acirc") + \
				common_cpp_end
		if gate_type == "b2y":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "bcirc") + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "ycirc") + \
				common_cpp_end
		if gate_type == "y2a":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "acirc") + \
				gate_yao_preset + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "acirc") + \
				common_cpp_end
		if gate_type == "y2b":
			output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original.replace("CIRC", "acirc") + \
				gate_yao_preset + \
				get_common_cpp_compute(test_name, count, gate_type).replace("CIRC", "bcirc") + \
				common_cpp_end
		return output
	else:
		circ = gate_circ[aby]
		output =  common_cpp_include.replace("PLACEHOLDER", test_name) + \
				common_cpp_func_prev + \
				test_name + \
				common_cpp_cun_succ + \
				common_cpp_setup_compile + \
				common_cpp_server_original + \
				get_common_cpp_compute(test_name, count, gate_type) + \
				common_cpp_end

		return output.replace("CIRC", circ)


## CMakeList.txt
def get_cmake_list(test_name):
    return "add_executable(" + \
            test_name + \
            "_test " + \
            test_name + \
            "_test.cpp common/" + \
			test_name + \
            ".cpp)\n" + \
            "target_link_libraries(" + \
            test_name + \
            "_test ABY::aby ENCRYPTO_utils::encrypto_utils)\n"


## .cpp
cpp_template = \
"""#include <stdio.h>
#include <ctype.h>

#include <ENCRYPTO_utils/crypto/crypto.h>
#include <ENCRYPTO_utils/parse_options.h>

#include "../../../../../abycore/aby/abyparty.h"

#include "common/PLACEHOLDER.h"

int32_t read_test_options(int32_t* argcp, char*** argvp, e_role* role,
		uint32_t* bitlen, uint32_t* nvals, uint32_t* secparam, std::string* address,
		uint16_t* port, int32_t* test_op, std::string* parameters) {

	uint32_t int_role = 0, int_port = 0;

	parsing_ctx options[] =
			{ { (void*) &int_role, T_NUM, "r", "Role: 0/1", true, false }, {
			        (void*) parameters, T_PARAMETERS, "i", 
					"MPC Parameters", true, false }, {
					(void*) nvals, T_NUM, "n",
					"Number of parallel operation elements", false, false }, {
					(void*) bitlen, T_NUM, "b", "Bit-length, default 32", false,
					false }, { (void*) secparam, T_NUM, "s",
					"Symmetric Security Bits, default: 128", false, false }, {
					(void*) address, T_STR, "a",
					"IP-address, default: localhost", false, false }, {
					(void*) &int_port, T_NUM, "p", "Port, default: 7766", false,
					false }, { (void*) test_op, T_NUM, "t",
					"Single test (leave out for all operations), default: off",
					false, false } };

	if (!parse_options(argcp, argvp, options,
			sizeof(options) / sizeof(parsing_ctx))) {
		print_usage(*argvp[0], options, sizeof(options) / sizeof(parsing_ctx));
		std::cout << "Exiting" << std::endl;
		exit(0);
	}

	assert(int_role < 2);
	*role = (e_role) int_role;

	if (int_port != 0) {
		assert(int_port < 1 << (sizeof(uint16_t) * 8));
		*port = (uint16_t) int_port;
	}

	return 1;
}

std::map<std::string, std::string> parameters_to_map(std::string s, std::string del = ",") {
	std::vector<std::string> v = {};
	int start = 0;
    int end = s.find(del);
    while (end != -1) {
        v.push_back(s.substr(start, end - start));
        start = end + del.size();
        end = s.find(del, start);
    }
    v.push_back(s.substr(start, end - start));

	// TODO: this input parameter map does not support strings since it 
	// uses strings as parameter keys
	
	std::map<std::string, std::string> m;
	int idx = 0;
	std::string base_key = "";
	for (int i = 0; i < v.size(); i++) {
		if (!isdigit(*v[i].c_str())) {
			idx = 0;
			base_key = v[i];
		} else {
			std::string key = "";
			if (i+1 < v.size()) {
				if (idx == 0 && !isdigit(*v[i+1].c_str())) {
					key = base_key;
				}
				else {
					key = base_key + '_' + std::to_string(idx);
					idx++;
				}
			} else if (idx > 0) {
				key = base_key + '_' + std::to_string(idx);
			} else {
				key = base_key;
			}
			m[key] = v[i];
		}
	}
	return m;
}


int main(int argc, char** argv) {

	e_role role;
	uint32_t bitlen = 32, nvals = 31, secparam = 128, nthreads = 1;
	uint16_t port = 7766;
	std::string address = "127.0.0.1";
	int32_t test_op = -1;
	e_mt_gen_alg mt_alg = MT_OT;
	std::string parameters = "";

	read_test_options(&argc, &argv, &role, &bitlen, &nvals, &secparam, &address,
			&port, &test_op, &parameters);

	seclvl seclvl = get_sec_lvl(secparam);

	std::map<std::string, std::string> params = parameters_to_map(parameters, ",");

	test_PLACEHOLDER_circuit(params, role, address, port, seclvl, 32,
			nthreads, mt_alg, S_BOOL);

	return 0;
}

"""

def get_cpp(test_name):
    return cpp_template.replace("PLACEHOLDER", test_name)