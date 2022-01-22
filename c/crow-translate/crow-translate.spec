%define version_SingleApplication v3.3.2
%define version_QTaskbarControl 2.0.2
%define version_QOnlineTranslator 1.5.2
%define version_QHotkey 1.4.2
%define version_circle_flags v2.3.0
%define version_Fluent 2021-12-20

Name: crow-translate
Version: 2.9.1
Release: alt1

Summary: A Qt GUI for Google, Yandex and Bing translators
Summary(ru_RU.UTF-8): Графический интерфейс Qt для переводчиков Google, Yandex и Bing

License: GPL-3.0-only and MIT and BSD-3-Clause
Group: System/Internationalization
Url: https://crow-translate.github.io
Packager: Evgeny Chuck <koi at altlinux.org>

Source: %name-%version.tar
# Source-url: https://github.com/crow-translate/crow-translate/archive/refs/tags/%version.tar.gz
Source1: SingleApplication.tar
# Source1-url: https://github.com/itay-grudev/SingleApplication/archive/refs/tags/%version_SingleApplication.tar.gz
Source2: QTaskbarControl.tar
# Source2-url: https://github.com/Skycoder42/QTaskbarControl/archive/refs/tags/%version_QTaskbarControl.tar.gz
Source3: QOnlineTranslator.tar
# Source3-url: https://github.com/crow-translate/QOnlineTranslator/archive/refs/tags/%version_QOnlineTranslator.tar.gz
Source4: QHotkey.tar
# Source4-url: https://github.com/Skycoder42/QHotkey/archive/refs/tags/%version_QHotkey.tar.gz
Source5: circle-flags.tar
# Source5-url: https://github.com/HatScripts/circle-flags/archive/refs/tags/%version_circle_flags.tar.gz
Source6: Fluent-icon-theme.tar
# Source6-url: https://github.com/vinceliuice/Fluent-icon-theme/archive/refs/tags/%version_Fluent.tar.gz

Patch: crow-2.9.1-alt-fetchcontent.patch
Patch1: crow-2.9.1-alt-icon_theme.patch

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
%cmake
%cmake_build

%install
%cmake_install

%files
%doc README.md COPYING
%_bindir/crow
%_desktopdir/io.crow_translate.CrowTranslate.desktop
%_datadir/Crow*/*
%_iconsdir/hicolor/*/*/crow-translate*

%changelog
* Sun Jan 09 2022 Evgeny Chuck <koi@altlinux.org> 2.9.1-alt1
- initial build for ALT Linux Sisyphus
- Fixed display of theme icons
