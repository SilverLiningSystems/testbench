#from distutils.core import setup
from setuptools import setup

setup(
    name = 'getid_tool',
    packages = ['getid_tool'],
    scripts = ['getid_tool/getid'],
    version = '1.1',
    description = 'SLS Get ID Tool',
    author = 'SLS-BrianKe',
    author_email = 'brian.ke@silverlining-systems.com',
    url = 'https://github.com/SilverLiningSystems/testbench',
    download_url = 'https://github.com/SilverLiningSystems/testbench',
    keywords = ['GetID'],
    classifiers = [],
)
