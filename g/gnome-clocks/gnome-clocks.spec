%def_disable snapshot
%define xdg_name org.gnome.clocks
%define ver_major 44
%define beta %nil

Name: gnome-clocks
Version: %ver_major.0
Release: alt1%beta

Summary: Clock application designed for GNOME 3
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://wiki.gnome.org/Apps/Clocks

%if_disabled snapshot
Source: https://download.gnome.org/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.72
%define gweather_ver 3.99
%define geocode_ver 3.26.0
%define geoclue_ver 2.4
%define gtk4_ver 4.5
%define adwaita_ver 1.2

Requires: geoclue2

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools glib2-devel >= %glib_ver
BuildRequires: /usr/bin/appstream-util desktop-file-utils yelp-tools
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: libgsound-devel pkgconfig(gnome-desktop-4)
BuildRequires: gobject-introspection-devel libgtk4-gir-devel libgweather4.0-vala
BuildRequires: libgweather4.0-devel >= %gweather_ver libgeocode-glib2.0-devel >= %geocode_ver
BuildRequires: libgeoclue2-devel >= %geoclue_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

%description
Clock application designed for GNOME 3

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%xdg_name.desktop
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* NEWS*

%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0 (ported to GTK4)

* Sun Oct 17 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 42.beta

* Wed Sep 16 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun May 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sun Apr 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt2
- updated to 3.36.0-10-g107805f
  (fixed https://gitlab.gnome.org/GNOME/gnome-clocks/-/issues/91)

* Thu Mar 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Mar 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Oct 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sat Sep 01 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

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

