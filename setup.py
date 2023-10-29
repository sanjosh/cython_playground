
from setuptools import setup
from Cython.Build import cythonize

setup(
    ext_modules = cythonize(["cython_mod/helloworld.pyx", "cython_mod/primes.pyx"], annotate=True)
)