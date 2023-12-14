# -*- coding: utf-8 -*-
# Copyright 2022 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

from __future__ import absolute_import, division, print_function


__metaclass__ = type

"""
The Interfaces parser templates file. This contains
a list of parser definitions and associated functions that
facilitates both facts gathering and native command generation for
the given network resource.
"""

import re

from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.rm_base.network_template import (
    NetworkTemplate,
)


class VlansTemplate(NetworkTemplate):
    def __init__(self, lines=None, module=None):
        super(VlansTemplate, self).__init__(lines=lines, tmplt=self, module=module)

    # fmt: off
    PARSERS = [
        {
            'name': 'vlan_id',
            'getval': re.compile(
                r'''
              ^(?P<vlan_id>[\d]+).*(?P<type>std)\s*(?P<admin>Ena|Dis)\s*(?P<oper>Ena|Dis)\s*(?P<ip>Ena|Dis)\s*(?P<mtu>[\d]+)\s*(?P<name>.*)$
              ''', re.VERBOSE,
            ),
            'setval': 'vlan {{ vlan_id }} admin-state {{ admin }} name {{ name }} ',
            'result': {
                '{{ vlan_id }}': {
                    'vlan_id': '{{ vlan_id }}',
                    'name': '{{ name }}',
                    'mtu': '{{ mtu }}',
                    'admin': '{{ admin }}',
                },
            },
            'shared': True,
        },
    ]
    # fmt: on