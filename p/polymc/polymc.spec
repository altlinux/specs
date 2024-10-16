Name: polymc
Version: 6.1
Release: alt2

Summary: Minecraft launcher with ability to manage multiple instances

License: GPL-3.0-only
Group: Games/Strategy
Url: https://polymc.org

# Source-url: https://github.com/PolyMC/PolyMC/archive/%version/polymc-%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/PolyMC/libnbtplusplus/archive/refs/heads/master.zip
Source1: %name-libnbtplusplus-%version.tar

ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake

BuildRequires: zlib-devel bzlib-devel libGLU-devel
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel qt6-svg
BuildRequires: qt6-charts-devel qt6-5compat-devel

BuildRequires: cmake gcc-c++ extra-cmake-modules

BuildRequires: java-devel
BuildRequires: jre-openjdk-headless
BuildRequires: scdoc libgamemode-devel
BuildRequires: libtomlplusplus-devel libghc_filesystem-devel quazip-qt6-devel

Requires: qt6-svg qt6-imageformats
# 'libgl' 'qt6-base' 'qt6-5compat' 'qt6-svg' 'qt6-imageformats' 'zlib' 'hicolor-icon-theme' 'quazip-qt6')

# for older minecraft versions
Requires: xrandr

%add_optflags -Wno-error=return-type

%description
PolyMC is a free, open source launcher for Minecraft. It allows you to have
multiple, separate instances of Minecraft (each with their own mods, texture
packs, saves, etc) and helps you manage them and their associated options with
a simple interface.

%prep
%setup -a1
%__subst 's|share/jars|share/polymc/jars|' CMakeLists.txt launcher/Application.cpp

%build
%cmake \
    -DLauncher_BUILD_PLATFORM="alt" \
    -DLauncher_QT_VERSION_MAJOR="6" \
    -DLauncher_UPDATER_BASE:STRING="" \
    %nil
%cmake_build

%install
%cmake_install

%files
%doc README.md COPYING.md
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/*.svg
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%dir %_datadir/%name/
%dir %_datadir/%name/jars/
%_datadir/%name/jars/NewLaunch.jar
%_datadir/%name/jars/JavaCheck.jar
%_man6dir/%name.6*
#_datadir/mime/packages/modrinth-mrpack-mime.xml
#_datadir/qlogging-categories6/*.categories

%changelog
* Thu Apr 04 2024 Roman Alifanov <ximper@altlinux.org> 6.1-alt2
- fix META URL (ALT bug 48495)

* Sun Feb 04 2024 Vitaly Lipatov <lav@altlinux.ru> 6.1-alt1
- new version 6.1 (with rpmrb script)

* Sun Nov 26 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt4
- fix META URL (ALT bug 48495)
- fix build with Qt 6.6.0

* Sun Aug 20 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt3
- fix summary, add README, set license to GPL-3.0-only

* Sun Aug 13 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt2
- build with external quazip-qt6
- add Requires: qt6-svg qt6-imageformats

* Wed Mar 29 2023 Vitaly Lipatov <lav@altlinux.ru> 5.1-alt1
- initial build for ALT Sisyphus
