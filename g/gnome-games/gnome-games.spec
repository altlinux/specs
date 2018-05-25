%define ver_major 3.28
%define xdg_name org.gnome.Games

Name: gnome-games
Version: %ver_major.0
Release: alt1

Summary: Simple game launcher for GNOME
License: GPLv3
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Games

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz

BuildRequires: intltool
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(grilo-0.3)
BuildRequires: pkgconfig(libarchive)
BuildRequires: pkgconfig(librsvg-2.0)
BuildRequires: pkgconfig(libsoup-2.4)
BuildRequires: pkgconfig(libxml-2.0)
BuildRequires: pkgconfig(manette-0.2) >= 0.2.0
BuildRequires: pkgconfig(retro-gtk-0.14) >= 0.14.0
BuildRequires: pkgconfig(sqlite3)
BuildRequires: pkgconfig(tracker-sparql-2.0)
BuildRequires: vala-tools

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
%autoreconf
%configure --disable-static
%make_build

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/plugins/
%exclude %_libdir/%name/plugins/*.la
%_desktopdir/%xdg_name.desktop
%_iconsdir/HighContrast/*/apps/%{xdg_name}*
%_iconsdir/hicolor/*/apps/%{xdg_name}*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml

%files devel
%_includedir/lib%name.h
%_vapidir/%name.vapi


%changelog
* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0, no more virtual package

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0
