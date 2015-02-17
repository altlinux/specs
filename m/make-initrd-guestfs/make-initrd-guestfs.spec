Name: make-initrd-guestfs
Version: 0.3
Release: alt1

Summary: Build appliance for libguestfs by make-initrd
License: GPL
Group: System/Base

Source0: %name-%version.tar

Requires: make-initrd
Requires: make-initrd-mdadm make-initrd-devmapper make-initrd-lvm make-initrd-luks

Requires: /usr/sbin/guestfsd
Requires: /usr/sbin/parted
Requires: /sbin/wipefs
Requires: /usr/sbin/zerofree
Requires: /usr/sbin/sparsify
Requires: /usr/bin/rsync
Requires: /bin/grep
Requires: /bin/uname
Requires: /bin/date
Requires: /sbin/ip
Requires: fuse ntfs-3g nfs-utils mount
Requires: util-linux btrfs-progs e2fsprogs jfsutils dosfstools reiserfsprogs xfsprogs
Requires: fdisk sfdisk gdisk
Requires: hivex
Requires: libaugeas
Requires: glibc-gconv-modules


BuildArch: noarch
AutoReq: noshell, noshebang


%description
Make-initrd feature, able to make a appliance for libguestfs.

%prep
%setup

%install
mkdir -p %buildroot%_datadir/make-initrd/features
cp -a guestfs %buildroot%_datadir/make-initrd/features/
mkdir -p %buildroot%_sysconfdir/initrd.mk.d
cp -a guestfs.mk.example %buildroot%_sysconfdir/initrd.mk.d

%files
%_datadir/make-initrd/features/guestfs
%_sysconfdir/initrd.mk.d/guestfs.mk.example

%changelog
* Tue Feb 17 2015 Alexey Shabalin <shaba@altlinux.ru> 0.3-alt1
- thx to legion@:
  + Remove 015-fstab
  +Fix requires

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
