#!/usr/bin/env python3
# Copyright 2021 Matheus Tosta
# See LICENSE file for licensing details.

"""Charm the service.

Refer to the following post for a quick-start guide that will help you
develop a new k8s charm using the Operator Framework:

    https://discourse.charmhub.io/t/4208
"""

import logging

from ops.framework import StoredState
from ops.model import ActiveStatus
from ops.charm import CharmBase
from ops.main import main

from blockbook_ops import BlockbookOps
from ports import open_port
from version import VERSION

logger = logging.getLogger(__name__)


class BlockbookLbCharm(CharmBase):
    """Charm the service."""

    _stored = StoredState()

    def __init__(self, *args):
        super().__init__(*args)

        self.log = logging.getLogger(self.__class__.__name__)

        self._ondemand_ops = BlockbookOps()

        self._stored.set_default(things=[])

        events = {
            self.on.install: self._on_install
        }

        for event, handler in events.items():
            self.framework.observe(event, handler)

    def _on_install(self, event):

        self.unit.set_workload_version(VERSION)

        self.log.info("Installing docker")
        self._ondemand_ops.setup_docker()

        self.log.info("Start blockbook service")
        self._ondemand_ops.setup_blockbook()

        self.log.info("Opening port")
        open_port(19035)

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