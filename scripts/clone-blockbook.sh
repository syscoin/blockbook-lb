#!/bin/sh

apt-get update -y && \
    apt-get upgrade -y && \
    apt-get install -y \
      python3 \
      python3-pip \
      make git

pip3 install watchgod

git clone https://github.com/syscoin/blockbook.git

cd blockbook && \
    git reset 3b9a4860567d3fab73c22199bfe1c192add5959f --hard