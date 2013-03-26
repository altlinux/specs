%define _unpackaged_files_terminate_build 1

%define _name klotski
%define __name gnome-%_name
%define ver_major 3.8
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: Derivative game from Klotski
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release
Obsoletes: gnome-games-gnotski
Provides:  gnome-games-gnotski = %version-%release

%define glib_ver 2.32.0
%define gtk_ver 3.4.0

BuildRequires: gnome-common intltool yelp-tools
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: librsvg-devel vala-tools

%description
Gnome Klotski is a small game for GNOME. The idea is originally
from a game called "Klotski".

%prep
%setup -n %__name-%version

%build
%autoreconf
%configure --disable-schemas-compile
%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%attr(2711,root,games) %_bindir/%__name
%_desktopdir/gnotski.desktop
%_datadir/%__name/
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/scalable/apps/%__name.svg
%_iconsdir/HighContrast/*x*/apps/%__name.png
%_man6dir/%__name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
#%config(noreplace) %attr(0664,games,games) %_localstatedir/games/%__name.*


%changelog
* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



