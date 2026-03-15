%define _unpackaged_files_terminate_build 1

Name: corepins
Version: 5.0.1
Release: alt1

Summary: Bookmarking app for C Suite
License: GPL-3.0-or-later
Group: Office
Url: https://gitlab.com/cubocore/coreapps/corepins

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
sed -i "s|Utility;|Office;Database;|" cc.cubocore.CorePins.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corepins.png LICENSE README.md
%_bindir/corepins
%_desktopdir/cc.cubocore.CorePins.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CorePins.svg
%_datadir/metainfo/cc.cubocore.CorePins.metainfo.xml

%changelog
* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
