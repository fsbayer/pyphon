from setuptools import setup, find_packages
# The following is just some junk to generate dependencies
import phondler as libphondler
langs = libphondler.phondler.LANGUAGES

setup(
    name='pyphon',
    version='0.0.1',
    packages=find_packages(),
    url='https://github.com/fsbayer/pyphon',
    license='GPL-3.0',
    author='Frederic Bayer',
    author_email='',
    description='Python sound change applier',
    install_requires=[
        # Phondler
        'phondler @ git+https://git@github.com/fsbayer/phondler.git'
    ]
)
