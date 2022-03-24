%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define _name five-or-more
%define xdg_name org.gnome.%_name
%define ver_major 3.32
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.2
Release: alt2

Summary: A GNOME version of the color lines program
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Five-or-more

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

Provides:  %_name = %version-%release
Obsoletes: gnome-games-glines
Provides:  gnome-games-glines = %version-%release

%define glib_ver 2.32
%define gtk_ver 3.22.0

BuildRequires(pre): meson
BuildRequires: vala-tools
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: gsettings-desktop-schemas-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: pkgconfig(libgnome-games-support-1)

%description
Glines, is the GNOME port of the once popular Windows game called Color
Lines. The game's objective is to align as often as possible five balls
or more of the same color causing them to disappear, play as long as
possible, and be #1 in the High Scores.

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
%_iconsdir/hicolor/*/*/%{xdg_name}*.*
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Thu Mar 24 2022 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt2
- updated to 3.32.2-7-g4b26bc1 (fixed build with vala-0.56)

* Sat Mar 28 2020 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Fri Mar 13 2020 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Nov 08 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Aug 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Mon Aug 01 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
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

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Apr 03 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- fixed crash on startup

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



