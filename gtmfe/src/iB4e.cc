// Copyright (c) 2014 Andrew Gainer-Dewar.

#include <stdlib.h>
#include <iostream>
#include <set>
#include <string>
#include <boost/bind.hpp>
#include <boost/function.hpp>
#include <boost/filesystem.hpp>
#include <boost/lexical_cast.hpp>

#include "iB4e.h"
#include "mfe_main.h"
#include "parametrizer_types.h"

QPoint run_gtmfe_on_q4vector(QVector param_vector, boost::filesystem::path seq_file, boost::filesystem::path output_dir, boost::filesystem::path param_dir) {
    ParameterVector params;
    ScoreVector scores;

    std::string structure_ext = ".ct";
    boost::filesystem::path seq_base_name = seq_file.stem();
    boost::filesystem::path initial_output_file = output_dir / seq_base_name;
    initial_output_file.replace_extension(structure_ext);

    params = ParameterVector(param_vector);
    scores = mfe_main(seq_file.string(), initial_output_file.string(), param_dir.string(), params);

    std::string score_sep (", ");
    std::string w_score_string (boost::lexical_cast<std::string>(mpf_class(scores.w).get_d()));
    std::string score_string =
        ".[" +
        scores.multiloops.get_str(10) + score_sep +
        scores.unpaired.get_str(10) + score_sep +
        scores.branches.get_str(10) + score_sep +
        w_score_string +
        "]";

    boost::filesystem::path updated_output_file = initial_output_file;
    updated_output_file.replace_extension(score_string + structure_ext);
    boost::filesystem::rename(initial_output_file, updated_output_file);

    return scores.get_q4point();
}

int iB4e_main(std::string seq_file_path, std::string param_dir_path) {
    // Work in four dimensions
    int dim = 4;

    // Initialize the convex hull object
    ConvexHull CH(dim);

    // Create directory path objects
    boost::filesystem::path param_dir(param_dir_path);

    boost::filesystem::path seq_file(seq_file_path);
    boost::filesystem::path seq_base_name = seq_file.stem();

    boost::filesystem::path struct_dir = seq_file.parent_path() / seq_base_name;
    boost::filesystem::remove_all(struct_dir);
    boost::filesystem::create_directory(struct_dir);

    // Fancy functional trick to create a vertex oracle function
    boost::function<QPoint (QVector param_vector)> vertex_finder =
        boost::bind(&run_gtmfe_on_q4vector, _1, seq_file, struct_dir, param_dir);

    // BEGIN LOGIC
    // INITIALIZATION

    // We keep a list of vectors which have been tested or are in the polytope
    std::vector<LVector> test_vectors;

    // To bootstrap the process, we manually check the zero parameter vector
    QVector zero(dim, CGAL::NULL_VECTOR);
    QPoint null_mfe = vertex_finder(zero);
    CH.insert(null_mfe);
    test_vectors.push_back(LVector(null_mfe.cartesian_begin(), null_mfe.cartesian_end()));

    // Huggins' initialization loop
    while (CH.current_dimension() < dim) {
        // Construct some helper objects
        LMatrix A(test_vectors);
        A = LinearAlgebra::transpose(A); // Transpose due to design choices in CGAL
        LMatrix orthogonal_vectors;
        LVector x;
        bool done = false;

        // Find a vector orthogonal to all the test vectors
        if (LinearAlgebra::homogeneous_linear_solver(A, orthogonal_vectors)) {
            LVector x = orthogonal_vectors.column(0);
            QVector c(dim, x.begin(), x.end());
            LVector new_test_vector;

            // If either of c or -c yields a point that increases the dimension of CH, add it
            if (!done) {
                QPoint mfe_point = vertex_finder(c);
                if (CH.number_of_vertices() == 0 || CH.is_dimension_jump(mfe_point)) {
                    CH.insert(mfe_point);
                    new_test_vector = LVector(mfe_point.cartesian_begin(), mfe_point.cartesian_end());
                    done = true;
                }
            }

            if (!done) {
                QPoint mfe_point = vertex_finder(-c);
                if (CH.is_dimension_jump(mfe_point)) {
                    CH.insert(mfe_point);
                    new_test_vector = LVector(mfe_point.cartesian_begin(), mfe_point.cartesian_end());
                    done = true;
                }
            }

            // Otherwise, add c as a test vector
            if (!done) {
                new_test_vector = x;
                done = true;
            }

            test_vectors.push_back(new_test_vector);
        } else { // If no orthogonal vector was found, the polytope is not full-dimensional and the algorithm will fail
            exit(1);
        }
    }

    assert(CH.is_valid());
    assert(CH.current_dimension() == dim);

    // MAIN LOOP
    bool all_confirmed_so_far = false;
    int confirmed = 0;
    while (!all_confirmed_so_far) {
        all_confirmed_so_far = true;

        // Attempt to confirm every facet
        for (Facet_iterator f = CH.facets_begin(); f != CH.facets_end() && all_confirmed_so_far ; f++) {
            if (!f->is_confirmed()) { // If the facet is not already confirmed, test it
                Hyperplane hp = CH.hyperplane_supporting(f);
                QVector innernormal = -hp.orthogonal_vector(); // CGAL returns the outer normal
                innernormal *= innernormal[0].denominator();
                QPoint mfe_point = vertex_finder(innernormal);

                switch (hp.oriented_side(mfe_point)) {
                case CGAL::ON_POSITIVE_SIDE:
                    CH.insert(mfe_point); // If so, add the new point and break the inner loop
                    all_confirmed_so_far = false;
                    break;

                case CGAL::ON_ORIENTED_BOUNDARY:
                    f->confirm(); // Otherwise, mark the facet as confirmed and continue
                    confirmed++;
                    break;

                case CGAL::ON_NEGATIVE_SIDE:
                    std::cout << "Failed vector test!" << std::endl;
                    std::cout << "Hyperplane: " << hp << std::endl;
                    std::cout << "Inner normal: " << innernormal << std::endl;
                    std::cout << "MFE point: " << mfe_point << std::endl;
                    std::cout << "Known vertex: " << CH.vertex_of_facet(f, 0)->point() << std::endl << std::endl;
                    f->confirm();
                    break;
                }
            }
        }
    }

    // END LOGIC
    // BEGIN OUTPUT

    assert(CH.is_valid());
    CH.print_statistics();
    std::cout << CH.all_facets().size() << " facets, " << confirmed << " confirmed." << std::endl;

    std::cout << "[";

    for (Vertex_iterator v = CH.vertices_begin(); v != CH.vertices_end(); v++) {
        QPoint p = v->point();
        std::cout << "[" << p[0] << ", " << p[1] << ", " << p[2] << ", " << p[3] << "], ";
    }

    std::cout << "]" << std::endl;

    // END OUTPUT

    return 0;
}