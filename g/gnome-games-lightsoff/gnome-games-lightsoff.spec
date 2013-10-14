%define _unpackaged_files_terminate_build 1

%define _name lightsoff
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: Lights Off is a puzzle game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libclutter-gtk3-devel

%description
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked tile
and its non-diagonal neighbors.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name

%files -f %_name.lang
%attr(-,root,games) %_bindir/%_name
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/scalable/apps/%_name.svg
%_iconsdir/HighContrast/*x*/apps/%_name.png
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/%_name.appdata.xml

%changelog
* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



