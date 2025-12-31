%define _unpackaged_files_terminate_build 1

Name: corepdf
Version: 5.0.0
Release: alt1

Summary: PDF viewer for C Suite
License: GPL-3.0-or-later
Group: Office
Url: https://gitlab.com/cubocore/coreapps/corepdf

Source: %name-%version.tar

BuildRequires(pre): rpm-build-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6DocumentView)
BuildRequires: pkgconfig(cprime-core)

Requires: hicolor-icon-theme

%description
%summary. It is based on Poppler.

%prep
%setup
sed -i "s|Office;|Office;Viewer;|" cc.cubocore.CorePDF.desktop

%build
%cmake
%cmake_build

%install
%cmake_install

%files
%doc corepdf.png LICENSE README.md
%_bindir/corepdf
%_desktopdir/cc.cubocore.CorePDF.desktop
%_iconsdir/hicolor/scalable/apps/cc.cubocore.CorePDF.svg

%changelog
* Tue Dec 30 2025 Nikolay Strelkov <snk@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus
