#include <string>
#include <pybind11/pybind11.h>
#include "Cohort.h"


Cohort::Cohort(int count)
    : count(count) { }

const int Cohort::getCount() const
{
    return count;
}

void Cohort::setCount(const int count_)
{
    count = count_;
}


namespace py = pybind11;

PYBIND11_MODULE(emod, m) {

    py::class_<Cohort>(m, "Cohort")
        .def(py::init<int>())
        .def_property("count", &Cohort::getCount, &Cohort::setCount)
        .def("__repr__",
            [](const Cohort &a) {
                std::string s = std::to_string(a.getCount());
                return "<emod.Cohort with count of " + s + ">";
            }
        );
}
