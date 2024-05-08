%def_enable snapshot

%define ver_major 2024.5
%define rdn_name io.github.giantpinkrobots.varia

%def_enable check

Name: varia
Version: %ver_major.7
Release: alt1

Summary: Download manager based on aria2
License: MPL-2.0
Group: Networking/WWW
Url: https://github.com/giantpinkrobots/varia

%if_disabled snapshot
Source: %url/-/archive/v%version/%name-%version.tar.gz
%else
Vcs: https://github.com/giantpinkrobots/varia.git
Source: %name-%version.tar
%endif

%define adw_ver 1.4

Requires: /usr/bin/aria2p /usr/bin/aria2c
Requires: typelib(Adw) = 1 libadwaita >= %adw_ver
Requires: dconf yelp

BuildArch: noarch

%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson yelp-tools
BuildRequires: pkgconfig(libadwaita-1)
%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Varia is a simple download manager that conforms to the latest
Libadwaita design guidelines, integrating nicely with GNOME.
It uses the amazing aria2 to handle the downloads.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang --with-gnome --output=%name.lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_bindir/%name-py.py
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_iconsdir/hicolor/*/apps/%{rdn_name}*.svg
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Wed May 08 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.5.7-alt1
- 2024.5.7

* Wed Mar 20 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.3.20-alt1
- 2024.3.20

* Tue Mar 05 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.2.29.2-alt1
- 2024.2.29-2

* Wed Feb 14 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.2.6-alt1
- first build for Sisyphus (v2024.2.6-5-g6fb6073)


