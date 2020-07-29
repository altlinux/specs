%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%define _name quadrapassel
%define ver_major 3.36
%define xdg_name org.gnome.Quadrapassel

Name: gnome-games-%_name
Version: %ver_major.04
Release: alt1

Summary: A tetris clone
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Quadrapassel

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.12.0

BuildRequires(pre): meson
BuildRequires: vala-tools
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: librsvg-devel libclutter-gtk3-devel libcanberra-gtk3-devel libcanberra-vala
BuildRequires: libmanette-devel libgsound-devel

%description
GNOME version of the popular russian game Tetris.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %_name

%files -f %_name.lang
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/scalable/apps/%{xdg_name}*.svg
%_iconsdir/hicolor/symbolic/apps/%{xdg_name}*.svg
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml


%changelog
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



