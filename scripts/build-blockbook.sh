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
    git reset d27b218c1e0190edf5476dbd06d549ac77d993d1 --hard

make all-syscoin_testnet

cd build && \
    apt install -y ./backend-syscoin-testnet_4.2.0.14-satoshilabs-1_amd64.deb

systemctl start backend-syscoin-testnet.service

cd ../../

python3 watcher.py

cd blockbook/build && \
    apt install -y ./blockbook-syscoin-testnet_0.3.54_amd64.deb

systemctl start blockbook-syscoin-testnet.service