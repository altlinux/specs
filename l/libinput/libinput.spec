Name: libinput
Version: 0.1.0
Release: alt1

Summary: Input devices library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libinput/

Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz

%define mtdev_ver 1.1.0
%define evdev_ver 0.4

BuildRequires: libmtdev-devel >= %mtdev_ver libevdev-devel >= %evdev_ver
BuildRequires: libudev-devel libcheck-devel

%description
libinput is a library that handles input devices for display servers and
other applications that need to directly deal with input devices.

It provides device detection, device handling, input device event
processing and abstraction so minimize the amount of custom input code
the user of libinput need to provide the common set of functionality
that users expect.

Input event processing includes scaling touch coordinates, generating
pointer events from touchpads, pointer acceleration, etc.


%package devel
Summary: libinput development package
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
%_libdir/%name.so.*
%doc COPYING README

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%changelog
* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus



