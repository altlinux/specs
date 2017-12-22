Name: megasync
Version: 3.5.3.0
Release: alt1

Summary: Easy automated syncing between your computers and your MEGA Cloud Drive

License: MEGA LIMITED CODE REVIEW LICENCE
Group: File tools
Url: https://github.com/meganz/MEGAsync

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/meganz/MEGAsync/archive/v%{version}_Linux.tar.gz
Source: %name-%version.tar
Source1: qt5sdk.pri

BuildPreReq: rpm-macros-qt5

BuildRequires: cmake

BuildRequires: libmegasdk-devel >= 3.2 libmegasdk-devel-qt5

# Automatically added by buildreq on Sat Jun 13 2015
# optimized out: fontconfig glib2-devel glibc-devel-static libGL-devel libX11-devel libatk-devel libavcodec-devel libavutil-devel libcairo-devel libcloog-isl4 libdc1394-22 libgdk-pixbuf libgdk-pixbuf-devel libgio-devel libjson-c libopencore-amrnb0 libopencore-amrwb0 libp11-kit libpango-devel libqt5-core libqt5-gui libqt5-network libqt5-opengl libqt5-sql libqt5-svg libqt5-widgets libqt5-xml libraw1394-11 libsodium-devel libstdc++-devel libswscale-devel libvpx-devel libwayland-client libwayland-server python3-base qt5-base-devel qt5-declarative-devel qt5-script-devel qt5-tools xorg-scrnsaverproto-devel xorg-xproto-devel
BuildRequires: gcc-c++ qt5-connectivity-devel qt5-location-devel qt5-multimedia-devel qt5-phonon-devel qt5-quick1-devel qt5-tools-devel qt5-webkit-devel qt5-websockets-devel qt5-svg-devel

%description
Easy automated syncing between your computers and your MEGA cloud drive.

This repository contains all the development history
of the official sync client of MEGA: https://mega.nz/sync

%prep
%setup
#__subst "s|.*-Werror.*||g" CMakeLists.txt
mkdir -p src/MEGASync/mega/bindings/qt/
cp -a %_datadir/libmegasdk/qt5/*.* src/MEGASync/mega/bindings/qt/
cp %SOURCE1 src/MEGASync/mega/bindings/qt/sdk.pri

mkdir -p src/MEGASync/mega/include/mega/
ln -s %_includedir/mega/config.h src/MEGASync/mega/include/mega/config.h

# TODO: use external only
#rm -rf src/MEGASync/google_breakpad

%build
cd src
%qmake_qt5 CONFIG+="release" MEGA.pro
lrelease-qt5 MEGASync/MEGASync.pro
%make_build

%install
cd src/MEGASync/
mkdir -p %buildroot%_bindir/
install -m 0755 %name %buildroot%_bindir/%name

cd platform/linux/data
mkdir -p %buildroot%_desktopdir/
install -m 0644 megasync.desktop %buildroot%_desktopdir/%name.desktop

mkdir -p %buildroot%_iconsdir/
cp -a icons/hicolor/ %buildroot%_iconsdir/

%files
%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/*

%changelog
* Fri Dec 22 2017 Vitaly Lipatov <lav@altlinux.ru> 3.5.3.0-alt1
- initial build for ALT Linux Sisyphus
