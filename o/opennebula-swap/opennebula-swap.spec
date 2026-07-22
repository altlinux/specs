Name: opennebula-swap
Version: 7.2.1
Release: alt1
Summary: CLI tool for migrating Virtual Machines from VMware vCenter/ESXi to OpenNebula
License: Apache-2.0
Group: System/Servers
Url: https://github.com/OpenNebula/one-swap

Source: %name-%version.tar

BuildRequires: gcc

Requires: gem-opennebula-cli
Requires: gem(rbvmomi)
Requires: virt-v2v

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
%_libexecdir/one/ruby/cli/one_helper/windows_tuner.rb
%config(noreplace) %_sysconfdir/one/oneswap.yaml
%dir %_libexecdir/one/oneswap/scripts
%_libexecdir/one/oneswap/scripts/vmware_tools_removal.*

%changelog
* Thu Jul 09 2026 Alexander Burmatov <thatman@altlinux.org> 7.2.1-alt1
- New 7.2.1 version.

* Wed Jul 08 2026 Alexander Burmatov <thatman@altlinux.org> 6.10.5-alt2
- Add missing requirement (ALT #59764).
- Assign conversion result to img_ids in convert_vm (ALT #59765).

* Thu Jun 11 2026 Alexander Burmatov <thatman@altlinux.org> 6.10.5-alt1
- Initial build for Sisyphus.
