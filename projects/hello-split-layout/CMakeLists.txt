cmake_minimum_required(VERSION 3.14...3.22)

project(hello-pybind11 VERSION "0.1")

# Define CMAKE_INSTALL_xxx: LIBDIR, INCLUDEDIR
include(GNUInstallDirs)

# Fetch pybind11
include(FetchContent)

FetchContent_Declare(
  pybind11
  URL https://github.com/pybind/pybind11/archive/refs/tags/v2.9.1.tar.gz
  URL_HASH SHA256=c6160321dc98e6e1184cc791fbeadd2907bb4a0ce0e447f2ea4ff8ab56550913
)
FetchContent_MakeAvailable(pybind11)

add_subdirectory(src)

# Quiet a warning, since this project is only valid with SKBUILD
set(ignoreMe "${SKBUILD}")
