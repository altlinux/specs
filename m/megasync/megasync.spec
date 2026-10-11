Name: megasync
Version: 6.6.2.0
Release: alt1

Summary: Easy automated syncing between your computers and your MEGA Cloud Drive

License: MEGA LIMITED CODE REVIEW LICENCE
Group: File tools
Url: https://github.com/meganz/MEGAsync

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/meganz/MEGAsync/archive/v%{version}_Linux.tar.gz
Source: v%{version}_Linux.tar.gz

# MEGAsync v6.6.2.0_Linux pins the MEGA SDK submodule to v10.19.0.
# The SDK has no stable ABI: update megasync and libmegasdk together (one task).
%define sdk_version 10.19.0
%define sdk_abiversion %(echo %sdk_version | cut -d. -f1-2)

# Build with the installed MEGA SDK instead of the src/MEGASync/mega submodule
Patch1: megasync-6.6.2.0-system-sdk.patch
Patch2: megasync-6.6.2.0-vcpkg-install-only.patch
Patch3: megasync-6.6.2.0-system-gfxworker.patch
Patch4: megasync-6.6.2.0-offline-clang-format.patch
Patch5: megasync-6.6.2.0-zlib.patch

BuildRequires(pre): rpm-build-cmake rpm-macros-qt5
BuildRequires: gcc-c++
BuildRequires: libmegasdk-devel = %sdk_version
BuildRequires: qt5-base-devel qt5-declarative-devel qt5-svg-devel qt5-tools-devel qt5-x11extras-devel
BuildRequires: libxcb-devel zlib-devel

# the soname (libmega.so.%sdk_abiversion) does not pin the SDK patch release
Requires: libmega%sdk_abiversion = %sdk_version
Requires: libmega-qt%sdk_abiversion = %sdk_version
# the graphics helper is started by the path, not linked
Requires: libmegasdk-gfxworker = %sdk_version
# QML modules imported by the UI from the embedded resources
Requires: qt5-quickcontrols qt5-quickcontrols2 qt5-graphicaleffects

%description
Easy automated syncing between your computers and your MEGA cloud drive.

This repository contains all the development history
of the official sync client of MEGA: https://mega.nz/sync

%prep
%setup
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1
%patch5 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DUSE_SYSTEM_MEGA_SDK=ON \
    -DENABLE_DESKTOP_APP_WERROR=OFF \
    -DENABLE_DESKTOP_UPDATE_GEN=OFF \
    -DENABLE_DESIGN_TOKENS_IMPORTER=OFF \
    -DENABLE_DESKTOP_APP_TESTS=OFF \
    -DENABLE_LINUX_EXT=OFF \
    -DUSE_BREAKPAD=OFF \
    %nil
%cmake_build

%install
# the project installs into usr/... relative to an empty prefix
DESTDIR=%buildroot cmake --install %_cmake__builddir --prefix /

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*
%_iconsdir/hicolor/*/status/*
%_iconsdir/ubuntu-mono-dark/status/24/mega*.svg
%_datadir/%name/

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 6.6.2.0-alt1
- new version 6.6.2.0 (CMake build)
- build with the installed MEGA SDK 10.19.0 (libmegasdk) instead of the submodule
- use the SDK gfxworker helper for thumbnails and previews
- drop obsolete qmake-era workarounds, build without breakpad

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 4.11.0.0-alt1
- new version 4.11.0.0 (with rpmrb script)

* Tue Nov 07 2023 Vitaly Lipatov <lav@altlinux.ru> 4.10.0.0-alt1
- new version 4.10.0.0 (with rpmrb script)

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 4.6.1.0-alt1
- new version 4.6.1.0 (with rpmrb script)

* Mon Dec 13 2021 Vitaly Lipatov <lav@altlinux.ru> 4.5.3.0-alt1
- new version 4.5.3.0 (with rpmrb script)

* Tue Dec 01 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.7.0-alt1
- new version 4.3.7.0 (with rpmrb script)

* Tue Sep 15 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.3.0-alt1
- new version 4.3.3.0 (with rpmrb script)

* Sun Mar 29 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.1.0-alt1
- new version 4.3.1.0 (with rpmrb script)

* Sun Mar 08 2020 Vitaly Lipatov <lav@altlinux.ru> 4.3.0.8-alt1
- new version 4.3.0.8

* Wed Apr 10 2019 Fr. Br. George <george@altlinux.ru> 4.0.2.0-alt1
- Autobuild version bump to 4.0.2.0

* Tue Feb 12 2019 Vitaly Lipatov <lav@altlinux.ru> 3.7.1.0-alt1
- new version 3.7.1.0 (with rpmrb script)
- use system fonts instead of compiled in ones

* Sun Nov 25 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6.6.0-alt3
- rebuild with libcryptopp.so.7

* Wed Aug 15 2018 Fr. Br. George <george@altlinux.ru> 3.6.6.0-alt2
- Rebuild with new sdk

* Sun Jun 10 2018 Vitaly Lipatov <lav@altlinux.ru> 3.6.6.0-alt1
- new version 3.6.6.0 (with rpmrb script)

* Fri Dec 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.5.3.0-alt1
- initial build for ALT Linux Sisyphus
