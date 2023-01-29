Name: srb2kart
Summary: Sonic Robo Blast 2 Kart racing game
Version: 1.6
Release: alt1
License: GPL2
Group: Games/Arcade
Packager:  Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
Source1: srb2kart-v16-Installer.exe
Url: https://www.srb2.org/
BuildRequires: cmake gcc-c++ rpm-macros-cmake nasm ImageMagick
BuildRequires: libupnp-devel libgme-devel
BuildRequires: libSDL2-devel libSDL2_mixer-devel
BuildRequires: zlib-devel libpng-devel libcurl-devel
BuildRequires: unrar
Requires:      %name-data = %version

%description
Sonic Robo Blast 2 Kart racing game.

%package data
Summary: Sonic Robo Blast 2 Kart racing game - common files
Group: Games/Arcade
Requires:      %name = %version

%description data
Common files for Sonic Robo Blast 2 Kart.

%prep
%setup -n %name-%version

unrar x %{SOURCE1} ./assets/installer/
find . -name *.c -exec sed -i 's|%{_prefix}/games/SRB2Kart|%{_datadir}/srb2kart|g' {} \;
%build

%cmake

%cmake_build
%install
mkdir -p %{buildroot}%_licensedir

install -D -m 0775 %_cmake__builddir/bin/srb2kart %{buildroot}/%{_bindir}/srb2kart
install -d %{buildroot}/%{_datadir}/srb2kart/
install -m 0644 assets/installer/*.{kart,srb} %{buildroot}/%{_datadir}/srb2kart/

# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name.desktop << EOF
[Desktop Entry]
Name=Sonic Robo Blast 2 Kart
Comment=Sonic Robo Blast 2 Kart racing game
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
%doc LICENSE README.md
%_bindir/%name
%_desktopdir/%name.desktop

%files data
%_datadir/%name
%_iconsdir/hicolor/*/apps/%name.png

%changelog
* Sun Jan 29 2023 Artyom Bystrov <arbars@altlinux.org> 1.6-alt1
- initial build for ALT Sisyphus
