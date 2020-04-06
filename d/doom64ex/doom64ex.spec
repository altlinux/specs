Name: doom64ex
Version: 2.5.1
Release: alt2

Summary: Doom64EX is a project aimed to recreate Doom64 as close as possible
Summary(ru_RU.UTF-8): Doom64EX - проект, суть которого - воссоздание игры Doom64 настолько точно, насколько это возможно
License: GPLv2+
Group: Games/Arcade

Url: http://doom64ex.wordpress.com/
Source: %name-%version.tar
Source1: %name.desktop
Source2: %name.png
Source3: %name.6
Packager: Artyom Bystrov <arbars@altlinux.org>

BuildPreReq: cmake rpm-macros-cmake
BuildPreReq: libSDL2-devel libSDL2_net-devel zlib-devel libpng-devel  libfluidsynth-devel

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: libGLU-devel
BuildRequires: libSDL2_net-devel
BuildRequires: libfluidsynth
BuildRequires: libpng-devel
BuildRequires: unzip
BuildRequires: desktop-file-utils

%description
Doom 64 EX is a faithful recreation of the original game
using the Doom source code as the base with the benefit
from newer control methods like mouse look, high resolutions
and color depth. In addition to that, Doom 64 EX will also
feature mod support to allow users to create custom levels,
textures and sprites. Doom 64 EX is also aimed to be 100%% accurate
to the original game as close as possible and offer some PC-specific
features that can enhance the game.

%description -l ru_RU.UTF-8
Doom 64 EX - точное воссоздание оригинальной Doom64 на базе исходного кода
Doom с поддержкой мыши, высоких разрешений и глубины цвета. Также
Doom 64 EX позволяет создавать свои модификации с кастомными
текстурами, спрайтами и уровнями. Doom 64 EX создавался как перенос,
100%% близкий к оригиналу настолько, насколько это возможно, с включением
особенностей, свойственных ПК-играм.

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build VERBOSE=1

%install
%cmakeinstall_std
desktop-file-install --dir %buildroot%_desktopdir %SOURCE1
mkdir -p %buildroot%_iconsdir/hicolor/48x48/apps/
install -pDm644 %SOURCE2 %buildroot%_iconsdir/hicolor/48x48/apps/
install -pDm644 %SOURCE3 %buildroot%_man6dir/%name.6
install -pDm644 ./BUILD/%name.pk3 %buildroot%_gamesdatadir/%name.pk3

%files
%doc README.md AUTHORS COPYING LICENSE
%_bindir/%name
%_desktopdir/%name.desktop
%_gamesdatadir/%name.pk3
%_iconsdir/hicolor/48x48/apps/%name.png
%_man6dir/*

%changelog
* Mon Apr 06 2020 Artyom Bystrov <arbars@altlinux.org> 2.5.1-alt2
- fix missing doom64ex.pk3

* Wed Jan 29 2020 Artyom Bystrov <arbars@altlinux.org> 2.5.1-alt1
- initial build for ALT Sisyphus
