%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define ver_major 3.34
%define xdg_name ca.desrt.dconf-editor

Name: dconf-editor
Version: %ver_major.3
Release: alt1

Summary: dconf confuguration editor
Group: Graphical desktop/GNOME
License: GPLv3
Url: https://wiki.gnome.org/Projects/dconf

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.55.1
%define gtk_ver 3.22.27
%define dconf_ver 0.26.1
%define vala_ver 0.36.11

Requires: dconf >= %dconf_ver

BuildRequires(pre): meson
BuildPreReq: libgio-devel >= %glib_ver
BuildPreReq: libgtk+3-devel >= %gtk_ver libdconf-devel >= %dconf_ver
BuildPreReq: vala-tools >= %vala_ver
BuildRequires: libxml2-devel rpm-build-gnome
BuildRequires: libappstream-glib-devel yelp-tools
BuildRequires: libdconf-vala

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides graphical dconf configuration editor.


%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name dconf

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/*.*
%_man1dir/%name.1.*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
# "nosort" bad option?
%_datadir/bash-completion/completions/%name
%doc README

%changelog
* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sat Jan 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

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

