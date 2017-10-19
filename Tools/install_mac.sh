#!/usr/bin/env bash

echo " Copyright (c) 2017 Shota Shimazu"
echo " Licensed by Labbiness 2017."
echo ""
echo " See, LICENSE for detail."



function log () {
    echo "INSTALLER:" $1
}



## -------------------- MAIN -------------------- ##
if [ "$(uname)" == 'Darwin' ]; then
    log "Using macOS."
else
    log "This installer is macOS only."
    exit 1
fi
