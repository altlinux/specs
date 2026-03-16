%def_disable snapshot
%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%define _name quadrapassel
%define ver_major 50
%define beta %nil
%define xdg_name org.gnome.Quadrapassel

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: Fit falling blocks together
Group: Games/Boards
License: GPL-3.0-or-later
Url: https://wiki.gnome.org/Apps/Quadrapassel

Vcs: https://gitlab.gnome.org/GNOME/quadrapassel.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Provides:  %_name = %EVR

%define glib_ver 2.44
%define gtk_ver 4.20
%define adw_ver 1.8
%define manette_ver 0.2.10

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools blueprint-compiler
BuildRequires: yelp-tools desktop-file-utils /usr/bin/appstreamcli
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: librsvg-devel
BuildRequires: pkgconfig(sndfile) pkgconfig(openal)
BuildRequires: libmanette-devel >= %manette_ver

%description
GNOME version of the popular russian game Tetris.
The goal of the game is to create complete horizontal lines of blocks,
which will disappear.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --all-name --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/sounds/%_name/
%_iconsdir/hicolor/scalable/apps/%{xdg_name}*.svg
%_iconsdir/hicolor/symbolic/apps/%{xdg_name}*.svg
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml


%changelog
* Mon Mar 16 2026 Yuri N. Sedunov <aris@altlinux.org> 50.0-alt1%beta
- 50.0

* Fri Dec 12 2025 Yuri N. Sedunov <aris@altlinux.org> 49.2.3-alt1
- 49.2.3

* Wed Dec 10 2025 Yuri N. Sedunov <aris@altlinux.org> 49.2.2-alt1
- 49.2.2

* Sat Nov 22 2025 Yuri N. Sedunov <aris@altlinux.org> 49.2.1-alt1
- 49.2.1

* Fri Nov 21 2025 Yuri N. Sedunov <aris@altlinux.org> 49.2-alt1
- 49.2

* Mon Oct 13 2025 Yuri N. Sedunov <aris@altlinux.org> 49.1-alt1
- 49.1

* Wed Sep 17 2025 Yuri N. Sedunov <aris@altlinux.org> 49.0.1-alt1
- 49.0.1

* Fri Jun 11 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Tue May 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Mon Oct 26 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Thu Aug 27 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.05-alt1
- 3.36.05

* Wed Jul 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.04-alt1
- 3.36.04

* Wed Apr 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.02-alt1
- 3.36.02

* Thu Mar 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.00-alt1
- 3.36.00

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Sat Sep 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Sun Jul 28 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



