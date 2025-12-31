%define _unpackaged_files_terminate_build 1

Name: corestuff
Version: 5.0.0
Release: alt1

Summary: An activity viewer for C Suite
License: GPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://gitlab.com/cubocore/coreapps/corestuff

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: kf6-kglobalaccel-devel
BuildRequires: pkgconfig(cprime-core)
BuildRequires: pkgconfig(csys)
BuildRequires: pkgconfig(xcb-atom)
BuildRequires: pkgconfig(xcb-ewmh)
BuildRequires: pkgconfig(xi)
BuildRequires: pkgconfig(xcomposite)

Requires: hicolor-icon-theme
Requires: coreshot
Requires: plasma6-kglobalacceld
Requires: coregarage

%description
%summary.

%prep
%setup
sed -i "s|System;|System;Monitor;|" cc.cubocore.CoreStuff.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corestuff.png corestuff2.png LICENSE README.md
%config %_sysconfdir/xdg/autostart/cc.cubocore.CoreStuff.desktop
%_bindir/corestuff
%_desktopdir/cc.cubocore.CoreStuff.desktop
%_datadir/coreapps/background/default.svg
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CoreStuff.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
