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
    git reset f10def21c023f764d4d6da325912a6128bc75031 --hard