# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function
import json


__metaclass__ = type

"""
The aos8 vlans fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""


from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import utils

from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.argspec.vlans.vlans import (
    VlansArgs,
)
from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.rm_templates.vlans import (
    VlansTemplate,
)


class VlansFacts(object):
    """The aos8 vlans facts class"""

    def __init__(self, module):
        self._module = module
        self.argument_spec = VlansArgs.argument_spec

    def get_vlans_data(self, connection):
        return connection.get("show vlan")

    def populate_facts(self, connection, ansible_facts, data=None):
        """Populate the facts for VLANs network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        if not data:
            data = self.get_vlans_data(connection)

        # parse native config using the Interfaces template
        interfaces_parser  = VlansTemplate(lines=data.splitlines(), module=self._module)
        objs = sorted(list(interfaces_parser.parse().values()), key=lambda k, sk="name": k[sk])
        ansible_facts["ansible_network_resources"].pop("vlans", None)
        facts = {"vlans": []}
        params = utils.remove_empties(
            interfaces_parser .validate_config(self.argument_spec, {"config": objs}, redact=True),
        )

        facts["vlans"] = params["config"]
        ansible_facts["ansible_network_resources"].update(facts)

        return ansible_facts