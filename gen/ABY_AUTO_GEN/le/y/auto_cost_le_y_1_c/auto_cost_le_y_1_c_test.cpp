#include <stdio.h>
#include <ctype.h>

#include <ENCRYPTO_utils/crypto/crypto.h>
#include <ENCRYPTO_utils/parse_options.h>

#include "../../../../../abycore/aby/abyparty.h"

#include "common/auto_cost_le_y_1_c.h"

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

	test_auto_cost_le_y_1_c_circuit(params, role, address, port, seclvl, 32,
			nthreads, mt_alg, S_BOOL);

	return 0;
}

