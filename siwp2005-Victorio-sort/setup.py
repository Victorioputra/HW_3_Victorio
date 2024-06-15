from setuptools import setup, find_packages

setup(
    name='siwp2005-Victorio-sort',
    version='0.1.2',
    packages=find_packages(where='src'),
    long_description = open('README.md').read(),
    long_description_content_type = 'text/markdown',
    install_requires=[],
    test_suite='tests',
    tests_require=['unittest'],
    entry_points={
        'console_scripts': [
            'siwp2005-Victorio-sort=src.sort:main',
        ],
    },
)