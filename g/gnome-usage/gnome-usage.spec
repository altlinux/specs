%define _unpackaged_files_terminate_build 1

%define xdg_name org.gnome.Usage
%define ver_major 3.28

Name: gnome-usage
Version: %ver_major.0
Release: alt1

Summary: The GNOME system information viewer
License: GPLv3+
Group: Graphical desktop/GNOME
Url: https://wiki.gnome.org/Apps/Usage

Source: %gnome_ftp/%name/%ver_major/%name-%version.tar.xz

%define gtk_ver 3.20.10
%define gtop_ver 2.34.0
%define accountsservice_ver 0.6.40

Requires: accountsservice >= %accountsservice_ver

BuildRequires(pre): meson rpm-build-gnome
BuildRequires: yelp-tools libappstream-glib-devel
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libgtop-devel >= %gtop_ver
BuildRequires: vala-tools

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
%_iconsdir/hicolor/*/apps/%xdg_name.png
%config %_datadir/glib-2.0/schemas/%xdg_name.gschema.xml
%_datadir/metainfo/%xdg_name.appdata.xml
%doc README* NEWS

%changelog
* Mon Mar 12 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Sun Mar 04 2018 Yuri N. Sedunov <aris@altlinux.org> 3.27.92-alt1
- first build for Sisyphus


