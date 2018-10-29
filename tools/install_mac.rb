#!/usr/bin/env ruby
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

require 'rbconfig'



$__name__="__main__"


def copyright()
    puts " Copyright (c) 2017 Shota Shimazu"
    puts " Licensed by Labbiness 2017."
    puts ""
    puts " See, LICENSE for detail."
end

def log (str)
    puts "INSTALLER: " + str
end

def os
    @os ||= (
        host_os = RbConfig::CONFIG['host_os']
        case host_os
        when /mswin|msys|mingw|cygwin|bccwin|wince|emc/
            :Windows
        when /darwin|mac os/
            :macOS
        when /linux/
            :Linux
        when /solaris|bsd/
            :Unix
        else
            :Unknown
        end
    )
end





if __FILE__ == $0 then
    copyright()

    puts os()

    if os() == 'macOS' then
        log("Using macOS.")
    else
        log("This installer is macOS only.")
        exit 1
    end
end




# MOVE TO HOME DIRECTORY
#cd


#if [ -e ./pancake_installation ]; then
#    rm -rf ./pancake_installation
#fi
#mkdir ./pancake_installation
#cd ./pancake_installation


## --------------------- Clone -------------------- ##
#git clone https://github.com/shotastage/Pancake.git
