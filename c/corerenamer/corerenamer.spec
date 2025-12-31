%define _unpackaged_files_terminate_build 1

Name: corerenamer
Version: 5.0.0
Release: alt1

Summary: Batch file renamer for C Suite
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.com/cubocore/coreapps/corerenamer

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme

%description
%summary.

%prep
%setup
sed -i "s|Utility;|Utility;FileTools;|" cc.cubocore.CoreRenamer.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corerenamer.png LICENSE README.md
%_bindir/corerenamer
%_desktopdir/cc.cubocore.CoreRenamer.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreRenamer.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
