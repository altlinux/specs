%define _unpackaged_files_terminate_build 1

Name: coreterminal
Version: 5.0.0
Release: alt1

Summary: Terminal emulator for C Suite
License: GPL-3.0-or-later
Group: Terminals
Url: https://gitlab.com/cubocore/coreapps/coreterminal

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6SerialPort)
BuildRequires: pkgconfig(qtermwidget6)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme
Requires: corestats

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
%doc coreterminal.png LICENSE README.md
%_bindir/coreterminal
%_desktopdir/cc.cubocore.CoreTerminal.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreTerminal.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
