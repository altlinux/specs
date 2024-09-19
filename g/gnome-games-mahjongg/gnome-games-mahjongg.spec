%def_disable snapshot

%define _unpackaged_files_terminate_build 1

%define _name mahjongg
%define xdg_name org.gnome.Mahjongg
%define __name gnome-%_name
%define ver_major 47
%define beta %nil
%define _libexecdir %_prefix/libexec

%def_enable check

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: Classic Chinese Tile Game
Group: Games/Boards
License: GPL-2.0-or-later
Url: https://wiki.gnome.org/Apps/Mahjongg

Vcs: https://gitlab.gnome.org/GNOME/gnome-mahjongg.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version%beta.tar.xz
%else
Source: %__name-%version%beta.tar
%endif

Provides:  %__name = %EVR

%define glib_ver 2.72.0
%define gtk4_ver 4.14.0
%define adw_ver 1.5
%define rsvg_ver 2.46

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson vala-tools yelp-tools 
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk4-devel >= %gtk4_ver
BuildRequires: libadwaita-devel >= %adw_ver
BuildRequires: librsvg-devel >= %rsvg_ver
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Gnome Mahjongg, or Mahjongg for short, is a solitaire (one player)
version of the classic Eastern tile game, Mahjongg.

%prep
%setup -n %__name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%check
%__meson_test

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_datadir/%__name
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%_man6dir/%__name.*

%changelog
* Sat Sep 14 2024 Yuri N. Sedunov <aris@altlinux.org> 47.0-alt1
- 47.0

* Thu Apr 18 2024 Yuri N. Sedunov <aris@altlinux.org> 3.40.1-alt1
- 3.40.1

* Wed May 31 2023 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0 (ported to GTK4/Libadwaita)

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt2
- updated to 3.38.3-7-g2d161cc
- fixed build with meson >= 0.61

* Sun Nov 01 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sat Oct 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Sep 19 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Apr 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Fri Mar 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Thu Sep 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
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

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

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

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Sep 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- no more sgid bit for /usr/bin/gnome-mahjongg

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



