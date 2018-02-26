Name:		jvgs
Version:	0.5
Release:	alt2
Summary:	Minimalistic platform game with xkc-like graphics
Group:		Games/Arcade
License:	GPL
Source:		%name-%version-src.tar.gz
Requires:	%name-data
URL:		http://jvgs.sourceforge.net/

# Automatically added by buildreq on Mon Mar 14 2011
BuildRequires: ImageMagick-tools cmake gcc-c++ libSDL_mixer-devel libXScrnSaver-devel libXcomposite-devel libXcursor-devel libXdmcp-devel libXft-devel libXinerama-devel libXpm-devel libXrandr-devel libXt-devel libXtst-devel libXv-devel liblua5-devel libxkbfile-devel swig zlib-devel

%description
JVGS is a free, minimalistic platform game that runs on windows, mac, linux and
most other obscure systems out there. Some elements are loosely based on xkcd.
The Ghosts album by Nine Inch Nails was chosen as soundtrack (install it from
separate package %name-music).

This game takes place in a world much like ours, which has started fading away.
At a point where nearly everything has gone, a poet finds himself, alone in a
strange world of danger. He starts a journey along the broken stream of
thoughts that's left.

%package data
License:	Public domain
Summary:	Game data for %name (except music)
Group:		Games/Arcade

%description data
%summary

%package music
License:	CC-NC-SA
Summary:	Sountrack for %name game, derived from "The Ghosts" album by Nine Inch Nails
Group:		Sound

%description music
%summary

%prep
%setup -n %name-%version-src

%build
cmake -DCMAKE_INSTALL_PREFIX:PATH=%_prefix -DCMAKE_SKIP_RPATH:BOOL=YES .
%make_build

for D in %_iconsdir/hicolor/*[0-9]x[0-9]*; do
  S=`basename $D`
  convert resources/player/walking-01.svg -resize $S $S.png
done

cat > %name.sh << @@@
#!/bin/sh
cd %_gamesdatadir/%name
%_gamesbindir/%name.bin main.lua "$@"
@@@

cat > %name.desktop << @@@
[Desktop Entry]
Type=Application
Comment=Jasper Van der Jeugt platform game
Terminal=false
Exec=%name
Icon=%name
Name=JVGS
Categories=Game;ArcadeGame;
@@@

%install
install -D src/%name %buildroot%_gamesbindir/%name.bin
install -D -m755 %name.sh %buildroot%_gamesbindir/%name
install -D main.lua %buildroot%_gamesdatadir/%name/main.lua
install -D data.xml %buildroot%_gamesdatadir/%name/data.xml
cp -a resources %buildroot%_gamesdatadir/%name
for D in %_iconsdir/hicolor/*[0-9]x[0-9]*; do
  S=`basename $D`
  install -D $S.png %buildroot$D/apps/%name.png
done
install -D resources/player/walking-01.svg %buildroot%_iconsdir/hicolor/scalable/apps/%name.svg
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%doc README.markdown AUTHORS util
%_gamesbindir/%{name}*
%_iconsdir/hicolor/*/apps/*
%_desktopdir/*

%files data
%_gamesdatadir/%name
%exclude %_gamesdatadir/%name/resources/music/*

%files music
%_gamesdatadir/%name/resources/music/*

%changelog
* Mon Mar 14 2011 Fr. Br. George <george@altlinux.ru> 0.5-alt2
- Buildreq regenerated

* Fri Feb 19 2010 Fr. Br. George <george@altlinux.ru> 0.5-alt1
- Initial build from scratch
- Desktop and icons generated
