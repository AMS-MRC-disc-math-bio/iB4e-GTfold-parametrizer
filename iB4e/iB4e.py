# This file was automatically generated by SWIG (http://www.swig.org).
# Version 2.0.12
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.





from sys import version_info
if version_info >= (2,6,0):
    def swig_import_helper():
        from os.path import dirname
        import imp
        fp = None
        try:
            fp, pathname, description = imp.find_module('_iB4e', [dirname(__file__)])
        except ImportError:
            import _iB4e
            return _iB4e
        if fp is not None:
            try:
                _mod = imp.load_module('_iB4e', fp, pathname, description)
            finally:
                fp.close()
            return _mod
    _iB4e = swig_import_helper()
    del swig_import_helper
else:
    import _iB4e
del version_info
try:
    _swig_property = property
except NameError:
    pass # Python < 2.2 doesn't have 'property'.
def _swig_setattr_nondynamic(self,class_type,name,value,static=1):
    if (name == "thisown"): return self.this.own(value)
    if (name == "this"):
        if type(value).__name__ == 'SwigPyObject':
            self.__dict__[name] = value
            return
    method = class_type.__swig_setmethods__.get(name,None)
    if method: return method(self,value)
    if (not static):
        self.__dict__[name] = value
    else:
        raise AttributeError("You cannot add attributes to %s" % self)

def _swig_setattr(self,class_type,name,value):
    return _swig_setattr_nondynamic(self,class_type,name,value,0)

def _swig_getattr(self,class_type,name):
    if (name == "thisown"): return self.this.own()
    method = class_type.__swig_getmethods__.get(name,None)
    if method: return method(self)
    raise AttributeError(name)

def _swig_repr(self):
    try: strthis = "proxy of " + self.this.__repr__()
    except: strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)

try:
    _object = object
    _newclass = 1
except AttributeError:
    class _object : pass
    _newclass = 0


try:
    import weakref
    weakref_proxy = weakref.proxy
except:
    weakref_proxy = lambda x: x


class EuclideanVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, EuclideanVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, EuclideanVector, name)
    __repr__ = _swig_repr
    __swig_setmethods__["dimension"] = _iB4e.EuclideanVector_dimension_set
    __swig_getmethods__["dimension"] = _iB4e.EuclideanVector_dimension_get
    if _newclass:dimension = _swig_property(_iB4e.EuclideanVector_dimension_get, _iB4e.EuclideanVector_dimension_set)
    __swig_setmethods__["data"] = _iB4e.EuclideanVector_data_set
    __swig_getmethods__["data"] = _iB4e.EuclideanVector_data_get
    if _newclass:data = _swig_property(_iB4e.EuclideanVector_data_get, _iB4e.EuclideanVector_data_set)
    __swig_setmethods__["id"] = _iB4e.EuclideanVector_id_set
    __swig_getmethods__["id"] = _iB4e.EuclideanVector_id_get
    if _newclass:id = _swig_property(_iB4e.EuclideanVector_id_get, _iB4e.EuclideanVector_id_set)
    def __init__(self, *args): 
        this = _iB4e.new_EuclideanVector(*args)
        try: self.this.append(this)
        except: self.this = this
    def deletedata(self): return _iB4e.EuclideanVector_deletedata(self)
    def __eq__(self, *args): return _iB4e.EuclideanVector___eq__(self, *args)
    def __lt__(self, *args): return _iB4e.EuclideanVector___lt__(self, *args)
    def get_split_value(self, *args): return _iB4e.EuclideanVector_get_split_value(self, *args)
    def set_split_value(self, *args): return _iB4e.EuclideanVector_set_split_value(self, *args)
    def as_param_vector(self): return _iB4e.EuclideanVector_as_param_vector(self)
    __swig_destroy__ = _iB4e.delete_EuclideanVector
    __del__ = lambda self : None;
    def Print(self): return _iB4e.EuclideanVector_Print(self)
    def Constructor(self, *args): return _iB4e.EuclideanVector_Constructor(self, *args)
    def Negation(self): return _iB4e.EuclideanVector_Negation(self)
    def plusequals(self, *args): return _iB4e.EuclideanVector_plusequals(self, *args)
    def minusequals(self, *args): return _iB4e.EuclideanVector_minusequals(self, *args)
    def timesequals(self, *args): return _iB4e.EuclideanVector_timesequals(self, *args)
    def get_frac_values(self):
        from fractions import Fraction
        split_values = self.get_split_values()
        return [Fraction(val[0], val[1]) for val in split_values]

    def get_split_values(self):
        split_values = [self.get_split_value(i) for i in xrange(self.dimension)]
        return split_values

    def set_frac_values(self, frac_values):
        from fractions import Fraction
        split_values = [(value.numerator, value.denominator) for value in frac_values]
        self.set_split_values(split_values)                      

    def set_split_values(self, split_values):
        for index in xrange(self.dimension):
            val = split_values[index]
            self.set_split_value(index, val[0], val[1])

