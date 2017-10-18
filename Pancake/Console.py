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

import platform
import os


""":
  Logger
"""
def log(string, withError = False): # -> Void
    if withError:
        print('\033[31m Pancake: ' + string + '\033[0m')
    else:
        print('\033[32m Pancake: \033[0m' + string)

def notify(string): # -> Void
    if platform.system() == 'Darwin':
        os.system("osascript -e 'display notification \"" + "Pancake: " + string + "\"'")
