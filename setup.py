from setuptools import setup
from setuptools import find_packages


setup(name='Pancake',
      version='0.0.1',
      description='A integrated builder and tools for developers.',
      author='Shota Shimazu',
      author_email='hornet.live.mf@gmail.com',
      url='https://github.com/Labbiness/Pancake',
      download_url='https://github.com/Labbiness/Pancake/tarball/0.0.1',
      license='Apache',
      install_requires = [
      ],
      extras_require={
          'tests': ['pytest',],
      },
      packages=find_packages())
