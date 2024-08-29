Name: pve-acme
Summary: PVE ACME integration perl library
Version: 1.5.1
Release: alt1
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/

ExclusiveArch: x86_64 aarch64
BuildRequires: pve-common python3 perl(Date/Parse.pm) perl(JSON.pm) perl(HTTP/Daemon.pm)

Source: pve-acme.tar.xz
# Patch1: pve-acme-rm-openstack.patch
Patch2: pve-acme-nogroup.patch

Requires: curl

Conflicts: pve-manager < 7.0.11-alt1

%description
Used in perl-based PVE project as common interface for DNS and HTTP ACME challenges

#%%add_findreq_skiplist %%perl_vendor_privlib/PVE/ACME.pm
#%%add_findreq_skiplist %%perl_vendor_privlib/PVE/ACME/DNSChallenge.pm
%add_findreq_skiplist %_datadir/proxmox-acme/**/*

%prep
%setup -q -n %name
# %%patch1 -p1 -b .rm-openstack
%patch2 -p1

%install
%make DESTDIR=%buildroot -C src install
chmod a+x %buildroot%_datadir/proxmox-acme/dnsapi/*.sh

%files
%perl_vendor_privlib/PVE/ACME.pm
%perl_vendor_privlib/PVE/ACME
%_datadir/proxmox-acme

%changelog
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

