%define _unpackaged_files_terminate_build 1

Name: coreimage
Version: 5.0.1
Release: alt1

Summary: Image viewer for C Suite
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.com/cubocore/coreapps/coreimage

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme
Requires: corestuff

%description
%summary.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc coreimage.png LICENSE README.md
%_bindir/coreimage
%_desktopdir/cc.cubocore.CoreImage.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreImage.svg
%_datadir/metainfo/cc.cubocore.CoreImage.metainfo.xml

%changelog
* Fri Feb 06 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
