from setuptools import setup, find_packages

setup(
    name='bigdata_lib',
    version='0.1',
    packages=find_packages(),
    description='A Python library for various big data structures including graphs, trees, and more.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Aditya',
    author_email='adityathestar2006@gmail.com',
    url='https://github.com/AdityaSrivastavDS/bigdata_lib',
    install_requires=[],
    python_requires='>=3.6',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
)