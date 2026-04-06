Name: crow-translate
Version: 4.0.2
Release: alt1

Summary: A Qt GUI for Google, Yandex and Bing translators
Summary(ru_RU.UTF-8): GUI интерфейс Qt для переводчиков Google, Yandex и Bing

License: GPL-3.0-only and MIT and BSD-3-Clause
Group: System/Internationalization
Url: https://invent.kde.org/office/crow-translate

Source: %name-%version.tar

Source1: breeze-icons.tar
Source2: espeak-ng.tar
Source3: qhotkey.tar
Source4: singleapplication.tar

Requires: tesseract >= 4.0.0
Requires: icon-theme-breeze
Requires: libqt6-svg

BuildRequires(pre): rpm-macros-cmake
BuildRequires: extra-cmake-modules
BuildRequires: libleptonica-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-tools-devel
BuildRequires: tesseract-devel >= 4.0.0
BuildRequires: libqt6-concurrent
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libqt6-dbus
BuildRequires: qt6-scxml-devel
BuildRequires: qt6-speech-devel
BuildRequires: plasma6-kwayland-devel
BuildRequires: libonnxruntime-devel

%description
A simple and lightweight translator that allows you to translate and voice text
using Google, Yandex and Bing, written in Qt6 for KDE6.
To make the application look native in DE built on GTK, you need to customize
the Qt application style with plugins like qt6ct, adwaita-qt6.
Recommended icons for the Breeze app.

%description -l ru_RU.UTF-8
Простой и легкий переводчик, позволяющий переводить и озвучивать текст с
помощью Google, Yandex и Bing, написанный на Qt6 для KDE6.
Чтобы приложение выглядело родным в DE, построенном на GTK, вам нужно настроить
стиль приложения Qt с помощью плагинов, таких как qt6ct, adwaita-qt6.
Рекомендуемые значки для приложения Breeze.

%prep
%setup

%ifarch %e2k
# workaround of SIGILL in ecf_opt64 from LCC 1.25.23
sed -i -E "s/qOverload<([^>]*)>\(&([^:]*::)/(void(\\2*)(\\1))(\&\\2/" \
	src/mainwindow.cpp
%endif

tar -xf %SOURCE1 -C data/icons/3rdparty/
tar -xf %SOURCE2 -C src/3rdparty/
tar -xf %SOURCE3 -C src/3rdparty/
tar -xf %SOURCE4 -C src/3rdparty/

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release
%cmake_build

%install
%cmake_install
%find_lang %name --with-qt

%files -f %name.lang
%doc *.md
%_bindir/crow
%_desktopdir/org.kde.CrowTranslate.desktop
%_datadir/crow-translate
%_datadir/metainfo/org.kde.CrowTranslate.metainfo.xml
%_iconsdir/hicolor/*/*/org.kde.CrowTranslate*

%changelog
* Mon Apr 06 2026 Aleksandr Shamaraev <shad@altlinux.org> 4.0.2-alt1
- 3.1.0 -> 4.0.2 (ALT #55988)
- build with Qt6

* Thu Jun 19 2025 Roman Alifanov <ximper@altlinux.org> 3.1.0-alt1
- new version 3.1.0 (with rpmrb script)

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
