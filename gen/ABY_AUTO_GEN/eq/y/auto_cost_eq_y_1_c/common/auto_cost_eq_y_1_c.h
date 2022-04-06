#include "../../../../../../abycore/circuit/booleancircuits.h"
#include "../../../../../../abycore/circuit/arithmeticcircuits.h"
#include "../../../../../../abycore/circuit/circuit.h"
#include "../../../../../../abycore/aby/abyparty.h"
#include <math.h>
#include <cassert>
#include <chrono>

using namespace std::chrono;
int32_t test_auto_cost_eq_y_1_c_circuit(std::map<std::string, std::string> params, e_role role, const std::string& address, 
		uint16_t port, seclvl seclvl, uint32_t bitlen, uint32_t nthreads, e_mt_gen_alg mt_alg, e_sharing sharing);