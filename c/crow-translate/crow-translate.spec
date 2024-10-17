%define version_SingleApplication v3.5.1
%define version_QHotkey 1.5.0
%define version_Breeze 6.7.0

Name: crow-translate
Version: 3.0.0
Release: alt1

Summary: A Qt GUI for Google, Yandex and Bing translators
Summary(ru_RU.UTF-8): GUI интерфейс Qt для переводчиков Google, Yandex и Bing

License: GPL-3.0-only and MIT and BSD-3-Clause
Group: System/Internationalization
Url: https://invent.kde.org/office/crow-translate

# Source-url: https://invent.kde.org/office/crow-translate/-/archive/v%version/crow-translate-v%version.tar.gz
Source: %name-%version.tar

# Source1-url: https://github.com/itay-grudev/SingleApplication/archive/refs/tags/%version_SingleApplication.tar.gz
Source1: SingleApplication.tar

# Source2-url: https://github.com/Skycoder42/QHotkey/archive/refs/tags/%version_QHotkey.tar.gz
Source2: QHotkey.tar

# Source3-url: https://invent.kde.org/frameworks/breeze-icons/-/archive/v%version_Breeze/breeze-icons-v%version_Breeze.tar.gz
Source3: Breeze-icon-theme.tar

BuildRequires: extra-cmake-modules
BuildRequires: libleptonica-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-x11extras-devel
BuildRequires: kf5-kwayland-devel
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

%ifarch %e2k
# workaround of SIGILL in ecf_opt64 from LCC 1.25.23
sed -i -E "s/qOverload<([^>]*)>\(&([^:]*::)/(void(\\2*)(\\1))(\&\\2/" \
	src/mainwindow.cpp
%endif

tar -xf %SOURCE1 -C src/3rdparty/singleapplication/ --strip-components=1
tar -xf %SOURCE2 -C src/3rdparty/qhotkey/ --strip-components=1
tar -xf %SOURCE3 -C data/icons/3rdparty/breeze-icons --strip-components=1

# Analog of crow-2.10.0-alt-desktop.patch
subst "s|Categories=Office;Qt;|Categories=Qt;Graphics;OCR;Scanning;|" data/org.kde.CrowTranslate.desktop.in

# Fix QX11Info: No such file or directory
subst "s|<QX11Info>|<QtX11Extras/QX11Info>|" src/mainwindow.cpp
subst "s|<QX11Info>|<QtX11Extras/QX11Info>|" src/ocr/screengrabbers/abstractscreengrabber.cpp
subst "s|<QX11Info>|<QtX11Extras/QX11Info>|" src/ocr/snippingarea.cpp
subst "s|<QX11Info>|<QtX11Extras/QX11Info>|" src/xdgdesktopportal.cpp

%build
%cmake \
    -DWITH_KWAYLAND=ON

%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

%files -f %name.lang
%doc README.md
%_bindir/crow
%_desktopdir/org.kde.CrowTranslate.desktop
%_datadir/metainfo/org.kde.CrowTranslate.metainfo.xml
%_iconsdir/hicolor/*/*/org.kde.CrowTranslate*

%changelog
* Thu Oct 17 2024 Roman Alifanov <ximper@altlinux.org> 3.0.0-alt1
- new version 3.0.0 (with rpmrb script)
- remove old submodules
- change upstream

* Sun Nov 12 2023 Roman Alifanov <ximper@altlinux.org> 2.11.0-alt1
- new version (2.11.0) with rpmgs script (ALT bug 48383)
- updated libraries and icons
- added fix for error "QX11Info: there is no such file or directory"
- enabled build with kwayland
- dropped (or replaced with a subst analog) some patches

* Wed Apr 19 2023 Evgeny Chuck <koi@altlinux.org> 2.10.4-alt1
- new version (2.10.4) with rpmgs script

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
