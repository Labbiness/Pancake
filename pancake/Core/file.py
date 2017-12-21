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

import os
import shutil


def homeDirectory():
    return os.environ['HOME']

def currentDirectory():
    return os.getcwd()

def exsitFile(file):
    return os.path.exists(file)

def exists(file_path):
    return os.path.exists(file_path)

def mkdir(path, override = False):
    if override:
        os.makedirs(path)
    else:
        os.makedirs(path)
