Name: whatsie
Version: 4.16.3
Release: alt1

Summary: Feature rich WhatsApp Client for Desktop Linux

License: MIT
Group: Networking/Chat
Url: https://github.com/keshavbhatt/whatsie

# Source-url: https://github.com/keshavbhatt/whatsie/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-qt5
BuildRequires(pre):rpm-build-intro

BuildRequires: pkgconfig(Qt5Core)
BuildRequires: pkgconfig(Qt5Help)
BuildRequires: pkgconfig(Qt5Location)
BuildRequires: pkgconfig(Qt5Positioning)
BuildRequires: pkgconfig(Qt5PositioningQuick)
BuildRequires: pkgconfig(Qt5Qml)
BuildRequires: pkgconfig(Qt5Quick)
BuildRequires: pkgconfig(Qt5QuickTest)
BuildRequires: pkgconfig(Qt5QuickWidgets)
BuildRequires: pkgconfig(Qt5WebChannel)
BuildRequires: pkgconfig(Qt5WebEngine)
BuildRequires: pkgconfig(Qt5WebEngineCore)
BuildRequires: pkgconfig(Qt5WebEngineWidgets)

%description
Feature rich WhatsApp Client for Desktop Linux.

%prep
%setup

%build
%qmake_qt5 src
%make_build

%install
make install INSTALL_ROOT=%buildroot
rm -v %buildroot/usr/share/licenses/whatsie/LICENSE

%files
%doc LICENSE
%doc CHANGELOG.md README.md
%_bindir/whatsie
%_desktopdir/com.ktechpit.whatsie.desktop
%_iconsdir/hicolor/*/apps/com.ktechpit.whatsie.png
%_iconsdir/hicolor/scalable/apps/com.ktechpit.whatsie.svg
%_iconsdir/hicolor/symbolic/apps/com.ktechpit.whatsie-symbolic.svg
%_metainfodir/com.ktechpit.whatsie.appdata.xml
%dir %_datadir/org.keshavnrj.ubuntu
%dir %_datadir/org.keshavnrj.ubuntu/WhatSie/
%dir %_datadir/org.keshavnrj.ubuntu/WhatSie/qtwebengine_dictionaries
%_datadir/org.keshavnrj.ubuntu/WhatSie/qtwebengine_dictionaries/*.bdic

%changelog
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

