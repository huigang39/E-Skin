#include <iostream>
#include <fstream>
#include <string>
#include <vector>

#include <boost/python.hpp>
#include <boost/python/numpy.hpp>

namespace p = boost::python;
namespace np = boost::python::numpy;

p::object LoadPickle(std::string filename){
    std::ifstream ifs(filename, std::ios::binary);
    return p::object(p::handle<>(p::allow_null(PyImport_ImportModule("pickle"))).attr("load")(ifs));
}
