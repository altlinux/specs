Name: fb2edit
Version: 0.0.9
Release: alt1

Summary: FB2 editor
License: GPLv3
Group: Editors

Url: https://github.com/lintest/fb2edit
# Repacked %url/archive/%version/%name-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Fri Jan 20 2017
# optimized out: cmake-modules fontconfig libgst-plugins1.0 libqt4-core libqt4-devel libqt4-gui libqt4-location libqt4-network libqt4-opengl libqt4-qt3support libqt4-script libqt4-sensors libqt4-sql-sqlite libqt4-svg libqt4-webkit libqt4-webkit-devel libqt4-xml libqt4-xmlpatterns libstdc++-devel pkg-config python-base python-modules
BuildRequires: cmake gcc-c++ libqt4-sql-mysql phonon-devel qt4-designer

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
* Fri Jan 20 2017 Gleb F-Malinovskiy <glebfm@altlinux.org> 0.0.9-alt1
- Initial build.
