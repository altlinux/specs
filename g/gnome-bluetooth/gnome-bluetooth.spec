%define ver_major 3.4

%def_enable introspection
%def_enable sendto
%def_enable geoclue
%def_enable gtk_doc

Name: gnome-bluetooth
Version: %ver_major.2
Release: alt1

Summary: The GNOME Bluetooth Subsystem
License: GPLv2/LGPLv2
Group: System/Libraries
Url: http://live.gnome.org/GnomeBluetooth

Provides: bluez-gnome = %version
Obsoletes: bluez-gnome < %version
Conflicts: blueman < 1.10-alt4
Requires: lib%name = %version-%release bluez obex-data-server obexd rfkill

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
# https://bugzilla.redhat.com/show_bug.cgi?id=514798
Source1: 61-gnome-bluetooth-rfkill.rules

Patch: %name-3.3.92-alt-gir.patch

BuildRequires: gnome-common gtk-doc intltool
BuildRequires: libgio-devel libgtk+3-devel libnotify-devel libXi-devel libdbus-glib-devel
%{?_enable_sendto:BuildRequires: nautilus-sendto-devel}
%{?_enable_geoclue:BuildRequires: libGConf-devel libgeoclue-devel}
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

%package -n nautilus-sendto-bluetooth
Summary: Send files from nautilus to bluetooth
Group: Graphical desktop/GNOME
Requires: %name = %version-%release
Requires: lib%name = %version-%release
Provides: nautilus-sendto-plugin = %version-%release

%description -n nautilus-sendto-bluetooth
This application provides integration between nautilus and bluetooth.
It adds a Nautilus context menu component ("Send To...") and features
a dialog for insert the bluetooth device which you want to send the
file/files

%prep
%setup -q
%patch -p1

%build
gnome-doc-prepare -f
%autoreconf
%configure \
	--disable-schemas-compile \
	--disable-icon-update \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}
%make_build

%install
%make DESTDIR=%buildroot install

install -pD -m0644 %{SOURCE1} %buildroot/lib/udev/rules.d/61-gnome-bluetooth-rfkill.rules

# temporarily fix for gnome-shell that requires libgnome-bluetooth-applet library
for f in %buildroot%_libdir/%name/lib%name-applet*; do
ln -s %name/`basename $f` %buildroot%_libdir/`basename $f`
done

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
%_sysconfdir/xdg/autostart/bluetooth-applet.desktop
%_bindir/*
%dir %_libdir/%name
%dir %_libdir/%name/plugins
%_libdir/%name/plugins/*.so
/lib/udev/rules.d/61-gnome-bluetooth-rfkill.rules
%_desktopdir/*.desktop
%_datadir/%name
%_datadir/GConf/gsettings/*
%_datadir/glib-2.0/schemas/*.xml
%_iconsdir/hicolor/*/*/*
%_man1dir/*.1*

%if_enabled sendto
%files -n nautilus-sendto-bluetooth
%_libdir/nautilus-sendto/plugins/*.so
%endif

%files -n lib%name
%_libdir/*.so.*
%_libdir/%name/lib%name-applet.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so
%_libdir/%name/lib%name-applet.so
%_pkgconfigdir/*

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/GnomeBluetooth-1.0.typelib
%_typelibdir/GnomeBluetoothApplet-1.0.typelib

%files -n lib%name-gir-devel
%_girdir/GnomeBluetooth-1.0.gir
%_girdir/GnomeBluetoothApplet-1.0.gir
%endif

%changelog
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
