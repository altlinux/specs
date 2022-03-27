%def_enable snapshot

%define _unpackaged_files_terminate_build 1
%define ver_major 41
%define beta %nil
%define xdg_name org.gnome.Screenshot

Name: gnome-screenshot
Version: %ver_major.0
Release: alt2%beta

Summary: The GNOME Screenshot Tool
Group: Graphical desktop/GNOME
License: GPLv2+
Url: https://gitlab.gnome.org/GNOME/gnome-screenshot

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version%beta.tar
%endif

%define glib_ver 2.36
%define gtk_ver 3.12
%define handy_ver 1.5.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver libcanberra-gtk3-devel
BuildRequires: libX11-devel libXext-devel
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: %_bindir/appstream-util

%description
GNOME Screenshot Tool makes screenshots from desktop.

%prep
%setup -n %name-%version%beta

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/org.gnome.%name.gschema.xml
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_datadir/metainfo/%xdg_name.metainfo.xml
%_man1dir/%name.1.*
%doc NEWS README*

%changelog
* Mon Mar 28 2022 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt2
- updated to 41.0-25-g45f08f0 (fixed build with meson >= 0.61)

* Sun Nov 14 2021 Yuri N. Sedunov <aris@altlinux.org> 41.0-alt1
- 41.0

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 40.0-alt1
- 40.0

* Thu Sep 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Mon Oct 14 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Fri Mar 15 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Jun 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Sat Jun 18 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Wed Sep 23 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Wed May 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Nov 19 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Tue Sep 24 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Wed Jul 10 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Tue May 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Tue Nov 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0-alt1
- 3.6.0

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Mar 19 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.92-alt1
- 3.3.92

* Mon Feb 06 2012 Yuri N. Sedunov <aris@altlinux.org> 3.3.2-alt1
- first build for Sisyphus

