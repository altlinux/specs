Name: seadrive-gui
Version: 3.0.27
Release: alt1

Summary: Seafile Drive client

Group: Networking/File transfer
License: Apache License
Url: https://github.com/haiwen/seadrive-gui

# Source-url: https://github.com/haiwen/seadrive-gui/archive/v%version.tar.gz
Source: %name-%version.tar
Patch0: seadrive-gui-no-return-error.patch
Patch1: seadrive-gui-cmake-dbus-link.patch

# seadrive daemon is packaged as seafile-fuse
Requires: seafile-fuse >= %version

# Qt6 build requires Qt6 WebEngine
ExclusiveArch: %qt6_qtwebengine_arches

BuildRequires(pre): rpm-build-cmake
BuildRequires(pre): rpm-macros-qt6
BuildRequires(pre): rpm-macros-qt6-webengine

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Linguist)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Test)
BuildRequires: pkgconfig(Qt6Core5Compat)
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: pkgconfig(Qt6DBus)
BuildRequires: qt6-imageformats

# see CMakeLists.txt
BuildRequires: pkgconfig(glib-2.0) >= 2.16.0
BuildRequires: pkgconfig(jansson) >= 2.0
BuildRequires: pkgconfig(libsearpc) >= 1.0
BuildRequires: pkgconfig(openssl) >= 0.98
BuildRequires: pkgconfig(sqlite3) >= 3.0.0

%description
Seafile Drive client.
Seafile is an open source cloud storage system with features
on privacy protection and teamwork. Collections of files are
called libraries, and each library can be synced separately.
A library can also be encrypted with a user chosen password.
Seafile also allows users to create groups and easily sharing
files into groups.

The seadrive daemon is provided by the seafile-fuse package.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
export PATH=%_qt6_bindir:$PATH
%cmake
%cmake_build

%install
%cmakeinstall_std

%find_lang %name

%files -f %name.lang
%_bindir/seadrive-gui
%_desktopdir/seadrive.desktop
%_iconsdir/hicolor/*/apps/*
%_pixmapsdir/*

%changelog
* Wed Oct 28 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.27-alt1
- new version 3.0.27

* Mon Oct 12 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0.26-alt1
- new version 3.0.26
- switch to Qt6 (build with Qt6 WebEngine)
- fix build: add missing return on Linux, fix Qt6::DBus link signature
- add Requires: seafile-fuse (seadrive daemon)

* Mon Nov 27 2023 Ivan A. Melnikov <iv@altlinux.org> 2.0.19-alt2.1
- NMU: use rpm-macros-qt5-webengine (fixes build on loongarch64)

* Mon Jan 31 2022 Sergey V Turchin <zerg@altlinux.org> 2.0.19-alt2
- build with qtwebkit on ppc64le

* Mon Jan 24 2022 Vitaly Lipatov <lav@altlinux.ru> 2.0.19-alt1
- new version 2.0.19 (with rpmrb script)

* Sun Dec 19 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.18-alt1
- new version 2.0.18 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.15-alt1
- new version 2.0.15 (with rpmrb script)

* Tue Aug 03 2021 Michael Shigorin <mike@altlinux.org> 2.0.14-alt1.1
- E2K: use webkit instead of the (missing) webengine

* Tue Jun 08 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.14-alt1
- new version 2.0.14 (with rpmrb script)

* Wed Apr 07 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.13-alt1
- new version (2.0.13) with rpmgs script
- fix build with glib >= 2.67.3

* Wed Feb 24 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.12-alt1
- new version 2.0.12 (with rpmrb script)

* Fri Jan 22 2021 Vitaly Lipatov <lav@altlinux.ru> 2.0.10-alt1
- new version 2.0.10 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 2.0.7-alt1
- new version 2.0.7 (with rpmrb script)

* Wed Jun 12 2019 Vitaly Lipatov <lav@altlinux.ru> 1.0.5-alt1
- initial build for ALT Sisyphus
