%define ver_major 3.22
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define _name org.gnome.Maps

Name: gnome-maps
Version: %ver_major.2
Release: alt1

Summary: Maps is a map application for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Maps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

%set_typelibdir %_libdir/%name/girepository-1.0

%define glib_ver 2.39.3
%define gjs_ver 1.44.0
%define tracker_ver 0.16
%define geocode_ver 3.20.0
%define geoclue_ver 2.4.0
%define champlain_ver 0.12.14

Requires: geoclue2 >= %geoclue_ver
Requires: libgeocode-glib-gir >= %geocode_ver
Requires: libchamplain-gir >= %champlain_ver

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Champlain)
Requires: typelib(Clutter)
Requires: typelib(Gdk)
Requires: typelib(GdkPixbuf)
Requires: typelib(Geoclue)
Requires: typelib(GeocodeGlib)
Requires: typelib(GFBGraph)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeMaps)
Requires: typelib(Goa)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(GtkChamplain)
Requires: typelib(GtkClutter)
Requires: typelib(GWeather)
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Rest)
Requires: typelib(Secret)
Requires: typelib(Soup)
Requires: typelib(WebKit2)

BuildPreReq: libgio-devel >= %glib_ver
BuildRequires: libgjs-devel >= %gjs_ver gobject-introspection-devel
BuildRequires: gnome-common intltool yelp-tools
BuildRequires: geoclue2-devel >= %geoclue_ver
BuildRequires: libgee0.8-devel libfolks-devel libgeocode-glib-devel libchamplain-gtk3-devel
BuildRequires: libgeocode-glib-gir-devel libchamplain-gtk3-gir-devel librest-gir-devel
BuildRequires: libclutter-gir-devel libcogl-gir-devel

%description
Maps is a map application for GNOME.

%prep
%setup

%build
%autoreconf
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
%_libdir/%name/
%_datadir/applications/*
%_datadir/%name/
%_iconsdir/hicolor/*x*/*/%_name.png
%_iconsdir/hicolor/symbolic/apps/%{_name}*.svg
%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/appdata/%_name.appdata.xml
%doc README NEWS

%exclude %_libdir/%name/*.la
%exclude %_libdir/%name/*.so
%exclude %_girdir/GnomeMaps-%api_ver.gir

%changelog
* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu Sep 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3.1-alt1
- 3.20.3.1

* Mon Aug 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Sun Jul 31 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Sun Oct 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Fri Sep 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0.1-alt1
- 3.18.0.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

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

