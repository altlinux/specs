%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-maps
Version: %ver_major.0
Release: alt1

Summary: Maps is a map application for GNOME
License: GPLv2+
Group: Graphical desktop/GNOME
Url: http://live.gnome.org/Design/Apps/Maps

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildArch: noarch

%define glib_ver 2.28
%define gtk_ver 3.7.10
%define tracker_ver 0.16
%define geoclue_ver 1.99.3

Requires: geoclue2 >= %geoclue_ver

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
%_datadir/%name
%_iconsdir/hicolor/*x*/*/%name.png
%config %_datadir/glib-2.0/schemas/org.gnome.maps.gschema.xml
%_datadir/appdata/%name.appdata.xml
%doc README NEWS

%changelog
* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Aug 01 2013 Yuri N. Sedunov <aris@altlinux.org> 3.9.5-alt1
- first build for people/gnome

