%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define xdg_name org.gnome.Photos
%define ver_major 44
%define _libexecdir %_prefix/libexec
%define gegl_api_ver 0.4
%define tracker_api_ver 3.0

%def_disable check

Name: gnome-photos
Version: %ver_major.0
Release: alt1

Summary: Photos - access, organize and share your photos on GNOME
License: GPL-2.0-or-later
Group: Graphics
Url: https://wiki.gnome.org/Apps/Photos

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.58
%define gtk_ver 3.22.16
%define tracker_ver 3.0
%define gdata_ver 0.15.2
%define gegl_ver 0.4.2
%define png_ver 1.6
%define dazzle_ver 3.28
%define gexiv2_ver 0.14.0
%define handy_ver 1.1.90

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson yelp-tools %_bindir/appstream-util desktop-file-utils
BuildRequires: libgio-devel >= %glib_ver gsettings-desktop-schemas-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(tracker-sparql-%tracker_api_ver) >= %tracker_ver
BuildRequires: libgdata-devel >= %gdata_ver
BuildRequires: libgegl-devel >= %gegl_ver
BuildRequires: libpng-devel >= %png_ver
BuildRequires: libgexiv2-devel >= %gexiv2_ver
BuildRequires: libexempi-devel liblcms2-devel librsvg-devel
BuildRequires: libjpeg-devel
BuildRequires: libgnome-desktop3-devel libgnome-online-accounts-devel zlib-devel
BuildRequires: libgeocode-glib2.0-devel
BuildRequires: gobject-introspection-devel libgtk+3-gir-devel
BuildRequires: libdazzle-devel > %dazzle_ver
BuildRequires: libdbus-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: pkgconfig(libportal)
BuildRequires: pkgconfig(libportal-gtk3)
%{?_enable_check:BuildRequires: dbus dogtail}

%description
Photos, like Documents, Music and Videos, is one of the core GNOME
applications meant for find and reminding the user about her content.
The internal architecture Photos is based on Documents -- the document
manager application for GNOME, because they share similar UI/UX
patterns and objectives.

%prep
%setup

%build
%meson -Dbuildtype=plain
%meson_build

%install
%meson_install
rm -rf %buildroot/%_datadir/doc/%name
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%dir %_libdir/%name
%_libdir/%name/*.so
%_libexecdir/gnome-photos-thumbnailer
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.appdata.xml
%_datadir/gnome-shell/search-providers/%xdg_name.search-provider.ini
%_datadir/dbus-1/services/%xdg_name.service
%config %_datadir/glib-2.0/schemas/org.gnome.photos.gschema.xml
%doc ARTISTS AUTHORS NEWS README

%changelog
* Tue Mar 07 2023 Yuri N. Sedunov <aris@altlinux.org> 44.0-alt1
- 44.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- 42.0

* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1.1
- fixed meson options

* Thu Mar 25 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Tue Feb 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Wed Sep 23 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri May 29 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Wed Feb 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Wed Sep 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Tue Aug 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 18 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Fri Feb 22 2019 Yuri N. Sedunov <aris@altlinux.org> 3.31.91-alt1
- 3.31.91

* Thu Sep 27 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Thu Sep 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.29.92-alt1
- 3.29.92

* Thu Mar 15 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Mar 06 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- 3.27.92

* Wed Dec 20 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Fri Nov 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Tue Oct 03 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Aug 26 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.3-alt1
- 3.24.3

* Tue Jul 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt2
- updated to 3.24.2-4-g9d70654

* Wed May 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Apr 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Tue Mar 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.5-alt1
- 3.22.5

* Thu Feb 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.4-alt1
- 3.22.4

* Fri Jan 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Sat Nov 05 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.2-alt1
- 3.22.2

* Thu Oct 06 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Sat Sep 17 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Tue Aug 09 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Tue Jun 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Wed Apr 13 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Mon Mar 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Tue Mar 15 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.3-alt1
- 3.18.3 (CVE-2013-7447)

* Sun Nov 08 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Sep 07 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt3
- rebuilt against libgrilo-0.2.so.10

* Sun Aug 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt2
- rebuilt against libgdata.so.22

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Nov 10 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Wed Sep 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Mar 17 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.92-alt1
- 3.11.92

* Wed Nov 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.3-alt1
- first build for people/gnome

