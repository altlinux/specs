%define _unpackaged_files_terminate_build 1

%define _name org.gnome.taquin
%define __name gnome-taquin
%define xdg_name org.gnome.Taquin
%define ver_major 3.34
%define _libexecdir %_prefix/libexec

Name: gnome-games-taquin
Version: %ver_major.2
Release: alt1

Summary: Gnome tiles game
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Taquin

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.40.0
%define gtk_ver 3.15.0

BuildRequires(pre): meson
BuildRequires: vala-tools
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libgsound-devel

%description
Move tiles so that they reach their places.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_man6dir/%__name.*
#%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc AUTHORS NEWS COPYING*

%changelog
* Wed Nov 27 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 07 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Thu Mar 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Oct 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
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

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Fri Dec 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.15.3-alt1
- first build for people/gnome

