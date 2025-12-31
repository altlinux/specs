%define _unpackaged_files_terminate_build 1

Name: coreuniverse
Version: 5.0.0
Release: alt1

Summary: Shows information about apps for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/coreuniverse

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
%doc coreuniverse.png LICENSE README.md
%_bindir/coreuniverse
%_desktopdir/cc.cubocore.CoreUniverse.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreUniverse.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
