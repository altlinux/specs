%def_disable snapshot

%define _name gnome-bluetooth
%define ver_major 42
%define beta %nil
%define api_ver 3.0
%define sover 13
%define _libexecdir %_prefix/libexec

%def_enable introspection
%def_enable gtk_doc
%def_enable sendto
%def_disable check

Name: %_name%api_ver
Version: %ver_major.5
Release: alt1%beta

Summary: The GNOME Bluetooth Subsystem
License: GPL-2.0 and LGPL-2.1
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/GnomeBluetooth

Requires:  bluez >= 5.51
Requires: lib%name = %EVR rfkill

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define gtk_ver 4.4.0
%define adwaita_ver 1.1
%define dbusmock_ver 0.23.0
%define upower_ver 0.99.14

BuildRequires(pre): rpm-macros-meson rpm-macros-alternatives
BuildRequires: meson gtk-doc yelp-tools
BuildRequires: libgio-devel libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: libudev-devel libnotify-devel
BuildRequires: pkgconfig(upower-glib) >= %upower_ver libgsound-devel
%if_enabled introspection
BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel
%endif
%{?_enable_check:BuildRequires: bluez dbus python3-module-pygobject3 python3-module-dbus
BuildRequires: python3-module-dbusmock >= %dbusmock_ver typelib(Gtk) = 4.0}

%description
The GNOME Bluetooth Subsystem

%package -n lib%name
Summary: The GNOME Bluetooth Subsystem library
Group: System/Libraries

%description -n lib%name
This package provides GNOME Bluetooth Subsystem library.

%package -n lib%name-ui
Summary: The GNOME Bluetooth UI library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-ui
This package provides GNOME Bluetooth UI library.

%package -n lib%name-gir
Summary: GObject introspection data for the GNOME Bluetooth library
Group: System/Libraries
Requires: lib%name = %EVR

%description -n lib%name-gir
GObject introspection data for the GNOME Bluetooth library

%package -n lib%name-devel
Summary: The GNOME Bluetooth Subsystem development package
Group: Development/C
Requires: lib%name = %EVR

%description -n lib%name-devel
This package provides GNOME Bluetooth Subsystem development files

%package -n lib%name-ui-devel
Summary: The GNOME Bluetooth Subsystem development package
Group: Development/C
Requires: lib%name-ui = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-ui-devel
This package provides GNOME Bluetooth Subsystem development files

%package -n lib%name-devel-doc
Summary: The GNOME Bluetooth Subsystem development documentation
Group: Development/C
BuildArch: noarch
Conflicts: lib%name < %version

%description -n lib%name-devel-doc
This package provides GNOME Bluetooth Subsystem development documentation

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the GNOME Bluetooth library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-devel = %EVR
Requires: lib%name-gir = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Bluetooth library

%prep
%setup -n %_name-%version%beta

%build
%meson \
	%{?_enable_gtk_doc:-Dgtk_doc=true} \
	%{?_enable_introspection:-Dintrospection=true} \
	%{?_disable_sendto:-Dsendto=false}
%nil
%meson_build

%install
%meson_install

%if_enabled sendto
mv %buildroot%_bindir/bluetooth-sendto %buildroot%_bindir/%name-sendto
mv %buildroot%_desktopdir/bluetooth-sendto.desktop \
   %buildroot%_desktopdir/%name-bluetooth-sendto.desktop
sed -i 's|\(Exec=\)bluetooth\(-sendto\)|\1%name\2|' \
%buildroot%_desktopdir/%name-bluetooth-sendto.desktop

mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_bindir/bluetooth-sendto	%_bindir/%name-sendto	5
EOF
%endif

%find_lang --with-gnome --output=%_name.lang %_name-%api_ver

%check
dbus-run-session %__meson_test


%files -f %_name.lang
%{?_enable_sendto:%_altdir/%name
%_bindir/%name-sendto
%_desktopdir/%name-bluetooth-sendto.desktop
%_man1dir/bluetooth-sendto.1*}
%_datadir/%_name-%api_ver
%doc AUTHORS README* NEWS

