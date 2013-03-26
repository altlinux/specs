%define ver_major 3.8
%define _libexecdir %_prefix/libexec

Name: gnome-weather
Version: %ver_major.0
Release: alt1

Summary: Access current weather conditions and forecasts
Group: Graphical desktop/GNOME
License: GPLv3+
Url: https://live.gnome.org/Design/Apps/Weather

#Source: %name-%version.tar
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

Requires: %name-data = %version-%release
Requires: libgweather-gir

%add_typelib_req_skiplist typelib(Gd)

%define gtk_ver 3.7.10
%define gi_ver 1.35.9

BuildRequires: rpm-build-gnome gnome-common intltool
BuildRequires: libgtk+3-devel >= %gtk_ver libgjs-devel
BuildRequires: gobject-introspection-devel >= %gi_ver libgtk+3-gir-devel

%description
%name is a small application that allows you to monitor the current
weather conditions for your city, or anywhere in the world, and to
access updated forecasts provided by various internet services.

%package data
Summary: Arch independent files for %name
Group: Graphical desktop/GNOME
BuildArch: noarch

%description data
This package provides noarch data needed for %name to work.


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

%find_lang --with-gnome %name

%files
%_bindir/%name
%dir %_libdir/%name/
%dir %_libdir/%name/girepository-1.0
%_libdir/%name/girepository-1.0/Gd-1.0.typelib
%_libdir/%name/libgd.so
%doc NEWS

%exclude %_libdir/%name/libgd.la

%files data  -f %name.lang
%_datadir/applications/%name.desktop
%_datadir/%name/
%_datadir/glib-2.0/schemas/org.gnome.Weather.Application.gschema.xml


%changelog
* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Fri Mar 08 2013 Yuri N. Sedunov <aris@altlinux.org> 0.2-alt1
- first preview for people/gnome

