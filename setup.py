from setuptools import setup, find_packages
import kad

with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='kad.py',
    version=kad.__version__,
    description='Python3 DHT Implementation',
    long_description=readme,
    author='Isaac Zafuta, Davide Gessa',
    author_email='isaac@zafuta.com, gessadavide@gmail.com',
    url='https://github.com/dakk/kad.py',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
