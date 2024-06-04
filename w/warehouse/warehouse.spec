%define _name warehouse
%define ver_major 1.6
%define rdn_name io.github.flattool.Warehouse

# online screenshots
%def_disable check

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: Flatpak manager for GNOME
License: GPL-3.0-or-later
Group: System/Configuration/Packaging
Url: https://github.com/flattool/warehouse

BuildArch: noarch

Vcs: https://github.com/flattool/warehouse.git
Source: %name-%version.tar

%add_python3_path %_datadir/%_name

Requires: dconf flatpak-spawn
Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler typelib(Adw)
BuildRequires: /usr/bin/glib-compile-resources
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli /usr/bin/glib-compile-schemas}

%description
Warehouse is an app that manages installed Flatpaks, their user data,
and Flatpak remotes.

%prep
%setup
# with appstream-util "Validate appstream file" failed
sed -i "s/\('appstream\)-util'/\1cli'/" data/meson.build

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%check
%__meson_test

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/glib-2.0/schemas/%rdn_name.gschema.xml
%_datadir/metainfo/%rdn_name.metainfo.xml
%doc README*

%changelog
* Tue Jun 04 2024 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- first build for Sisyphus



