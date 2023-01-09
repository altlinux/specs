Name: rpm-build-guestfs
Version: 0.8
Release: alt4

Summary: RPM helper post script for build guestfs appliance
License: GPL
Group: Development/Other

Requires(pre):  make-initrd >= 2.2.6
Requires(pre):  kernel >= 5.4
Requires: /proc

Requires(pre): make-initrd-guestfs
Requires(pre): make-initrd-mdadm
Requires(pre): make-initrd-devmapper
Requires(pre): make-initrd-lvm
Requires(pre): make-initrd-luks

%description
RPM helper post script for build guestfs appliance

%install 
mkdir -p %buildroot%_libdir/guestfs


%post
mkdir -p %_libdir/guestfs
VMLINUZ="$(readlink -e -- /boot/vmlinuz-*alt*)"
KVER="${VMLINUZ##*/vmlinuz-}"
echo "VMLINUZ = $VMLINUZ"
echo "KVER = $KVER"
cp $VMLINUZ %_libdir/guestfs/vmlinuz.%_arch
ARCH="%_arch" make-initrd --verbose --no-checks \
    --config=/etc/initrd.mk.d/guestfs.mk.example --kernel=$KVER
chmod 644 %_libdir/guestfs/*

%files
%dir %_libdir/guestfs

%changelog
* Sat Dec 31 2022 Egor Ignatov <egori@altlinux.org> 0.8-alt4
- Clean up spec; Requires moved to make-initrd-guestfs

* Fri Dec 30 2022 Alexey Gladkov <legion@altlinux.ru> 0.8-alt3
- Requires: make-initrd-guestfs

* Fri Sep 16 2022 Egor Ignatov <egori@altlinux.org> 0.8-alt2
- fix initramfs arch name on i586 and armh

* Wed Nov 17 2021 Alexey Shabalin <shaba@altlinux.org> 0.8-alt1
- Requires: /proc for fix install check

* Tue Dec 08 2020 Mikhail Gordeev <obirvalger@altlinux.org> 0.7-alt1
- Requires file and findfs (Closes: 39367)

* Mon Jul 06 2020 Alexey Shabalin <shaba@altlinux.org> 0.6-alt1
- Requires kernel >= 5.4
- rebuild with make-initrd-2.8.1
- rebuild with libguestfs-1.42.0

* Fri Apr 05 2019 Alexey Shabalin <shaba@altlinux.org> 0.5-alt1
- build package as arch

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
