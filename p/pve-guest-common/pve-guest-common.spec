%def_enable check
%define _unpackaged_files_terminate_build 1

Name: pve-guest-common
Summary: PVE common guest-related modules
Version: 6.0.3
Release: alt1
License: AGPL-3.0+
Group: Development/Perl
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-guest-common.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64 loongarch64

Provides: perl-%name = %EVR
# from debian/control
Provides: libpve-guest-common-perl = %EVR
Conflicts: pve-common < 4.0.89
Conflicts: pve-container < 3.1.4
Conflicts: pve-manager < 8.0.0
Conflicts: qemu-server < 6.1.19
Conflicts: pve-http-server < 5.0.2

Requires: libpve-cluster-perl >= 8.1.0
Requires: pve-access-control
Requires: pve-cluster
Requires: pve-common >= 8.0.2
Requires: pve-storage >= 8.3.4
Requires: proxmox-websocket-tunnel

BuildRequires: libpve-cluster-perl >= 8.1.0
BuildRequires: pve-cluster
BuildRequires: pve-common >= 8.0.2
BuildRequires: pve-storage >= 8.3.4

%description
This package contains a common code base used by pve-container and qemu-server

%prep
%setup

%install
%makeinstall_std -C src

%files
%doc debian/copyright
%perl_vendor_privlib/PVE/*

%changelog
* Wed Jun 10 2026 Sergey Konev <darisishe@altlinux.org> 6.0.3-alt1
- 6.0.3

* Tue Jan 20 2026 Sergey Konev <darisishe@altlinux.org> 6.0.2-alt2
- Minor fixes

* Tue Aug 19 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 6.0.2-alt1
- 6.0.2 

* Fri Jul 11 2025 Ivan A. Melnikov <iv@altlinux.org> 5.2.2-alt2
- NMU: build on loongarch64

* Thu Apr 17 2025 Konstantin Kozoriz <kozorizki@altlinux.org> 5.2.2-alt1
- 5.2.2 

* Thu Nov 28 2024 Alexey Shabalin <shaba@altlinux.org> 5.1.6-alt1
- 5.1.6

* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.1.4-alt1
- 5.1.4

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.6-alt1
- 5.0.6

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.2.4-alt2
- add copyright file

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

