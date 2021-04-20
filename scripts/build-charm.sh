#!/bin/sh

# make sure charmcraft is installed and install packages
pip3 install charmcraft
pip3 install -r requirements.txt

# build charm
charmcraft build --verbose