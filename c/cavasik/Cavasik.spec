%define nameL io.github.TheWisker.Cavasik

Name: cavasik

Version: 3.2.0
Release: alt1

Summary:  Audio visualizer based on CAVA
License: GPL-3.0-only
Group: Sound

Url: https://github.com/TheWisker/Cavasik
Vcs: https://github.com/TheWisker/Cavasik

Source: %name-%version.tar

Requires: cava
%add_python3_path %_datadir/%name

BuildRequires(pre): rpm-macros-meson rpm-build-python3
BuildRequires: meson cmake
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: /usr/bin/appstream-util
BuildRequires: pkgconfig(gio-2.0)

BuildArch: noarch

%description
This is an audio visualizer based on CAVA with extended capabilities.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name --with-gnome --all-name

%files -f %name.lang
%_bindir/%name
%_datadir/applications/%nameL.desktop
%_datadir/%name
%_datadir/glib-2.0/schemas/%nameL.gschema.xml
%_iconsdir/hicolor/*/apps/*.svg
%_datadir/metainfo/%nameL.metainfo.xml
%doc *.md

%changelog
* Fri Aug 08 2025 Aleksandr Shamaraev <shad@altlinux.org> 3.2.0-alt1
- Initial build for ALT Linux.
