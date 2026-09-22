%define _unpackaged_files_terminate_build 1

Name:    dish-linux
Version: 2.1.0
Release: alt1

Summary: Native Linux client for the Satellite wireless-gamepad server
License: LGPL-3.0-or-later
Group:   System/Configuration/Hardware
URL:     https://tinkernorth.github.io/dish-linux/
VCS:     https://github.com/TinkerNorth/dish-linux

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake gcc-c++
BuildRequires: qt6-base-devel qt6-svg-devel qt6-declarative-devel qt6-tools-devel
BuildRequires: libsodium-devel libSDL2-devel libopus-devel librsvg-utils
Requires: icon-theme-hicolor
Requires: libqt6-quickcontrols2basic
Requires: libqt6-quicklayouts
Requires: libqt6-quickeffects
Requires: libqt6-svg

ExcludeArch: i586

%description
Turns the gamepads attached to a Linux machine into wireless controllers
for another machine on the same network.

Dish is one half of a pair: it does nothing on its own. For full operation
a Satellite server must run on the gaming machine on the same LAN. On Linux
the receiver side is packaged as satellite-dish (install it on the gaming
host, not on the machine with the gamepads); on Windows use the official
SatelliteSetup.exe with the ViGEmBus driver.

%prep
%setup

%build
%cmake \
    -DDISH_BUILD_TESTS=OFF \
    -DDISH_REQUIRE_TRANSLATIONS=ON

%cmake_build

%install
%cmake_install

%files
%_bindir/dish
%dir %_datadir/metainfo
%_datadir/metainfo/com.tinkernorth.Dish.metainfo.xml
%_docdir/dish
%_desktopdir/com.tinkernorth.Dish.desktop
%_iconsdir/hicolor/*/apps/com.tinkernorth.Dish.png
%_iconsdir/hicolor/scalable/apps/com.tinkernorth.Dish.svg
%_udevrulesdir/70-dish-hidraw.rules
%_man1dir/dish.1*

%changelog
* Tue Sep 22 2026 Sergey Palcheh <minergenon@altlinux.org> 2.1.0-alt1
- new version 2.1.0

* Fri Sep 18 2026 Sergey Palcheh <minergenon@altlinux.org> 2.0.0-alt1
- Initial build for Sisyphus
