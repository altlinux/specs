Name: usbmuxd
Version: 1.0.8
Release: alt1

Summary: Daemon for communicating with Apple's iPod Touch and iPhone
Group: System/Servers
License: GPLv3+
Url: http://www.libimobiledevice.org/

Source: http://marcansoft.com/uploads/%name/%name-%version.tar.bz2

BuildRequires: gcc-c++ cmake libusb-devel >= 1.0.3 libplistmm-devel
Requires: lib%name = %version-%release

%description
usbmuxd (USB Multiplex Daemon) is a daemon used for communicating with
Apple's iPod Touch and iPhone devices. It allows multiple services on
the device to be accessed simultaneously.

%package -n lib%name
Summary: Shared library for %name
Group: System/Libraries

%description -n lib%name
This package contains shared library required for %name to work.

%package -n lib%name-devel
Summary: Development package for %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package provides headers and libraries needed for development
%name clients

%prep
%setup -q

%build
%cmake
pushd BUILD
%make_build

%install
pushd BUILD
make DESTDIR=%buildroot install

%files
/lib/udev/rules.d/85-usbmuxd.rules
%_bindir/iproxy
%_sbindir/usbmuxd
%doc AUTHORS README

%files -n lib%name
%_libdir/libusbmuxd.so.*

%files -n lib%name-devel
%_includedir/*.h
%_libdir/libusbmuxd.so
%_libdir/pkgconfig/libusbmuxd.pc
%doc README.devel

%changelog
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

