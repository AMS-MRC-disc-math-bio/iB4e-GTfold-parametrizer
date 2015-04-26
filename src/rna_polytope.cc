// Copyright (c) 2015 Andrew Gainer-Dewar.

#include "rna_polytope.h"
#include "pmfe_types.h"
#include "nntm.h"
#include "nndb_constants.h"
#include "BBPolytope.h"
#include "mfe.h"

#include <map>

#include <CGAL/Gmpq.h>

#include "boost/filesystem.hpp"
#include "boost/filesystem/fstream.hpp"

namespace fs = boost::filesystem;

namespace pmfe {
    ParameterVector fv_to_pv(BBP::FVector v) {
        ParameterVector pv (
            mpq_class(v.cartesian(0).mpq()),
            mpq_class(v.cartesian(1).mpq()),
            mpq_class(v.cartesian(2).mpq()),
            mpq_class(v.cartesian(3).mpq())
            );
        return pv;
    };

    BBP::FPoint scored_structure_to_fp(RNAStructureWithScore structure) {
        mpq_t values [4];
        mpq_inits(values[0], values[1], values[2], values[3], NULL);

        mpq_set_z(values[0], structure.score.multiloops.get_mpz_t());
        mpq_set_z(values[1], structure.score.unpaired.get_mpz_t());
        mpq_set_z(values[2], structure.score.branches.get_mpz_t());
        mpq_set(values[3], structure.score.w.get_mpq_t());

        BBP::FPoint result(4, values, values+4);
        mpq_clears(values[0], values[1], values[2], values[3], NULL);
        return result;
    };

    RNAPolytope::RNAPolytope(RNASequence sequence, pmfe::dangle_mode dangles):
        BBPolytope(4),
        sequence(sequence),
        dangles(dangles)
        {};

    BBP::FPoint RNAPolytope::vertex_oracle(FVector objective) {
        // Set up the computational environment
        ParameterVector params = fv_to_pv(objective);
        Turner99 constants(params);
        NNTM energy_model(constants, dangles);

        // Compute the energy tables
        RNASequenceWithTables seq_annotated = energy_model.energy_tables(sequence);

        // Find the MFE structure
        RNAStructureWithScore scored_structure = energy_model.mfe_structure(seq_annotated);
        BBP::FPoint result = scored_structure_to_fp(scored_structure);

        // TODO: Handle storing stuctures in class after conversion to dD_triangulation
        structures[result] = scored_structure;
        return result;
    };

    void RNAPolytope::write_to_file(const fs::path poly_file) const {
        fs::ofstream outfile(poly_file);

        if(!outfile.is_open()) {
            std::cerr << "Couldn't open polytope file " << poly_file << "." << std::endl;
            exit(EXIT_FAILURE);
        }

        outfile << "# Points: " << number_of_vertices() << std::endl;
        outfile << "# Facets: " << number_of_simplices() << std::endl << std::endl;

        outfile << "#\t" << sequence << "m\tu\th\tw\te" << std::endl;

        // Initializing variables outside the loop is bad manners, but
        // we need it in order to have both indices
        int i;
        BBP::Hull_vertex_const_iterator v;
        for (i = 1, v = hull_vertices_begin(); v != hull_vertices_end(); ++i, ++v) {
            outfile << i << "\t" << structures.at(associated_point(v)) << std::endl;
        }
    };
};
