#include "auto_cost_ne_b_1_c.h"
#include "../../../../../../abycore/circuit/booleancircuits.h"
#include "../../../../../../abycore/circuit/arithmeticcircuits.h"
#include "../../../../../../abycore/circuit/circuit.h"
#include "../../../../../../../EZPC/ezpc.h"

#include "../../../../../../abycore/sharing/sharing.h"
int32_t test_auto_cost_ne_b_1_c_circuit(std::map<std::string, std::string> params, e_role role, const std::string& address, 
	uint16_t port, seclvl seclvl, uint32_t bitlen, uint32_t nthreads, e_mt_gen_alg mt_alg, e_sharing sharing) {	// setup
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
if (role == SERVER) {
	s_main_f0_lex0_a_v0 = bcirc->PutINGate(main_f0_lex0_a_v0, bitlen, SERVER);
	s_main_f0_lex0_b_v0 = bcirc->PutDummyINGate(bitlen);
}
if (role == CLIENT) {
	s_main_f0_lex0_b_v0 = bcirc->PutINGate(main_f0_lex0_b_v0, bitlen, CLIENT);
	s_main_f0_lex0_a_v0 = bcirc->PutDummyINGate(bitlen);
}
share* s_0 = ((BooleanCircuit *)bcirc)->PutINVGate(bcirc->PutXORGate(bcirc->PutXORGate(bcirc->PutGTGate(s_main_f0_lex0_a_v0, s_main_f0_lex0_b_v0), bcirc->PutGTGate(s_main_f0_lex0_b_v0, s_main_f0_lex0_a_v0)), bcirc->PutCONSGate((uint64_t)1, (uint32_t)1)));
add_to_output_queue(out_q, bcirc->PutOUTGate(s_0, ALL), role, std::cout);

	high_resolution_clock::time_point start_exec_time = high_resolution_clock::now();
	party->ExecCircuit();
	high_resolution_clock::time_point end_exec_time = high_resolution_clock::now();
	duration<double> exec_time = duration_cast<duration<double>>(end_exec_time - start_exec_time);
	std::cout << "LOG: " << (role == SERVER ? "Server exec time: " : "Client exec time: ") << exec_time.count() << std::endl;
	flush_output_queue(out_q, role, bitlen);
	return 0;
}
