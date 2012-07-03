Name:		Primrose
Version:	6
Release:	alt2
Group:		Games/Puzzles
License:	public domain
Source:		%{name}_v%{version}_UnixSource.tar.gz
Source1:	%name.desktop
URL:		http://primrose.sourceforge.net
Summary:	A captivating tile-clearing puzzle game
Packager:	Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sat Mar 07 2009
BuildRequires: ImageMagick-tools gcc-c++ libGL-devel libSDL-devel libX11-devel

%description
You're given random pairs of colored tiles that you must place on a 7x7 grid. When you surround a group of one color with another color, the surrounded group clears, scoring points. The surrounding tiles flip to the color of the tiles that were cleared. When tiles flip color, chain reactions are possible. Larger groups and longer chain reactions are awarded more points.

As the game progresses, more colors are added to the pool, making the grid more and more constrained. Pressure builds until the grid finally fills up, and the game ends.

%prep
%setup -n %{name}_v%{version}_UnixSource

cat > %name.sh <<@@@
#!/bin/sh
PDir="\$HOME/.%name"
test -d "\$PDir" || { mkdir -p "\$PDir"; ln -s %_gamesdatadir/%name/* "\$PDir"/; }

mkdir -p "\$PDir/settings"
cd "\$PDir"
%_gamesbindir/%name.bin
@@@

%build
cd tilePlacementGames/game1
echo 1 | sh configure
cd gameSource
%make_build

convert iPhone/icon.png  -background transparent -extent 64x64-3-3 ../../../%name-64x64.png
convert iPhone/icon.png -resize 48x48 ../../../%name-48x48.png
convert iPhone/icon.png -resize 32x32 ../../../%name-32x32.png
convert iPhone/icon.png -resize 16x16 ../../../%name-16x16.png

%install
mkdir -p %buildroot%_gamesdatadir/%name/graphics
install -s -D tilePlacementGames/game1/gameSource/%name %buildroot%_gamesbindir/%name.bin
install -m755 -D %name.sh %buildroot%_gamesbindir/%name
install tilePlacementGames/game1/gameSource/graphics/* %buildroot%_gamesdatadir/%name/graphics/
install -D %name-16x16.png %buildroot%_miconsdir/%name.png
install -D %name-32x32.png %buildroot%_niconsdir/%name.png
install -D %name-48x48.png %buildroot%_liconsdir/%name.png
install -D %name-64x64.png %buildroot%_iconsdir/hicolor/64x64/apps/%name.png
install -D %SOURCE1 %buildroot%_desktopdir/%name.desktop
%files
%doc tilePlacementGames/game1/documentation/Readme.txt tilePlacementGames/game1/gameSource/iPhone/storeDescription.txt
%_gamesbindir/%{name}*
%dir %_gamesdatadir/%name
%_gamesdatadir/%name/*
%_iconsdir/hicolor/*/apps/%name.png
%_desktopdir/%name.desktop


%changelog
* Tue May 11 2010 Fr. Br. George <george@altlinux.ru> 6-alt2
- Fix repocop warnings

* Sun Feb 07 2010 Fr. Br. George <george@altlinux.ru> 6-alt1
- Version up

* Sat Mar 07 2009 Fr. Br. George <george@altlinux.ru> 3-alt1
- Initial build from scratch

