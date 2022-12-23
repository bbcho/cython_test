from setuptools import setup
import Cython.Build
import numpy

setup(
    install_requires=[
        "numpy",
        "cython",
    ],
    ext_modules = Cython.Build.cythonize("test_cython.pyx"),
    include_dirs=[numpy.get_include()]
    )