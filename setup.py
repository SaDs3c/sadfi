from setuptools import setup

setup(
    name='sadfii',
    version='0.1',
    packages=['sadfii','sadfi'],
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'sadfi=sadfi.sadwifi.main:main',
        ],
    },
)
