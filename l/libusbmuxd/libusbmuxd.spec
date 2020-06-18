%def_disable snapshot
%define api_ver 2.0
%def_enable check

Name: libusbmuxd
Version: 2.0.2
Release: alt1

Summary: Interface library for usbmuxd
Group: System/Libraries
License: LGPL-2.1
Url: http://www.libimobiledevice.org/

%if_disabled snapshot
Source: https://github.com/libimobiledevice/libusbmuxd/archive/%version/%name-%version.tar.gz
%else
# VCS: https://github.com/libimobiledevice/libusbmuxd.git
Source: %name-%version.tar
%endif

BuildRequires: gcc-c++ libusb-devel >= 1.0.3 libplistmm-devel >= 2.2.0

%description
usbmuxd (USB Multiplex Daemon) is a daemon used for communicating with
Apple's iPod Touch and iPhone devices. It allows multiple services on
the device to be accessed simultaneously.

This package contains the usbmuxd communication interface library -
'libusbmuxd'.

%package devel
Summary: Development package for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides headers and libraries needed for development
%name clients.

%prep
%setup

%build
%add_optflags %(getconf LFS_CFLAGS)
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/iproxy
%_bindir/inetcat
%_libdir/libusbmuxd-%api_ver.so.*
%_man1dir/iproxy.1*
%_man1dir/inetcat.1*

%files devel
%_includedir/*.h
%_libdir/libusbmuxd-%api_ver.so
%_pkgconfigdir/libusbmuxd-%api_ver.pc

%changelog
* Tue Jun 16 2020 Yuri N. Sedunov <aris@altlinux.org> 2.0.2-alt1
- 2.0.2

* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1
- new %%check section

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.10-alt1
- 1.0.10

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.9-alt1
- 1.0.9

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.8-alt1
- 1.0.8

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.7-alt1
- 1.0.7

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt2
- rebuilt for debuginfo

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.5-alt1
- 1.0.5

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Mar 14 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu Dec 03 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1.rc2
- first build for Sisyphus

