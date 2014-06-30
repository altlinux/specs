%define _unpackaged_files_terminate_build 1

%define _name sudoku
%define __name gnome-%_name
%define ver_major 3.12
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.3
Release: alt1

Summary: GNOME Sudoku game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release

# use python3
AutoReqProv: nopython
%define __python %nil

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools libgio-devel 
BuildRequires: python3 rpm-build-python3 python3-module-pygobject3-devel

%description
Sudoku is a logic game with a Japanese name that has recently exploded
in popularity.

%prep
%setup -n %__name-%version
# fix DOMAIN
subst 's/gnome-games/%__name/' src/lib/defaults.py

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f %__name.lang
%_bindir/%__name
%_desktopdir/%__name.desktop
%_datadir/%__name/
%python3_sitelibdir_noarch/gnome_sudoku/
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name.svg
%_iconsdir/HighContrast/*x*/apps/%__name.png
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%__name.gschema.xml
%_datadir/appdata/%__name.appdata.xml

%changelog
* Mon Jun 30 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.3-alt1
- 3.12.3

* Mon May 12 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Sun Mar 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Tue Apr 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- no more sgid on /usr/bin/gnome-sudoku (ALT# 28820)

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



