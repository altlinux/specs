%define _name ascii-draw
%define ver_major 0.4
%define rdn_name io.github.nokse22.asciidraw

# online screenshots
%def_disable check

Name: %_name
Version: %ver_major.0
Release: alt1

Summary: A character drawing utility for the GNOME Desktop
License: GPL-3.0-or-later
Group: Graphics
Url: https://github.com/Nokse22/ascii-draw

BuildArch: noarch
Vcs: https://github.com/Nokse22/ascii-draw.git
Source0: %name-%version.tar

%add_python3_path %_datadir/%_name

Requires: typelib(Adw) = 1

BuildRequires(pre): rpm-macros-meson rpm-build-python3 rpm-build-gir
BuildRequires: meson gtk4-update-icon-cache
%{?_enable_check:BuildRequires: /usr/bin/desktop-file-validate /usr/bin/appstreamcli
BuildRequires: /usr/bin/glib-compile-schemas}

%description
This app lets you draw diagrams, tables, tree view, art and more using only characters.
There are many stiles to choose from and multiple tools available to use.

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
* Tue Jul 09 2024 Yuri N. Sedunov <aris@altlinux.org> 0.4.0-alt1
- 0.4.0

* Thu May 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.4-alt1
- 0.3.4

* Sun Apr 07 2024 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1.1
- first build for Sisyphus

* Wed Apr 03 2024 Semen Fomchenkov <armatik@altlinux.org> 0.3.2-alt1
- 0.3.2 version

* Wed Mar 20 2024 Semen Fomchenkov <armatik@altlinux.org> 0.3.0-alt2
- Spec-file refactoring

* Tue Mar 19 2024 Semen Fomchenkov <armatik@altlinux.org> 0.3.0-alt1
- Init build for Sisyphus
