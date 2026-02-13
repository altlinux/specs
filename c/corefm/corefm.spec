%define _unpackaged_files_terminate_build 1

Name: corefm
Version: 5.0.1
Release: alt1

Summary: Lightweight file-manager for C Suite
License: GPL-3.0-or-later
Group: File tools
Url: https://gitlab.com/cubocore/coreapps/corefm

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Multimedia)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)

Requires: hicolor-icon-theme

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
%doc corefm.png LICENSE README.md
%_bindir/corefm
%_desktopdir/cc.cubocore.CoreFM.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreFM.svg
%_datadir/metainfo/cc.cubocore.CoreFM.metainfo.xml

%changelog
* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
