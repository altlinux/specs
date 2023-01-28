%define version_SingleApplication v3.3.4
%define version_QTaskbarControl 2.0.2
%define version_QOnlineTranslator 1.6.1
%define version_QHotkey 1.4.2
%define version_circle_flags v2.6.1
%define version_Fluent 2022-11-30

Name: crow-translate
Version: 2.10.3
Release: alt1

Summary: A Qt GUI for Google, Yandex and Bing translators
Summary(ru_RU.UTF-8): GUI интерфейс Qt для переводчиков Google, Yandex и Bing

License: GPL-3.0-only and MIT and BSD-3-Clause
Group: System/Internationalization
Url: https://crow-translate.github.io

# Source-url: https://github.com/crow-translate/crow-translate/releases/download/%version/crow-translate-%version-source.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/itay-grudev/SingleApplication/archive/refs/tags/%version_SingleApplication.tar.gz
Source1: SingleApplication.tar

# Source2-url: https://github.com/Skycoder42/QTaskbarControl/archive/refs/tags/%version_QTaskbarControl.tar.gz
Source2: QTaskbarControl.tar

# Source3-url: https://github.com/crow-translate/QOnlineTranslator/archive/refs/tags/%version_QOnlineTranslator.tar.gz
Source3: QOnlineTranslator.tar

# Source4-url: https://github.com/Skycoder42/QHotkey/archive/refs/tags/%version_QHotkey.tar.gz
Source4: QHotkey.tar

# Source5-url: https://github.com/HatScripts/circle-flags/archive/refs/tags/%version_circle_flags.tar.gz
Source5: circle-flags.tar

# Source6-url: https://github.com/vinceliuice/Fluent-icon-theme/archive/refs/tags/%version_Fluent.tar.gz
Source6: Fluent-icon-theme.tar

Patch1: crow-2.9.1-alt-icon_theme.patch
Patch2: crow-2.10.0-alt-desktop.patch

BuildRequires: extra-cmake-modules
BuildRequires: libleptonica-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: tesseract-devel >= 4.0.0
BuildRequires: libqt5-concurrent
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libqt5-dbus

BuildRequires(pre): rpm-macros-cmake

Requires: tesseract >= 4.0.0
Requires: icon-theme-breeze
Requires: libqt5-svg

%description
A simple and lightweight translator that allows you to translate and voice text
using Google, Yandex and Bing, written in Qt5 for KDE5.
To make the application look native in DE built on GTK, you need to customize
the Qt application style with plugins like qt5ct, adwaita-qt5.
Recommended icons for the Breeze app.

%description -l ru_RU.UTF-8
Простой и легкий переводчик, позволяющий переводить и озвучивать текст с
помощью Google, Yandex и Bing, написанный на Qt5 для KDE5.
Чтобы приложение выглядело родным в DE, построенном на GTK, вам нужно настроить
стиль приложения Qt с помощью плагинов, таких как qt5ct, adwaita-qt5.
Рекомендуемые значки для приложения Breeze.

%prep
%setup
%autopatch -p2
%ifarch %e2k
# workaround of SIGILL in ecf_opt64 from LCC 1.25.23
sed -i -E "s/qOverload<([^>]*)>\(&([^:]*::)/(void(\\2*)(\\1))(\&\\2/" \
	src/mainwindow.cpp
%endif

# preparing external libraries for building
mkdir -p \
    src/qonlinetranslator/ \
    src/third-party/qhotkey/ \
    src/third-party/qtaskbarcontrol/ \
    src/third-party/singleapplication/ \
    src/circle-flags \
    src/Fluent-icon-theme

tar -xf %SOURCE1 -C src/third-party/singleapplication/ --strip-components=1
tar -xf %SOURCE2 -C src/third-party/qtaskbarcontrol/ --strip-components=1
tar -xf %SOURCE3 -C src/qonlinetranslator/ --strip-components=1
tar -xf %SOURCE4 -C src/third-party/qhotkey/ --strip-components=1
tar -xf %SOURCE5 -C src/circle-flags/ --strip-components=1
tar -xf %SOURCE6 -C src/Fluent-icon-theme/ --strip-components=1

%build
%cmake \
    -DWITH_KWAYLAND=OFF

%cmake_build

%install
%cmake_install

%files
%doc README.md COPYING
%_bindir/crow
%_desktopdir/io.crow_translate.CrowTranslate.desktop
%_datadir/Crow*/*
%_datadir/metainfo/io.crow_translate.CrowTranslate.metainfo.xml
%_iconsdir/hicolor/*/*/crow-translate*

%changelog
* Sat Jan 28 2023 Evgeny Chuck <koi@altlinux.org> 2.10.3-alt1
- new version (2.10.3) with rpmgs script
- updated library (1.6.1) QOnlineTranslator
- updated icons in flag circles (2.6.1)
- updated icons from Fluent-icon-theme (2022-11-30)

* Thu Nov 03 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 2.10.1-alt1.1
- Fixed build for Elbrus

* Tue Oct 25 2022 Evgeny Chuck <koi@altlinux.org> 2.10.1-alt1
- new version (2.10.1) with rpmgs script

* Sat Sep 17 2022 Evgeny Chuck <koi@altlinux.org> 2.10.0-alt2
- Fixed desktop category as per policy

* Tue Sep 06 2022 Evgeny Chuck <koi@altlinux.org> 2.10.0-alt1
- new version (2.10.0) with rpmgs script
- new version (1.6.0) QOnlineTranslator with rpmgs script

* Tue Aug 16 2022 Evgeny Chuck <koi@altlinux.org> 2.9.12-alt2
- Fixed display of interface icons

* Mon Aug 15 2022 Evgeny Chuck <koi@altlinux.org> 2.9.12-alt1
- new version (2.9.12) with rpmgs script

* Fri Aug 12 2022 Evgeny Chuck <koi@altlinux.org> 2.9.11-alt1
- new version (2.9.11) with rpmgs script

* Sun Aug 07 2022 Evgeny Chuck <koi@altlinux.org> 2.9.10-alt1
- new version (2.9.10) with rpmgs script
- updated SingleApplication v3.3.4
- updated circle_flags v2.5.2
- updated Fluent-icon-theme 2022-02-28

* Fri Mar 11 2022 Evgeny Chuck <koi@altlinux.org> 2.9.2-alt1
- new version (2.9.2) with rpmgs script
- updated QOnlineTranslator library version 1.5.3
- cleanup spec

* Sun Jan 09 2022 Evgeny Chuck <koi@altlinux.org> 2.9.1-alt1
- initial build for ALT Linux Sisyphus
- Fixed display of theme icons
