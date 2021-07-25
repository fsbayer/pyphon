from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyphon-fsbayer',
    version='0.0.1',
    license='GPL-3.0',
    author='Frederic Bayer',
    author_email='frederic.s.bayer@gmail.com',
    description='Python sound change applier',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/fsbayer/pyphon',
    project_urls={
        "Bug Tracker": "https://github.com/pypa/sampleproject/issues",
    },
    package_dir={"": "\\"},
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Development Status :: 1 - Planning",
        "Intended Audience :: End Users/Desktop",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research"
    ],
    python_requires=">=3.9",
    install_requires=[
        # Phondler
        'phondler @ git+https://git@github.com/fsbayer/phondler.git'
    ]
)
