from setuptools import setup, find_packages

setup(
    name='pysdl',
    version='1.0',
    url='',
    license='',
    author='NewtonX',
    author_email='',
    python_requires='>=3.4',
    test_suite="tests.tests",
    package_dir={'': 'pydsl'},
    packages=find_packages("pydsl", exclude="tests"),
    description='A python library that helps Stackdriver consume python logs appropriately built on madzak/python-json-logger',
)
