#!/bin/bash 

sudo python ./paradrop/setup.py install

pex paradrop -o paradrop.pex -e paradrop:main

mv paradrop.pex ./build/bin/paradrop