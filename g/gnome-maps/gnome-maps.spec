%define ver_major 3.12
%define _libexecdir %_prefix/libexec

Name: gnome-maps
Version: %ver_major.0
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
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/*
%_datadir/applications/*
%_datadir/%name/
%_iconsdir/hicolor/*x*/*/%name.png
%config %_datadir/glib-2.0/schemas/org.gnome.maps.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README NEWS

%changelog
* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Aug 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- first build for people/gnome

