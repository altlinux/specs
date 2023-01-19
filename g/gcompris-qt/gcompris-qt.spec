Name:    gcompris-qt
Version: 3.0
Release: alt1
Summary: Educational suite for kids 2-10 years old
Summary(ru_RU.UTF8): Набор образовательных игр для детей от 2 до 10 лет

License: GPL-3.0
Group:   Games/Educational
URL:     http://www.gcompris.net

Source:  %name-%version.tar
Source1: submodules.tar

Packager: Andrey Cherepanov <cas@altlinux.org>

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt5-base-devel
BuildRequires: qt5-declarative-devel
BuildRequires: qt5-multimedia-devel
BuildRequires: qt5-sensors-devel
BuildRequires: qt5-svg-devel
BuildRequires: qt5-tools-devel
BuildRequires: qt5-xmlpatterns-devel
BuildRequires: libssl-devel
BuildRequires: kf5-kdoctools-devel
BuildRequires: kf5-kdoctools-devel-static
BuildRequires: qt5-quickcontrols2-devel
BuildRequires: qt5-charts-devel

Requires: libqt5-multimedia
Requires: libqt5-svg
Requires: qt5-graphicaleffects
Requires: qt5-quickcontrols2
Requires: libqt5-quickcontrols2
Requires: libqt5-quickparticles
Requires: chess sqlite3 gnucap tuxpaint
# needed for sound support
Requires: gst-plugins-base1.0

%description
GCompris / I Got IT is an educationnal game for children starting at 2.
More than 150 different activities are proposed:
* Click on the animals => learn the mouse/click usage
* Type the falling letters => learn the keyboard usage
* Falling Dices
* Falling words
* Basic algebra
* Time learning with an analog clock
* Puzzle game with famous paintings
* Drive Plane to catch clouds in increasing number
* Balance the scales
* And much more...

%description -l ru_RU.UTF8
GCompris - набор образовательных игр и программ для детей от двух лет
Предоставляется более 150 различных обучающих игр:
* Обучение использованию мыши
* Обучение использованию клавиатуры
* Падающие кубики
* Падающие слова
* Основы счёта
* Обучение времени
* Паззл с известными картинами
* На летящем самолёте ловить облака с возрастающими цифрами
* И многое другое...

%prep
%setup
tar xf %SOURCE1

%build
%cmake \
       -DKDE_INSTALL_APPDIR=%_desktopdir \
       -DKDE_INSTALL_METAINFODIR=%_datadir/metainfo
%cmake_build

%install
%cmakeinstall_std
%find_lang --with-qt %name

%files -f %name.lang
%doc README README.md
%_bindir/%name
%_libexecdir/qml/Box2D.2.0
%dir %_datadir/%name
%dir %_datadir/%name/translations
%_datadir/%name/rcc
%_desktopdir/*.desktop
%_datadir/metainfo/*.appdata.xml
%_iconsdir/hicolor/*/apps/%name.*

%changelog
* Thu Jan 19 2023 Andrey Cherepanov <cas@altlinux.org> 3.0-alt1
- New version.

* Thu Apr 14 2022 Andrey Cherepanov <cas@altlinux.org> 2.4-alt1
- New version.

* Mon Feb 28 2022 Andrey Cherepanov <cas@altlinux.org> 2.3-alt1
- New version.

* Thu Feb 24 2022 Andrey Cherepanov <cas@altlinux.org> 2.2-alt1
- New version.

* Sun Jan 23 2022 Andrey Cherepanov <cas@altlinux.org> 2.1-alt1
- New version.

* Sun Jan 02 2022 Andrey Cherepanov <cas@altlinux.org> 2.0-alt1
- New version.

* Mon Mar 22 2021 Andrey Cherepanov <cas@altlinux.org> 1.1-alt1
- New version.

* Fri Nov 20 2020 Andrey Cherepanov <cas@altlinux.org> 1.0-alt1
- New version.

* Mon Jun 29 2020 Andrey Cherepanov <cas@altlinux.org> 0.97.1-alt1
- New version.
- Fix License tag according to SPDX.

* Thu Dec 12 2019 Andrey Cherepanov <cas@altlinux.org> 0.97-alt1
- New version.

* Thu Apr 25 2019 Andrey Cherepanov <cas@altlinux.org> 0.96-alt2
- Add strict requirement of libqt5-svg.
- Add static library for build with old kf5-kdoctools.

* Fri Apr 05 2019 Andrey Cherepanov <cas@altlinux.org> 0.96-alt1
- Full rewrite of GCompris using the QtQuick technology.
