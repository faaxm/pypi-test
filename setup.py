from setuptools import setup, find_packages

setup(
    name='lipomerge_test_faaxm',
    version='0.3.0',
    author='Falko Axmann',
    description='A tool to merge directories containing static libraries into universal binaries.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/lipomerge',
    packages=find_packages(),
    py_modules=['lipomerge'],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: MacOS :: MacOS X',
    ],
    python_requires='>=3.6',
    install_requires=[],
    entry_points={
        'console_scripts': [
            'lipomerge=lipomerge:main',
        ],
    },
) 