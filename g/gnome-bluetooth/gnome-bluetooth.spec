%def_disable snapshot

%define ver_major 3.20
%define api_ver 1.0
%define _libexecdir %_prefix/libexec

%def_enable introspection
%def_enable gtk_doc

Name: gnome-bluetooth
Version: %ver_major.1
Release: alt1

Summary: The GNOME Bluetooth Subsystem
License: GPLv2/LGPLv2
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/GnomeBluetooth

Provides: bluez-gnome = %version
Obsoletes: bluez-gnome < %version
Requires:  bluez >= 5
Requires: lib%name = %version-%release rfkill

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define gtk_ver 3.12.0

BuildRequires: gnome-common gtk-doc intltool yelp-tools itstool
BuildRequires: libgio-devel libgtk+3-devel >= %gtk_ver libudev-devel libnotify-devel
BuildRequires: libcanberra-gtk3-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}

%description
The GNOME Bluetooth Subsystem

%package -n lib%name
Summary: The GNOME Bluetooth Subsystem library
Group: System/Libraries

%description -n lib%name
This package provides GNOME Bluetooth Subsystem library

%package -n lib%name-gir
Summary: GObject introspection data for the GNOME Bluetooth library
Group: System/Libraries
Requires: lib%name = %version-%release

%description -n lib%name-gir
GObject introspection data for the GNOME Bluetooth library

%package -n lib%name-devel
Summary: The GNOME Bluetooth Subsystem development package
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
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
Requires: lib%name = %version-%release
Requires: lib%name-gir = %version-%release

%description -n lib%name-gir-devel
GObject introspection devel data for the GNOME Bluetooth library

%prep
%setup -q
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-icon-update \
	--disable-desktop-update \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}
%make_build

%install
%makeinstall_std

mv %buildroot%_bindir/bluetooth-sendto %buildroot%_bindir/%name-sendto
mkdir -p %buildroot%_altdir
cat > %buildroot%_altdir/%name <<EOF
%_bindir/bluetooth-sendto	%_bindir/%name-sendto	10
EOF

find %buildroot -name "*.la" -delete

%find_lang --with-gnome --output=global.lang %name gnome-bluetooth2


%files -f global.lang
%doc AUTHORS README NEWS
%_altdir/%name
%_bindir/*
%_desktopdir/*.desktop
%_datadir/%name
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/lib%name.so.*

%files -n lib%name-devel
%_includedir/%name/
%_libdir/lib%name.so
%_pkgconfigdir/%name-%api_ver.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/GnomeBluetooth-%api_ver.typelib

%files -n lib%name-gir-devel
%_girdir/GnomeBluetooth-%api_ver.gir
%endif

%changelog
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
