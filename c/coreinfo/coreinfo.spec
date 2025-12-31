%define _unpackaged_files_terminate_build 1

Name: coreinfo
Version: 5.0.0
Release: alt1

Summary: File information tool for C Suite
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.com/cubocore/coreapps/coreinfo

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(libzen)
BuildRequires: pkgconfig(libmediainfo)

Requires: hicolor-icon-theme

%description
%summary.

%prep
%setup
sed -i "s|Utility;|Utility;FileTools;|" cc.cubocore.CoreInfo.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coreinfo.png LICENSE README.md
%_bindir/coreinfo
%_desktopdir/cc.cubocore.CoreInfo.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreInfo.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
