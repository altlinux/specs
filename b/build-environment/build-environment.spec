Name: build-environment
Version: 0.1
Release: alt3

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: build enviroment
License: GPL-2.0
Group: System/Base
BuildArch: noarch

#implicit hasher requires
Requires: setup filesystem rpm fakeroot
Requires: basesystem rpm-build kernel-headers-common sisyphus_check
Requires: glibc-utils
Requires: mkisofs
Requires: rsync
Requires: propagator
Requires: squashfsprogs

#build tools
Requires: apt rpm-build hasher
Requires: mkimage

Source1: build-environment-firsttime
Source2: build-pkg
Source3: build-indexes

%description
This package setup build environment

%install
install -Dpm755 %SOURCE1 %buildroot%_sysconfdir/firsttime.d/%name
install -Dpm755 %SOURCE2 %buildroot%_bindir/build-pkg
install -Dpm755 %SOURCE3 %buildroot%_bindir/build-indexes

%files
%_bindir/*
%_sysconfdir/firsttime.d/%name

%changelog
* Sun Jul 10 2022 Andrey Cherepanov <cas@altlinux.org> 0.1-alt3
- return to Sisyphus (without spt, syslinux and mar) (ALT #43197).

* Sat Dec 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add cdrom hack

* Sat Dec 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
