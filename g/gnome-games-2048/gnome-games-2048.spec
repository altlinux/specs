%define _unpackaged_files_terminate_build 1
%define _libexecdir %_prefix/libexec

%define _name 2048
%define __name gnome-%_name
%define ver_major 3.34
%define xdg_name org.gnome.TwentyFortyEight

Name: gnome-games-%_name
Version: %ver_major.4
Release: alt1

Summary: A 2048 clone for GNOME
Group: Games/Boards
License: %gpl3plus
Url: https://wiki.gnome.org/Apps/2048

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release

%define gtk_ver 3.22.3
%define clutter_gtk_ver 1.6
%define gee_ver 0.14
%define libgames_ver 1.2.0
%define vala_ver 0.24

BuildRequires(pre): meson rpm-build-licenses
BuildRequires: yelp-tools libappstream-glib-devel desktop-file-utils
BuildRequires: vala-tools >= %vala_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libclutter-gtk3-devel >= %clutter_gtk_ver
BuildRequires: libgee0.8-devel >= %gee_ver libgnome-games-support-devel >= %libgames_ver

%description
Move the tiles until you obtain the 2048 tile.

%prep
%setup -n %__name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%changelog
* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4
- updated License tag

* Tue Oct 29 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Sun Oct 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- rebuilt against libgnome-games-support-1.so.3

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- first build for Sisyphus
