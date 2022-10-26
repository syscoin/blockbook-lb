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
    git reset dfc9413b3df273004378b215c5c33b3149c09163 --hard