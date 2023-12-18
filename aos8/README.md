# Alcatel AOS8 Collection

[![CI](https://zuul-ci.org/gated.svg)](https://dashboard.zuul.ansible.com/t/ansible/project/github.com/ansible-collections/alcatel.aos8)
[![Codecov](https://codecov.io/gh/ansible-collections/alcatel.aos8/branch/main/graph/badge.svg)](https://codecov.io/gh/ansible-collections/alcatel.aos8)
[![CI](https://github.com/ansible-collections/alcatel.aos8/actions/workflows/tests.yml/badge.svg?branch=main&event=schedule)](https://github.com/ansible-collections/alcatel.aos8/actions/workflows/tests.yml)

The Ansible Alcatel AOS 8 collection includes a variety of Ansible content to help automate the management of Alcatel AOS 8 netowork appliances.

This collection has been tested against Alcatel AOS 8.9.R01 on CML.

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
[alcatel.aos8.aos8_acl_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_acl_interfaces_module.rst)|Resource module to configure ACL interfaces.
[alcatel.aos8.aos8_acls](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_acls_module.rst)|Resource module to configure ACLs.
[alcatel.aos8.aos8_banner](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_banner_module.rst)|Module to configure multiline banners.
[alcatel.aos8.aos8_bgp_address_family](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_bgp_address_family_module.rst)|Resource module to configure BGP Address family.
[alcatel.aos8.aos8_bgp_global](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_bgp_global_module.rst)|Resource module to configure BGP.
[alcatel.aos8.aos8_command](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_command_module.rst)|Module to run commands on remote devices.
[alcatel.aos8.aos8_config](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_config_module.rst)|Module to manage configuration sections.
[alcatel.aos8.aos8_evpn_evi](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_evpn_evi_module.rst)|Resource module to configure L2VPN EVPN EVI.
[alcatel.aos8.aos8_evpn_global](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_evpn_global_module.rst)|Resource module to configure L2VPN EVPN.
[alcatel.aos8.aos8_facts](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_facts_module.rst)|Module to collect facts from remote devices.
[alcatel.aos8.aos8_hostname](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_hostname_module.rst)|Resource module to configure hostname.
[alcatel.aos8.aos8_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_interfaces_module.rst)|Resource module to configure interfaces.
[alcatel.aos8.aos8_l2_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_l2_interfaces_module.rst)|Resource module to configure L2 interfaces.
[alcatel.aos8.aos8_l3_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_l3_interfaces_module.rst)|Resource module to configure L3 interfaces.
[alcatel.aos8.aos8_lacp](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lacp_module.rst)|Resource module to configure LACP.
[alcatel.aos8.aos8_lacp_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lacp_interfaces_module.rst)|Resource module to configure LACP interfaces.
[alcatel.aos8.aos8_lag_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lag_interfaces_module.rst)|Resource module to configure LAG interfaces.
[alcatel.aos8.aos8_linkagg](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_linkagg_module.rst)|Module to configure link aggregation groups.
[alcatel.aos8.aos8_lldp](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lldp_module.rst)|(deprecated, removed after 2024-06-01) Manage LLDP configuration on Alcatel AOS 8 network devices.
[alcatel.aos8.aos8_lldp_global](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lldp_global_module.rst)|Resource module to configure LLDP.
[alcatel.aos8.aos8_lldp_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_lldp_interfaces_module.rst)|Resource module to configure LLDP interfaces.
[alcatel.aos8.aos8_logging_global](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_logging_global_module.rst)|Resource module to configure logging.
[alcatel.aos8.aos8_ntp](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ntp_module.rst)|(deprecated, removed after 2024-01-01) Manages core NTP configuration.
[alcatel.aos8.aos8_ntp_global](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ntp_global_module.rst)|Resource module to configure NTP.
[alcatel.aos8.aos8_ospf_interfaces](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ospf_interfaces_module.rst)|Resource module to configure OSPF interfaces.
[alcatel.aos8.aos8_ospfv2](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ospfv2_module.rst)|Resource module to configure OSPFv2.
[alcatel.aos8.aos8_ospfv3](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ospfv3_module.rst)|Resource module to configure OSPFv3.
[alcatel.aos8.aos8_ping](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_ping_module.rst)|Tests reachability using ping from aos8 switch.
[alcatel.aos8.aos8_prefix_lists](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_prefix_lists_module.rst)|Resource module to configure prefix lists.
[alcatel.aos8.aos8_route_maps](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_route_maps_module.rst)|Resource module to configure route maps.
[alcatel.aos8.aos8_service](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_service_module.rst)|Resource module to configure service.
[alcatel.aos8.aos8_snmp_server](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_snmp_server_module.rst)|Resource module to configure snmp server.
[alcatel.aos8.aos8_static_routes](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_static_routes_module.rst)|Resource module to configure static routes.
[alcatel.aos8.aos8_system](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_system_module.rst)|Module to manage the system attributes.
[alcatel.aos8.aos8_user](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_user_module.rst)|Module to manage the aggregates of local users.
[alcatel.aos8.aos8_vlans](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_vlans_module.rst)|Resource module to configure VLANs.
[alcatel.aos8.aos8_vrf](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_vrf_module.rst)|Module to configure VRF definitions.
[alcatel.aos8.aos8_vxlan_vtep](https://github.com/ansible-collections/alcatel.aos8/blob/main/docs/alcatel.aos8.aos8_vxlan_vtep_module.rst)|Resource module to configure VXLAN VTEP interface.

<!--end collection content-->

## Installing this collection

You can install the Alcatel AOS 8 collection with the Ansible Galaxy CLI:

    ansible-galaxy collection install alcatel.aos8

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
      - name: GigabitEthernet0/2
        trunk:
          - allowed_vlans: 20-25,40
            native_vlan: 20
            pruning_vlans: 10
            encapsulation: isl
    state: replaced
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