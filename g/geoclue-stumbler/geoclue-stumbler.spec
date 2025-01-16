%def_enable snapshot

%define _name geoclue-stumbler
%define ver_major 1.1
%define rdn_name org.kop316.stumbler

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: Geoclue Stumbler
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://gitlab.com/kop316/geoclue-stumbler

Vcs: https://gitlab.com/kop316/geoclue-stumbler.git

%if_disabled snapshot
Source: %url/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define geoclue_ver 2.7.2-alt2
%define adw_ver 1.6

Requires: geoclue2 >= %geoclue_ver dconf

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: pkgconfig(libadwaita-1) >= %adw_ver
BuildRequires: pkgconfig(libgeoclue-2.0)
BuildRequires: pkgconfig(shumate-1.0)
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils}

%description
Geoclue has the ability (assuming the hardware is supported) to collect
Cell tower and WiFi Access Point (AP) location data and submit the data
to an Ichnaea (https://ichnaea.readthedocs.io/en/latest/api/geosubmit2.html)
compatible server (e.g. beaconDB (https://beacondb.net/)). However,
geoclue only collects/submits data if and only if a client is actively
connected to geoclue.

Geoclue Stumbler is geoclue client in GTK4/Libadwaita. While running, it ensures
geoclue is active to submit cell tower/WiFi Access point data, provides the user
feedback on if geoclue can submit data.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%_bindir/%_name
%_bindir/%_name-http
%_desktopdir/%rdn_name.desktop
%_datadir/dbus-1/services/%rdn_name.service
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Fri Jan 17 2025 Yuri N. Sedunov <aris@altlinux.org> 1.1-alt1
- first build for Sisyphus (1.1-1-gd5dd771)


