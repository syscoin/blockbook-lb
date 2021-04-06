from watchgod import watch
import sys
import re

location = '/opt/coins/data/syscoin_testnet/backend/testnet3'

for changes in watch(location):
    
    if (list(changes)[0][1]).split('/')[-1] == 'debug.log':
        f = open(list(changes)[0][1], 'r')
        text = f.readlines()[-1]
        dct = dict(map(
            lambda pair: tuple(pair),
            map(
                lambda _split: _split.split("="),
                filter(
                    lambda split: len(split.split("=")) == 2,
                    text.split(" ")
                )
            )
        ))
        
        if float(dct["progress"]) == 1.0000000:
            sys.exit()