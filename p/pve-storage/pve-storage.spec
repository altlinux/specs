Name: pve-storage
Summary: Proxmox VE storage management library
Version: 4.0.50
Release: alt1
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64

Requires: nfs-utils open-iscsi clvm glusterfs3

Source: pve-storage.tar.xz
Patch: pve-storage-path.patch

BuildRequires: pve-common pve-cluster pve-doc-generator pve-access-control xmlto
BuildRequires: perl(File/chdir.pm)
BuildRequires: perl(Net/DBus.pm)

%description
This package contains the storage management library used by Proxmox VE

%prep
%setup -q -n %name
%patch -p1

%install
%make DESTDIR=%buildroot install

%files
%_sysconfdir/bash_completion.d/*
%_sbindir/pvesm
%perl_vendor_privlib/PVE
%_man1dir/pvesm.1*

%changelog
* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.50-alt1
- 4.0-50

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt1
- 4.0-40

* Thu Dec 03 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.35-alt1
- initial release

