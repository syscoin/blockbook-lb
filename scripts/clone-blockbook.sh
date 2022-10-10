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
    git reset c2d8542bf2f3fc8b0dc16c12c208a555510b08ce --hard