%define _unpackaged_files_terminate_build 1

Name: corestats
Version: 5.0.0
Release: alt1

Summary: System resource viewer for C Suite
License: GPL-3.0-or-later
Group: Monitoring
Url: https://gitlab.com/cubocore/coreapps/corestats

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)
BuildRequires: libsensors3-devel

Requires: hicolor-icon-theme

%description
%summary.

%prep
%setup
sed -i "s|Utility;|System;Monitor;|" cc.cubocore.CoreStats.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corestats.png LICENSE README.md
%_bindir/corestats
%_desktopdir/cc.cubocore.CoreStats.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreStats.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