EuclideanVector_swigregister = _iB4e.EuclideanVector_swigregister
EuclideanVector_swigregister(EuclideanVector)


def computesubfactors(*args):
  return _iB4e.computesubfactors(*args)
computesubfactors = _iB4e.computesubfactors

def dotproduct(*args):
  return _iB4e.dotproduct(*args)
dotproduct = _iB4e.dotproduct

def fourbyfourdet(*args):
  return _iB4e.fourbyfourdet(*args)
fourbyfourdet = _iB4e.fourbyfourdet

def gcd(*args):
  return _iB4e.gcd(*args)
gcd = _iB4e.gcd

def gcd2(*args):
  return _iB4e.gcd2(*args)
gcd2 = _iB4e.gcd2
class vertexnode(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vertexnode, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vertexnode, name)
    __repr__ = _swig_repr
    __swig_setmethods__["next"] = _iB4e.vertexnode_next_set
    __swig_getmethods__["next"] = _iB4e.vertexnode_next_get
    if _newclass:next = _swig_property(_iB4e.vertexnode_next_get, _iB4e.vertexnode_next_set)
    __swig_setmethods__["item"] = _iB4e.vertexnode_item_set
    __swig_getmethods__["item"] = _iB4e.vertexnode_item_get
    if _newclass:item = _swig_property(_iB4e.vertexnode_item_get, _iB4e.vertexnode_item_set)
    def __init__(self): 
        this = _iB4e.new_vertexnode()
        try: self.this.append(this)
        except: self.this = this
    __swig_destroy__ = _iB4e.delete_vertexnode
    __del__ = lambda self : None;
vertexnode_swigregister = _iB4e.vertexnode_swigregister
vertexnode_swigregister(vertexnode)

