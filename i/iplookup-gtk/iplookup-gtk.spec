%define _name iplookup
%define __name %{_name}-gtk
%define ver_major 0.3.4
%define rdn_name io.github.bytezz.IPLookup

# online screenshots
%def_disable check

Name: %__name
Version: %ver_major
Release: alt1

Summary: An IP address information search utility for the GNOME Desktop
License: GPL-3.0-or-later
Group: Networking/WWW
Url: https://github.com/bytezz/iplookup-gtk

BuildArch: noarch

Vcs: https://github.com/Bytezz/IPLookup-gtk.git
Source0: %__name-%version.tar

%add_python3_path %_datadir/%_name

Requires: typelib(Adw) = 1 dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli}

%description
Look up details such as the internet provider and geographic location for an IP address.

%prep
%setup

# with appstream-util "Validate appstream file" failed
sed -i "s/\('appstream\)-util'/\1cli'/" data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%_name
%_datadir/%_name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/appdata/%rdn_name.appdata.xml
%doc README.*

%changelog
* Sat May 25 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sat Apr 13 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt2
- prepared for Sisyphus

* Sat Apr 13 2024 Semen Fomchenkov <armatik@altlinux.org> 0.3.3-alt1
- Init build for Sisyphus
