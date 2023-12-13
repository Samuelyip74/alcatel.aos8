#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright 2023 Red Hat
# GNU General Public License v3.0+
# (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

"""
The module file for aos8_command
"""

from __future__ import absolute_import, division, print_function

__metaclass__ = type

DOCUMENTATION = """
---
GENERATOR_VERSION: '1.0'

NETWORK_OS: aos8
RESOURCE: command
COPYRIGHT: Copyright 2019 Red Hat
LICENSE: gpl-3.0.txt

DOCUMENTATION: |
module: aos8_command
author: Samuel Yip
short_description: Module to run commands on remote devices.
description:
  - Sends arbitrary commands to an aos8 node and returns the results read from the device.
    This module includes an argument that will cause the module to wait for a specific
    condition before returning or timing out if the condition is not met.
  - This module does not automatically save the configuration into memory and flash. 
version_added: 1.0.0
notes:
  - Tested against Alcatel AOS8 8.9.221.R03 GA.
  - This module works with connection C(network_cli).
    See U(https://docs.ansible.com/ansible/latest/network/user_guide/platform_aos8.html)
options:
  commands:
    description:
      - List of commands to send to the remote aos8 device over the configured provider.
        The resulting output from the command is returned. If the I(wait_for) argument
        is provided, the module is not returned until the condition is satisfied or
        the number of retries has expired. If a command sent to the device requires
        answering a prompt, it is possible to pass a dict containing I(command), I(answer)
        and I(prompt). Common answers are 'y' or "\\r" (carriage return, must be double
        quotes). See examples.
    required: true
    type: list
    elements: raw
  wait_for:
    description:
      - List of conditions to evaluate against the output of the command. The task will
        wait for each condition to be true before moving forward. If the conditional
        is not true within the configured number of retries, the task fails. See examples.
    aliases:
      - waitfor
    type: list
    elements: str
  match:
    description:
      - The I(match) argument is used in conjunction with the I(wait_for) argument to
        specify the match policy.  Valid values are C(all) or C(any).  If the value
        is set to C(all) then all conditionals in the wait_for must be satisfied.  If
        the value is set to C(any) then only one of the values must be satisfied.
    default: all
    type: str
    choices:
      - any
      - all
  retries:
    description:
      - Specifies the number of retries a command should by tried before it is considered
        failed. The command is run on the target device every retry and evaluated against
        the I(wait_for) conditions.
    default: 9
    type: int
  interval:
    description:
      - Configures the interval in seconds to wait between retries of the command. If
        the command does not pass the specified conditions, the interval indicates how
        long to wait before trying the command again.
    default: 1
    type: int

EXAMPLES:
- name: Run show version on remote devices
  alcatel.aos8.aos8_command:
    commands: show system

- name: Run show version and check to see if output contains aos8
  alcatel.aos8.aos8_command:
    commands: show system
    wait_for: result[0] contains aos8

- name: Run multiple commands on remote nodes
  alcatel.aos8.aos8_command:
    commands:
      - show system
      - show interfaces

- name: Run multiple commands and evaluate the output
  alcatel.aos8.aos8_command:
    commands:
      - show system
      - show interfaces
    wait_for:
      - result[0] contains aos8
      - result[1] contains Loopback0
"""

EXAMPLES = """

"""

RETURN = """
before:
  description: The configuration prior to the module execution.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
after:
  description: The resulting configuration after module execution.
  returned: when changed
  type: dict
  sample: >
    This output will always be in the same format as the
    module argspec.
commands:
  description: The set of commands pushed to the remote device.
  returned: when I(state) is C(merged), C(replaced), C(overridden), C(deleted) or C(purged)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
rendered:
  description: The provided configuration in the task rendered in device-native format (offline).
  returned: when I(state) is C(rendered)
  type: list
  sample:
    - sample command 1
    - sample command 2
    - sample command 3
gathered:
  description: Facts about the network resource gathered from the remote device as structured data.
  returned: when I(state) is C(gathered)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
parsed:
  description: The device native config provided in I(running_config) option parsed into structured data as per module argspec.
  returned: when I(state) is C(parsed)
  type: list
  sample: >
    This output will always be in the same format as the
    module argspec.
"""
import time
from ansible.module_utils._text import to_text
from ansible.module_utils.basic import AnsibleModule
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.parsing import (
    Conditional,
)
from ansible_collections.ansible.netcommon.plugins.module_utils.network.common.utils import (
    to_lines,
    transform_commands,
)
from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.argspec.command.command import (
    CommandArgs,
)

from ansible_collections.alcatel.aos8.plugins.module_utils.network.aos8.aos8 import run_commands

def parse_commands(module, warnings):
    commands = transform_commands(module)
    if module.check_mode:
        for item in list(commands):
            if not item["command"].startswith("show"):
                warnings.append(
                    "Only show commands are supported when using check mode, not executing %s"
                    % item["command"],
                )
                commands.remove(item)
    return commands


def main():
    """
    Main entry point for module execution

    :returns: the result form module invocation
    """
    module = AnsibleModule(
        argument_spec=CommandArgs.argument_spec,
        supports_check_mode=True,
    ) 
    warnings = list()
    result = {"changed": False, "warnings": warnings}
    commands = parse_commands(module, warnings)
    responses = run_commands(module, commands)

    module.params["output"] = list(to_lines(responses))

    result.update({"stdout": responses, "stdout_lines": list(to_lines(responses))})
    module.exit_json(**result)

if __name__ == "__main__":
    main()
