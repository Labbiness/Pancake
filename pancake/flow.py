# -*- coding: utf-8 -*-
"""
Copyright (c) 2017-2018 Shota Shimazu.
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

from pancake.command import log
from abc import ABCMeta, abstractmethod


class Workflow():

    def __init__(self, parser):
        self.inherited       = parser
        self._action        = self.inherited[0]
        self._subaction     = self.inherited[1]
        self._option        = self.inherited[2]
        self._option_detail = self.inherited[3]
        self._values        = self.inherited[4]
        self.constructor()


    def constructor(self): pass

    def get_first_arg(self):
        try:
            return self._values[0]
        except:
            raise ValueError

    def register(self, flow):
        self.Stepflows.append(flow)
    
    def main(self):
        # Main flow structure
        pass

    def run(self):
        self.main()

        # Flow
        for flow in self.Stepflows:
            try:
                flow.run()
            except:
                raise Exception
