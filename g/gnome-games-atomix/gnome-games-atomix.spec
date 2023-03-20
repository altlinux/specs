%def_disable snapshot
%define _unpackaged_files_terminate_build 1

%define _name atomix
%define xdg_name org.gnome.Atomix
%define ver_major 44
%define beta %nil
%define _libexecdir %_prefix/libexec

Name: gnome-games-%_name
Version: %ver_major.0
Release: alt1%beta

Summary: Build molecules out of single atoms
Group: Games/Boards
License: GPLv2+
Url: https://wiki.gnome.org/Apps/Atomix

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif

Provides:  %_name = %version-%release

%define glib_ver 2.36.0
%define gtk_ver 3.22.0

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson yelp-tools /usr/bin/appstream-util desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libxml2-devel libgnome-games-support-devel

%description
Atomix is a puzzle game in which you have to build full molecules, from simple
inorganic ones in the first levels to extremely complex organic ones in the
last levels, out of isolated atoms, which are laying around among walls and
other obstacles on the playfield.

%prep
%setup -n %_name-%version%beta

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome %_name

%files -f %_name.lang
%_bindir/%_name
%_desktopdir/%_name.desktop
%_datadir/%_name/
%_iconsdir/hicolor/*/*/%{_name}*.*
%_datadir/metainfo/%_name.appdata.xml
%doc AUTHORS NEWS README*


%changelog
* Sat Mar 18 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Thu Dec 03 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- updated to 3.34.0-11-gbfe0acc (fixed build with gcc10/-fno-common)

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0.1-alt1
- 3.30.0.1

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




