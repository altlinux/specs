%define _unpackaged_files_terminate_build 1

%define _name org.gnome.taquin
%define __name gnome-taquin
%define ver_major 3.28
%define _libexecdir %_prefix/libexec

Name: gnome-games-taquin
Version: %ver_major.0
Release: alt1

Summary: Gnome tiles game
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Taquin

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.40.0
%define gtk_ver 3.15.0

BuildRequires: gnome-common intltool yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libcanberra-gtk3-devel

%description
Move tiles so that they reach their places.

%prep
%setup -n %__name-%version

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%_name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name-symbolic.svg
%_man6dir/%__name.*
%_datadir/dbus-1/services/%_name.service
%config %_datadir/glib-2.0/schemas/%_name.gschema.xml
%_datadir/metainfo/%_name.appdata.xml
%doc AUTHORS NEWS

%changelog
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

