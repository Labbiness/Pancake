# -*- coding: utf-8 -*-
"""
Copyright 2017 Shota Shimazu.
   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at
       http://www.apache.org/licenses/LICENSE-2.0
   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
"""

import sys
import functools
from subprocess import check_output, DEVNULL, STDOUT


def log(string, withError = False, withExitOnError = False, withInput = False):
    if withError:
        print('\033[31mDjango Console: ' + string + '\033[0m')

        if withExitOnError:
            sys.exit(1)

    elif withInput:
        return input('\033[32m' + string + ' >> \033[0m')

    else:
        print('\033[32mDjango Coneole: \033[0m' + string)



def command(command, withOutput = False):
    separated_cmds = command.split(" ")

    if withOutput:
        try:
            check_output(separated_cmds, stderr=STDOUT)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)

    else:
        try:
            check_output(separated_cmds, stderr=DEVNULL)
        except:
            log("Failed to exec " + command + "!", withError = True, withExitOnError = True)


def reserve_as_command(*reserved_args):

    def _decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for reserve in reserved_args:
                if args[1] == reserve:
                    re = func(*args, **kwargs)
                    return re
        return wrapper
    return _decorator
