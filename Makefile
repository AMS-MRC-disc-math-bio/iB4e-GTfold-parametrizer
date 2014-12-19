# source files
SRC = $(wildcard src/*.cc)
OBJ = $(SRC:.cc=.o)
DEP = $(SRC:.cc=.d)
HDR = $(wildcard include/*.h)

OBJ-GTMFE = $(filter-out src/iB4e_wrapper.o src/rnascorer_wrapper.o src/pyparam.o, $(OBJ))
OBJ-PARAM = $(filter-out src/gtmfe_wrapper.o src/rnascorer_wrapper.o src/pyparam.o, $(OBJ))
OBJ-RNASCORING = $(filter-out src/gtmfe_wrapper.o src/iB4e_wrapper.o src/pyparam.o, $(OBJ))
OBJ-PYPARAM = $(filter-out src/gtmfe_wrapper.o src/iB4e_wrapper.o src/rnascorer_wrapper.o, $(OBJ))
EXEC = gtmfe-param parametrizer rnascorer
PYPARAM = pyparam/pyparam_base.so

# include directories
INCLUDES += -Iinclude -Irna-scoring/ -I/usr/include/python2.7

# C++ compiler flags
CXXFLAGS += -fPIC
CXXFLAGS += -Wall
CXXFLAGS += -g
#CXXFLAGS += -O2
CXXFLAGS += -O0

# library paths
LIBS += -lCGAL
LIBS += -lgmp
LIBS += -lm
LIBS += -lboost_system
LIBS += -lboost_filesystem
LIBS += -lboost_program_options
LIBS += -lboost_python
LIBS += -lpython2.7
LIBS += -L./rna-scoring -Wl,-R./rna-scoring -lrnascoring

# Optional OpenMP-related flags
HAS_OPENMP = $(shell $(CXX) -lgomp test.cc -o /dev/null 2>&1 > /dev/null ; echo $$?)
ifeq ($(HAS_OPENMP), 0)
CXXFLAGS += -fopenmp
CXXFLAGS += -DHAVE_OPENMP
LIBS += -lgomp
endif

all: rnascoring $(OBJ) $(EXEC) $(PYPARAM)

gtmfe-param: $(OBJ-GTMFE)
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) $(OBJ-GTMFE) -o $@ $(LIBS)

parametrizer: $(OBJ-PARAM)
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) $(OBJ-PARAM) -o $@ $(LIBS)

rnascorer: $(OBJ-RNASCORING)
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) $(OBJ-RNASCORING) -o $@ $(LIBS)

-include $(DEP)

%.o: %.cc
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) -c $*.cc -o $*.o $(LIBS)
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) -MM $*.cc $(LIBS) | sed -e 's@^\(.*\)\.o:@src/\1.d src/\1.o:@' > $*.d

$(PYPARAM): $(OBJ-PYPARAM)
	$(CXX) $(INCLUDES) $(LDFLAGS) $(CXXFLAGS) $(LIBFLAGS) $(LIBS) $^ -shared -Wl,-soname,$@ -o $@

rnascoring:
	$(MAKE) -C rna-scoring

clean:
	-rm -vf $(EXEC) $(OBJ) $(DEP) $(PYPARAM)

.PHONY: clean
