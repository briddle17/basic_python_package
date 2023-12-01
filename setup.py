# my_package/setup.py
from setuptools import setup, find_packages

setup(
    name="my_pkg",
    version="0.1",
    description="Minimal example python package",
    author="Brennan Riddle",
    url="https://github.com/briddle17/basic_python_package",
    packages=find_packages(),
    install_requires=[
        "pandas",
    ],
)
