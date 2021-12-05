%define ver_major 41
%define beta %nil
%define api_ver 1.0
%define _libexecdir %_prefix/libexec
%define xdg_name org.gnome.Maps

Name: gnome-maps
Version: %ver_major.2
Release: alt1%beta

Summary: Maps is a map application for GNOME
License: GPL-2.0 and LGPL-2.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Maps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz

%set_typelibdir %_libdir/%name/girepository-1.0

%define glib_ver 2.44
%define gjs_ver 1.66
%define geocode_ver 3.20.0
%define geoclue_ver 2.4.0
%define champlain_ver 0.12.19

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
Requires: typelib(Gtk) = 3.0
Requires: typelib(GtkChamplain)
Requires: typelib(GtkClutter)
Requires: typelib(GWeather)
Requires: typelib(Handy) = 1
Requires: typelib(Pango)
Requires: typelib(PangoCairo)
Requires: typelib(Rest)
Requires: typelib(Secret)
Requires: typelib(Soup) = 2.4
Requires: typelib(WebKit2) = 4.0

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgjs-devel >= %gjs_ver gobject-introspection-devel
BuildRequires: pkgconfig(geoclue-2.0) >= %geoclue_ver
BuildRequires: libgee0.8-devel libfolks-devel libgeocode-glib-devel libchamplain-gtk3-devel
BuildRequires: libgeocode-glib-gir-devel libchamplain-gtk3-gir-devel librest-gir-devel
BuildRequires: libclutter-gir-devel libcogl-gir-devel
BuildRequires: pkgconfig(libhandy-1)

%description
Maps is a map application for GNOME.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_libdir/%name/
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/symbolic/apps/%{xdg_name}*.svg
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README NEWS

%exclude %_libdir/%name/*.so
%exclude %_datadir/%name/gir-1.0/GnomeMaps-%api_ver.gir

%changelog
* Sun Dec 05 2021 Yuri N. Sedunov <aris@altlinux.org> 41.2-alt1
- 41.2

* Sun Oct 31 2021 Yuri N. Sedunov <aris@altlinux.org> 41.1-alt1
- 41.1

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sat Sep 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.5-alt1
- 40.5

* Fri Aug 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Sat Jul 10 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Fri Jun 04 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sun May 02 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sat Mar 13 2021 Yuri N. Sedunov <aris@altlinux.org> 40-alt0.8.rc
- 40.rc

* Sat Feb 13 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.4-alt1
- 3.38.4

* Sat Jan 09 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sat Nov 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Oct 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1.1-alt1
- 3.38.1.1

* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sat Jul 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sat Apr 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sat Jan 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Mon Nov 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Mon Sep 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri May 24 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2.1-alt1
- 3.32.2.1

* Mon May 06 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Sun Mar 31 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Dec 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Thu Nov 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2.1-alt1
- 3.30.2.1

* Mon Oct 22 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Mon Sep 24 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Apr 09 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon May 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Tue May 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

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

