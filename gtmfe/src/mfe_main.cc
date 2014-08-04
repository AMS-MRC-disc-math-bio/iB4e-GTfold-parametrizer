/*
 GTfold: compute minimum free energy of RNA secondary structure
 Copyright (C) 2007-2011  David A. Bader, Christine E. Heitsch, 
 and Steve C. Harvey
 http://www.cc.gatech.edu/~bader

 This program is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.

 This program is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.

 You should have received a copy of the GNU General Public License
 along with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
#include <math.h>
#include <sstream>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cassert>

#include "main.h"
#include "mfe_main.h"
#include "utils.h"
#include "loader.h"
//#include "options.h"
#include "global.h"
#include "energy.h"
#include "algorithms.h"
#include "constraints.h"
#include "traceback.h"
#include "shapereader.h"

using namespace std;

static string seqfile = "";
static string outputFile = "";
static string outputDir = "";

static int dangles=-1;

static int nThreads = -1;

void init_fold(const char* seq) {
  assert(seq != NULL);
  int len = strlen(seq);

  init_global_params(len);

  if (!encodeSequence(seq)) {
    free_fold(len);
    exit(0);
  }

  create_tables(len);

  g_nthreads = nThreads;
  g_unamode  = false;
  g_mismatch = false;
  g_verbose  = false;
  g_prefilter_mode  = false;
  g_prefilter1  = 2;
  g_prefilter2  = 2;
  g_dangles = dangles;

}

void free_fold(int len) {
        free_tables(len);
	free_global_params();
}


PolytopeVector mfe_main(string seq_file, string output_file, string param_dir, double a, double b, double c, double d, int dangle_model) {
        std::string seq;
        double energy;
        ParameterVector params;
	
        dangles = dangle_model;
             
        if (!(dangles == 0 || dangles == 1 || dangles == 2)) {
          dangles = -1;
        }

        outputFile = output_file;

	if (read_sequence_file(seq_file.c_str(), seq) == FAILURE) {
		printf("Failed to open sequence file: %s.\n\n", seqfile.c_str());
		exit(-1);
	}

	init_fold(seq.c_str());
	
	// Read in thermodynamic parameters. Always use Turner99 data (for now)
        params.a = a;
        params.b = b;
        params.c = c;
        params.d = d;
        readThermodynamicParameters(param_dir.c_str(), params);

	energy = calculate(seq.length()) ;

        struct PolytopeVector result;
        result = trace(seq.length());
        result.energy = energy;
        result.w = result.energy + result.x * Ea + result.y * Eb + result.z * Ec;
	
	save_ct_file(outputFile, seq, energy);

	free_fold(seq.length());

        return result;
}