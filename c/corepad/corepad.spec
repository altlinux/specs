%define _unpackaged_files_terminate_build 1

Name: corepad
Version: 5.0.0
Release: alt1

Summary: Document editor for C Suite
License: GPL-3.0-or-later
Group: Text tools
Url: https://gitlab.com/cubocore/coreapps/corepad

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

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corepad.png LICENSE README.md
%_bindir/corepad
%_desktopdir/cc.cubocore.CorePad.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CorePad.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
