Name: wrath
Version: rev20140513
Release: alt1

Summary: Fork of DarkPlaces Quake engine for WRATH: Aeon of Ruin
License: GPL
Group: Games/Arcade
Url: https://github.com/KillPixelGames/wrath-darkplaces

Packager: %packager
Source: %name-%version.tar
Source1: run_wrath.sh

ExclusiveArch: x86_64 %ix86 %e2k

BuildRequires: gcc-c++ make libSDL2-devel libsdl2_sound-devel libXext-devel libXpm-devel libXxf86vm-devel libalsa-devel libjpeg-devel zlib-devel

%description

Fork of LordHavoc's DarkPlaces Quake engine that is used in the game WRATH: Aeon of Ruin.

%description -l ru_RU.UTF-8
Modification of the darkplaces engine for the commercial
game WRATH: Aeon of Ruin.

This package only contains the core engine files but not any data
files required to play the game. For playing, copy the kp1 folder from game distribution
to /home/<username>/.config/wrath


Also let it be known that due to some changes it might be that other
games such as Quake and any of it's mission packs might not run
with this version of the engine.

%prep
%setup -q

%build

%make sdl2-release

%install
mkdir -p %buildroot/%_bindir/
mkdir -p %buildroot/%_iconsdir/
mv darkplaces-sdl %name
install -pm755 %name  %buildroot/%_bindir/wrath_bin
install -pm755 %SOURCE1  %buildroot/%_bindir/%name
chmod +x %buildroot%_bindir/%name

install -D -m 0644 darkplaces.ico %buildroot%_datadir/pixmaps/%name.png

%define docdir %_docdir/%name-%version
mkdir -p %buildroot%docdir

install -pm644 COPYING %buildroot%docdir/

mkdir -p %buildroot%_desktopdir
cat << EOF > %buildroot%_desktopdir/%name.desktop
[Desktop Entry]
Type=Application
Name=WRATH: Aeon of Ruin
Comment=%{summary}
Exec=wrath
Icon=%{name}.png
Categories=Game;ArcadeGames;
EOF

%files
%_bindir/wrath_bin
%_bindir/%name
%_datadir/pixmaps/%name.png
%_desktopdir/%name.desktop
%dir %docdir
%docdir/COPYING

%changelog
* Tue May 9 2023 Artyom Bystrov <arbars@altlinux.org> rev20140513-alt1
- Initial release for Sisyphus.

