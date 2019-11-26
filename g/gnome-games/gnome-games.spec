%def_disable snapshot
%define ver_major 3.34
%define xdg_name org.gnome.Games

Name: gnome-games
Version: %ver_major.2
Release: alt1

Summary: Simple game launcher for GNOME
License: %gpl3plus
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Games

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): meson rpm-build-licenses
BuildRequires: vala-tools
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(librsvg-2.0) >= 2.44
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(manette-0.2) >= 0.2.3
BuildRequires: pkgconfig(retro-gtk-0.14) >= 0.18.0
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tracker-sparql-2.0)
BuildRequires: libhandy-devel >= 0.0.8

%description
Games is a GNOME3 application to browse your video games library and to
easily pick and play a game from it.

%package devel
Summary: Development package for GNOME Games
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides files needed to develop plugins for GNOME Games.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/plugins/
%_datadir/%name/
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

#%files devel
#%_includedir/lib%name.h
#%_vapidir/%name.vapi


%changelog
* Tue Nov 26 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2
- updated License tag

* Sat Oct 05 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Tue Mar 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- updated to 3.32.0-7-g03815ac3

* Sun Oct 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Sun Sep 23 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Sun Sep 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0, no more virtual package

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0
