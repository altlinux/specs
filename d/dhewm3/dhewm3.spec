%define git %nil

Name: dhewm3
Version: 1.5.4
Release: alt1
Summary: DOOM 3 source port
Summary(ru_RU.UTF-8): Порт движка оригинального Doom 3
License: GPL-3.0-only
Group: Games/Arcade
Url: https://github.com/dhewm/dhewm3
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-macros-cmake ImageMagick-tools

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libSDL2-devel
BuildRequires: libcurl-devel
BuildRequires: libopenal-devel
BuildRequires: zlib-devel
BuildRequires: libbacktrace-devel

%description
dhewm3 is a DOOM 3 GPL source port.
Unlike the original DOOM 3, dhewm3 uses:

- SDL for low level OS support, OpenGL and input handling
- OpenAL for audio output, all OS specific audio backends are gone
- OpenAL EFX for EAX reverb effects
- Better support for widescreen (and arbitrary display resolutions)

WARNING! Playing Doom 3 still requires a legitimate copy of
the game. You can purchase a copy from Steam or your favorite retailer.

Place "base" folder from the Doom 3 installation to:
%_gamesdatadir/%name/
or
$HOME/.dhewm3/

%description -l ru_RU.UTF-8
dhewm3 - это порт движка DOOM 3, открытого под GPL.
В отличие от оригинального DOOM 3, dhewm3 использует:

- SDL для низкоуровневой поддержки в ОС, OpenGL и обработки звука
- OpenAL для вывода звука, все ОС-специфичные бэкенды убраны
- OpenAL EFX для поддержки отражений EAX
- Улучшена поддержка широкоформатных дисплеев (и произвольных разрешений экрана)

ВНИМАНИЕ! Для игры необходимо наличие файлов с данными игры,
которые можно добыть, например, из копии в Steam.

Положите каталог "base" по следующуему пути:
%_gamesdatadir/%name/
или
$HOME/.dhewm3/

%prep
%setup

%build
cd neo
%cmake_insource

%make_build

%install
mkdir -p %buildroot%_gamesbindir/
mkdir -p %buildroot%_gamesdatadir/%name
mkdir -p %buildroot%_libdir/%name
install -m 0755 ./neo/%name %buildroot%_gamesbindir/%name
install -m 0664 ./neo/*.so %buildroot%_libdir/%name

# install menu entry
mkdir -p %buildroot%_desktopdir
install -m 0644 dist/linux/share/applications/*.desktop %buildroot%_desktopdir/

# install menu icons
for N in 128 256;
do
mkdir -p %buildroot%_iconsdir/hicolor/${N}x${N}/apps
install -m 0644 dist/linux/share/icons/hicolor/${N}x${N}/apps/*.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/
done
mkdir -p %buildroot%_iconsdir/hicolor/scalable/apps
install -m 0644 dist/linux/share/icons/hicolor/scalable/apps/*.svg %buildroot%_iconsdir/hicolor/scalable/apps/

%files
%doc COPYING.txt
%_gamesbindir/%name
%_gamesdatadir/%name
%_libdir/%name
%_desktopdir/*.desktop
%_iconsdir/hicolor/*/apps/*.png
%_iconsdir/hicolor/*/apps/*.svg

%changelog
* Mon Sep  2 2024 Artyom Bystrov <arbars@altlinux.org> 1.5.4-alt1
 - Update to new version

* Tue Jul 16 2024 Artyom Bystrov <arbars@altlinux.org> 1.5.3-alt1
 - Update to new version

* Tue Aug 16 2022 L.A. Kostis <lakostis@altlinux.ru> 1.5.2-alt1
- 1.5.2.

* Sun Mar 27 2022 L.A. Kostis <lakostis@altlinux.ru> 1.5.1-alt2.gadad73c
- GIT adad73c.

* Mon Jun 07 2021 L.A. Kostis <lakostis@altlinux.ru> 1.5.1-alt1.g1aedbe7
- NMU update:
  + GIT 1aedbe7.
  + add libbacktrace support.

* Fri Nov 15 2019 Artyom Bystrov <arbars@altlinux.org> 1.5.0-alt1
- initial build for ALT Sisyphus
