#
# Copyright (c) 2017 Shota Shimazu
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

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
