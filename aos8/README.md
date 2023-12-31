# Alcatel AOS8 Collection

[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/alcatel.aos8)
[![Codecov](https://codecov.io/gh/ansible-collections/alcatel.aos8/branch/main/graph/badge.svg)](https://codecov.io/gh/ansible-collections/alcatel.aos8)
[![CI](https://github.com/ansible-collections/alcatel.aos8/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/ansible-collections/alcatel.aos8/actions/workflows/tests.yml)

The Ansible Alcatel AOS 8 collection includes a variety of Ansible content to help automate the management of Alcatel AOS 8 netowork appliances.

This collection has been tested against Alcatel AOS 8.9.221.R03 GA.


<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.14.0**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `alcatel.aos8.aos8`).
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

### Supported connections

The Alcatel AOS 8 collection supports `network_cli` connections.

## Included content

<!--start collection content-->
### Cliconf plugins
Name | Description
--- | ---
[alcatel.aos8.aos8](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_cliconf.rst)|Use aos8 cliconf to run command on Alcatel AOS 8 platform

### Modules
Name | Description
--- | ---
[alcatel.aos8.aos8_command](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_command_module.rst)|Module to run commands on remote devices.
[alcatel.aos8.aos8_facts](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_facts_module.rst)|Module to collect facts from remote devices.
[alcatel.aos8.aos8_hostname](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_hostname_module.rst)|Resource module to configure hostname.
[alcatel.aos8.aos8_l2_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_l2_interfaces_module.rst)|Resource module to configure L2 interfaces.
[alcatel.aos8.aos8_vlans](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_vlans_module.rst)|Resource module to configure VLANs.


<!--end collection content-->

## Installing this collection

You can install the Alcatel AOS 8 collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install alcatel.aos8  
    ansible-galaxy collection install alcatel-aos8-<version>.tar.gz --force

You can also include it in a `requirements.yml` file and install it with `ansible-galaxy collection install -r requirements.yml`, using the format:

```yaml
---
collections:
  - name: alcatel.aos8
```

## Using this collection

This collection includes [network resource modules](https://docs.ansible.com/ansible/latest/network/user_guide/network_resource_modules.html).

### Using modules from the Alcatel AOS 8 collection in your playbooks

You can call modules by their Fully Qualified Collection Namespace (FQCN), such as `alcatel.aos8.aos8_l2_interfaces`.
The following example task replaces configuration changes in the existing configuration on a Alcatel AOS 8 network device, using the FQCN:

```yaml
---
- name: Replace device configuration of specified L2 interfaces with provided configuration.
  alcatel.aos8.aos8_l2_interfaces:
    config:
      - vlan_id: 20
        port_type: port
        port_number: 1/1/27
        mode: tagged  
    state: merged
```

**NOTE**: For Ansible 2.9, you may not see deprecation warnings when you run your playbooks with this collection. Use this documentation to track when a module is deprecated.

### See Also:

- [Alcatel AOS 8 Platform Options](https://docs.ansible.com/ansible/latest/network/user_guide/platform_aos8.html)
- [Ansible Using collections](https://docs.ansible.com/ansible/latest/user_guide/collections_using.html) for more details.

## Contributing to this collection

We welcome community contributions to this collection. If you find problems, please open an issue or create a PR against the [Alcatel AOS 8 collection repository](https://github.com/ansible-collections/alcatel.aos8). See [Contributing to Ansible-maintained collections](https://docs.ansible.com/ansible/devel/community/contributing_maintained_collections.html#contributing-maintained-collections) for complete details.

You can also join us on:

- IRC - the `#ansible-network` [libera.chat](https://libera.chat/) channel
- Slack - https://ansiblenetwork.slack.com

See the [Ansible Community Guide](https://docs.ansible.com/ansible/latest/community/index.html) for details on contributing to Ansible.

### Code of Conduct

This collection follows the Ansible project's
[Code of Conduct](https://docs.ansible.com/ansible/devel/community/code_of_conduct.html).
Please read and familiarize yourself with this document.

## Release notes

<!--Add a link to a changelog.md file or an external docsite to cover this information. -->

Release notes are available [here](https://github.com/ansible-collections/alcatel.aos8/blob/main/CHANGELOG.rst).

## Roadmap

<!-- Optional. Include the roadmap for this collection, and the proposed release/versioning strategy so users can anticipate the upgrade/update cycle. -->

## More information

- [Ansible network resources](https://docs.ansible.com/ansible/latest/network/getting_started/network_resources.html)
- [Ansible Collection Overview](https://github.com/ansible-collections/overview)
- [Ansible User guide](https://docs.ansible.com/ansible/latest/user_guide/index.html)
- [Ansible Developer Guide](https://docs.ansible.com/ansible/latest/dev_guide/index.html)
- [Ansible Community Code of Conduct](https://docs.ansible.com/ansible/latest/community/code_of_conduct.html)

## Licensing

GNU General Public License v3.0 or later.

See [LICENSE](https://www.gnu.org/licenses/gpl-3.0.txt) to see the full text.