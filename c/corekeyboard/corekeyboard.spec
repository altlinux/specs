%define _unpackaged_files_terminate_build 1

Name: corekeyboard
Version: 5.0.1
Release: alt1

Summary: X11 based virtual keyboard for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/corekeyboard

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(xtst)

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
%doc corekeyboard.png LICENSE README.md
%_bindir/corekeyboard
%_desktopdir/cc.cubocore.CoreKeyboard.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreKeyboard.svg
%_datadir/metainfo/cc.cubocore.CoreKeyboard.metainfo.xml

%changelog
* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
