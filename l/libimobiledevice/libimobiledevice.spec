%def_enable snapshot
%def_disable python
%def_enable check

Name: libimobiledevice
Version: 1.2.1
Release: alt0.3

Summary: Library for connecting to Apple iPhone and iPod touch
Group: System/Libraries
License: LGPLv2+
Url: http://www.libimobiledevice.org

%if_disabled snapshot
Source: %url/downloads/%name-%version.tar.bz2
%else
# VCS: https://github.com/libimobiledevice/libimobiledevice.git
Source: %name-%version.tar
%endif

%define plist_ver 1.11
%define usbmuxd_ver 1.1.0
%define cython_ver 0.18

BuildPreReq: libplist-devel >= %plist_ver
BuildPreReq: libusbmuxd-devel >= %usbmuxd_ver

BuildRequires: gcc-c++ autoconf-archive glib2-devel libxml2-devel libusb-devel libplistmm-devel
BuildRequires: libgnutls-devel libtasn1-devel libgcrypt-devel libssl-devel
%{?_enable_python:BuildRequires: python-devel python-module-Cython >= %cython_ver python-module-libplist}

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
%configure --disable-static \
	%{?_disable_python:--without-cython}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_bindir/idevice*
%_libdir/*.so.*
%_man1dir/*
%doc AUTHORS NEWS README*

%files devel
%_includedir/%name
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled python
%files -n python-module-%name
%python_sitelibdir/imobiledevice.so
%exclude %python_sitelibdir/imobiledevice.la
%endif

%changelog
* Thu Dec 12 2019 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt0.3
- updated to 1.2.0-152-g9f79242

* Fri Aug 31 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt0.2
- rebuilt with openssl-1.1

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt0.1
- updated to 1.2.0-75-g26373b3 (ALT #35060)

* Fri Apr 08 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt2
- rebuilt for new gcc, python, cython etc.

* Sat Feb 14 2015 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Oct 15 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Mon Jun 16 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Tue Feb 18 2014 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt2
- use Cython-0.18

* Fri Mar 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5 release

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

