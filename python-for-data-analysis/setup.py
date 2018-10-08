from distutils.core import setup

setup(
    name='pythonForDataAnalysis',
    version='0.1.0',
    author='M-Watson',
    author_email='',
    license='LICENSE.txt',
    description='Data science practice',
    long_description=open('README.md').read(),
    install_requires=[
        "Requests",
        "pandas",
        "seabourn"
    ],
)
