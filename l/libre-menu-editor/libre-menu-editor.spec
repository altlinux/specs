%def_disable snapshot

%define _name libre-menu-editor
%define ver_major 1.7
%define rdn_name page.codeberg.libre_menu_editor.LibreMenuEditor

Name: %_name
Version: %ver_major.2
Release: alt1

Summary: Menu editor
License: GPL-3.0-or-later
Group: Graphical desktop/GNOME
Url: https://codeberg.org/libre-menu-editor/libre-menu-editor
Epoch: 1

Vcs: https://codeberg.org/libre-menu-editor/libre-menu-editor.git

BuildArch: noarch

%if_disabled snapshot
Source: %url/archive/v%version.tar.gz
%else
Source: %name-%version.tar
%endif

%add_python3_path %_datadir/%_name

Requires: typelib(Adw) = 1
Requires: xdg-utils

BuildRequires(pre): rpm-build-python3 rpm-build-gir

%description
Menu editor for GNOME.

%prep
%setup -n %name%{?_enable_snapshot:-%version}

%install
%makeinstall_std
%find_lang %name

%files -f %name.lang
%attr(0755,root,root) %_bindir/%name
%_datadir/%name/
%_desktopdir/%rdn_name.desktop
%_datadir/icons/hicolor/*/apps/*
%_datadir/metainfo/%rdn_name.appdata.xml
%doc readme.*

%changelog
* Thu Oct 03 2024 Yuri N. Sedunov <aris@altlinux.org> 1:1.7.2-alt1
- 1.7.2

* Thu Jun 27 2024 Yuri N. Sedunov <aris@altlinux.org> 2024.05.10-alt1
- first build for Sisyphus (2024-05-10)
