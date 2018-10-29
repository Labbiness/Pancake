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


from abc import ABCMeta, abstractmethod
from pancake.core import *


class Workflow():

    def __init__(self):
        self.workflow_will_run()
        self.workflow_running()
        self.workflow_did_run()


    def workflow_will_run(self) -> Void:
        pass    

    def workflow_running(self) -> Void:
        pass

    def workflow_did_run(self) -> Void:
        pass
