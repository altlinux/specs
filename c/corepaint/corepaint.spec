%define _unpackaged_files_terminate_build 1

Name: corepaint
Version: 5.0.1
Release: alt1

Summary: Paint app for C Suite
License: GPL-3.0-or-later
Group: Graphics
Url: https://gitlab.com/cubocore/coreapps/corepaint

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
sed -i "s|Graphics;|Graphics;2DGraphics;|" cc.cubocore.CorePaint.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corepaint.png LICENSE README.md
%_bindir/corepaint
%_desktopdir/cc.cubocore.CorePaint.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CorePaint.svg
%_datadir/metainfo/cc.cubocore.CorePaint.metainfo.xml

%changelog
* Fri Feb 13 2026 Nikolay Strelkov <snk@altlinux.org> 5.0.1-alt1
- New version 5.0.1.

* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
