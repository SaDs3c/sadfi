from setuptools import setup

setup(
    name='sadfi',
    version='0.1',
    packages=['sadfi'],
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'sadfi=sadfi.main:main',
        ],
    },
)
