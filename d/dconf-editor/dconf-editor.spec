%def_disable snapshot

%define _unpackaged_files_terminate_build 1
%define ver_major 45
%define beta %nil
%define xdg_name ca.desrt.dconf-editor

Name: dconf-editor
Version: %ver_major.0
Release: alt1%beta

Summary: dconf confuguration editor
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://wiki.gnome.org/Projects/dconf

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version%beta.tar.xz
%else
Source: %name-%version.tar
%endif
#https://l10n.gnome.org/media/upload/dconf-editor-master-po-ru-812899_sj2ZdlN.merged.po
Source1: %name-3.38.3.ru.po.finziyr

%define glib_ver 2.56
%define dconf_ver 0.26.1
%define gtk_ver 3.22.27
%define handy_ver 1.6
%define vala_ver 0.40


Requires: dconf >= %dconf_ver

BuildRequires(pre): rpm-macros-meson gnome-common
BuildRequires: meson vala-tools >= %vala_ver
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libdconf-devel >= %dconf_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: libxml2-devel rpm-build-gnome
BuildRequires: libappstream-glib-devel yelp-tools
BuildRequires: libdconf-vala

%description
dconf is a low-level configuration system. Its main purpose is to
provide a backend to GSettings API in Glib for storing and retrieving
application settings.

This package provides graphical dconf configuration editor.


%prep
%setup -n %name-%version%beta
cp %SOURCE1 po/ru.po

%build
%meson
%meson_build

%install
%meson_install

%find_lang --with-gnome --output=%name.lang %name dconf

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%xdg_name.desktop
%_datadir/dbus-1/services/%xdg_name.service
%_iconsdir/hicolor/*/*/*.*
%_man1dir/%name.1.*
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
# "nosort" bad option?
%_datadir/bash-completion/completions/%name
%doc README*

%changelog
* Mon Sep 18 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0

* Wed Sep 21 2022 Yuri N. Sedunov <aris@altlinux.org> 43.0-alt1
- 43.0

* Sun Mar 27 2022 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt2
- updated to 3.38.2-34-g41691c16 from master branch
  (fixed build with meson >= 0.61)

* Fri Oct 15 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1.1
- updated russian translation

* Tue Mar 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.3-alt1
- 3.38.3

* Mon Mar 01 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt2
- updated to 3.38.2-9-g49d445f9 (fixed build with vala-0.50.4)

* Sun Nov 22 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.2-alt1
- 3.38.2

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Mon Jul 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.4-alt1
- 3.36.4

* Sat Apr 25 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.2-alt1
- 3.36.2

* Tue Mar 10 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Fri Feb 14 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.4-alt1
- 3.34.4

* Mon Jan 06 2020 Yuri N. Sedunov <aris@altlinux.org> 3.34.3-alt1
- 3.34.3

* Tue Oct 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.2-alt1
- 3.34.2

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.1-alt1
- 3.34.1

* Tue Mar 12 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.2-alt1
- 3.30.2

* Tue Sep 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Mar 13 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Tue Oct 31 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Oct 02 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Sat Jan 14 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.3-alt1
- 3.22.3

* Tue Oct 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Thu Jun 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.3-alt1
- 3.20.3

* Tue May 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.2-alt1
- 3.20.2

* Thu Apr 14 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Thu Nov 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon Apr 13 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Mon Mar 02 2015 Yuri N. Sedunov <aris@altlinux.org> 3.15.91-alt1
- first build for people/gnome

