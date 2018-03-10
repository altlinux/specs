%define xdg_name org.gnome.clocks
%define ver_major 3.28

Name: gnome-clocks
Version: %ver_major.0
Release: alt1

Summary: Clock application designed for GNOME 3
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Clocks

Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version.tar.xz

%define gweather_ver 3.27.2
%define geocode_ver 3.18.0
%define geoclue_ver 2.4
%define gtk_ver 3.20.0

Requires: geoclue2

BuildRequires(pre): meson yelp-tools
BuildRequires: yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel libgtk+3-devel >= %gtk_ver libnotify-devel
BuildRequires: libgsound-devel libgnome-desktop3-devel
BuildRequires: vala-tools gobject-introspection-devel libgtk+3-gir-devel libgweather-vala
BuildRequires: libgweather-devel >= %gweather_ver libgeocode-glib-devel >= %geocode_ver
BuildRequires: libgeoclue2-devel >= %geoclue_ver

%description
Clock application designed for GNOME 3

%prep
%setup

%build
%meson -Ddisable-schemas-compile=true
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/%name/
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_datadir/icons/*/*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README NEWS

%changelog
* Sat Mar 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Oct 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Sat Sep 03 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Sun May 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

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

