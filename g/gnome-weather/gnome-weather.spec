%define xdg_name org.gnome.Weather
%define ver_major 3.20
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

%define gtk_ver 3.12
%define gi_ver 1.36.0
%define gjs_ver 1.40.0
%define gweather_ver 3.20.1

Requires: libgweather-gir >= %gweather_ver
# find ./ -name "*.js" |/usr/lib/rpm/gir-js.req |sort|uniq|sed -e 's/^/Requires: /'
Requires: typelib(Gdk)
Requires: typelib(Geoclue)
Requires: typelib(Gio)
Requires: typelib(GLib)
Requires: typelib(GnomeDesktop)
Requires: typelib(GObject)
Requires: typelib(Gtk)
Requires: typelib(GWeather)

BuildRequires: rpm-build-gnome gnome-common intltool rpm-build-gir
BuildRequires: libgtk+3-devel >= %gtk_ver libgjs-devel >= %gjs_ver
BuildRequires: libgweather-devel >= %gweather_ver libgeoclue2-devel
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel libgweather-gir-devel
BuildRequires: libappstream-glib-devel

%description
%name is a small application that allows you to monitor the current
weather conditions for your city, or anywhere in the world, and to
access updated forecasts provided by various internet services.


%prep
%setup
[ ! -d m4 ] && mkdir m4
subst 's@\$(LN_S)@ln -s@' src/Makefile.am

%build
%autoreconf
%configure \
	--disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %xdg_name

%files -f %xdg_name.lang
%_bindir/%name
%_datadir/applications/%xdg_name.Application.desktop
%_datadir/%xdg_name/
%_datadir/dbus-1/services/%xdg_name.Application.service
%_datadir/dbus-1/services/%xdg_name.BackgroundService.service
%_datadir/glib-2.0/schemas/%xdg_name.Application.gschema.xml
%_iconsdir/hicolor/*/apps/%xdg_name.png
%_iconsdir/hicolor/symbolic/apps/%xdg_name-symbolic.svg
%_datadir/gnome-shell/search-providers/%xdg_name.Application.search-provider.ini
%_datadir/appdata/%xdg_name.Application.appdata.xml
%doc NEWS

%changelog
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