class BBPolytope(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, BBPolytope, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, BBPolytope, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        if self.__class__ == BBPolytope:
            _self = None
        else:
            _self = self
        this = _iB4e.new_BBPolytope(_self, *args)
        try: self.this.append(this)
        except: self.this = this
    def Build(self): return _iB4e.BBPolytope_Build(self)
    def BlackBoxOptimize(self, *args): return _iB4e.BBPolytope_BlackBoxOptimize(self, *args)
    __swig_setmethods__["vertices"] = _iB4e.BBPolytope_vertices_set
    __swig_getmethods__["vertices"] = _iB4e.BBPolytope_vertices_get
    if _newclass:vertices = _swig_property(_iB4e.BBPolytope_vertices_get, _iB4e.BBPolytope_vertices_set)
    def get_split_vertices(self):
        return [vertex.get_split_values() for vertex in self.vertices]

    def get_frac_vertices(self):
        return [vertex.get_frac_values() for vertex in self.vertices]

    __swig_destroy__ = _iB4e.delete_BBPolytope
    __del__ = lambda self : None;
    def __disown__(self):
        self.this.disown()
        _iB4e.disown_BBPolytope(self)
        return weakref_proxy(self)
BBPolytope_swigregister = _iB4e.BBPolytope_swigregister
BBPolytope_swigregister(BBPolytope)

class SwigPyIterator(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, SwigPyIterator, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, SwigPyIterator, name)
    def __init__(self, *args, **kwargs): raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr
    __swig_destroy__ = _iB4e.delete_SwigPyIterator
    __del__ = lambda self : None;
    def value(self): return _iB4e.SwigPyIterator_value(self)
    def incr(self, n=1): return _iB4e.SwigPyIterator_incr(self, n)
    def decr(self, n=1): return _iB4e.SwigPyIterator_decr(self, n)
    def distance(self, *args): return _iB4e.SwigPyIterator_distance(self, *args)
    def equal(self, *args): return _iB4e.SwigPyIterator_equal(self, *args)
    def copy(self): return _iB4e.SwigPyIterator_copy(self)
    def next(self): return _iB4e.SwigPyIterator_next(self)
    def __next__(self): return _iB4e.SwigPyIterator___next__(self)
    def previous(self): return _iB4e.SwigPyIterator_previous(self)
    def advance(self, *args): return _iB4e.SwigPyIterator_advance(self, *args)
    def __eq__(self, *args): return _iB4e.SwigPyIterator___eq__(self, *args)
    def __ne__(self, *args): return _iB4e.SwigPyIterator___ne__(self, *args)
    def __iadd__(self, *args): return _iB4e.SwigPyIterator___iadd__(self, *args)
    def __isub__(self, *args): return _iB4e.SwigPyIterator___isub__(self, *args)
    def __add__(self, *args): return _iB4e.SwigPyIterator___add__(self, *args)
    def __sub__(self, *args): return _iB4e.SwigPyIterator___sub__(self, *args)
    def __iter__(self): return self
SwigPyIterator_swigregister = _iB4e.SwigPyIterator_swigregister
SwigPyIterator_swigregister(SwigPyIterator)

class ParameterVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ParameterVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ParameterVector, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _iB4e.new_ParameterVector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["multiloop_penalty"] = _iB4e.ParameterVector_multiloop_penalty_set
    __swig_getmethods__["multiloop_penalty"] = _iB4e.ParameterVector_multiloop_penalty_get
    if _newclass:multiloop_penalty = _swig_property(_iB4e.ParameterVector_multiloop_penalty_get, _iB4e.ParameterVector_multiloop_penalty_set)
    __swig_setmethods__["unpaired_penalty"] = _iB4e.ParameterVector_unpaired_penalty_set
    __swig_getmethods__["unpaired_penalty"] = _iB4e.ParameterVector_unpaired_penalty_get
    if _newclass:unpaired_penalty = _swig_property(_iB4e.ParameterVector_unpaired_penalty_get, _iB4e.ParameterVector_unpaired_penalty_set)
    __swig_setmethods__["branch_penalty"] = _iB4e.ParameterVector_branch_penalty_set
    __swig_getmethods__["branch_penalty"] = _iB4e.ParameterVector_branch_penalty_get
    if _newclass:branch_penalty = _swig_property(_iB4e.ParameterVector_branch_penalty_get, _iB4e.ParameterVector_branch_penalty_set)
    __swig_setmethods__["dummy_scaling"] = _iB4e.ParameterVector_dummy_scaling_set
    __swig_getmethods__["dummy_scaling"] = _iB4e.ParameterVector_dummy_scaling_get
    if _newclass:dummy_scaling = _swig_property(_iB4e.ParameterVector_dummy_scaling_get, _iB4e.ParameterVector_dummy_scaling_set)
    def set_from_pairs(self, *args): return _iB4e.ParameterVector_set_from_pairs(self, *args)
    def set_from_words(self, *args): return _iB4e.ParameterVector_set_from_words(self, *args)
    def get_pairs(self): return _iB4e.ParameterVector_get_pairs(self)
    def get_words(self): return _iB4e.ParameterVector_get_words(self)
    def get_python_fractions_dict(self):
        from fractions import Fraction
        pairs = self.get_pairs()
        result = {"multiloop penalty" : Fraction(pairs[0][0], pairs[0][1]),
                  "unpaired base penalty": Fraction(pairs[1][0], pairs[1][1]),
                  "branching helix penalty": Fraction(pairs[2][0], pairs[2][1]),
                  "dummy scaling parameter": Fraction(pairs[3][0], pairs[3][1]),
        }
                 
        return result
      
    __swig_destroy__ = _iB4e.delete_ParameterVector
    __del__ = lambda self : None;
ParameterVector_swigregister = _iB4e.ParameterVector_swigregister
ParameterVector_swigregister(ParameterVector)

class ScoreVector(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, ScoreVector, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, ScoreVector, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _iB4e.new_ScoreVector(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["multiloops"] = _iB4e.ScoreVector_multiloops_set
    __swig_getmethods__["multiloops"] = _iB4e.ScoreVector_multiloops_get
    if _newclass:multiloops = _swig_property(_iB4e.ScoreVector_multiloops_get, _iB4e.ScoreVector_multiloops_set)
    __swig_setmethods__["branches"] = _iB4e.ScoreVector_branches_set
    __swig_getmethods__["branches"] = _iB4e.ScoreVector_branches_get
    if _newclass:branches = _swig_property(_iB4e.ScoreVector_branches_get, _iB4e.ScoreVector_branches_set)
    __swig_setmethods__["unpaired"] = _iB4e.ScoreVector_unpaired_set
    __swig_getmethods__["unpaired"] = _iB4e.ScoreVector_unpaired_get
    if _newclass:unpaired = _swig_property(_iB4e.ScoreVector_unpaired_get, _iB4e.ScoreVector_unpaired_set)
    __swig_setmethods__["w"] = _iB4e.ScoreVector_w_set
    __swig_getmethods__["w"] = _iB4e.ScoreVector_w_get
    if _newclass:w = _swig_property(_iB4e.ScoreVector_w_get, _iB4e.ScoreVector_w_set)
    __swig_setmethods__["energy"] = _iB4e.ScoreVector_energy_set
    __swig_getmethods__["energy"] = _iB4e.ScoreVector_energy_get
    if _newclass:energy = _swig_property(_iB4e.ScoreVector_energy_get, _iB4e.ScoreVector_energy_set)
    def set_from_pairs(self, *args): return _iB4e.ScoreVector_set_from_pairs(self, *args)
    def set_from_words(self, *args): return _iB4e.ScoreVector_set_from_words(self, *args)
    def get_pairs(self): return _iB4e.ScoreVector_get_pairs(self)
    def get_words(self): return _iB4e.ScoreVector_get_words(self)
    def get_python_fractions_dict(self):
        from fractions import Fraction
        pairs = self.get_pairs()
        result = {"multiloops" : pairs[0][0],
                  "unpaired": pairs[1][0],
                  "branches": pairs[2][0],
                  "w": Fraction(pairs[3][0], pairs[3][1]),
                  "energy": Fraction(pairs[4][0], pairs[4][1]),
        }
                 
        return result
      
    __swig_destroy__ = _iB4e.delete_ScoreVector
    __del__ = lambda self : None;
ScoreVector_swigregister = _iB4e.ScoreVector_swigregister
ScoreVector_swigregister(ScoreVector)


def get_mpq_from_word(*args):
  return _iB4e.get_mpq_from_word(*args)
get_mpq_from_word = _iB4e.get_mpq_from_word
class pairll(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, pairll, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, pairll, name)
    __repr__ = _swig_repr
    def __init__(self, *args): 
        this = _iB4e.new_pairll(*args)
        try: self.this.append(this)
        except: self.this = this
    __swig_setmethods__["first"] = _iB4e.pairll_first_set
    __swig_getmethods__["first"] = _iB4e.pairll_first_get
    if _newclass:first = _swig_property(_iB4e.pairll_first_get, _iB4e.pairll_first_set)
    __swig_setmethods__["second"] = _iB4e.pairll_second_set
    __swig_getmethods__["second"] = _iB4e.pairll_second_get
    if _newclass:second = _swig_property(_iB4e.pairll_second_get, _iB4e.pairll_second_set)
    def __len__(self): return 2
    def __repr__(self): return str((self.first, self.second))
    def __getitem__(self, index): 
      if not (index % 2): 
        return self.first
      else:
        return self.second
    def __setitem__(self, index, val):
      if not (index % 2): 
        self.first = val
      else:
        self.second = val
    __swig_destroy__ = _iB4e.delete_pairll
    __del__ = lambda self : None;
pairll_swigregister = _iB4e.pairll_swigregister
pairll_swigregister(pairll)

class vecll(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vecll, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vecll, name)
    __repr__ = _swig_repr
    def iterator(self): return _iB4e.vecll_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _iB4e.vecll___nonzero__(self)
    def __bool__(self): return _iB4e.vecll___bool__(self)
    def __len__(self): return _iB4e.vecll___len__(self)
    def pop(self): return _iB4e.vecll_pop(self)
    def __getslice__(self, *args): return _iB4e.vecll___getslice__(self, *args)
    def __setslice__(self, *args): return _iB4e.vecll___setslice__(self, *args)
    def __delslice__(self, *args): return _iB4e.vecll___delslice__(self, *args)
    def __delitem__(self, *args): return _iB4e.vecll___delitem__(self, *args)
    def __getitem__(self, *args): return _iB4e.vecll___getitem__(self, *args)
    def __setitem__(self, *args): return _iB4e.vecll___setitem__(self, *args)
    def append(self, *args): return _iB4e.vecll_append(self, *args)
    def empty(self): return _iB4e.vecll_empty(self)
    def size(self): return _iB4e.vecll_size(self)
    def clear(self): return _iB4e.vecll_clear(self)
    def swap(self, *args): return _iB4e.vecll_swap(self, *args)
    def get_allocator(self): return _iB4e.vecll_get_allocator(self)
    def begin(self): return _iB4e.vecll_begin(self)
    def end(self): return _iB4e.vecll_end(self)
    def rbegin(self): return _iB4e.vecll_rbegin(self)
    def rend(self): return _iB4e.vecll_rend(self)
    def pop_back(self): return _iB4e.vecll_pop_back(self)
    def erase(self, *args): return _iB4e.vecll_erase(self, *args)
    def __init__(self, *args): 
        this = _iB4e.new_vecll(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _iB4e.vecll_push_back(self, *args)
    def front(self): return _iB4e.vecll_front(self)
    def back(self): return _iB4e.vecll_back(self)
    def assign(self, *args): return _iB4e.vecll_assign(self, *args)
    def resize(self, *args): return _iB4e.vecll_resize(self, *args)
    def insert(self, *args): return _iB4e.vecll_insert(self, *args)
    def reserve(self, *args): return _iB4e.vecll_reserve(self, *args)
    def capacity(self): return _iB4e.vecll_capacity(self)
    __swig_destroy__ = _iB4e.delete_vecll
    __del__ = lambda self : None;
vecll_swigregister = _iB4e.vecll_swigregister
vecll_swigregister(vecll)

class vecstr(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vecstr, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vecstr, name)
    __repr__ = _swig_repr
    def iterator(self): return _iB4e.vecstr_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _iB4e.vecstr___nonzero__(self)
    def __bool__(self): return _iB4e.vecstr___bool__(self)
    def __len__(self): return _iB4e.vecstr___len__(self)
    def pop(self): return _iB4e.vecstr_pop(self)
    def __getslice__(self, *args): return _iB4e.vecstr___getslice__(self, *args)
    def __setslice__(self, *args): return _iB4e.vecstr___setslice__(self, *args)
    def __delslice__(self, *args): return _iB4e.vecstr___delslice__(self, *args)
    def __delitem__(self, *args): return _iB4e.vecstr___delitem__(self, *args)
    def __getitem__(self, *args): return _iB4e.vecstr___getitem__(self, *args)
    def __setitem__(self, *args): return _iB4e.vecstr___setitem__(self, *args)
    def append(self, *args): return _iB4e.vecstr_append(self, *args)
    def empty(self): return _iB4e.vecstr_empty(self)
    def size(self): return _iB4e.vecstr_size(self)
    def clear(self): return _iB4e.vecstr_clear(self)
    def swap(self, *args): return _iB4e.vecstr_swap(self, *args)
    def get_allocator(self): return _iB4e.vecstr_get_allocator(self)
    def begin(self): return _iB4e.vecstr_begin(self)
    def end(self): return _iB4e.vecstr_end(self)
    def rbegin(self): return _iB4e.vecstr_rbegin(self)
    def rend(self): return _iB4e.vecstr_rend(self)
    def pop_back(self): return _iB4e.vecstr_pop_back(self)
    def erase(self, *args): return _iB4e.vecstr_erase(self, *args)
    def __init__(self, *args): 
        this = _iB4e.new_vecstr(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _iB4e.vecstr_push_back(self, *args)
    def front(self): return _iB4e.vecstr_front(self)
    def back(self): return _iB4e.vecstr_back(self)
    def assign(self, *args): return _iB4e.vecstr_assign(self, *args)
    def resize(self, *args): return _iB4e.vecstr_resize(self, *args)
    def insert(self, *args): return _iB4e.vecstr_insert(self, *args)
    def reserve(self, *args): return _iB4e.vecstr_reserve(self, *args)
    def capacity(self): return _iB4e.vecstr_capacity(self)
    __swig_destroy__ = _iB4e.delete_vecstr
    __del__ = lambda self : None;
vecstr_swigregister = _iB4e.vecstr_swigregister
vecstr_swigregister(vecstr)

class vecEV(_object):
    __swig_setmethods__ = {}
    __setattr__ = lambda self, name, value: _swig_setattr(self, vecEV, name, value)
    __swig_getmethods__ = {}
    __getattr__ = lambda self, name: _swig_getattr(self, vecEV, name)
    __repr__ = _swig_repr
    def iterator(self): return _iB4e.vecEV_iterator(self)
    def __iter__(self): return self.iterator()
    def __nonzero__(self): return _iB4e.vecEV___nonzero__(self)
    def __bool__(self): return _iB4e.vecEV___bool__(self)
    def __len__(self): return _iB4e.vecEV___len__(self)
    def pop(self): return _iB4e.vecEV_pop(self)
    def __getslice__(self, *args): return _iB4e.vecEV___getslice__(self, *args)
    def __setslice__(self, *args): return _iB4e.vecEV___setslice__(self, *args)
    def __delslice__(self, *args): return _iB4e.vecEV___delslice__(self, *args)
    def __delitem__(self, *args): return _iB4e.vecEV___delitem__(self, *args)
    def __getitem__(self, *args): return _iB4e.vecEV___getitem__(self, *args)
    def __setitem__(self, *args): return _iB4e.vecEV___setitem__(self, *args)
    def append(self, *args): return _iB4e.vecEV_append(self, *args)
    def empty(self): return _iB4e.vecEV_empty(self)
    def size(self): return _iB4e.vecEV_size(self)
    def clear(self): return _iB4e.vecEV_clear(self)
    def swap(self, *args): return _iB4e.vecEV_swap(self, *args)
    def get_allocator(self): return _iB4e.vecEV_get_allocator(self)
    def begin(self): return _iB4e.vecEV_begin(self)
    def end(self): return _iB4e.vecEV_end(self)
    def rbegin(self): return _iB4e.vecEV_rbegin(self)
    def rend(self): return _iB4e.vecEV_rend(self)
    def pop_back(self): return _iB4e.vecEV_pop_back(self)
    def erase(self, *args): return _iB4e.vecEV_erase(self, *args)
    def __init__(self, *args): 
        this = _iB4e.new_vecEV(*args)
        try: self.this.append(this)
        except: self.this = this
    def push_back(self, *args): return _iB4e.vecEV_push_back(self, *args)
    def front(self): return _iB4e.vecEV_front(self)
    def back(self): return _iB4e.vecEV_back(self)
    def assign(self, *args): return _iB4e.vecEV_assign(self, *args)
    def resize(self, *args): return _iB4e.vecEV_resize(self, *args)
    def insert(self, *args): return _iB4e.vecEV_insert(self, *args)
    def reserve(self, *args): return _iB4e.vecEV_reserve(self, *args)
    def capacity(self): return _iB4e.vecEV_capacity(self)
    __swig_destroy__ = _iB4e.delete_vecEV
    __del__ = lambda self : None;
vecEV_swigregister = _iB4e.vecEV_swigregister
vecEV_swigregister(vecEV)

# This file is compatible with both classic and new-style classes.

