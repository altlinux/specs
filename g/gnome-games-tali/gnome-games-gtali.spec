%define _unpackaged_files_terminate_build 1

%define _name tali
%define xdg_name org.gnome.Tali
%define ver_major 40
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.9
Release: alt1

Summary: Gnome version of Yahtzee Dice Game
Group: Games/Boards
License: GPL-2.0
Url: https://wiki.gnome.org/Apps/Tali

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides: %_name = %version-%release
Obsoletes: gnome-games-gtali
Provides: gnome-games-gtali = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.16.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson yelp-tools desktop-file-utils
BuildRequires: gsettings-desktop-schemas-devel libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libgnome-games-support-devel

%description
Gnome Tali is a sort of poker with dice and less money. You roll five
dice three times and try to create the best hand. Your two rerolls may
include any or all of your dice.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%_name.lang %_name gtali

%files -f %_name.lang
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/%xdg_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Tue Jan 24 2023 Yuri N. Sedunov <aris@altlinux.org> 40.9-alt1
- 40.9

* Sat Aug 06 2022 Yuri N. Sedunov <aris@altlinux.org> 40.8-alt1
- 40.8

* Sat Apr 23 2022 Yuri N. Sedunov <aris@altlinux.org> 40.7-alt1
- 40.7

* Sun Mar 20 2022 Yuri N. Sedunov <aris@altlinux.org> 40.6-alt1
- 40.6

* Thu Mar 03 2022 Yuri N. Sedunov <aris@altlinux.org> 40.5-alt1
- 40.5

* Sat Oct 30 2021 Yuri N. Sedunov <aris@altlinux.org> 40.4-alt1
- 40.4

* Sun Sep 19 2021 Yuri N. Sedunov <aris@altlinux.org> 40.3-alt1
- 40.3

* Mon Aug 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40.2-alt1
- 40.2

* Sat May 15 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Sun Jan 10 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Sun Nov 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Mon Sep 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Sun Jul 05 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sun Mar 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Thu Aug 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

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

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Sep 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome

