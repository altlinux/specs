%define _unpackaged_files_terminate_build 1

Name: coreshot
Version: 5.0.0
Release: alt1

Summary: Screen capture utility for C Suite
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.com/cubocore/coreapps/coreshot

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme
Requires: coregarage

%description
%summary.

%prep
%setup
sed -i "s|Utility;|Utility;FileTools;|" cc.cubocore.CoreShot.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coreshot.png LICENSE README.md
%_bindir/coreshot
%_desktopdir/cc.cubocore.CoreShot.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreShot.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
