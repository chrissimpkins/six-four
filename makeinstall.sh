#!/bin/sh

# Used to create source distributions that can be installed with the following command:
# python setup.py install

# create the main script that will run from the command line
cp sixfour.py sixfour
# create install distributions in gzip and zip formats + PKG-INFO file
# python setup.py sdist --formats=gztar,zip