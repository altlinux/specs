%define _unpackaged_files_terminate_build 1
%define ver_major 3.20
%define _name ca.desrt.dconf-editor

Name: dconf-editor
Version: %ver_major.3
Release: alt1

Summary: dconf confuguration editor
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://wiki.gnome.org/Projects/dconf

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define gtk_ver 3.19.7
%define dconf_ver 0.24

Requires: dconf >= %dconf_ver

BuildPreReq: libgtk+3-devel >= %gtk_ver libdconf-devel >= %dconf_ver
BuildRequires: libxml2-devel rpm-build-gnome gnome-common vala-tools
BuildRequires: intltool libappstream-glib-devel yelp-tools

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides graphical dconf configuration editor.


%prep
%setup

%build
%autoreconf
%configure

%make_build

%install
%makeinstall_std

%find_lang --with-gnome --output=%name.lang %name dconf

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_iconsdir/hicolor/*/apps/*.*
%_man1dir/%name.1.*
%_datadir/appdata/%_name.appdata.xml
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%doc README

%changelog
* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- first build for people/gnome

