from setuptools import setup
import Cython.Build
import numpy

setup(
    name="cython_numpy_test",
    version="0.0.6",
    install_requires=[
        "numpy",
        "cython",
    ],
    ext_package='cython_numpy_test',
    ext_modules = Cython.Build.cythonize("cython_test.pyx"),
    include_dirs=[numpy.get_include()]
    )