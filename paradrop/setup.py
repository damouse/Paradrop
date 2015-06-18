from setuptools import setup, find_packages
 
setup(
    name="spack",
    version="0.1",
    author="Damouse",
    description="A simple PEX example",
    install_requires=['flask', 'sphinx'],
    packages=find_packages(),

    entry_points={
        'console_scripts': [
            'spack=spack.spack:main',
        ],
    },
)