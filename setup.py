"""Setup the module"""
from setuptools import setup, find_packages

# If you want the sane directory structure with a `src` folder, then you need some magic like this to get it to work.
# Run this to amke it happen:
# pip -e install .
setup(
    name='listentothis',
    version='0.3.0',
    packages=find_packages('src'),
    package_dir={'':'src'}
    )
