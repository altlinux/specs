%def_enable snapshot
%define _unpackaged_files_terminate_build 1

%define xdg_name org.gnome.Usage
%define ver_major 46

Name: gnome-usage
Version: %ver_major.0
Release: alt2

Summary: The GNOME system information viewer
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Usage

%if_disabled snapshot
Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define gtk_ver 4.14
%define gtop_ver 2.34.0
%define accountsservice_ver 0.6.40
%define adw_ver 1.5

Requires: accountsservice >= %accountsservice_ver

BuildRequires(pre): rpm-macros-meson rpm-build-gnome
BuildRequires: meson vala-tools yelp-tools
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: libgtop-devel >= %gtop_ver
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(tracker-sparql-3.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Gnome Usage is a graphical tool to view system resources, like memory and
disk space.

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
%_desktopdir/%xdg_name.desktop
%_iconsdir/hicolor/*/apps/%{xdg_name}*.svg
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.metainfo.xml
%doc README* NEWS

%changelog
* Tue Sep 17 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt2
- updated to 46.0-41-g83f58b0

* Wed Mar 20 2024 Yuri N. Sedunov <aris@altlinux.org> 46.0-alt1
- 46.0

* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 45.0-alt1
- 45.0 (ported to GTK4/Libadwaita)

* Fri Mar 19 2021 Yuri N. Sedunov <aris@altlinux.org> 3.38.1-alt1
- 3.38.1

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Wed Mar 20 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Tue Sep 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- first build for Sisyphus


