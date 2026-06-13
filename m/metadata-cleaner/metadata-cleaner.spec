%def_enable check

%define _name io.gitlab.metadatacleaner.metadatacleaner

Name: metadata-cleaner
Version: 4.0.0
Release: alt1

Summary:  Metadata Cleaner
License: GPL-3.0-or-later and CC-BY-SA-4.0
Group: Graphical desktop/GNOME

Url: https://gitlab.com/metadatacleaner/metadatacleaner
Vcs: https://gitlab.com/metadatacleaner/metadatacleaner

BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson itstool
BuildRequires: pkgconfig(pygobject-3.0)
BuildRequires: pkgconfig(python3)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(libadwaita-1) typelib(Adw)

%add_python3_path %_datadir/%name

%{?_enable_check:BuildRequires: /usr/bin/appstreamcli desktop-file-utils /usr/bin/glib-compile-schemas}

%description
Metadata within a file can tell a lot about you. Cameras record data about when and where a picture was taken and which camera was used. Office applications automatically add author and company information to documents and spreadsheets. This is sensitive information and you may not want to disclose it.
This tool allows you to view metadata in your files and to get rid of it, as much as possible.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%find_lang %name --all-name

%check
%__meson_test

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%_name.desktop
%_datadir/dbus-1/services/%_name.service
%_datadir/glib-2.0/schemas/%_name.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/%name/*
%_datadir/metainfo/%_name.metainfo.xml
%doc *.md

%changelog
* Sat Jun 13 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.0.0-alt1
- 2.5.6 -> 4.0.0
- changed url && vcs

* Sat Nov 23 2024 Aleksandr Shamaraev <shad@altlinux.org> 2.5.6-alt1
- Initial build for Sisyphus.
