set(python_module_name _hello)
pybind11_add_module(${python_module_name} MODULE
  ${CMAKE_CURRENT_LIST_DIR}/hello_py.cpp
  )

install(TARGETS ${python_module_name} DESTINATION "src/pymodule")
