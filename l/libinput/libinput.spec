%define _libexecdir %_prefix/libexec
%def_enable libwacom
%def_disable gui

Name: libinput
Version: 1.6.3
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
%{?_enable_libwacom:BuildRequires: libwacom-devel}
%{?_enable_gui:BuildRequires: libgtk+3-devel}
# for check
#BuildRequires: libunwind-devel valgrind

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
           %{subst_enable libwacom} \
           %{?_enable_gui:--enable-event-gui} \
           --with-udev-dir=/lib/udev
%make_build

%install
%makeinstall_std

%check
#%make check

%files
%_libdir/%name.so.*
/lib/udev/%name-device-group
/lib/udev/%name-model-quirks
%_udevhwdbdir/90-%name-model-quirks.hwdb
%_udevrulesdir/80-%name-device-groups.rules
%_udevrulesdir/90-%name-model-quirks.rules
%doc COPYING README*

%files devel
%_includedir/%name.h
%_libdir/%name.so
%_pkgconfigdir/%name.pc

%files tools
%_bindir/%name-list-devices
%_bindir/%name-debug-events
%{?_enable_gui%_bindir/event-gui}
%_man1dir/%name-list-devices.1.*
%_man1dir/%name-debug-events.1.*


%changelog
* Wed Mar 08 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.3-alt1
- 1.6.3

* Tue Feb 21 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Thu Feb 02 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri Jan 20 2017 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Jan 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Sun Dec 11 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.3-alt1
- 1.5.3

* Sun Nov 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Sun Nov 13 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.1-alt1
- 1.5.1

* Wed Sep 14 2016 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Tue Aug 30 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Fri Aug 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Mon Jul 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Fri Jun 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.3-alt1
- 1.3.3

* Sun Jun 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.1-alt1
- 1.3.1

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Tue Apr 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.4-alt1
- 1.2.4

* Tue Apr 12 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Mon Feb 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Tue Feb 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Thu Feb 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.8-alt1
- 1.1.8

* Wed Feb 10 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.7-alt1
- 1.1.7

* Fri Feb 05 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.6-alt1
- 1.1.6

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.5-alt1
- 1.1.5

* Tue Dec 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.4-alt1
- 1.1.4

* Wed Dec 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.3-alt1
- 1.1.3

* Wed Dec 09 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Mon Nov 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.1-alt1
- 1.1.1

* Tue Oct 27 2015 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0

* Wed Oct 21 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Fri Sep 04 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- 1.0.1

* Wed Aug 26 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Sun Aug 23 2015 Yuri N. Sedunov <aris@altlinux.org> 0.99.1-alt1
- 0.99.1

* Wed Aug 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.21.0-alt1
- 0.21.0

* Thu Jul 16 2015 Yuri N. Sedunov <aris@altlinux.org> 0.20.0-alt1
- 0.20.0

* Tue Jul 07 2015 Yuri N. Sedunov <aris@altlinux.org> 0.19.0-alt1
- 0.19.0

* Mon Jun 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.18.0-alt1
- 0.18.0

* Thu Jun 04 2015 Yuri N. Sedunov <aris@altlinux.org> 0.17.0-alt1
- 0.17.0

* Wed Jun 03 2015 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Tue May 05 2015 Yuri N. Sedunov <aris@altlinux.org> 0.15.1-alt1
- 0.15.1

* Wed Apr 22 2015 Yuri N. Sedunov <aris@altlinux.org> 0.14.1-alt1
- 0.14.1

* Sun Mar 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.13.0-alt1
- 0.13.0

* Fri Mar 13 2015 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

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



