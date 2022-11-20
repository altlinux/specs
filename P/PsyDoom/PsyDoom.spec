%define optflags_lto %nil

Name: PsyDoom
Version: 1.0.1
Release: alt1

Summary: Port Doom from PSOne to PC
License: GPLv2+
Group: Games/Arcade

Url: https://github.com/BodbDearg/PsyDoom

Packager: Artyom Bystrov <arbars@altlinux.org>

ExcludeArch: %ix86 armh

Source: %name-%version.tar
Source2: PsyDoom.png

BuildRequires: cmake gcc-c++ rpm-macros-cmake libspirv-tools-devel bzip2
BuildRequires: libSDL2-devel libSDL2_mixer-devel libsdl2_sound-devel libpulseaudio-devel libXcursor-devel zlib-devel libgme-devel libpng-devel
BuildRequires: libfreetype-devel libXft-devel libfltk-devel libsndfile-devel libvpx-devel ImageMagick-tools
BuildRequires: libXfixes-devel libX11-devel libXext-devel libXi-devel libXrandr-devel
BuildRequires: libXinerama-devel libstdc++-devel-static libXxf86vm-devel

%description
Port Doom from PSOne to PC

%prep
%setup -n %name-%version

%build
%cmake
%cmake_build

%install

mkdir -p %buildroot%_bindir
install -m 0755 ./%_arch-alt-linux/game/PsyDoom -t %buildroot%_bindir/

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=PsyDoom
Comment=Port Doom from PSOne to PC
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert %SOURCE2 -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files

%_bindir/%name
%_desktopdir/%name.desktop
%_iconsdir/hicolor/*/apps/%name.png

%changelog

* Sun Nov 20 2022 Artyom Bystrov <arbars@altlinux.org> 1.0.1-alt1
- initial build for ALT Sisyphus
