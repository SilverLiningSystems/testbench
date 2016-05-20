#from distutils.core import setup
from setuptools import setup

setup(
    name = 'getid_tools',
    packages = ['getid_tool'],
    scripts = ['getid_tool/getid'],
    version = '1.3c',
    description = 'SLS Get ID Tool',
    long_description=open("README").read(),
    author = 'sls.jarvis, SLS-BrianKe',
    author_email = 'pkg-admin@silverlining-systems.com',
    url = 'https://github.com/SilverLiningSystems/testbench',
    download_url = 'https://github.com/SilverLiningSystems/testbench/archive/v1.1.tar.gz',
    keywords = ['Calxeda SilverLining SLS'],
    classifiers = ['License :: OSI Approved :: BSD License', 'Programming Language :: Python :: 2.7'],
)
