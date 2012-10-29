# encoding: utf-8

from setuptools import setup, find_packages

requires = ["requests", "beautifulsoup4"]
 
setup(
    name='pybeeradvocate',
    version='0.0.1',
    description="Python bindings for Beer Advocate",
    long_description="""Py Beer Advocate is a python wrapper using Requests & BeautifulSoup to extract beer information from beeradvocate.com""",
    classifiers=[
        "Topic :: Internet :: Beer",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Intended Audience :: Developers",
    ],
    keywords='',
    author='Doug Morgan',
    author_email='',
    url='https://github.com/dsmorgan/py_beer_advocate',
    license='MIT',
    packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
    include_package_data=True,
    zip_safe=False,
    install_requires=requires,
)