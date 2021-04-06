import subprocess
import logging
import os

class BlockbookOps:

    def __init__(self) -> None:
        self.name = "BlockbookOps"

    def setup_docker(self):
        """
        Utility method to install and setup [docker](https://www.docker.com/)
        """

        # check whether docker has been already installed
        try:

            subprocess.call(["docker", "version"])

        except Exception as e:

            # install docker via bash script
            subprocess.call(["sh", os.path.join("scripts", "get-docker.sh")])

            pass

    def setup_blockbook(self):
        """
        Utility method to start blockbook service
        """

        subprocess.call(["sh", os.path.join("scripts", "build-blockbook.sh")])