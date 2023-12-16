#!/usr/bin/python
#
# This file is part of Ansible
#
# Ansible is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Ansible is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Ansible.  If not, see <http://www.gnu.org/licenses/>.
#
"""
The module file for aos8_vlans
"""
from __future__ import absolute_import, division, print_function


__metaclass__ = type

DOCUMENTATION = """
module: aos8_vlans
short_description: Resource module to configure VLANs on AOS8 devices
description:
  This module provides declarative management of VLANs on Cisco aos8 network
  devices.
version_added: 1.0.0
author: Samuel Yip (@samuelyip)
notes:
  - Tested against Alcatel-Lucent AOS8 OmniSwitch with Version 8.9.221.R03 GA.
  - This module works with connection C(network_cli).
options:
  config:
    description: A dictionary of VLANs options
    type: list
    elements: dict
    suboptions:
      name:
        description:
          - Ascii name of the VLAN.
          - NOTE, I(name) should not be named/appended with I(default) as it is reserved
            for device default vlans.
        type: str
      vlan_id:
        description:
          - ID of the VLAN. Range 1-4094
        type: int
        required: true
      mtu:
        description:
          - VLAN Maximum Transmission Unit.
          - Refer to vendor documentation for valid values.
        type: int
      admin:
        description:
          - Administration state of the VLAN
        type: str
        choices:
          - enable
          - disable
  running_config:
    description:
      - This option is used only with state I(parsed).
      - The value of this option should be the output received from the aos8 device
        by executing the command B(show vlan).
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into Ansible structured data as per the resource module's argspec
        and the value is then returned in the I(parsed) key within the result.
    type: str
  state:
    description:
      - The state the configuration should be left in
      - The states I(rendered), I(gathered) and I(parsed) does not perform any change
        on the device.
      - The state I(rendered) will transform the configuration in C(config) option to
        platform specific CLI commands which will be returned in the I(rendered) key
        within the result. For state I(rendered) active connection to remote host is
        not required.
      - The state I(gathered) will fetch the running configuration from device and transform
        it into structured data in the format as per the resource module argspec and
        the value is returned in the I(gathered) key within the result.
      - The state I(parsed) reads the configuration from C(running_config) option and
        transforms it into JSON format as per the resource module parameters and the
        value is returned in the I(parsed) key within the result. The value of C(running_config)
        option should be the same format as the output of command I(show running-config
        | include ip route|ipv6 route) executed on device. For state I(parsed) active
        connection to remote host is not required.
    type: str
    choices:
      - merged
      - replaced
      - overridden
      - deleted
      - rendered  
      - gathered
      - parsed
    default: merged
"""

