%define _unpackaged_files_terminate_build 1

%define _name atomix
%define ver_major 3.22
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1

Summary: Build molecules out of single atoms
Group: Games/Boards
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Atomix

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz

Provides:  %_name = %version-%release

%define glib_ver 2.36.0
%define gtk_ver 3.14.0

BuildRequires: gnome-common intltool yelp-tools libappstream-glib-devel
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libxml2-devel

%description
Atomix is a puzzle game in which you have to build full molecules, from simple
inorganic ones in the first levels to extremely complex organic ones in the
last levels, out of isolated atoms, which are laying around among walls and
other obstacles on the playfield.

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
%_bindir/%_name
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*x*/apps/%_name.png
%_iconsdir/hicolor/symbolic/apps/%_name-symbolic.svg
%_datadir/appdata/%_name.appdata.xml
%doc AUTHORS NEWS README


%changelog
* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Jan 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.4-alt1
- first build for people/gnome




