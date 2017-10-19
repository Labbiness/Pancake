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

import Console
import Core.io as IO

import os


def __setup_install_env():
    home = IO.homeDirectory

    if not os.path.exists(home):
        Console.log("Creating maple packge bin...")
        os.mkdir(home + "/.pancake_maples")

def _downloader(git_url):
    Console.cmd("git clone " + git_url)

def install(package):
    Console.log("Installing " + package + "...")

    # Prepare installing
    __setup_install_env()

    # Download package
    