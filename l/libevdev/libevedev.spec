%define api_ver 1.0

Name: libevdev
Version: 0.4
Release: alt1.1

Summary: kernel evdev device wrapper library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libevdev

Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz

BuildRequires: libcheck-devel python-modules doxygen

%description
%name is a wrapper library for evdev devices.

%package devel
Summary: kernel evdev device wrapper library development package
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
	--disable-gcov

%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_libdir/libevdev.so.*
%doc COPYING

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1.1
- disable coverage testing

* Fri Sep 20 2013 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- first build for Sisyphus


