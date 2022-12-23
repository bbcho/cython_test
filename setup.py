from setuptools import setup, find_packages
from setuptools.extension import Extension
import Cython.Build
import numpy

extensions = [Extension(
    name="cython_test", 
    sources=["cython_test.pyx"],
    include_dirs=[numpy.get_include()]
)]

setup(
    name="cython_numpy_test",
    packages=find_packages("src"),
    package_dir={"": "src"},
    version="0.0.6",
    install_requires=[
        "numpy",
        "cython",
    ],
    ext_package='cython_numpy_test',
    ext_modules = Cython.Build.cythonize(extensions),
    # include_dirs=[numpy.get_include()]
    )