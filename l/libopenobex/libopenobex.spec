Name: libopenobex
Version: 1.7.2
Release: alt1

Summary: OpenOBEX - Free implementation of the Object Exchange protocol
License: LGPL
Group: System/Libraries
URL: http://openobex.sourceforge.net
Packager: Valery Inozemtsev <shrek@altlinux.ru>

# VCS: https://gitlab.com/openobex/mainline.git
Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ cmake libbluez-devel libusb-devel libudev-devel
BuildRequires: doxygen xmlto

%description
OpenOBEX - Free implementation of the Object Exchange protocol

%package devel
Summary: Development files of OpenOBEX libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains development files of Open OBEX library

%define _pkgdocdir %_docdir/%name-%version

%prep
%setup
%patch -p1
# fix udev rule
#subst 's|GROUP=\"plugdev\"|ENV{ID_MEDIA_PLAYER}="1"|' udev/openobex.rules.in
sed -i 's|MODE="660", GROUP="plugdev"|TAG+="uaccess"|' udev/openobex.rules.in

%build
%cmake -DCMAKE_INSTALL_DOCDIR=%_pkgdocdir
%cmake_build

%install
%cmakeinstall_std
cp AUTHORS ChangeLog README %buildroot%_pkgdocdir

%files
%_sbindir/obex-check-device
%_libdir/*.so.*
%_udevrulesdir/60-openobex.rules
%doc %_pkgdocdir/AUTHORS
%doc %_pkgdocdir/ChangeLog
%doc %_pkgdocdir/README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/OpenObex-%version/openobex-config-version.cmake
%_libdir/cmake/OpenObex-%version/openobex-config.cmake
%_libdir/cmake/OpenObex-%version/openobex-target-release.cmake
%_libdir/cmake/OpenObex-%version/openobex-target.cmake
%doc %_pkgdocdir/html/

%changelog
* Thu Jun 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.7.2-alt1
- 1.7.2

* Mon Jan 19 2015 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt2
- fixed incorrect udev.rules

* Sat Dec 06 2014 Yuri N. Sedunov <aris@altlinux.org> 1.7.1-alt1
- 1.7.1

* Thu Aug 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.6-alt1
- 1.6

* Sun Dec 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt3
- updated build dependencies

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.5-alt2
- updated build dependencies

* Mon Mar 23 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.5-alt1
- 1.5 release.

* Thu Nov 20 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.4-alt1
- 1.4 release.
- Removed %%post/%%postun stuff.

* Mon Jan 28 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.3-alt2
- Fix #14024.

* Fri Aug 11 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.3-alt1
- 1.3 version.
- Added libusb-devel, pkg-config and xmlto to BuildRequires.
- Removed -config from %%files section as it doesn't exist anymore.
- Rewrote %%descriptions and %%summaries.
- Build docs (thx vsu@).
- Substited Copyright tag with License.
- Fixed Requires.
- s/relaname/realname.
- Fixed %%post and %%postun.
- Added a switch to deal with static. Default: off.

* Wed Feb 01 2006 Anton Farygin <rider@altlinux.ru> 1.0.1-alt2.1
- NMU: fixed build for x86_64 (added autoreconf into build section)

* Fri Dec 12 2003 Grigory Milev <week@altlinux.ru> 1.0.1-alt2
- remove *.la files due policy

* Wed Oct 22 2003 Grigory Milev <week@altlinux.ru> 1.0.1-alt1
- new version released

* Thu Apr 17 2003 Grigory Milev <week@altlinux.ru> 1.0.0-alt2
- move static devellibraries to separate package

* Tue Jan 21 2003 Grigory Milev <week@altlinux.ru> 1.0.0-alt1
- new version released

* Tue Dec 10 2002 Grigory Milev <week@altlinux.ru> 0.9.8-alt1
- Initial build

