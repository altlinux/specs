Name:    gcompris-qt
Version: 25.0
Release: alt1
Summary: Educational suite for kids 2-10 years old
Summary(ru_RU.UTF8): Набор образовательных игр для детей от 2 до 10 лет

License: GPL-3.0
Group:   Games/Educational
URL:     http://www.gcompris.net

Source:  %name-%version.tar
Source1: submodules.tar
Source2: gcompris_qt.po
Source3: gcompris_voices.po

Patch0: gcompris-qt-box2d-disable-stripping.patch

BuildRequires(pre): cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: gcc-c++
BuildRequires: extra-cmake-modules
BuildRequires: qt6-base-devel
BuildRequires: qt6-declarative-devel
BuildRequires: qt6-multimedia-devel
BuildRequires: qt6-sensors-devel
BuildRequires: qt6-svg-devel
BuildRequires: qt6-tools-devel
BuildRequires: libssl-devel
#BuildRequires: kf6-kdoctools-devel
#BuildRequires: kf6-kdoctools-devel-static
BuildRequires: qt6-charts-devel
BuildRequires: qt6-wayland-devel
BuildRequires: libvulkan-devel
BuildRequires: chrpath

Requires: libqt6-multimedia
Requires: libqt6-svg
Requires: libqt6-quickcontrols2
Requires: libqt6-quickparticles
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
%patch0 -p1
install -Dpm0644 %SOURCE2 poqm/ru/gcompris_qt.po
install -Dpm0644 %SOURCE3 po/ru/gcompris_voices.po
# Remove geography activity due to non actial maps
subst '/geography/d' src/activities/activities.txt

%build
export LANG=en_US.UTF-8
%cmake -GNinja \
       -DKDE_INSTALL_APPDIR=%_desktopdir \
       -DKDE_INSTALL_METAINFODIR=%_datadir/metainfo
%ninja_build -C "%_cmake__builddir"

%install
export LANG=en_US.UTF-8
%ninja_install -C "%_cmake__builddir"
chrpath -d %buildroot%_libexecdir/qml/Box2D.2.0/libqmlbox2d.so
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
* Tue Feb 04 2025 Andrey Cherepanov <cas@altlinux.org> 25.0-alt1
- New version.
- Built with Qt6.

* Fri Nov 29 2024 Andrey Cherepanov <cas@altlinux.org> 4.3-alt1
- New version.

* Fri Nov 01 2024 Andrey Cherepanov <cas@altlinux.org> 4.2-alt2
- Removed geography activity due to non actial maps.

* Fri Sep 20 2024 Andrey Cherepanov <cas@altlinux.org> 4.2-alt1
- New version.

* Thu May 23 2024 Andrey Cherepanov <cas@altlinux.org> 4.1-alt1
- New version.

* Fri Mar 15 2024 Andrey Cherepanov <cas@altlinux.org> 4.0-alt1
- New version.
- Completed Russian translation (thanks Olesya Gerasimenko).

* Thu Jun 08 2023 Andrey Cherepanov <cas@altlinux.org> 3.3-alt1
- New version.

* Mon Apr 10 2023 Andrey Cherepanov <cas@altlinux.org> 3.2-alt1
- New version.

* Sat Jan 21 2023 Andrey Cherepanov <cas@altlinux.org> 3.1-alt1
- New version.

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
