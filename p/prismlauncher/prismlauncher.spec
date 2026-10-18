%define oname PrismLauncher
Name: prismlauncher
Version: 11.1.1
Release: alt2

Summary: Minecraft launcher with ability to manage multiple instances

License: GPLv3
Group: Games/Strategy
Url: https://prismlauncher.org/

# Source-url: https://github.com/PrismLauncher/PrismLauncher/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/PolyMC/libnbtplusplus/archive/refs/heads/master.zip
Source1: %name-libnbtplusplus-%version.tar

ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake

BuildRequires: zlib-devel bzlib-devel libGLU-devel
BuildRequires: qt6-base-devel qt6-svg-devel qt6-networkauth-devel qt6-5compat-devel

BuildRequires: rpm-build-cmake gcc-c++ extra-cmake-modules

BuildRequires: java-devel >= 17

Requires: icon-theme-hicolor
Requires: jre-headless >= 17
BuildRequires: scdoc libgamemode-devel
BuildRequires: libtomlplusplus-devel libghc_filesystem-devel quazip-qt6-devel

# Check https://bugzilla.altlinux.org/47223
BuildRequires: cmark-devel cmark
BuildRequires: libqrencode-devel
BuildRequires: libarchive-devel

Requires: qt6-svg qt6-imageformats

# for older minecraft versions
Requires: xrandr

%description
A custom launcher for Minecraft that allows you to easily manage multiple installations of Minecraft at once (Fork of MultiMC).

%prep
%setup -a1
# --release 8 compiles against the Java 8 API (ct.sym): java.applet is gone from JDK 26+ runtime classes
%__subst 's| -target 7 -source 7| --release 8|' libraries/launcher/CMakeLists.txt libraries/javacheck/CMakeLists.txt

%build
%cmake \
    -DLauncher_BUILD_PLATFORM="alt" \
    -DLauncher_QT_VERSION_MAJOR="6"
%cmake_build

%install
%cmake_install

%files
%doc COPYING.md
%_bindir/%name
%_iconsdir/hicolor/scalable/apps/*.svg
%_iconsdir/hicolor/*/apps/*.png
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%dir %_datadir/%oname/
%_datadir/%oname/NewLaunch.jar
%_datadir/%oname/NewLaunchLegacy.jar
%_datadir/%oname/JavaCheck.jar
%_datadir/%oname/qtlogging.ini
%_man6dir/*
%_datadir/mime/packages/org.prismlauncher.PrismLauncher.xml
%_datadir/qlogging-categories6/

%changelog
* Sat Oct 17 2026 Vitaly Lipatov <lav@altlinux.ru> 11.1.1-alt2
- fix FTBFS with JDK 26+: compile java parts with --release 8 (java.applet API)
- replaced BuildRequires: cmake with rpm-build-cmake

* Tue Oct 06 2026 Vitaly Lipatov <lav@altlinux.ru> 11.1.1-alt1
- new version 11.1.1

* Mon Jul 20 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.3-alt1
- new version 11.0.3 (with rpmrb script)

* Wed May 06 2026 Vitaly Lipatov <lav@altlinux.ru> 11.0.2-alt1
- new version

* Sat May 10 2025 Vitaly Lipatov <lav@altlinux.ru> 9.4-alt1
- new version 9.4 (with rpmrb script)

* Mon Dec 02 2024 Vitaly Lipatov <lav@altlinux.ru> 9.1-alt1
- new version 9.1 (with rpmrb script)

* Sun Feb 04 2024 Vitaly Lipatov <lav@altlinux.ru> 8.0-alt2
- fix build with new java

* Mon Dec 25 2023 Vitaly Lipatov <lav@altlinux.ru> 8.0-alt1
- new version 8.0 (with rpmrb script)

* Sun Aug 13 2023 Vitaly Lipatov <lav@altlinux.ru> 7.2-alt1
- new version 7.2 (with rpmrb script)
- build with external quazip-qt6
- add BR: cmark-devel

* Sat Mar 18 2023 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt1
- initial build for ALT Sisyphus
