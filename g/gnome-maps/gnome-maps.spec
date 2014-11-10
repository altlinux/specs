%define ver_major 3.14
%define _libexecdir %_prefix/libexec
%define _name org.gnome.Maps

Name: gnome-maps
Version: %ver_major.2
Release: alt1

Summary: Maps is a map application for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/Design/Apps/Maps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.39.3
%define gtk_ver 3.10.0
%define tracker_ver 0.16
%define geocode_ver 3.11.92
%define geoclue_ver 2.1.0
%define champlain_ver 0.12.6

Requires: geoclue2 >= %geoclue_ver
Requires: libgeocode-glib-gir >= %geocode_ver
Requires: libchamplain-gir >= %champlain_ver

# find ./ -name *.js |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Champlain)
Requires: typelib(Clutter)
Requires: typelib(Cogl)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(GeocodeGlib)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(GtkChamplain)
Requires: typelib(GtkClutter)
Requires: typelib(Soup)

BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildRequires: libgjs-devel libgtk+3-gir-devel
BuildRequires: gnome-common intltool yelp-tools
BuildRequires: geoclue2-devel >= %geoclue_ver

%description
Maps is a map application for GNOME. It is currently in early
development with the goal of having a preview included in GNOME 3.10 due
in fall of 2013.

%prep
%setup

%build
%configure \
	--disable-static \
	--disable-schemas-compile
# SMP-incompatible build
%make

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
%_iconsdir/hicolor/*x*/*/%name.png
%_iconsdir/HighContrast/*x*/apps/%name.png
%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/org.gnome.maps.gschema.xml
%_datadir/appdata/%_name.appdata.xml
%doc README NEWS

%changelog
* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1.2-alt1
- 3.14.1.2

* Fri Oct 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Aug 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- first build for people/gnome

