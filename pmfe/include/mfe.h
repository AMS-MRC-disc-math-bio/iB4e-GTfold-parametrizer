#ifndef _MFE_MAIN_H_
#define _MFE_MAIN_H_

#include "pmfe_types.h"
#include <gmpxx.h>

namespace pmfe{
    ScoreVector mfe(std::string seq_file, std::string output_file, ParameterVector params, std::string param_dir = "Turner99", int dangle_model = 1);
    ScoreVector mfe(std::string seq_file, std::string output_file, std::string param_dir = "Turner99", int dangle_model = 1);

    ScoreVector mfe_pywrap(std::string seq_file, std::string output_file, ParameterVector params, std::string param_dir = "Turner99", int dangle_model = 1);

    void init_fold(const char* seq, ParameterVector params);
    void free_fold(int len);
}

#endif