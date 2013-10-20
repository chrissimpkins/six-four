#!/bin/sh

# Developer install distribution instructions:
# 1 > Run tests/test.sh
# 2 > Update version number in:
#		- PKG-INFO
#		- sixfour.py
#		- setup.py
# 3 > Run this file
#    - creates sixfour 'binary' script for user to run at CL
# 4 > Upload to PyPi
#    - python setup.py sdist upload

# create the main script that will run from the command line
cp sixfour.py sixfour
# create install distributions in gzip and zip formats + PKG-INFO file
# python setup.py sdist --formats=gztar,zip