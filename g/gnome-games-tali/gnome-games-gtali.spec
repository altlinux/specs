%define _unpackaged_files_terminate_build 1

%define _name tali
%define ver_major 3.8
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: Gnome version of Yahtzee Dice Game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release
Obsoletes: gnome-games-gtali
Provides:  gnome-games-gtali = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools 
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel

%description
Gnome Tali is a sort of poker with dice and less money. You roll five
dice three times and try to create the best hand. Your two rerolls may
include any or all of your dice.

%prep
%setup -n %_name-%version

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

%find_lang --with-gnome --output=%_name.lang %_name gtali

%files -f %_name.lang
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/gtali.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*x*/apps/%_name.png
%_iconsdir/hicolor/scalable/apps/%_name.svg
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gtali.*

%changelog
* Mon Sep 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



