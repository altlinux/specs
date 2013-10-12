%define _unpackaged_files_terminate_build 1

%define _name nibbles
%define __name gnome-%_name
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: A cute little game that has no short description
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Nibbles

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release
Obsoletes: gnome-games-gnibbles
Provides:  gnome-games-gnibbles = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0
%define clutter_ver 1.14.4

BuildRequires: gnome-common
BuildRequires: intltool yelp-tools libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libcanberra-gtk3-devel libclutter-devel >= %clutter_ver libclutter-gtk3-devel

%description
Gnibbles is a game where the user controls a snake. The snake moves
around the board, eating diamonds while avoiding the walls placed around
it.


%prep
%setup -n %__name-%version

%build
%autoreconf
%configure \
    --disable-schemas-compile \
    --enable-setgid \
    --with-scores-group=games \
    --with-scores-user=games

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%attr(2711,root,games) %_bindir/%__name
%_desktopdir/gnibbles.desktop
%_datadir/%__name
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name.svg
%_iconsdir/HighContrast/*x*/apps/%__name.png
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/%__name.*
%_datadir/appdata/%__name.appdata.xml

%changelog
* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



