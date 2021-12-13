%define _unpackaged_files_terminate_build 1

Name: kometa-icons
Summary: Icons for Kometa distros
Summary(ru): Иконки для дистрибутивов Комета
License: CC-BY-SA-3.0 and GPL-3.0
Group: Graphics
Version: 1.0
Release: alt1
Source0: icons-kometa-classic-%version.tar
Source1: icon-theme-kometa-classic-%version.tar
Source3: COPYING
BuildArch: noarch
# mk-symlinks.sh
BuildRequires: bash

%description
Icons for Kometa distros
%description -l ru_RU.UTF-8
Иконки для дистрибутивов Комета

#---------------------------------------------------------

%package core-classic
Summary: Core icons of Kometa, classic variant
Summary(ru): Основные иконки Кометы, классический вариант
License: CC-BY-SA-3.0
Group: Graphics

%description core-classic
Core icons of Kometa, classic variant
%description core-classic -l ru_RU.UTF-8
Основные иконки Кометы, классический вариант

%files core-classic
%doc COPYING
%_iconsdir/hicolor/*x*/apps/kometa.png
%_iconsdir/hicolor/scalable/apps/kometa.svg

#---------------------------------------------------------

%package theme-classic
Summary: Kometa icon themes, classic variant
Summary(ru): Темы иконок Кометы, классический вариант
License: GPL-3.0
Group: Graphics
Requires: %name-core-classic = %EVR
Requires: icon-theme-breeze

%description theme-classic
Light and dark Kometa icon themes. Inherit Breeze and
replace some icons.
%description theme-classic -l ru_RU.UTF-8
Светлая и темные темы значков для Кометы. Наследуют
тему Breeze, заменяя некоторые иконки.

%files theme-classic
%doc COPYING
%_iconsdir/kometa-classic-light
%_iconsdir/kometa-classic-dark

#---------------------------------------------------------

%prep
%setup -q -c -a1
cp %{SOURCE3} .

%build

%install

# core
mkdir -p %buildroot%_iconsdir/hicolor
cp -rv icons-kometa-classic-%version/* %buildroot%_iconsdir/hicolor
# ensure correct modes
find %buildroot%_iconsdir -type f | xargs chmod 0644
find %buildroot%_iconsdir -type d | xargs chmod 0755

# themes
mkdir -p %buildroot%_iconsdir/kometa-classic-light
mkdir -p %buildroot%_iconsdir/kometa-classic-dark
sed icon-theme-kometa-classic-%version/index.theme -e '/^@dark /d' -e 's/^@light //' > %buildroot%_iconsdir/kometa-classic-light/index.theme
sed icon-theme-kometa-classic-%version/index.theme -e '/^@light /d' -e 's/^@dark //' > %buildroot%_iconsdir/kometa-classic-dark/index.theme
export SCRIPT="$PWD"/icon-theme-kometa-classic-%version/mk-symlinks.sh
export PREFIX="../../.."
( cd %buildroot%_iconsdir/kometa-classic-light
  bash "$SCRIPT"
)
( cd %buildroot%_iconsdir/kometa-classic-dark
  bash "$SCRIPT"
)

%changelog
* Mon Dec 13 2021 Mikhail Novosyolov <mikhailnov@altlinux.org> 1.0-alt1
- Init

