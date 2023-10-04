%define optflags_lto %nil

Name: doom2df
Version: 0.667
Release: alt1

Summary: Doom 2D Forever: A Doom 2D remake with multiplayer
License: GPLv2+
Group: Games/Arcade

Url: https://doom2d.org


Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source2: doom2df.png
Source3: doom2df-win32.zip
Source4: d2df-res.zip

BuildRequires: unzip fpc libenet-devel libSDL2-devel libSDL2_mixer-devel libminiupnpc-devel libglvnd-devel

ExcludeArch: ppc64le armh

%description
%summary

%prep
%setup -n %name-%version

%build

mkdir stuff
unzip %SOURCE3 -d ./stuff

unzip -o %SOURCE4 -d ./stuff

cd "./src/game"
fpc -g -gl -dUSE_SDL2 -dUSE_OPENGL -dUSE_SDLMIXER -dUSE_MINIUPNPC Doom2DF.lpr

%install

install -Dm755 ./src/game/Doom2DF %buildroot%_bindir/%name

mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Version=1.0
Name=Doom 2D Forever
Exec=Doom2DF
Icon=doom2df
Terminal=false
Type=Application
Categories=Game;Shooter;ActionGame
Comment=Doom-themed platformer with network play, modern port of the 1996 Doom 2D by Prikol Software
Comment[ru]=Платформер с сетевой игрой во вселенной классического Doom, современный порт игры Doom 2D от Prikol Software
Keywords=Doom;Doom2D;Doom2D Forever;Forever;Shooter;Doom 2D;
EOF

install -Dm644 %SOURCE2 %buildroot%_iconsdir/%name.png

mkdir -p %buildroot%_datadir/%name
for stuff in ./stuff/data/ ./stuff/maps/ ./stuff/wads/; do
cp -r $stuff %buildroot%_datadir/%name
done
%files

%_bindir/%name
%_datadir/%name/*
%_desktopdir/%name.desktop
%_iconsdir/%name.png

%changelog
* Wed Oct  4 2023 Artyom Bystrov <arbars@altlinux.org> 0.667-alt1
- Initial  commit