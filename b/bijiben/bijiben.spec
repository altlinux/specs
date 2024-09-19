%def_enable snapshot

%define _name gnome-notes
%define ver_major 41
%define beta .alpha
%define xdg_name org.gnome.Notes
%define _libexecdir %_prefix/libexec

Name: bijiben
Version: %ver_major
Release: alt0.3%beta

Summary: GNOME Notes
License: GPL-3.0
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Notes
Vcs: https://gitlab.gnome.org/GNOME/gnome-notes.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %_name-%version%beta.tar
%endif

Provides: %_name = %EVR
# to avoid conflict between webki2gtk{4.1,6.0}-debuginfo
%add_debuginfo_skiplist %_bindir/* %_libexecdir/*

%define glib_ver 2.68
%define gtk_ver 4.8
%define adw_ver 1.2
%define tracker_api_ver 3.0
%define tracker_ver 3.0
%define eds_ver 3.45.1
%define webkit_api_ver 6.0
%define webkit_ver 2.40

Requires: dconf tinysparql localsearch

BuildRequires(pre): rpm-macros-meson rpm-build-xdg
BuildRequires: meson yelp-tools
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: pkgconfig(tracker-sparql-%tracker_api_ver) >= %tracker_ver
BuildRequires: libxml2-devel pkgconfig(webkitgtk-%webkit_api_ver) >= %webkit_ver
BuildRequires: libgnome-online-accounts-devel libuuid-devel
BuildRequires: evolution-data-server-devel >= %eds_ver libcurl-devel
BuildRequires: libical-devel libicu-devel libjson-glib-devel

%description
GNOME Notes (Bijiben) is a simple application for creating, editing and
viewing notes.

%prep
%setup -n %_name-%version%beta

%build
%meson \
    -Dupdate_mimedb=false
# SMP-incompatible build
%meson_build -j 1

%install
%meson_install
%find_lang --with-gnome %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_libexecdir/%name-shell-search-provider
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_datadir/gnome-shell/search-providers/%xdg_name-search-provider.ini
%_datadir/dbus-1/services/%xdg_name.SearchProvider.service
%_xdgmimedir/packages/%xdg_name.xml
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* AUTHORS NEWS

%changelog
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.3.alpha
- updated to BIJIBEN_40_0-483-gd7c4b9c
- built against gnome-47 libraries

* Wed Mar 06 2024 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.2.alpha
- updated to BIJIBEN_40_0-472-g1e8cc33
- provides gnome-notes

* Thu Sep 08 2022 Yuri N. Sedunov <aris@altlinux.org> 41-alt0.1.alpha
- 41.alpha (BIJIBEN_40_0-243-ge700e1a)

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1.1
- fixed build with meson >= 0.61

* Fri Apr 30 2021 Yuri N. Sedunov <aris@altlinux.org> 40.1-alt1
- 40.1

* Thu Mar 18 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Mon Sep 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Fri Aug 21 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.3-alt1
- 3.36.3

* Wed Jul 08 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Mon Apr 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.1-alt1
- 3.36.1

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Mon Oct 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Jul 19 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.2-alt1
- 3.32.2

* Wed Apr 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Nov 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.3-alt1
- 3.30.3

* Sun Oct 21 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Jun 20 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Thu Jun 07 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt2
- fixed build options

* Thu May 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Tue Apr 10 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Mon Mar 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Thu Jan 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt2
- rebuilt against libical.so.3/libicu*.so.60

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Tue Aug 15 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Fri Jun 16 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- updated to 3_24_0-9-g5ce5172

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.21.2-alt1
- 3.21.2

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Fri Jan 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt2
- rebuilt against libical.so.2

* Mon Nov 09 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Sun Sep 20 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Tue May 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Sat Mar 28 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- 3.15.91

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 12 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Mon Aug 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.4-alt1
- 3.8.4

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Sat May 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Thu Apr 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Wed Mar 27 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Mon Mar 18 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.92-alt1
- first build for people/gnome

