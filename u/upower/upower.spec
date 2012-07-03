%define _libexecdir %_prefix/libexec/upower
%define systemdsystemunitdir /lib/systemd/system

Name: upower
Version: 0.9.17
Release: alt1
Summary: Power Management Service
License: GPLv2+
Group: System/Libraries
URL: http://cgit.freedesktop.org/upower/
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Provides: DeviceKit-power = 016
Obsoletes: DeviceKit-power < 016

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gtk-doc intltool libdbus-glib-devel libgio-devel libgudev-devel
BuildRequires: libpolkit1-devel libudev-devel libusb-devel gobject-introspection-devel
BuildRequires: libimobiledevice-devel systemd-devel

%description
UPower provides a daemon, API and command line tools for
managing power devices attached to the system.

%package -n lib%name
Summary: %name libraries
Group: System/Libraries
Provides: libdevkit-power = 016
Obsoletes: libdevkit-power < 016

%description -n lib%name
Libraries for %name

%package -n lib%name-devel
Summary: Development libraries and headers for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: libdevkit-power-devel = 016
Obsoletes: libdevkit-power-devel < 016

%description -n lib%name-devel
Headers, libraries and API docs for %name

%package -n lib%name-gir
Summary: GObject introspection data for the UPower library
Group: System/Libraries
Requires: lib%name = %version-%release
Provides: libdevkit-power-gir = 016
Obsoletes: libdevkit-power-gir < 016

%description -n lib%name-gir
GObject introspection data for the UPower library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the UPower library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release lib%name-devel = %version-%release
Provides: libdevkit-power-gir-devel = 016
Obsoletes: libdevkit-power-gir-devel < 016

%description -n lib%name-gir-devel
GObject introspection devel data for the UPower library

%prep
%setup -q
%patch -p1

rm -f acinclude.m4

%build
%autoreconf
%configure \
	--enable-gtk-doc \
	--with-systemdsystemunitdir=%systemdsystemunitdir \
	--libexecdir=%_libexecdir \
	--localstatedir=%_var \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%find_lang %name

%files -f %name.lang
%doc AUTHORS NEWS README
%dir %_sysconfdir/UPower
%_sysconfdir/UPower/*.conf
%_sysconfdir/dbus-1/system.d/*.conf
%systemdsystemunitdir/*
/lib/udev/rules.d/*.rules
%_bindir/*
%_libexecdir
%_datadir/dbus-1/system-services/*.service
%_datadir/polkit-1/actions/*.policy
%_mandir/man?/*
%dir %_var/lib/%name

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/dbus-1/interfaces/*.xml
%_datadir/gtk-doc/html/*

%files -n lib%name-gir
%_libdir/girepository-1.0/*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/*.gir

%changelog
* Tue Jun 26 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.17-alt1
- 0.9.17

* Wed May 02 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.16-alt1
- 0.9.16

* Mon Apr 09 2012 Valery Inozemtsev <shrek@altlinux.ru> 0.9.15-alt2
- rebuild with libimobiledevice 1.1.3

* Mon Dec 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.15-alt1
- 0.9.15

* Mon Oct 03 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.14-alt1
- 0.9.14

* Tue Sep 06 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.13-alt1
- 0.9.13

* Tue Jul 05 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.12-alt1
- 0.9.12

* Sat May 28 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.11-alt1
- 0.9.11

* Wed May 04 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.10-alt1
- 0.9.10

* Mon Mar 21 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Fri Jan 07 2011 Valery Inozemtsev <shrek@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt3
- dropped unused DeviceKit

* Fri Nov 05 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt2
- packaged /var/lib/upower

* Thu Nov 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Wed Oct 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt2
- fixed building with gobject-introspection 0.9.10

* Mon Oct 04 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Fri Jul 23 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.5-alt1
- 0.9.5

* Wed May 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.4-alt1
- 0.9.4

* Thu May 06 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Wed Apr 07 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Thu Apr 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt3
- rebuild

* Wed Mar 10 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt2
- rebuild with rpm-build-gir

* Wed Mar 03 2010 Valery Inozemtsev <shrek@altlinux.ru> 0.9.1-alt1
- 0.9.1

* Mon Feb 01 2010 Valery Inozemtsev <shrek@altlinux.ru> 015-alt1
- UPower 0.9.0

* Sat Jan 09 2010 Valery Inozemtsev <shrek@altlinux.ru> 014-alt1
- 014

* Mon Dec 28 2009 Valery Inozemtsev <shrek@altlinux.ru> 013-alt2
- fised build gtk doc

* Wed Dec 09 2009 Valery Inozemtsev <shrek@altlinux.ru> 013-alt1
- 013

* Fri Nov 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 012-alt2
- fixed incorrect battery recall warning for Lenovo T61

* Mon Oct 19 2009 Valery Inozemtsev <shrek@altlinux.ru> 012-alt1
- 012

* Fri Oct 16 2009 Valery Inozemtsev <shrek@altlinux.ru> 011-alt1
- 011

* Mon Aug 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 010-alt1
- 010

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 009-alt1
- 009

* Mon Jun 01 2009 Valery Inozemtsev <shrek@altlinux.ru> 008-alt1
- 008

* Wed May 27 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt4
- git snapshot 2009-05-26 (cf9692f1e93fd32759530fa98ec7b5947795eb6d)
- relocated devel files

* Fri May 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt3
- git snapshot 2009-05-13 (296a09988bba71183635843f143979c7551fc0f3)

* Mon Apr 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt2
- added hibernate-script support

* Sat Apr 04 2009 Valery Inozemtsev <shrek@altlinux.ru> 007-alt1
- 007

* Mon Dec 01 2008 Valery Inozemtsev <shrek@altlinux.ru> 002-alt1
- initial release

