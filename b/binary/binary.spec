%define _name binary
%define ver_major 4.0
%define rdn_name io.github.fizzyizzy05.%_name

%def_enable check

Name: %_name
Version: %ver_major
Release: alt1

Summary: Convert numbers between bases
License: GPL-3.0-or-later
Group: Sciences/Mathematics
Url: https://github.com/fizzyizzy05/binary

Vcs: https://github.com/fizzyizzy05/binary.git

BuildArch: noarch

Source: %name-%version.tar

%add_python3_path %_datadir/%_name

Requires: typelib(Adw) = 1
Requires: dconf

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson blueprint-compiler /usr/bin/glib-compile-resources
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
A small and simple graphical app used to convert between different
hexadecimal and binary numbers.

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
* Mon Aug 05 2024 Yuri N. Sedunov <aris@altlinux.org> 4.0-alt1
- first build for Sisyphus (4.0-5-g7d12c18)
