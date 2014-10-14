%define _name org.gnome.Weather

%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-weather
Version: %ver_major.1
Release: alt1

Summary: Access current weather conditions and forecasts
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://live.gnome.org/Design/Apps/Weather

#Source: %name-%version.tar
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

Obsoletes: %name-data
Provides:  %name-data = %version-%release

%define gtk_ver 3.11.4
%define gi_ver 1.35.9
%define gjs_ver 1.39.91
%define gweather_ver 3.14.1

Requires: libgweather-gir >= %gweather_ver
# find ./ -name *.js |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(GeocodeGlib)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(GWeather)

BuildRequires: rpm-build-gnome gnome-common intltool rpm-build-gir
BuildRequires: libgtk+3-devel >= %gtk_ver libgjs-devel >= %gjs_ver libgweather-devel >= %gweather_ver
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel libgweather-gir-devel
BuildRequires: libappstream-glib-devel

%description
%name is a small application that allows you to monitor the current
weather conditions for your city, or anywhere in the world, and to
access updated forecasts provided by various internet services.


%prep
%setup
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%name
%_datadir/applications/%_name.Application.desktop
%_datadir/%_name/
%_datadir/dbus-1/services/%_name.Application.service
%_datadir/dbus-1/services/%_name.BackgroundService.service
%_datadir/glib-2.0/schemas/%_name.Application.gschema.xml
%_iconsdir/hicolor/*/apps/%_name.Application.png
%_iconsdir/HighContrast/*x*/apps/%_name.Application.png
%_datadir/gnome-shell/search-providers/%_name.Application.search-provider.ini
%_datadir/appdata/%_name.Application.appdata.xml
%doc NEWS

%changelog
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

