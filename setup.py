from setuptools import setup, find_packages

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
        # Phond
        'phodic @ git+https://git@github.com/fsbayer/phodic.git'
    ]
)
