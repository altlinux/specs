Name: libusbmuxd
Version: 1.0.9
Release: alt1

Summary: Interface library for usbmuxd
Group: System/Libraries
License: GPLv3+
Url: http://www.libimobiledevice.org/

Source: %url/downloads/%name-%version.tar.bz2

BuildRequires: gcc-c++ libusb-devel >= 1.0.3 libplistmm-devel >= 1.11

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
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std

%files
%_bindir/iproxy
%_libdir/libusbmuxd.so.*

%files devel
%_includedir/*.h
%_libdir/libusbmuxd.so
%_libdir/pkgconfig/libusbmuxd.pc

%changelog
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

