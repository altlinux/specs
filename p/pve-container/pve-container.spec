%define _unpackaged_files_terminate_build 1
%set_perl_req_method relaxed

Name: pve-container
Summary: Proxmox VE Container management tool
Version: 5.0.9
Release: alt1.1
License: AGPL-3.0+
Group: System/Servers
Url: https://www.proxmox.com
Vcs: git://git.proxmox.com/git/pve-container.git
Source: %name-%version.tar

ExclusiveArch: x86_64 aarch64

Requires(pre,postun): shadow-submap
Requires: pve-lxc pve-lxc-syscalld pve-ha-manager >= 3.0.9 pve-access-control >= 8.0.0
Requires: dtach xz file binutils

BuildRequires: pve-common >= 8.1.0 pve-guest-common >= 5.0.3 pve-qemu-server pve-storage >= 7.2.10
BuildRequires: pve-firewall pve-cluster >= 4.0.8 libpve-cluster-perl pve-doc-generator xmlto pve-lxc >= 4.0.9
BuildRequires: pve-manager pve-ha-manager
BuildRequires: perl(Crypt/Eksblowfish/Bcrypt.pm) perl(UUID.pm)

%description
%summary.
Tool to manage Linux Containers on Proxmox VE.

%prep
%setup
sed -i 's!}/lib/systemd/!}/usr/lib/systemd/!' src/Makefile

%install
%makeinstall_std -C src

%post
%_sbindir/usermod --add-subgids 100000-165535 root ||:
%_sbindir/usermod --add-subuids 100000-165535 root ||:

%files
%doc debian/copyright
%_sysctldir/10-pve-ct-inotify-limits.conf
%_datadir/bash-completion/completions/*
%_datadir/zsh/vendor-completions/*
%_unitdir/*
%_sbindir/*
%_datadir/lxc
%perl_vendor_privlib/PVE/LXC
%perl_vendor_privlib/PVE/*.pm
%perl_vendor_privlib/PVE/API2/LXC
%perl_vendor_privlib/PVE/API2/*.pm
%perl_vendor_privlib/PVE/CLI/*.pm
%perl_vendor_privlib/PVE/VZDump/*.pm
%_man1dir/*
%_man5dir/*

%changelog
* Mon Jun 24 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.9-alt1.1
- FTBFS: fix sysctl.d and systemd path

* Fri Mar 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.9-alt1
- 5.0.9

* Wed Feb 28 2024 Andrew A. Vasilyev <andy@altlinux.org> 5.0.8-alt1
- 5.0.8

* Mon Feb 05 2024 Andrew A. Vasilyev <andy@altlinux.org> 4.4.6-alt1
- 4.4-6

* Thu May 25 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.4.3-alt2
- add copyright file

* Mon Mar 20 2023 Andrew A. Vasilyev <andy@altlinux.org> 4.4.3-alt1
- 4.4-3

* Tue Nov 29 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.4.2-alt1
- 4.4-2

* Tue Nov 29 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.3.3-alt1
- 4.3-3

* Mon Nov 14 2022 Alexey Shabalin <shaba@altlinux.org> 4.3.1-alt1
- 4.3-1

* Wed Jul 06 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.2.2-alt1
- 4.2-2

* Thu May 05 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.2.1-alt1
- 4.2-1

* Tue Apr 19 2022 Andrew A. Vasilyev <andy@altlinux.org> 4.1.4-alt2
- avoid that FirstBoot condition is set on CT creation

* Thu Mar 10 2022 Alexey Shabalin <shaba@altlinux.org> 4.1.4-alt1
- 4.1-4
- build as separate package

