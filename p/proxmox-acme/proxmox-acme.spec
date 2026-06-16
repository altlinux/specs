Name: proxmox-acme
Summary: Proxmox ACME integration perl library
Version: 1.7.1
Release: alt1
License: AGPL-3.0-or-later and GPL-3.0
Group: Development/Perl
Url: https://git.proxmox.com/
Vcs: git://git.proxmox.com/git/proxmox-acme.git

ExclusiveArch: x86_64 aarch64 loongarch64
BuildRequires: pve-common python3 perl(Date/Parse.pm) perl(JSON.pm) perl(HTTP/Daemon.pm)

Source: %name-%version.tar
Source2: acme.sh.tar
#Patch: %%name-%%version.patch

Requires: curl
Conflicts: pve-manager < 7.0.11-alt1
Provides: pve-acme = %EVR
Obsoletes: pve-acme < 1.7.0

%description
Used in perl-based Proxmox project as common interface for DNS and HTTP ACME
challenges.

#%%add_findreq_skiplist %%perl_vendor_privlib/PVE/ACME.pm
#%%add_findreq_skiplist %%perl_vendor_privlib/PVE/ACME/DNSChallenge.pm
%add_findreq_skiplist %_datadir/proxmox-acme/**/*

%prep
%setup
tar -xf %SOURCE2 -C src/acme.sh --strip-components 1
#%%patch -p1

%install
%make DESTDIR=%buildroot -C src install
chmod a+x %buildroot%_datadir/proxmox-acme/dnsapi/*.sh

%files
%perl_vendor_privlib/PVE/ACME.pm
%perl_vendor_privlib/PVE/ACME
%_datadir/proxmox-acme

%changelog
* Mon Jun 08 2026 Sergey Konev <darisishe@altlinux.org> 1.7.1-alt1
- 1.7.1

* Mon Jul 21 2025 Alexey Shabalin <shaba@altlinux.org> 1.7.0-alt1
- 1.7.0
- Rename package pve-acme -> proxmox-acme

* Fri Jul 11 2025 Ivan A. Melnikov <iv@altlinux.org> 1.5.1-alt2
- NMU: build on loongarch64

* Thu Aug 29 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.5.1-alt1
- 1.5.1

* Fri Mar 01 2024 Andrew A. Vasilyev <andy@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sun Oct 22 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.4.4-alt2
- ALT: change nogroup to nobody

* Sat Mar 11 2023 Andrew A. Vasilyev <andy@altlinux.org> 1.4.4-alt1
- 1.4.4

* Mon Dec 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt2
- removed OpenStack Barbican deploy hook

* Tue Nov 30 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Sep 27 2021 Valery Inozemtsev <shrek@altlinux.ru> 1.3.0-alt1
- initial release

