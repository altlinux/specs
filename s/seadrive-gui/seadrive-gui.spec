Name: seadrive-gui
Version: 2.0.10
Release: alt1

Summary: Seafile Drive client

Group: Networking/File transfer
License: Apache License
Url: https://github.com/haiwen/seadrive-gui

# Source-url: https://github.com/haiwen/seadrive-gui/archive/v%version.tar.gz
Source: %name-%version.tar

# TODO: is not opensourced
#Requires: seadrive-daemon >= 1.0.0

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake libsqlite3-devel libssl-devel zlib-devel libcurl-devel
BuildRequires: qt5-imageformats qt5-tools-devel qt5-base-devel qt5-webengine-devel

BuildRequires: libevent-devel >= 2.0
BuildRequires: libglib2-devel libuuid-devel libjansson-devel
BuildRequires: libsearpc-devel

%description
Seafile Drive client.
Seafile is an open source cloud storage system with features
on privacy protection and teamwork. Collections of files are
called libraries, and each library can be synced separately.
A library can also be encrypted with a user chosen password.
Seafile also allows users to create groups and easily sharing
files into groups.

Note: you need install seadrive-daemon also, which not opensourced.

%prep
%setup

%build
PATH=%_qt5_bindir:$PATH %cmake_insource
%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/seadrive-gui
%_desktopdir/seadrive.desktop
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- new version 2.0.10 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- new version 2.0.7 (with rpmrb script)

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Sisyphus
