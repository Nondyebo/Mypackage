from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='EDSA example python package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/Nondyebo/Mypackage/blob/master/setup.py',
    author='Nondyebo',
    author_email='nondyeboh@gmail.com'
)
