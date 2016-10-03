Name: pve-storage
Summary: Proxmox VE storage management library
Version: 4.0.63
Release: alt1
License: GPLv3
Group: Development/Perl
Url: https://git.proxmox.com/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

ExclusiveArch: x86_64

Requires: nfs-utils open-iscsi clvm glusterfs3-client smartmontools ceph gdisk parted hdparm

Source: pve-storage.tar.xz
Patch: pve-storage-alt.patch

BuildRequires: pve-common pve-cluster pve-doc-generator pve-access-control xmlto
BuildRequires: perl(File/chdir.pm) perl(Net/DBus.pm)

%description
This package contains the storage management library used by Proxmox VE

%prep
%setup -q -n %name
%patch -p1

%install
%make DESTDIR=%buildroot install

mkdir -p %buildroot%_sysconfdir/modules-load.d
cat << __EOF__ > %buildroot%_sysconfdir/modules-load.d/pve-storage.conf
rbd
__EOF__

%files
%_sysconfdir/bash_completion.d/*
%_sysconfdir/modules-load.d/pve-storage.conf
%_sbindir/pvesm
%perl_vendor_privlib/PVE
%_man1dir/pvesm.1*

%changelog
* Mon Oct 03 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.63-alt1
- 4.0-63

* Fri Sep 16 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.61-alt1
- 4.0-61

* Mon Aug 22 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.57-alt1
- 4.0-57

* Sun Jun 26 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.55-alt1
- 4.0-55

* Wed Jun 15 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.54-alt1
- 4.0-54

* Wed Jun 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.52-alt1
- 4.0-52

* Wed Jun 01 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.50-alt1
- 4.0-50

* Mon Feb 08 2016 Valery Inozemtsev <shrek@altlinux.ru> 4.0.40-alt1
- 4.0-40

* Thu Dec 03 2015 Valery Inozemtsev <shrek@altlinux.ru> 4.0.35-alt1
- initial release

