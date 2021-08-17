Name: srb2
Summary: Sonic Robo Blast 2
Version: 2.2.9
Release: alt1
License: GPL2
Group: Games/Arcade
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: SRB2-v229-Full.zip

Url: https://www.srb2.org/
BuildRequires(pre):  rpm-macros-cmake
BuildRequires: cmake gcc-c++ ImageMagick-tools
BuildRequires: hicolor-icon-theme
BuildRequires: nasm
BuildRequires: pkg-config
BuildRequires: unzip
BuildRequires: libSDL2_mixer-devel
BuildRequires: libcurl-devel
BuildRequires: libgme-devel
BuildRequires: libopenmpt-devel
BuildRequires: libpng-devel
BuildRequires: libSDL2-devel
BuildRequires: zlib-devel
BuildRequires: libupnp-devel
Requires: %name-data = %version

%description
Sonic Robo Blast 2 Kart racing game.

%package data
Summary: Sonic Robo Blast 2 Kart racing game - common files
Group: Games/Arcade
Requires: %name = %version

%description data
Common files for Sonic Robo Blast 2 Kart.

%prep
%setup -n %name-%version

mkdir -p assets/installer
unzip %SOURCE1 -d assets/installer

find . -name *.c -exec sed -i 's|%prefix/games/SRB2|%_datadir/srb2|g' {} \;

%build

mkdir BUILD
cd ./BUILD
cmake ..

%make
%install
install -D -m 0775 BUILD/bin/lsdlsrb2-* %buildroot/%_bindir/srb2
install -d %buildroot/%_datadir/srb2/
install -m 0644 assets/installer/*.{dta,pk3} %buildroot/%_datadir/srb2/

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Sonic Robo Blast 2
Comment=A free 3D Sonic the Hedgehog fangame closely inspired by the original Sonic games on the Sega Genesis.
Exec=%name
Icon=%name
Terminal=false
Type=Application
Categories=Game;ArcadeGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert ./srb2.png -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/%name.png
done

%files
%_bindir/%name
%_desktopdir/%name.desktop

%files data
%_datadir/srb2
%dir %_iconsdir/hicolor/64x64
%_iconsdir/hicolor/64x64/apps/%name.png
%dir %_iconsdir/hicolor/64x64/apps
%_iconsdir/hicolor/64x64/apps/%name.png
%dir %_iconsdir/hicolor/128x128
%_iconsdir/hicolor/128x128/apps/%name.png
%dir %_iconsdir/hicolor/128x128/apps
%_iconsdir/hicolor/128x128/apps/%name.png

%changelog
* Mon Aug 02 2021  Artyom Bystrov <arbars@altlinux.org> 2.2.9-alt1
- initial build for ALT Sisyphus
