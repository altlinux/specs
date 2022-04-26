%define _unpackaged_files_terminate_build 1

Name: mos-icons
Summary: Icons for M OS distros
Summary(ru): Иконки для дистрибутивов М ОС
License: CC-BY-SA-3.0 and GPL-3.0
Group: Graphics
Version: 2.1
Release: alt1
Source0: icons-mos-classic-%version.tar
Source1: icon-theme-mos-classic-%version.tar
Source3: COPYING
BuildArch: noarch
# mk-symlinks.sh
BuildRequires: bash

%description
Icons for M OS distros
%description -l ru_RU.UTF-8
Иконки для дистрибутивов М ОС

#---------------------------------------------------------

%package core-classic
Summary: Core icons of M OS, classic variant
Summary(ru): Основные иконки М ОС, классический вариант
License: CC-BY-SA-3.0
Group: Graphics
# package was renamed
Obsoletes: kometa-icons-core-classic < 2.0

%description core-classic
Core icons of M OS, classic variant
%description core-classic -l ru_RU.UTF-8
Основные иконки М ОС, классический вариант

%files core-classic
%doc COPYING
%_iconsdir/hicolor/*x*/apps/mos.png
%_iconsdir/hicolor/*x*/apps/mos.svg
%_iconsdir/hicolor/scalable/apps/mos.svg

#---------------------------------------------------------

%package theme-classic
Summary: M OS icon themes, classic variant
Summary(ru): Темы иконок М ОС, классический вариант
License: GPL-3.0
Group: Graphics
Requires: %name-core-classic = %EVR
Requires: icon-theme-breeze
# package was renamed
Obsoletes: kometa-icons-theme-classic < 2.0

%description theme-classic
Light and dark M OS icon themes. Inherit Breeze and
replace some icons.
%description theme-classic -l ru_RU.UTF-8
Светлая и темные темы значков для М ОС. Наследуют
тему Breeze, заменяя некоторые иконки.

%files theme-classic
%doc COPYING
%_iconsdir/mos-classic-light
%_iconsdir/mos-classic-dark

#---------------------------------------------------------

%prep
%setup -q -c -a1
cp %{SOURCE3} .

%build

%install

# core
mkdir -p %buildroot%_iconsdir/hicolor
cp -rv icons-mos-classic-%version/* %buildroot%_iconsdir/hicolor
# ensure correct modes
find %buildroot%_iconsdir -type f | xargs chmod 0644
find %buildroot%_iconsdir -type d | xargs chmod 0755

# themes
mkdir -p %buildroot%_iconsdir/mos-classic-light
mkdir -p %buildroot%_iconsdir/mos-classic-dark
sed icon-theme-mos-classic-%version/index.theme -e '/^@dark /d' -e 's/^@light //' > %buildroot%_iconsdir/mos-classic-light/index.theme
sed icon-theme-mos-classic-%version/index.theme -e '/^@light /d' -e 's/^@dark //' > %buildroot%_iconsdir/mos-classic-dark/index.theme
export SCRIPT="$PWD"/icon-theme-mos-classic-%version/mk-symlinks.sh
export PREFIX="../../.."
( cd %buildroot%_iconsdir/mos-classic-light
  bash "$SCRIPT"
)
( cd %buildroot%_iconsdir/mos-classic-dark
  bash "$SCRIPT"
)

%changelog
* Tue Apr 26 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.1-alt1
- Add 22x22 (fix typo in index.theme)

* Tue Apr 26 2022 Mikhail Novosyolov <mikhailnov@altlinux.org> 2.0-alt1
- Rename from Kometa to M OS (Moscow OS)
- Added SVG icons of different sizes alongside PNG

* Mon Dec 13 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt1
- Init

