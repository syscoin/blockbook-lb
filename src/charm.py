#!/usr/bin/env python3
# Copyright 2021 Matheus Tosta
# See LICENSE file for licensing details.

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging
import time
import os

from ops.framework import StoredState
from ops.model import ActiveStatus
from ops.charm import CharmBase
from ops.main import main

from blockbook_ops import BlockbookOps
from watcher import Watcher
from ports import open_port
from version import VERSION

logger = logging.getLogger(__name__)


class BlockbookLbCharm(CharmBase):
    """Charm the service."""

    location = '/opt/coins/data/syscoin/backend'

    _stored = StoredState()
    _watcher = Watcher(location)

    def __init__(self, *args):
        super().__init__(*args)

        self.log = logging.getLogger(self.__class__.__name__)

        self._blockbook_ops = BlockbookOps()

        self._stored.set_default(things=[])

        events = {
            self.on.install: self._on_install
        }

        for event, handler in events.items():
            self.framework.observe(event, handler)

    def _on_install(self, event):

        self.log.info("### Path: {}".format(os.getcwd()))

        self.unit.set_workload_version(VERSION)

        self.log.info("##### Installing docker")
        self._blockbook_ops.setup_docker()

        self.log.info("##### Cloning blockbook repo")
        self._blockbook_ops.clone_blockbook()

        self.log.info("##### Building Syscoin backend")
        self._blockbook_ops.build_syscoin_backend()

        self.log.info("##### Installing Syscoin backend")
        self._blockbook_ops.install_syscoin_backend()

        self.log.info("##### Starting Syscoin backend")
        self._blockbook_ops.start_syscoin_backend()

        self.log.info("##### Watching backend to sync")
        for i in range(60 * 50):
            self.log.info("#### Sleep: {}".format(i))
            time.sleep(1)
        # self._watcher(self.log)

        self.log.info("##### Building Syscoin")
        self._blockbook_ops.build_syscoin()

        self.log.info("##### Starting Syscoin Blockbook")
        self._blockbook_ops.start_syscoin()

        self.log.info("##### Opening port")
        open_port(9193)

        self.unit.status = ActiveStatus("Blockbook running")

    def _on_config_changed(self, _):
        # Note: you need to uncomment the example in the config.yaml file for this to work (ensure
        # to not just leave the example, but adapt to your configuration needs)
        current = self.config["thing"]
        if current not in self._stored.things:
            logger.debug("found a new thing: %r", current)
            self._stored.things.append(current)

    def _on_fortune_action(self, event):
        # Note: you need to uncomment the example in the actions.yaml file for this to work (ensure
        # to not just leave the example, but adapt to your needs for actions commands)
        fail = event.params["fail"]
        if fail:
            event.fail(fail)
        else:
            event.set_results({"fortune": "A bug in the code is worth two in the documentation."})


if __name__ == "__main__":
    main(BlockbookLbCharm)
