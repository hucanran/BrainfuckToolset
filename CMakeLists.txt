cmake_minimum_required(VERSION 3.10) 
project(bf VERSION 2.0) 
aux_source_directory(./src SRC_LIST)
# set(CMAKE_CXX_FLAGS   "-g") 调试
add_executable(bf ${SRC_LIST})