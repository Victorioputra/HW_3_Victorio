from setuptools import setup, find_packages

setup(
    name='siwp2005-Victorio-sort',
    version='0.1.0',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[],
    test_suite='tests',
    tests_require=['unittest'],
    entry_points={
        'console_scripts': [
            'siwp2005-Victorio-sort=src.sort:main',
        ],
    },
)