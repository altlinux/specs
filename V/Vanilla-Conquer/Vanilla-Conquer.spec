Name: Vanilla-Conquer
Version: 06032023
Release: alt1
Summary: Game Engine for the 1st generation Command and Conquer games
License: GPL-3.0-or-later
Group: Games/Strategy
Url: https://github.com/TheAssemblyArmada/Vanilla-Conquer
Packager: Artyom Bystrov <arbars@altlinux.org>

Source: %name-%version.tar
BuildRequires: ImageMagick-tools
BuildRequires: cmake
BuildRequires: pkg-config
BuildRequires: gcc-c++
BuildRequires: git-core
BuildRequires: libopenal-devel
BuildRequires: libSDL2-devel

%description
Vanilla Conquer is a fully portable version of the first generation
C&C engine and is capable of running both Tiberian Dawn and Red Alert
on multiple platforms. It can also be used for mod development for
the Remastered Collection.

The main focus of Vanilla Conquer is to keep the default out-of-box
experience faithful to what the games were back when they were
released and work as a drop-in replacement for the original
executables while also providing bug fixes, compatiblity and quality
of life improvements.

Note: This package only includes the binary files.
You still need the data files from the original C&C games to play
the game.

%prep
%setup

%build
%cmake
%cmake_build

%install
install -d %{buildroot}%{_bindir}
install -m 0755 ./%_cmake__builddir/vanillara %{buildroot}%{_bindir}/
install -m 0755 ./%_cmake__builddir/vanillatd %{buildroot}%{_bindir}/
# install menu entry
mkdir -p %buildroot%_desktopdir
cat > %buildroot%_desktopdir/%name-ra.desktop << EOF
[Desktop Entry]
Name=Vanilla Conquer - Red Alert
Comment=Vanilla Conquer - Red Alert
Exec=vanillara
Icon=vanillara_icon
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

cat > %buildroot%_desktopdir/%name-td.desktop << EOF
[Desktop Entry]
Name=Vanilla Conquer - Tiberium Dawn
Comment=Enhanced Doom engine
Exec=vanillatd
Icon=vanillatd_icon
Terminal=false
Type=Application
Categories=Game;StrategyGame;
EOF

# install menu icons
for N in 16 32 48 64 128;
do
convert resources/vanillara_icon.svg -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/vanillara_icon.png
done

for N in 16 32 48 64 128;
do
convert resources/vanillatd_icon.svg -scale ${N}x${N} $N.png;
install -D -m 0644 $N.png %buildroot%_iconsdir/hicolor/${N}x${N}/apps/vanillatd_icon.png
done

%files
%doc README.md License.txt
%_bindir/vanillara
%_bindir/vanillatd
%_iconsdir/hicolor/*/apps/vanillara_icon.png
%_iconsdir/hicolor/*/apps/vanillatd_icon.png
%_desktopdir/*.desktop

%changelog
* Mon May 15 2023 Artyom Bystrov <arbars@altlinux.org> 06032023-alt1
- initial build for ALT Sisyphus

* Sun Mar 28 2021 Martin Hauke <mardnh@gmx.de>
- Initial package, version 0~git20200924
