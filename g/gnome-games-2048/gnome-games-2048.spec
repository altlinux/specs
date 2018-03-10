%define _unpackaged_files_terminate_build 1

%define _name 2048
%define __name gnome-%_name
%define ver_major 3.26
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.1
Release: alt2

Summary: A 2048 clone for GNOME
Group: Games/Boards
License: GPLv3+
Url: https://wiki.gnome.org/Apps/2048

Source: ftp://ftp.gnome.org/pub/gnome/sources/%__name/%ver_major/%__name-%version.tar.xz

Provides:  %__name = %version-%release

%define gtk_ver 3.12.0
%define clutter_gtk_ver 1.6
%define gee_ver 0.14
%define libgames_ver 1.2.0
%define vala_ver 0.24

BuildRequires: intltool yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver libclutter-gtk3-devel >= %clutter_gtk_ver
BuildRequires: libgee0.8-devel >= %gee_ver libgnome-games-support-devel >= %libgames_ver
BuildRequires: vala-tools >= %vala_ver

%description
Move the tiles until you obtain the 2048 tile.

%prep
%setup -n %__name-%version
[ ! -d m4 ] && mkdir m4

%build
%autoreconf
%configure \
    --disable-schemas-compile

%make_build

%install
%makeinstall_std

%find_lang --with-gnome %__name

%files -f gnome-%_name.lang
%_bindir/%__name
%_desktopdir/org.gnome.%__name.desktop
%_iconsdir/hicolor/*x*/apps/%__name.png
%_iconsdir/hicolor/symbolic/apps/%{__name}*.svg
%config %_datadir/glib-2.0/schemas/org.gnome.%_name.gschema.xml
%_datadir/appdata/org.gnome.%__name.appdata.xml

%changelog
* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt2
- rebuilt against libgnome-games-support-1.so.3

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon May 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- first build for Sisyphus
