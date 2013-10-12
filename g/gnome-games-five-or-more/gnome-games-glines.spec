%define _unpackaged_files_terminate_build 1

%define _name five-or-more
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: A GNOME version of the color lines program
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
Patch: gnome-games-glines-3.8.0-segfault.patch

Provides:  %_name = %version-%release
Obsoletes: gnome-games-glines
Provides:  gnome-games-glines = %version-%release

%define glib_ver 2.31.13
%define gtk_ver 3.0.0

BuildRequires: gnome-common
BuildRequires: intltool yelp-tools libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel

%description
Glines, is the GNOME port of the once popular Windows game called Color
Lines. The game's objective is to align as often as possible five balls
or more of the same color causing them to disappear, play as long as
possible, and be #1 in the High Scores.


%prep
%setup -n %_name-%version
%patch -p1

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %_name

%files -f %_name.lang
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/glines.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*x*/apps/%_name.png
%_iconsdir/hicolor/scalable/apps/%_name.svg
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/glines*
%_datadir/appdata/%_name.appdata.xml

%changelog
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



