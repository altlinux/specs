Name: exofs-utils
Version: 0.1
Release: alt1

Summary: Utilities for managing EXOFS filesystems
License: GPLv2+
Group: System/Kernel and hardware

Url: http://www.open-osd.org/bin/view
Source: %name-%version.tar

%description
Utilities to work with EXOFS filesystems,
an open-source reference implementation of an OSD based file system.

%prep
%setup

%build
cd lib
%make_build

cd ../usr
%make_build

%install
cd lib
mkdir -p %buildroot/%_libdir/
install -m644 libosd.so %buildroot/%_libdir/
cd ../usr
mkdir -p %buildroot/%_sbindir/ %buildroot/sbin/
install -m755 mkfs.exofs %buildroot/sbin/
install -m755 osd %buildroot/%_sbindir/
install -m755 osd_test %buildroot/%_sbindir/

%files
%doc README
%doc do*
/sbin/mkfs.exofs
%_libdir/libosd.so
%_sbindir/osd
%_sbindir/osd_test

%changelog
* Mon Mar 12 2012 Vitaly Lipatov <lav@altlinux.ru> 0.1-alt1
- initial build for ALT Linux Sisyphus
