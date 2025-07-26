%define _unpackaged_files_terminate_build 1

Name: lomiri-filemanager-app
Version: 1.1.4
Release: alt1

Summary: Filemanager App for Lomiri Operating Environment
License: GPL-3.0
Group: Graphical desktop/Other
Url: https://gitlab.com/ubports/development/apps/lomiri-filemanager-app

Source: %name-%version.tar

# sync with version 1.1.4+dfsg-2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre): rpm-build-qml
BuildRequires(pre): rpm-build-python3

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(smbclient)

Requires: libqt5-quick
Requires: lomiri-ui-toolkit
Requires: lomiri-ui-extras
Requires: lomiri-content-hub
Requires: lomiri-thumbnailer
Requires: biometryd

%description
This app is a core app for Ubuntu Touch's shell Lomiri. Ubuntu Touch is
a mobile OS developed by the UBports Foundation. Lomiri is its operating
environment optimized for touch based human-machine interaction, but
also supports convergence (i.e. switching between tablet/phone and
desktop mode).

This package provides Lomiri's Filemanager App.

%prep
%setup
%patch -p1

%build
%cmake \
       -DCLICK_MODE=OFF \
       -DINSTALL_TESTS=OFF
%cmake_build

%install
%cmake_install

mkdir -pv %buildroot%_qt5_qmldir
mv -v %buildroot/Lomiri %buildroot%_qt5_qmldir/

%find_lang %name

%files -f %{name}.lang
%doc AUTHORS ChangeLog COPYING.BSD COPYING.GPL COPYING.LGPL NEWS README-Autopilot.md README-Developers.md README.md README-MergeRequest.md
%_bindir/lomiri-filemanager-app
%_desktopdir/lomiri-filemanager-app.desktop
%_datadir/lomiri-content-hub/peers/lomiri-filemanager-app
%_iconsdir/hicolor/scalable/apps/lomiri-filemanager-app.svg
%dir %_datadir/lomiri-filemanager-app
%_datadir/lomiri-filemanager-app/*
%_datadir/lomiri-url-dispatcher/urls/lomiri-filemanager-app.url-dispatcher
%exclude %_datadir/locale/it_CARES/LC_MESSAGES/lomiri-filemanager-app.mo
%exclude %_datadir/locale/zh_LATN@pinyin/LC_MESSAGES/lomiri-filemanager-app.mo
%dir %_qt5_qmldir/Lomiri/FileManager
%_qt5_qmldir/Lomiri/FileManager/*

%changelog
* Sun Jul 20 2025 Nikolay Strelkov <snk@altlinux.org> 1.1.4-alt1
- Initial build for Sisyphus
