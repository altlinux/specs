Name: rpm-build-guestfs
Version: 0.4
Release: alt2

Summary: RPM helper post script for build guestfs appliance
License: GPL
Group: Development/Other

BuildArch: noarch
Requires(pre):  make-initrd >= 2.2.6
Requires(pre):  kernel >= 4.3

Requires(pre): make-initrd-mdadm make-initrd-devmapper make-initrd-lvm make-initrd-luks

Requires(pre): /usr/sbin/guestfsd
Requires(pre): /usr/sbin/parted
Requires(pre): /sbin/wipefs
Requires(pre): /usr/sbin/zerofree
Requires(pre): /usr/sbin/sparsify
Requires(pre): /usr/bin/rsync
Requires(pre): /sbin/ip
Requires(pre): /bin/grep
Requires(pre): /bin/uname
Requires(pre): /bin/date
Requires(pre): /sbin/ip
Requires(pre): fuse ntfs-3g nfs-utils mount
Requires(pre): util-linux btrfs-progs e2fsprogs jfsutils dosfstools reiserfsprogs xfsprogs
Requires(pre): fdisk sfdisk gdisk
Requires(pre): hivex
Requires(pre): libaugeas
Requires(pre): glibc-gconv-modules
Requires(pre): mdadm

%description
RPM helper post script for build guestfs appliance


%post
mkdir -p %_libdir/guestfs
VMLINUZ="$(readlink -e -- /boot/vmlinuz-*alt*)"
KVER="${VMLINUZ##*/vmlinuz-}"
echo "VMLINUZ = $VMLINUZ"
echo "KVER = $KVER"
cp $VMLINUZ %_libdir/guestfs/vmlinuz.%_arch
make-initrd --verbose --no-checks --config=/etc/initrd.mk.d/guestfs.mk.example --kernel=$KVER
chmod 644 %_libdir/guestfs/*

%files

%changelog
* Fri Dec 21 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt2
- rebuild with make-initrd-2.2.6

* Mon Oct 15 2018 Alexey Shabalin <shaba@altlinux.org> 0.4-alt1
- rebuild with libguestfs-1.36.15-alt1
- build with new make-initrd v2
- fix detect kernel version for aarch64 too

* Thu May 26 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt6
- rebuld with libguestfs-1.32.4

* Mon Jan 11 2016 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt5
- rebuld with libguestfs-1.32.0

* Tue Oct 20 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt4
- rebuild

* Thu Jun 25 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt2
- add --verbose to make-initrd

* Fri Feb 13 2015 Alexey Shabalin <shaba@altlinux.ru> 0.2-alt1
- update

* Wed Feb 11 2015 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- initial build
