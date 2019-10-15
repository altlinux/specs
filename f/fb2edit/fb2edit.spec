Name: fb2edit
Version: 0.1.0
Release: alt1

Summary: FB2 editor

License: GPLv3
Group: Editors
Url: https://github.com/vitlav/fb2edit

# Source-url: https://github.com/vitlav/fb2edit/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires: qt5-imageformats qt5-tools-devel qt5-translations qt5-wayland-devel qt5-webkit-devel qt5-xmlpatterns-devel

BuildRequires: libxml2-devel

BuildRequires: cmake gcc-c++

%description
Editor for FB2 (FictionBook) files.

%prep
%setup

%build
%cmake
%cmake_build

%install
%cmakeinstall_std

%files
%_bindir/*
%_datadir/applications/*
%_datadir/pixmaps/*
%_iconsdir/hicolor/*/apps/*

%changelog
* Tue Oct 15 2019 Vitaly Lipatov <lav@altlinux.ru> 0.1.0-alt1
- NMU: new version (0.1.0) with rpmgs script
- build with Qt5

* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.9-alt1
- Initial build.
