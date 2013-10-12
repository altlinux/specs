%define _unpackaged_files_terminate_build 1

%define _name four-in-a-row
%define ver_major 3.10
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt1

Summary: Four in a row game
Group: Games/Boards
License: GPLv3+
Url: http://live.gnome.org/GnomeGames/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release
Obsoletes: gnome-games-gnect
Provides:  gnome-games-gnect = %version-%release

%define glib_ver 2.31.13
%define gtk_ver 3.0.0

BuildRequires: gnome-common
BuildRequires: intltool yelp-tools libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver librsvg-devel
BuildRequires: libcanberra-gtk3-devel zlib-devel

%description
Gnect is a four-in-a-row game for the GNOME Project. The object of the
game is to build a line of four of your marbles while trying to stop
your opponent (human or computer) building a line of his or her own. A
line can be horizontal, vertical or diagonal.

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
%_desktopdir/gnect.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*x*/apps/%_name.png
%_iconsdir/hicolor/scalable/apps/%_name.svg
%_iconsdir/HighContrast/*x*/apps/%_name.png
%_man6dir/%_name.*
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/%_name.appdata.xml

%changelog
* Sat Oct 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Dec 25 2012 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- first build for people/gnome



