%define _unpackaged_files_terminate_build 1

%define _name tetravex
%define __name gnome-%_name
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: A game based on Tetravex
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %_name = %version-%release
Obsoletes: gnome-games-gnotravex
Provides:  gnome-games-gnotravex = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel

%description
GNOME Tetravex is a simple puzzle where pieces must be positioned so
that the same numbers are touching each other. Your game is timed, these
times are stored in a system-wide scoreboard.

%prep
%setup -n %__name-%version

%build
%autoreconf
%configure  --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%__name.desktop
%_datadir/%__name/
%_iconsdir/hicolor/*x*/apps/*.png
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/HighContrast/*x*/apps/*.png
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/%__name.appdata.xml


%changelog
* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- no more sgid on /usr/bin/gnome-tetrevex (ALT #28820)

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



