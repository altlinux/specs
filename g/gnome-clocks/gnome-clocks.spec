%define _name org.gnome.clocks
%define ver_major 3.18

Name: gnome-clocks
Version: %ver_major.0
Release: alt1

Summary: Clock application designed for GNOME 3
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Clocks

Source: http://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define gweather_ver 3.14
%define geocode_ver 0.99.3

Requires: geoclue2

BuildRequires: intltool yelp-tools
BuildRequires: libgio-devel libgtk+3-devel >= 3.9.11 libnotify-devel
BuildRequires: libgsound-devel libgnome-desktop3-devel
BuildRequires: vala-tools gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libgweather-devel >= %gweather_ver libgeocode-glib-devel >= %geocode_ver
BuildRequires: geoclue2-devel

%description
Clock application designed for GNOME 3

%prep
%setup

%build
%autoreconf
%configure \
	--disable-schemas-compile
%make_build

%install
%makeinstall_std
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%_name.desktop
%_datadir/icons/*/*/apps/%name.png
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/dbus-1/services/%_name.service
%_datadir/gnome-shell/search-providers/%_name.search-provider.ini
%_iconsdir/hicolor/symbolic/apps/%name-symbolic.svg
%_datadir/appdata/%_name.appdata.xml
%doc README NEWS

%changelog
* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Feb 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.90-alt1
- first build for Sisyphus

