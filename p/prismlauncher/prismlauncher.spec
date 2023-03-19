Name: prismlauncher
Version: 6.3
Release: alt1

Summary: Minecraft launcher with ability to manage multiple instances

License: GPLv3
Group: Games/Strategy
Url: https://prismlauncher.org/

# Source-url: https://github.com/PrismLauncher/PrismLauncher/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/PolyMC/libnbtplusplus/archive/refs/heads/master.zip
Source1: %name-libnbtplusplus-%version.tar

# Source2-url: https://github.com/stachenov/quazip/archive/refs/tags/v1.4.tar.gz
Source2: %name-quazip-%version.tar

ExcludeArch: %arm

BuildRequires(pre): rpm-macros-cmake

BuildRequires: zlib-devel bzlib-devel libGLU-devel
BuildRequires: qt6-base-devel qt6-svg-devel qt6-5compat-devel

BuildRequires: cmake gcc-c++ extra-cmake-modules

BuildRequires: java-devel >= 17

Requires: icon-theme-hicolor
Requires: jre-headless >= 17
BuildRequires: scdoc libgamemode-devel libtomlplusplus-devel libghc_filesystem-devel

Requires: qt6-svg qt6-imageformats

# for older minecraft versions
Requires: xrandr

%description
A custom launcher for Minecraft that allows you to easily manage multiple installations of Minecraft at once (Fork of MultiMC).

%prep
%setup -a1 -a2

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
%_desktopdir/*.desktop
%_datadir/metainfo/*.xml
%_datadir/%name/NewLaunch.jar
%_datadir/%name/JavaCheck.jar
%_man6dir/*
%_datadir/mime/packages/modrinth-mrpack-mime.xml
%_datadir/qlogging-categories6/

%changelog
* Sat Mar 18 2023 Vitaly Lipatov <lav@altlinux.ru> 6.3-alt1
- initial build for ALT Sisyphus
