%ifarch %qt5_qtwebengine_arches
%def_enable qtwebengine
%else
%def_disable qtwebengine
%endif

Name: seadrive-gui
Version: 2.0.19
Release: alt2.1

Summary: Seafile Drive client

Group: Networking/File transfer
License: Apache License
Url: https://github.com/haiwen/seadrive-gui

# Source-url: https://github.com/haiwen/seadrive-gui/archive/v%version.tar.gz
Source: %name-%version.tar

# TODO: is not opensourced
#Requires: seadrive-daemon >= 1.0.0

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt5-webengine

BuildRequires: cmake libsqlite3-devel libssl-devel zlib-devel libcurl-devel
BuildRequires: qt5-imageformats qt5-tools-devel qt5-base-devel

BuildRequires: libevent-devel >= 2.0
BuildRequires: libglib2-devel libuuid-devel libjansson-devel
BuildRequires: libsearpc-devel

%if_enabled qtwebengine
BuildRequires: qt5-webengine-devel
%else
BuildRequires: qt5-webkit-devel
%endif

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
sed -i '1iADD_DEFINITIONS(-DGLIB_VERSION_MIN_REQUIRED=GLIB_VERSION_2_26)' CMakeLists.txt
%if_disabled qtwebengine
sed -i '/USE_QT_WEBKIT/ {s/OFF/ON/}' CMakeLists.txt
%endif

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