EXAMPLES = """
# Using merged

# Before state:
# -------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT

---
- hosts: all
  gather_facts: true
  ignore_errors: true
  tasks:
    - name: Run merged VLAN with existing VLANs
      alcatel.aos8.aos8_vlans:
        config:
          - vlan_id: 33
            name: "Vlan 33"
            admin: enable
            mtu: 1280
          - vlan_id: 99
            name: "Vlan 99"
            admin: enable
      configuration: false
      state: merged


# After state:
# ------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33
# 99     std       Ena     Dis   Dis    1500    Vlan_99

# results
# changed: [192.168.70.1] => {
#     "after": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1280,
#             "name": "Vlan_33",
#             "operational_state": "disable",
#             "vlan_id": 33
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan_99",
#             "operational_state": "disable",
#             "vlan_id": 99
#         },
#     ],
#     "before": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#     ],
#     "changed": true,
#     "commands": [
#         "vlan 33 name Vlan_33",
#         "vlan 33 admin-state enable",
#         "vlan 33 mtu-ip 1280",
#         "vlan 99 name Vlan_99",
#         "vlan 99 admin-state enable",
#         "vlan 99 mtu-ip 1500"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#                 {
#                     "admin": "enable",
#                     "mtu": 1280,
#                     "name": "Vlan_33",
#                     "operational_state": null,
#                     "vlan_id": 33
#                 },
#                 {
#                     "admin": "enable",
#                     "mtu": 1500,
#                     "name": "Vlan_99",
#                     "operational_state": null,
#                     "vlan_id": 99
#                 }
#             ],
#             "configuration": false,
#             "running_config": null,
#             "state": "merged"
#         }
#     }
# }

# Using overridden

# Before state:
# -------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33
# 99     std       Ena     Dis   Dis    1500    Vlan_99

# - name: Override device configuration of all VLANs with provided configuration
#   alcatel.aos8.aos8_vlans:
#     config:
#       - vlan_id: 1
#         name: MGNT
#         mtu: 1500
#       - vlan_id: 33
#         name: Vlan_33
#         mtu: 1280
#     state: overridden

# After state:
# ------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33

#     "after": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan_33",
#             "operational_state": "enable",
#             "vlan_id": 33
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan 99",
#             "operational_state": "disable",
#             "vlan_id": 99
#         }
#     ],
#     "changed": true,
#     "commands": [
#         "no vlan 99"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan_33",
#             "operational_state": "enable",
#             "vlan_id": 33
#         },
#             ],
#             "running_config": null,
#             "state": "overridden"
#         }
#     }
# }

# Using replaced

# Before state:
# -------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33

- name: Replaces device configuration of listed VLANs with provided configuration
  alcatel.aos8.aos8_vlans:
    config:
      - vlan_id: 33
        name: "Vlan 33"
        admin: enable
        mtu: 1500
      - vlan_id: 99
        name: "Vlan 99"
        admin: enable
    state: replaced

# After state:
# ------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33
# 99     std       Ena     Dis   Ena    1500    Vlan_99

#     "after": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan 33",
#             "operational_state": "disable",
#             "vlan_id": 33
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan 99",
#             "operational_state": "disable",
#             "vlan_id": 99
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Ucopia",
#             "operational_state": "enable",
#             "vlan_id": 200
#         },
#     ],
#     "before": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1280,
#             "name": "Vlan 33",
#             "operational_state": "disable",
#             "vlan_id": 33
#         },
#     ],
#     "changed": true,
#     "commands": [
#         "vlan 33 name \"Vlan 33\"",
#         "vlan 33 admin-state enable",
#         "vlan 33 mtu-ip 1500",
#         "vlan 99 name \"Vlan 99\"",
#         "vlan 99 admin-state enable",
#         "vlan 99 mtu-ip 1500"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#                 {
#                     "admin": "enable",
#                     "mtu": 1500,
#                     "name": "Vlan 33",
#                     "operational_state": null,
#                     "vlan_id": 33
#                 },
#                 {
#                     "admin": "enable",
#                     "mtu": 1500,
#                     "name": "Vlan 99",
#                     "operational_state": null,
#                     "vlan_id": 99
#                 }
#             ],
#             "running_config": null,
#             "state": "replaced"
#         }
#     }
# }

# Using deleted

# Before state:
# -------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT
# 33     std       Ena     Dis   Ena    1280    Vlan_33
# 99     std       Ena     Dis   Ena    1500    Vlan_99

  - name: Run VLAN resource module with state deleted
    alcatel.aos8.aos8_vlans:
      config:
        - vlan_id: 33
        - vlan_id: 99
      state: deleted


# After state:
# -------------
#
# ACSW01-> show vlan
#  vlan    type   admin   oper    ip    mtu          name
# ------+-------+-------+------+------+------+------------------
# 1      std       Ena     Ena   Ena    1500    MGNT

#     "after": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#     ],
#     "before": [
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "MGNT",
#             "operational_state": "enable",
#             "vlan_id": 1
#         },
#         {
#             "admin": "enable",
#             "mtu": 1280,
#             "name": "Vlan 33",
#             "operational_state": "disable",
#             "vlan_id": 33
#         },
#         {
#             "admin": "enable",
#             "mtu": 1500,
#             "name": "Vlan 99",
#             "operational_state": "disable",
#             "vlan_id": 99
#         },
#     ],
#     "changed": true,
#     "commands": [
#         "no vlan 33",
#         "no vlan 99"
#     ],
#     "invocation": {
#         "module_args": {
#             "config": [
#                 {
#                     "admin": "enable",
#                     "mtu": 1500,
#                     "name": null,
#                     "operational_state": null,
#                     "vlan_id": 33
#                 },
#                 {
#                     "admin": "enable",
#                     "mtu": 1500,
#                     "name": null,
#                     "operational_state": null,
#                     "vlan_id": 99
#                 }
#             ],
#             "running_config": null,
#             "state": "deleted"
#         }
#     }
# }


# Using Gathered (configuration: True)

# Before state:
# -------------
#
# Leaf-01#show run nve | sec ^vlan configuration
# vlan configuration 101
#  member evpn-instance 101 vni 10101
# vlan configuration 102
#  member evpn-instance 102 vni 10102
# vlan configuration 201
#  member evpn-instance 201 vni 10201
# vlan configuration 202
#  member evpn-instance 202 vni 10202
# vlan configuration 901
#  member vni 50901

- name: Gather listed vlans with provided configurations
  alcatel.aos8.aos8_vlans:
    config:
    configuration: true
    state: gathered

# Module Execution Result:
# ------------------------
#
# gathered = [
#     {
#         "member": {
#             "evi": 101,
#             "vni": 10101
#         },
#         "vlan_id": 101
#     },
#     {
#         "member": {
#             "evi": 102,
#             "vni": 10102
#         },
#         "vlan_id": 102
#     },
#     {
#         "member": {
#             "evi": 201,
#             "vni": 10201
#         },
#         "vlan_id": 201
#     },
#     {
#         "member": {
#             "evi": 202,
#             "vni": 10202
#         },
#         "vlan_id": 202
#     },
#     {
#         "member": {
#             "vni": 50901
#         },
#         "vlan_id": 901
#     },
#     {
#         "member": {
#             "vni": 50902
#         },
#         "vlan_id": 902
#     }
# ]

# Using Rendered

- name: Render the commands for provided  configuration
  alcatel.aos8.aos8_vlans:
    config:
      - name: Vlan_10
        vlan_id: 10
        state: active
        shutdown: disabled
        remote_span: true
      - name: Vlan_20
        vlan_id: 20
        mtu: 610
        state: active
        shutdown: enabled
      - name: Vlan_30
        vlan_id: 30
        state: suspend
        shutdown: enabled
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#         "vlan 10",
#         "name Vlan_10",
#         "state active",
#         "remote-span",
#         "no shutdown",
#         "vlan 20",
#         "name Vlan_20",
#         "state active",
#         "mtu 610",
#         "shutdown",
#         "vlan 30",
#         "name Vlan_30",
#         "state suspend",
#         "shutdown"
#     ]

# Using Rendered (configuration: True)

- name: Render the commands for provided  configuration
  alcatel.aos8.aos8_vlans:
    config:
      - vlan_id: 101
        member:
          vni: 10101
          evi: 101
      - vlan_id: 102
        member:
          vni: 10102
          evi: 102
    state: rendered

# Module Execution Result:
# ------------------------
#
# "rendered": [
#     "vlan configuration 101",
#     "member evpn-instance 101 vni 10101",
#     "vlan configuration 102",
#     "member evpn-instance 102 vni 10102"
# ]

# Using Parsed

# File: parsed.cfg
# ----------------
#
# VLAN Name                             Status    Ports
# ---- -------------------------------- --------- -------------------------------
# 1    default                          active    Gi0/1, Gi0/2
# 10   vlan_10                          active
# 20   vlan_20                          act/lshut
# 30   vlan_30                          sus/lshut
# 1002 fddi-default                     act/unsup
# 1003 token-ring-default               act/unsup
# 1004 fddinet-default                  act/unsup
# 1005 trnet-default                    act/unsup
#
# VLAN Type  SAID       MTU   Parent RingNo BridgeNo Stp  BrdgMode Trans1 Trans2
# ---- ----- ---------- ----- ------ ------ -------- ---- -------- ------ ------
# 1    enet  100001     1500  -      -      -        -    -        0      0
# 10   enet  100010     1500  -      -      -        -    -        0      0
# 20   enet  100020     1500  -      -      -        -    -        0      0
# 30   enet  100030     1500  -      -      -        -    -        0      0
# 1002 fddi  101002     1500  -      -      -        -    -        0      0
# 1003 tr    101003     1500  -      -      -        -    -        0      0
# 1004 fdnet 101004     1500  -      -      -        ieee -        0      0
# 1005 trnet 101005     1500  -      -      -        ibm  -        0      0

- name: Parse the commands for provided configuration
  alcatel.aos8.aos8_vlans:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#         {
#             "mtu": 1500,
#             "name": "default",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 1
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_10",
#             "shutdown": "disabled",
#             "state": "active",
#             "vlan_id": 10
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_20",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 20
#         },
#         {
#             "mtu": 1500,
#             "name": "vlan_30",
#             "shutdown": "enabled",
#             "state": "suspend",
#             "vlan_id": 30
#         },
#         {
#             "mtu": 1500,
#             "name": "fddi-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1002
#         },
#         {
#             "mtu": 1500,
#             "name": "token-ring-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1003
#         },
#         {
#             "mtu": 1500,
#             "name": "fddinet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1004
#         },
#         {
#             "mtu": 1500,
#             "name": "trnet-default",
#             "shutdown": "enabled",
#             "state": "active",
#             "vlan_id": 1005
#         }
#     ]

# Using Parsed (configuration: True)

# File: parsed.cfg
# ----------------
#
# vlan configuration 101
#  member evpn-instance 101 vni 10101
# vlan configuration 102
#  member evpn-instance 102 vni 10102
# vlan configuration 901
#  member vni 50901

- name: Parse the commands for provided configuration
  alcatel.aos8.aos8_vlans:
    running_config: "{{ lookup('file', './parsed.cfg') }}"
    configuration: true
    state: parsed

# Module Execution Result:
# ------------------------
#
# "parsed": [
#     {
#         "member": {
#             "evi": 101,
#             "vni": 10101
#         },
#         "vlan_id": 101
#     },
#     {
#         "member": {
#             "evi": 102,
#             "vni": 10102
#         },
#         "vlan_id": 102
#     },
#     {
#         "member": {
#             "vni": 50901
#         },
#         "vlan_id": 901
#     }
# ]
"""

RETURN = """
before:
  description: The configuration as structured data prior to module invocation.
  returned: always
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
after:
  description: The configuration as structured data after module completion.
  returned: when changed
  type: list
  sample: >
    The configuration returned will always be in the same format
     of the parameters above.
commands:
  description: The set of commands pushed to the remote device.
  returned: always
  type: list
  sample: ['vlan 20', 'name vlan_20', 'mtu 600', 'remote-span']
"""
from ansible.module_utils.basic import AnsibleModule

from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.argspec.vlans.vlans import (
    VlansArgs,
)
from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.config.vlans.vlans import Vlans


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    required_if = [
        ("state", "merged", ("config",)),
        ("state", "replaced", ("config",)),
        ("state", "overridden", ("config",)),
        ("state", "rendered", ("config",)),
        ("state", "parsed", ("running_config",)),
    ]
    mutually_exclusive = [("config", "running_config")]

    module = AnsibleModule(
        argument_spec=VlansArgs.argument_spec,
        required_if=required_if,
        mutually_exclusive=mutually_exclusive,
        supports_check_mode=True,
    )

    result = Vlans(module).execute_module()
    module.exit_json(**result)

if __name__ == "__main__":
    main()