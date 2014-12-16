%define _unpackaged_files_terminate_build 1

%define _name hitori
%define ver_major 3.14
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.2.1
Release: alt1

Summary: GTK+ application to generate and let you play games of Hitori
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/Hitori

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.14.0
%define cairo_ver 1.4

BuildRequires: gnome-common intltool yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libcairo-devel >= %cairo_ver

%description
Hitori is a small logic puzzle in a similar vein to the more
popular Sudoku. In the game, the player starts with a square
board of numbers, and has to paint out cells until there are no
duplicate numbers in each row and column.

The following rules apply:
- There must only be one of each number in the unpainted cells in each
  row and column.
- No painted cell may be adjacent to another, vertically or horizontally.
- All the unpainted cells must be joined together vertically and
  horizontally in one group.

These are the only three rules of the game, and so there may well be
multiple solutions to a Hitori puzzle board.

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
%attr(2711,root,games) %_bindir/%_name
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*x*/apps/%_name.png
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/%_name.appdata.xml

%changelog
* Tue Dec 16 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2.1-alt1
- 3.14.2.1

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- first build for Sisyphus


