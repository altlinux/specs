%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

%define appname com.github.sdv43.whaler

Name: whaler
Version: 1.2.5
Release: alt1

Summary: Docker Container Management
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/sdv43/whaler
ExclusiveArch: %go_arches
ExcludeArch: %ix86

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala
BuildRequires(pre): rpm-build-golang

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(libcurl)
BuildRequires: vapi(granite)

Requires: docker-cli

%description
Whaler provides basic functionality for managing Docker containers.
The app can start and stop both standalone containers and
docker-compose applications. Also, it supports container logs viewing.

The solution is perfect for those who are looking for a simple tool
to perform some basic actions. For the app to run correctly, make sure
that Docker is installed on your system.

%prep
%setup
sed -i "s|data/images/screenshots/screenshot-1.png?raw=true|screenshot-1.png|" README.md
sed -i "s|^Categories=.*|Categories=GTK;System;Monitor;|" data/com.github.sdv43.whaler.desktop.in

%build
%meson
%meson_build

%install
%meson_install

%find_lang %appname

%check
%meson_test

%files -f %{appname}.lang
%doc COPYING README.md data/images/screenshots/screenshot-1.png
%_bindir/%appname
%_desktopdir/%{appname}.desktop
%_iconsdir/hicolor/*/apps/%{appname}.png
%_datadir/glib-2.0/schemas/com.github.sdv43.whaler.gschema.xml
%_datadir/metainfo/com.github.sdv43.whaler.appdata.xml

%changelog
* Sat Mar 28 2026 Nikolay Strelkov <snk@altlinux.org> 1.2.5-alt1
- New version 1.2.5.

* Tue Nov 11 2025 Vladimir Didenko <cow@altlinux.org> 1.2.4-alt2
- NMU: exclude ix86 arches from the build (docker doesn't support it anymore)

* Sun Nov 02 2025 Nikolay Strelkov <snk@altlinux.org> 1.2.4-alt1
- Initial build for Sisyphus
