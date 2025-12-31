%define _unpackaged_files_terminate_build 1

Name: corearchiver
Version: 5.0.0
Release: alt1

Summary: Archiver for C Suite
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.com/cubocore/coreapps/corearchiver

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(archiveqt6)

Requires: hicolor-icon-theme

%description
%summary, to create and extract archives.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corearchiver.png LICENSE README.md
%_bindir/corearchiver
%_desktopdir/cc.cubocore.CoreArchiver.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreArchiver.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
