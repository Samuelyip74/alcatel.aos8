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
              ^(?P<vlan_id>[\d]+).*(?P<type>std|spb)\s*(?P<admin>Ena|Dis)\s*(?P<oper>Ena|Dis)\s*(?P<ip>Ena|Dis)\s*(?P<mtu>[\d]+)\s*(?P<name>.*)$
              ''', re.VERBOSE,
            ),
            'setval': 'vlan {{ vlan_id }}',
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
        {
            "name": "description",
            "getval": re.compile(
                r"""
                \s+description\s(?P<description>.+$)
                $""", re.VERBOSE,
            ),
            "setval": "description {{ description }}",
            "result": {
                '{{ name }}': {
                    'description': '{{ description }}',
                },
            },
        },
        {
            "name": "enabled",
            "getval": re.compile(
                r"""
                (?P<negate>\sno)?
                (?P<shutdown>\sshutdown)
                $""", re.VERBOSE,
            ),
            "setval": "shutdown",
            "result": {
                '{{ name }}': {
                    'enabled': "{{ False if shutdown is defined and negate is not defined else True }}",
                },
            },
        },
        {  # only applicable for switches
            "name": "mode",
            "getval": re.compile(
                r"""
                (?P<negate>\sno)?
                (?P<switchport>\sswitchport)
                $""", re.VERBOSE,
            ),
            "setval": "switchport",
            "result": {
                '{{ name }}': {
                    'mode': "{{ 'layer2' if switchport is defined and negate is not defined else 'layer3' }}",
                },
            },
        },
        {
            "name": "speed",
            "getval": re.compile(
                r"""
                \s+speed\s(?P<speed>.+$)
                $""", re.VERBOSE,
            ),
            "setval": "speed {{ speed|string }}",
            "result": {
                '{{ name }}': {
                    'speed': '{{ speed }}',
                },
            },
        },
        {
            "name": "mtu",
            "getval": re.compile(
                r"""
                \s+mtu\s(?P<mtu>.+$)
                $""", re.VERBOSE,
            ),
            "setval": "mtu {{ mtu|string }}",
            "result": {
                '{{ name }}': {
                    'mtu': '{{ mtu }}',
                },
            },
        },
        {
            "name": "duplex",
            "getval": re.compile(
                r"""
                \s+duplex\s(?P<duplex>full|half|auto)
                $""", re.VERBOSE,
            ),
            "setval": "duplex {{ duplex }}",
            "result": {
                '{{ name }}': {
                    'duplex': '{{ duplex }}',
                },
            },
        },
        {
            "name": "template",
            "getval": re.compile(
                r"""
                \s+source\stemplate\s(?P<template>.+$)
                """, re.VERBOSE,
            ),
            "setval": "source template {{ template }}",
            "result": {
                '{{ name }}': {
                    'template': '{{ template }}',
                },
            },
        },
    ]
    # fmt: on