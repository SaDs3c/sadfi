from setuptools import setup

setup(
    name='sad-Fi',
    version='0.1',
    packages=['sadfi'],
    install_requires=[
        'tabulate',
    ],
    entry_points={
        'console_scripts': [
            'sad-Fi=sadfi.main:main',
        ],
    },
)
