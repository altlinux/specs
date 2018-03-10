%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define ver_major 3.28
%define _name org.gnome.font-viewer

Name: gnome-font-viewer
Version: %ver_major.0
Release: alt1

Summary: The GNOME Font Viewer
Group: Graphical desktop/GNOME
License: GPLv2+
Url: http://www.gnome.org

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.38.0
%define gtk_ver 3.12.0

BuildRequires(Pre): meson rpm-build-gnome
BuildPreReq: libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: libfreetype-devel libharfbuzz-devel libgnome-desktop3-devel

%description
GNOME Font Viewer is a simple application to preview fonts.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%files -f %name.lang
%_bindir/%name
%_bindir/gnome-thumbnail-font
%_datadir/applications/%_name.desktop
%_datadir/thumbnailers/%name.thumbnailer
%_datadir/dbus-1/services/%_name.service
%_datadir/metainfo/%_name.appdata.xml
%doc NEWS

%changelog
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