%files -n lib%name
%_libdir/lib%_name-%api_ver.so.%{sover}*

%files -n lib%name-ui
%_libdir/lib%_name-ui-%api_ver.so.%{sover}*

%files -n lib%name-devel
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%files -n lib%name-ui-devel
%_includedir/%_name-%api_ver
%_libdir/lib%_name-ui-%api_ver.so
%_pkgconfigdir/%_name-ui-%api_ver.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/GnomeBluetooth-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GnomeBluetooth-%api_ver.gir
%endif

%changelog
* Tue Dec 13 2022 Yuri N. Sedunov <aris@altlinux.org> 42.5-alt1
- 42.5

* Mon Sep 05 2022 Yuri N. Sedunov <aris@altlinux.org> 42.4-alt1
- 42.4

* Wed Aug 24 2022 Yuri N. Sedunov <aris@altlinux.org> 42.3-alt1
- 42.3

* Thu Jul 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42.2-alt1
- 42.2

* Thu Jun 09 2022 Yuri N. Sedunov <aris@altlinux.org> 42.1-alt1
- 42.1

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Thu Mar 10 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (3.0 API)

* Fri Mar 26 2021 Yuri N. Sedunov <aris@altlinux.org> 3.34.5-alt1
- 3.34.5 (changed soname back)
- enabled %%check

* Mon Mar 22 2021 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4 (bumped soname)

* Thu Oct 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Wed Sep 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Mar 09 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Fri Sep 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Mar 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Aug 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Thu Jul 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Sep 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Feb 13 2017 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Wed Jul 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt2
- removed conflict with blueman provided by blueberry now

* Tue May 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3

* Mon Jan 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Nov 10 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sat Apr 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Dec 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2.1
- removed obex-data-server from rqs

* Sun Dec 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt2
- 3.10_60b39bce9
- improved 61-gnome-bluetooth-rfkill.rules

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Sep 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.91-alt1
- 3.9.91

* Mon Jun 03 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Nov 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Wed Jul 04 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Jun 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Wed Mar 21 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Tue Feb 07 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Mon Oct 17 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Mon Sep 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Wed Sep 21 2011 Yuri N. Sedunov <aris@altlinux.org> 3.1.92-alt1
- 3.1.92

* Tue Jun 07 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1 snapshot
- added rfkill do rqs and corresponding udev rule

* Sun May 29 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0
- move GnomeBluetoothApplet-1.0.{typelib,gir} in system introspection
  directories
- put symlinks to lib%%name-applet in %%_libdir so gnome-shell can find
  this libarary

* Tue Apr 26 2011 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt2
- updated build dependencies

* Tue Oct 12 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.32.0-alt1
- 2.32.0

* Tue Mar 30 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.30.0-alt1
- 2.30.0

* Sat Mar 13 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.91-alt2
- new subpackage nautilus-sendto-bluetooth

* Mon Feb 15 2010 Valery Inozemtsev <shrek@altlinux.ru> 2.29.91-alt1
- 2.29.91

* Wed Dec 23 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.6-alt1
- 2.28.6

* Sun Dec 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.4-alt1
- 2.28.4

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.3-alt1
- 2.28.3

* Tue Sep 29 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.1-alt1
- 2.28.1

* Thu Sep 24 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt2
- updated russian translations

* Sun Sep 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.28.0-alt1
- 2.28.0

* Thu Sep 03 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.90-alt1
- 2.27.90

* Wed Aug 05 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.9-alt1
- 2.27.9

* Wed Jul 22 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.8-alt1
- 2.27.8

* Mon Jul 06 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.7.1-alt1
- 2.27.7.1

* Thu Jun 25 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.7-alt1
- 2.27.7

* Wed Jun 17 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.6-alt1
- 2.27.6 release

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.6-alt0.pre1
- added requires obex-data-server, obexd

* Thu Jun 11 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.6-alt0.pre
- 2.27.6 prerelease

* Thu May 07 2009 Valery Inozemtsev <shrek@altlinux.ru> 2.27.5-alt1
- initial release
