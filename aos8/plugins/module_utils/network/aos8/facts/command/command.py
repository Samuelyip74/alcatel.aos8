# -*- coding: utf-8 -*-
# Copyright 2023 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function

__metaclass__ = type

"""
The aos8 command fact class
It is in this file the configuration is collected from the device
for a given resource, parsed, and the facts tree is populated
based on the configuration.
"""

from copy import deepcopy

from ansible.module_utils.six import iteritems
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common import (
    utils,
)
from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.rm_templates.command import (
    CommandTemplate,
)
from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.argspec.command.command import (
    CommandArgs,
)

class CommandFacts(object):
    """ The aos8 command facts class
    """

    def __init__(self, module, subspec='config', options='options'):
        self._module = module
        self.argument_spec = CommandArgs.argument_spec

    def populate_facts(self, connection, ansible_facts, data=None):
        """ Populate the facts for Command network resource

        :param connection: the device connection
        :param ansible_facts: Facts dictionary
        :param data: previously collected conf

        :rtype: dictionary
        :returns: facts
        """
        facts = {}
        objs = []

        if not data:
            data = connection.get()

        # parse native config using the Command template
        command_parser = CommandTemplate(lines=data.splitlines(), module=self._module)
        objs = list(command_parser.parse().values())

        ansible_facts['ansible_network_resources'].pop('command', None)

        params = utils.remove_empties(
            command_parser.validate_config(self.argument_spec, {"config": objs}, redact=True)
        )

        facts['command'] = params['config']
        ansible_facts['ansible_network_resources'].update(facts)

        return ansible_facts
