cmake_minimum_required(VERSION 2.8.12)
project(emod)

include_directories(src/MathFunctions)
add_subdirectory(src/MathFunctions)

add_subdirectory(pybind11)
pybind11_add_module(emod src/Cohort.cpp)

target_link_libraries(emod PRIVATE MathFunctions)
