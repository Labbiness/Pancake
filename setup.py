# -*- encoding:utf-8 -*-
#
# Copyright (c) 2017-2018 Shota Shimazu
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

from setuptools import setup, find_packages
import sys

sys.path.append('./pancake')
sys.path.append('./tests')

if __name__ == "__main__":
    setup(
        name = "Pancake",
        version='0.0.1',
        author = "Shota Shimazu",
        author_email = "hornet.live.mf@gmail.com",
        packages = find_packages(),
        install_requires=[
        ],
        entry_points = {
            'console_scripts':[
                'pancake = Pancake.Pancake:main',
            ],
        },
        description = "Abstract layer for any package manager.",
        long_description = "Abstract layer for any package manager.",
        url = "https://github.com/shotastage/Pancake.git",
        license = "Apache",
        platforms = ["POSIX", "Windows", "Mac OS X"],
        test_suite = "djconsole_test.suite",
    )
