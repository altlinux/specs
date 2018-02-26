Name: libimobiledevice
Version: 1.1.5
Release: alt0.1

Summary: Library for connecting to Apple iPhone and iPod touch
Group: System/Libraries
License: LGPLv2+
Url: http://www.libimobiledevice.org/

Source: %url/downloads/l/%name-%version.tar

%define plist_ver 1.8
%define usbmuxd_ver 1.0.8
%define cython_ver 0.16

BuildPreReq: libplist-devel >= %plist_ver
BuildPreReq: libusbmuxd-devel >= %usbmuxd_ver

BuildRequires: gcc-c++ glib2-devel libxml2-devel libusb-devel libplistmm-devel
BuildRequires: libgnutls-devel libtasn1-devel libgcrypt-devel libssl-devel
BuildRequires: python-devel python-module-Cython >= %cython_ver python-module-libplist

%description
libimobiledevice is a library for connecting to Apple's iPhone or iPod touch devices

%package devel
Summary: Development package for libimobiledevice
Group: Development/C
Requires: %name = %version-%release

%description devel
This package provides files for development using libimobiledevice.

%package -n python-module-%name
Summary: Python bindings for libimobiledevice
Group: Development/Python
Requires: %name = %version-%release

%description -n python-module-%name
Python bindings for libimobiledevice.

%prep
%setup

%build
%autoreconf
%configure --disable-static

%make_build

%install

%makeinstall_std

%files
%_bindir/idevice*
%_libdir/*.so.*
%_man1dir/*
%doc AUTHORS NEWS README

%files devel
%_includedir/%name
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%files -n python-module-%name
%python_sitelibdir/imobiledevice.so
%exclude %python_sitelibdir/imobiledevice.la

%changelog
* Sat Jun 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt0.1
- 1.1.5 snapshot

* Wed May 09 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Sun Apr 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Tue Oct 25 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.1-alt1.1
- Rebuild with Python-2.7

* Fri Apr 29 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Sun Mar 27 2011 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Sun Mar 27 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.6-alt1
- 1.0.6

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt2
- updated buildreqs

* Sat Dec 11 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue Nov 02 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.3-alt1
- 1.0.3

* Sun Aug 01 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt2
- fixed swig-2.0.0 detection

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Thu May 27 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Sun Mar 28 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Mar 14 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt2
- fixed swig/__init__.py

* Mon Feb 15 2010 Yuri N. Sedunov <aris@altlinux.org> 0.9.7-alt1
- first build for Sisyphus

