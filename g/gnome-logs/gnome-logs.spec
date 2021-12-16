%define _unpackaged_files_terminate_build 1
%define ver_major 3.36
%define xdg_name org.gnome.Logs

%def_with man
%def_enable tests

Name: gnome-logs
Version: %ver_major.0
Release: alt1.1

Summary: The GNOME logfile viewer
Group: Graphical desktop/GNOME
License: GPL-3.0
Url: https://wiki.gnome.org/Apps/Logs

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

#Obsoletes: gnome-system-log < 3.11
#Provides: gnome-system-log = %version-%release

Requires: gsettings-desktop-schemas

%define glib_ver 2.44
%define gtk_ver 3.22

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson libgio-devel >= %glib_ver libgtk+3-devel >= %gtk_ver
BuildRequires: gsettings-desktop-schemas-devel libsystemd-journal-devel
BuildRequires: libappstream-glib-devel yelp-tools desktop-file-utils
%{?_with_man:BuildRequires: docbook-dtds docbook-style-xsl xsltproc}

%description
GNOME Logs is a log viewer for the systemd journal.

%prep
%setup

%build
%meson %{?_with_man:-Dman=true}
%nil
%meson_build

%install
%meson_install

%find_lang --with-gnome %name

%check
%meson_test

%files -f %name.lang
%_bindir/%name
%_desktopdir/%xdg_name.desktop
%_datadir/%name/
%_datadir/dbus-1/services/%xdg_name.service
%_datadir/glib-2.0/schemas/%xdg_name.enums.xml
%_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_iconsdir/hicolor/*/*/%{xdg_name}*.svg
%_man1dir/%name.1.*
%_datadir/metainfo/%xdg_name.appdata.xml
%doc NEWS README

%changelog
* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1.1
- fixed meson options, updated BR

* Tue May 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.36.0-alt1
- 3.36.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Mon Apr 08 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.1-alt1
- 3.32.1

* Mon Mar 11 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Mon Sep 03 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Wed Jul 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.5-alt1
- 3.28.5

* Thu Jun 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.3-alt1
- 3.28.3

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.2-alt1
- 3.28.2

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Fri Feb 02 2018 Yuri N. Sedunov <aris@altlinux.org> 3.26.3-alt1
- 3.26.3

* Mon Oct 30 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.2-alt1
- 3.26.2

* Mon Sep 11 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Sat Jul 29 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.2-alt1
- 3.24.2

* Mon Apr 10 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.1-alt1
- 3.24.1

* Tue Mar 21 2017 Yuri N. Sedunov <aris@altlinux.org> 3.24.0-alt1
- 3.24.0

* Mon Oct 10 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.1-alt1
- 3.22.1

* Tue Sep 20 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 11 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Oct 12 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.1-alt1
- 3.18.1

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Mon May 11 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Nov 11 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.2-alt1
- 3.14.2

* Tue Oct 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.1-alt1
- 3.14.1

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Tue May 13 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Mon Apr 14 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Tue Feb 04 2014 Yuri N. Sedunov <aris@altlinux.org> 3.11.5-alt1
- first build for Sisyphus

