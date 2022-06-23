from skbuild import setup

setup(
    name="hello-split-layout",
    version="1.2.3",
    description="a minimal example package (with pybind11)",
    author='Roberto Di Remigio',
    license="MIT",
    packages=['hello'],
    package_dir={'hello': 'src/pymodule'},
    python_requires='>=3.7',
)
