%def_disable gui

Name: libinput
Version: 0.7.0
Release: alt1

Summary: Input devices library
Group: System/Libraries
License: MIT
Url: http://www.freedesktop.org/wiki/Software/libinput/

Source: http://www.freedesktop.org/software/%name/%name-%version.tar.xz

%define mtdev_ver 1.1.0
%define evdev_ver 0.4

BuildRequires: gcc-c++ libmtdev-devel >= %mtdev_ver libevdev-devel >= %evdev_ver
BuildRequires: libudev-devel libcheck-devel
%{?_enable_gui:BuildRequires: libgtk+3-devel}

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


%package tools
Summary: libinput GUI event viewer
Group: Development/Tools
Requires: %name = %version-%release

%description tools
This package contains GUI event viewer from %name.

%prep
%setup

%build
%autoreconf
%configure --disable-static \
           %{?_enable_gui:--enable-event-gui}
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

%if_enabled gui
%files tools
%_bindir/event-gui
%endif


%changelog
* Mon Dec 08 2014 Yuri N. Sedunov <aris@altlinux.org> 0.7.0-alt1
- 0.7.0

* Mon Sep 29 2014 Yuri N. Sedunov <aris@altlinux.org> 0.6.0-alt1
- 0.6.0

* Thu Jul 24 2014 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Tue Jul 01 2014 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu May 22 2014 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- 0.2.0

* Tue Mar 04 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.0-alt1
- first build for Sisyphus



