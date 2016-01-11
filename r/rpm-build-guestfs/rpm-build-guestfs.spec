Name: rpm-build-guestfs
Version: 0.2
Release: alt5

Summary: RPM helper post script for build guestfs appliance
License: GPL
Group: Development/Other

BuildArch: noarch
Requires(pre):  make-initrd-guestfs
Requires(pre):  kernel >= 4.3

%description
RPM helper post script for build guestfs appliance

%files

%post

mkdir -p %_libdir/guestfs
cp /boot/vmlinuz-*-*-def-* %_libdir/guestfs/vmlinuz.%_arch

kver=$(ls -1 /boot/vmlinuz-*-def-* | sed -e "s|/boot/vmlinuz-||")
make-initrd --verbose --no-checks --config=/etc/initrd.mk.d/guestfs.mk.example --kernel=$kver
chmod 644 %_libdir/guestfs/*

%postun
rm -rf %_libdir/guestfs

%changelog
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
