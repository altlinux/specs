%def_enable check
%define _unpackaged_files_terminate_build 1

Name: pve-guest-common
Summary: PVE common guest-related modules
Version: 4.2.4
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-guest-common.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-guest-common-perl = %EVR
Conflicts: pve-common < 4.0.89
Conflicts: pve-container < 3.1.4
Conflicts: pve-manager < 6.0.10
Conflicts: qemu-server < 6.1.19

Requires: libpve-cluster-perl >= 7.2.3
Requires: pve-cluster
Requires: pve-common >= 7.2.6
Requires: pve-storage >= 7.2.6
Requires: proxmox-websocket-tunnel

BuildRequires: libpve-cluster-perl >= 7.2.3
BuildRequires: pve-cluster
BuildRequires: pve-common >= 7.2.6
BuildRequires: pve-storage >= 7.2.6

%description
This package contains a common code base used by pve-container and qemu-server

%prep
%setup

%install
%makeinstall_std -C src

%files
%perl_vendor_privlib/PVE/*

%changelog
* Mon Mar 27 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.2.4-alt1
- 4.2-4

* Wed Nov 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.2.3-alt1
- 4.2-3

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 4.2.1-alt1
- 4.2-1

* Mon Oct 03 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.3-alt1
- 4.1-3

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.1.2-alt1
- 4.1-2

* Thu Feb 17 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.1-alt1
- 4.1-1
- build as separate package

