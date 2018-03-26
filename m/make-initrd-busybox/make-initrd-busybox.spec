Name: make-initrd-busybox
Version: 1.28.1
Release: alt1

Summary: Busybox for make-initrd
License: GPL
Group: System/Base

Source0: %name-%version.tar

%description
Busybox (%version) for make-initrd.

%prep
%setup
cp -f -- busybox-config busybox/.config

%build
cd busybox
%make_build

%install
mkdir -p -- %buildroot/lib/initrd/var/run

cd busybox
%make install CONFIG_PREFIX=%buildroot/lib/initrd

cd %buildroot/lib/initrd

ln -s ../usr/bin/readlink bin/readlink
ln -s ../usr/sbin/chroot  sbin/chroot

%files 
/lib/initrd/*

%changelog
* Mon Mar 26 2018 Alexey Gladkov <legion@altlinux.ru> 1.28.1-alt1
- New busybox version (1.28.1).

* Thu Mar 16 2017 Alexey Gladkov <legion@altlinux.ru> 1.24.2-alt2
- Add setsid, timeout utilities.

* Tue May 03 2016 Alexey Gladkov <legion@altlinux.ru> 1.24.2-alt1
- New busybox version (1.24.2).

* Wed Nov 18 2015 Alexey Gladkov <legion@altlinux.ru> 1.24.1-alt1
- New busybox version (1.24.1).

* Fri Jul 04 2014 Alexey Gladkov <legion@altlinux.ru> 0.2-alt1
- Add more utilities.

* Wed Mar 13 2013 Alexey Gladkov <legion@altlinux.ru> 0.1-alt1
- Initial.

