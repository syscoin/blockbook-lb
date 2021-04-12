from re import sub
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

    def clone_blockbook(self):
        """
        Utility method to start blockbook service
        """

        subprocess.call(["sudo", "sh", os.path.join("scripts", "clone-blockbook.sh")])

    def build_syscoin_testnet_backend(self):

        subprocess.call(["sudo", "sh", os.path.join("scripts", "build-backend.sh")])

    def install_syscoin_testnet_backend(self):

        subprocess.call(["sudo", "sh", os.path.join("scripts", "install-backend.sh")])

    def start_syscoin_testnet_backend(self):

        subprocess.call([
            "sudo", "systemctl", "start", "backend-syscoin-testnet.service"
        ])

    def build_syscoin_testnet(self):

        subprocess.call(["sudo", "sh", os.path.join("scripts", "build-app.sh")])

    def start_syscoin_testnet(self):

        subprocess.call([
            "sudo", "systemctl", "start", "blockbook-syscoin-testnet.service"
        ])