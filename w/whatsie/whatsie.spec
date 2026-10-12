Name: whatsie
Version: 6.1.1
Release: alt1

Summary: Feature rich WhatsApp Client for Desktop Linux

License: MIT
Group: Networking/Chat
Url: https://github.com/keshavbhatt/whatsie

# Source-url: https://github.com/keshavbhatt/whatsie/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-macros-qt6-webengine
ExclusiveArch: %qt6_qtwebengine_arches
BuildRequires(pre): rpm-build-intro
BuildRequires: rpm-build-cmake

BuildRequires: pkgconfig(Qt6Core)
BuildRequires: pkgconfig(Qt6Gui)
BuildRequires: pkgconfig(Qt6Widgets)
BuildRequires: pkgconfig(Qt6Network)
BuildRequires: pkgconfig(Qt6Concurrent)
BuildRequires: pkgconfig(Qt6Svg)
BuildRequires: pkgconfig(Qt6WebChannel)
BuildRequires: pkgconfig(Qt6WebEngineCore)
BuildRequires: pkgconfig(Qt6WebEngineWidgets)
BuildRequires: qt6-webengine-devel

# hunspell dictionaries converted to .bdic spell-check dictionaries
BuildRequires: hunspell-en_US hunspell-ru-lebedev hunspell-de hunspell-fr hunspell-es

%description
Feature rich WhatsApp Client for Desktop Linux.

%prep
%setup

%build
%cmake -DWHATSIE_BUILD_TESTS=OFF \
	-DWHATSIE_HUNSPELL_DIR=%_datadir/myspell \
	-DWHATSIE_CONVERT_DICT=%_libdir/qt6/libexec/qwebengine_convert_dict
%cmake_build

%install
%cmake_install

%files
%doc LICENSE
%doc README.md
%_bindir/whatsie
%_desktopdir/com.ktechpit.whatsie.desktop
%_iconsdir/hicolor/*/apps/com.ktechpit.whatsie*
%_metainfodir/com.ktechpit.whatsie.metainfo.xml
%dir %_datadir/whatsie
%dir %_datadir/whatsie/qtwebengine_dictionaries
%_datadir/whatsie/qtwebengine_dictionaries/*.bdic

%changelog
* Sun Oct 11 2026 Vitaly Lipatov <lav@altlinux.ru> 6.1.1-alt1
- new version 6.1.1
- migrate to Qt6 and CMake build
- build only on Qt6 WebEngine architectures

* Tue Mar 18 2025 Vitaly Lipatov <lav@altlinux.ru> 4.16.3-alt1
- initial build for ALT Sisyphus

* Fri Jan 10 2025 wally <wally> 4.16.3-1.mga10
+ Revision: 2136982
- new version 4.16.3

* Sat Aug 03 2024 daviddavid <daviddavid> 4.15.3-1.mga10
+ Revision: 2083540
- new version: 4.15.3

* Sat Dec 30 2023 daviddavid <daviddavid> 4.14.2-1.mga10
+ Revision: 2024484
- initial package whatsie (mga#32461)

