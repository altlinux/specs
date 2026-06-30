Name: opennebula-swap
Version: 6.10.5
Release: alt1
Summary: CLI tool for migrating Virtual Machines from VMware vCenter/ESXi to OpenNebula
License: Apache-2.0
Group: System/Servers
Url: https://github.com/OpenNebula/one-swap

Source: %name-%version.tar

BuildRequires: gcc

Requires: gem-opennebula-cli
Requires: gem(rbvmomi)

# script runs inside the migrated guest VM, not on the host
%add_findreq_skiplist %_libexecdir/one/oneswap/scripts/vmware_tools_removal.sh

%description
OneSwap is a command-line tool for migrating Virtual Machines from VMware
vCenter or ESXi directly to OpenNebula. It supports virt-v2v and qemu-img
based disk conversion, delta transfers, and importing Open Virtual
Appliances (OVAs) previously exported from vCenter/ESXi environments.

%prep
%setup

%build
%make_build

%install
export DESTDIR=%buildroot
./install.sh

%files
%_bindir/oneswap
%_bindir/sesparse
%_libexecdir/one/ruby/cli/one_helper/oneswap_helper.rb
%_libexecdir/one/ruby/cli/one_helper/vsphere_client.rb
%_libexecdir/one/ruby/cli/one_helper/esxi_client.rb
%_libexecdir/one/ruby/cli/one_helper/esxi_vm.rb
%config(noreplace) %_sysconfdir/one/oneswap.yaml
%dir %_libexecdir/one/oneswap/scripts
%_libexecdir/one/oneswap/scripts/vmware_tools_removal.*

%changelog
* Thu Jun 11 2026 Alexander Burmatov <thatman@altlinux.org> 6.10.5-alt1
- Initial build for Sisyphus.