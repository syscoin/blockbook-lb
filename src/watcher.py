from typing import Any
import logging
import sys

from watchgod import watch


class Watcher:

    def __init__(self, location: str) -> None:
        self.location = location
        pass

    def __call__(self, logger: logging.Logger, *args: Any, **kwds: Any) -> Any:

        logger.info("##### Start search for change in backend status")

        for changes in watch(self.location):

            logger.info("##### Change detected")
            
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

                if round(float(dct["progress"]), 2) == 0.2:
                    logger.info("##### Sync in 20%")

                if round(float(dct["progress"]), 2) == 0.4:
                    logger.info("##### Sync in 40%")

                if round(float(dct["progress"]), 2) == 0.6:
                    logger.info("##### Sync in 60%")
                    
                if round(float(dct["progress"]), 2) == 0.8:
                    logger.info("##### Sync in 80%")
                
                if float(dct["progress"]) == 1.0:
                    logger.info("##### Sync done. Exiting")
                    sys.exit()