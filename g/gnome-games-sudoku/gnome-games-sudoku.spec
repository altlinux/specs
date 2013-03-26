%define _unpackaged_files_terminate_build 1

%define _name sudoku
%define __name gnome-%_name
%define ver_major 3.8
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: GNOME Sudoku game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools python-module-pygobject3-devel libgio-devel

%description
Sudoku is a logic game with a Japanese name that has recently exploded
in popularity.

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
%attr(-,root,games) %_bindir/%__name
%_desktopdir/%__name.desktop
%_datadir/%__name/
%python_sitelibdir_noarch/gnome_sudoku/
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name.svg
%_iconsdir/HighContrast/*x*/apps/%__name.png
%_iconsdir/HighContrast/scalable/apps/%__name.svg
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%__name.gschema.xml

%changelog
* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



