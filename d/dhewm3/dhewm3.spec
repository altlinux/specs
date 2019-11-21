Name: dhewm3
Version: 1.5.0
Release: alt1
Summary: DOOM 3 source port
Summary(ru_RU.UTF-8): Порт движка оригинального Doom 3
License: GPL-3.0-only
Group: Games/Arcade
Url: https://github.com/dhewm/dhewm3
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar.gz
Source1: %name.png

BuildRequires(pre): rpm-macros-cmake ImageMagick-tools

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: pkg-config
BuildRequires: libSDL2-devel
BuildRequires: libcurl-devel
BuildRequires: libjpeg-devel
BuildRequires: libogg-devel
BuildRequires: libopenal-devel
BuildRequires: libvorbis-devel
BuildRequires: zlib-devel

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
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=dhewm3
Comment=DOOM 3 source port
Comment [ru]=порт движка DOOM 3
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE1 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%doc README.md COPYING.txt
%_gamesbindir/%name
%_gamesdatadir/%name
%_libdir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Fri Nov 15 2019 Artyom Bystrov <arbars@altlinux.org> 1.5.0-alt1
- initial build for ALT Sisyphus

