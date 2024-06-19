%define _name clicker
%define ver_major 0.1
%define rdn_name net.codelogistics.%_name

%def_enable check

Name: %_name
Version: %ver_major.7
Release: alt1

Summary: Simulate user input repeatedly
License: GPL-3.0-or-later
Group: Text tools
Url: https://codeberg.org/eyekay/clicker

BuildArch: noarch
Vcs: https://codeberg.org/eyekay/clicker.git
Source: %name-%version.tar

%add_python3_path %_datadir/%_name

%define glib_ver 2.54

Requires: typelib(Adw) = 1
Requires: typelib(GtkSource) = 5
Requires: typelib(Xdp) = 1.0
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson pkgconfig(gio-2.0) >= %glib_ver gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
Clicker is an auto clicker - it can simulate user input like mouse
clicks and key presses repeatedly at given intervals for a given
duration. This is useful in some video games or web applications.

%prep
%setup

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
%doc README.*

%changelog
* Wed Jun 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.1.7-alt1
- first build for Sisyphus
