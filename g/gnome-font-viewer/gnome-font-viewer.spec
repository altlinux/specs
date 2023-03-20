%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define ver_major 44
%define beta %nil
%define xdg_name org.gnome.font-viewer

Name: gnome-font-viewer
Version: %ver_major.0
Release: alt1%beta

Summary: The GNOME Font Viewer
Group: Graphical desktop/GNOME
License: GPL-2.0-or-later
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.56.0
%define gtk4_ver 4.5
%define adwaita_ver 1.2

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson /usr/bin/appstream-util
BuildRequires: libgio-devel >= %glib_ver libgtk4-devel >= %gtk4_ver
BuildRequires: fontconfig-devel libfreetype-devel
BuildRequires: libharfbuzz-devel libfribidi-devel
BuildRequires: pkgconfig(gnome-desktop-4)
BuildRequires: pkgconfig(libadwaita-1) >= %adwaita_ver

%description
GNOME Font Viewer is a simple application to preview fonts.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gnome-thumbnail-font
%_desktopdir/%xdg_name.desktop
%_datadir/thumbnailers/%name.thumbnailer
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS

%changelog
* Sun Mar 19 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Mon Mar 21 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Tue Mar 08 2022 Yuri N. Sedunov <aris@altlinux.org> 42-alt0.9.rc
- 42.rc (ported to GTK4)

* Tue Sep 21 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sun Mar 21 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Wed Mar 11 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt2
- rebuilt against libgnome-desktop-so.19

* Sat Sep 21 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Mar 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Aug 30 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Sep 19 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Thu Aug 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.90-alt1
- 3.25.90

* Thu Jul 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt2
- updated to 3.24.0-11-gea583a0 (fixed BGO ##=783611, 783613, 782738)

* Sat Apr 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Thu Mar 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.23.91-alt1
- 3.23.91

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu May 12 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 29 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Aug 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt2
- rebuilt against libgnome-desktop-3.so.12

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Wed Feb 18 2015 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Wed Mar 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Thu Dec 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.2-alt1
- 3.6.2

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

