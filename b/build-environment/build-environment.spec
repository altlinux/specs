Name: build-environment
Version: 0.1
Release: alt2

Packager: Stanislav Ievlev <inger@altlinux.org>

Summary: build enviroment
Copyright: GPL
Group: System/Base
BuildArch: noarch

#implicit hasher requires
Requires: setup filesystem rpm fakeroot
Requires: basesystem rpm-build kernel-headers-common sisyphus_check
Requires: glibc-utils
Requires: mar
Requires: mkisofs
Requires: rsync
Requires: propagator
Requires: rsync
Requires: squashfsprogs
Requires: syslinux

#build tools
Requires: apt rpm-build hasher
Requires: spt mkimage

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
* Sat Dec 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt2
- add cdrom hack

* Sat Dec 15 2007 Stanislav Ievlev <inger@altlinux.org> 0.1-alt1
- Initial build
