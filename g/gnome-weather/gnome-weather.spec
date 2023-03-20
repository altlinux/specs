%def_disable snapshot

%define xdg_name org.gnome.Weather
%define ver_major 44
%define beta %nil
%define _libexecdir %_prefix/libexec

Name: gnome-weather
Version: %ver_major.0
Release: alt1%beta

Summary: Access current weather conditions and forecasts
Group: Graphical desktop/GNOME
License: GPL-2.0
Url: https://wiki.gnome.org/Apps/Weather

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

BuildArch: noarch

Obsoletes: %name-data
Provides:  %name-data = %version-%release

%define gtk4_ver 4.5
%define gi_ver 1.36.0
%define gjs_ver 1.71.0
%define gweather4_ver 3.90
%define adwaita_ver 1.2

Requires: libgjs >= %gjs_ver
Requires: libgweather4.0-gir >= %gweather4_ver
Requires: geoclue2

# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Geoclue)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GObject)
Requires: typelib(Gtk) = 4.0
Requires: typelib(GWeather) = 4.0
Requires: typelib(Adw) = 1
Requires: typelib(Graphene)

BuildRequires(pre): rpm-macros-meson rpm-build-gnome rpm-build-gir
BuildRequires: meson yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgtk4-devel >= %gtk4_ver libgjs-devel >= %gjs_ver
BuildRequires: libgweather4.0-devel >= %gweather4_ver pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk4-gir-devel libgweather4.0-gir-devel

%description
%name is a small application that allows you to monitor the current
weather conditions for your city, or anywhere in the world, and to
access updated forecasts provided by various internet services.


%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name %xdg_name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%xdg_name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/dbus-1/services/%xdg_name.BackgroundService.service
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/scalable/apps/%xdg_name.svg
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_iconsdir/hicolor/scalable/status/*.svg
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS

%changelog
* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (ported to GTK4)

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Wed Aug 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Fri Apr 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Mon Apr 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Sat Apr 04 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 25 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Sun Apr 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Fri Apr 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Mar 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Aug 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2.1-alt1
- 3.16.2.1

* Mon Apr 27 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Oct 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Oct 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Wed Apr 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Fri Mar 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first preview for people/gnome

