Name:		lemmings-pp
Version:	20100311
Release:	alt2
Group:		Games/Puzzles
License:	public domain
Summary:	Lemmings variant featuring singleplayer and networked multiplayer
Source:		http://members.allegro.cc/simon/src.tar.gz
Patch:		lpp-FA_RDONLY.patch
URL:		http://lplusplus.co.cc
Packager:	Fr. Br. George <george@altlinux.ru>

# Automatically added by buildreq on Sun Apr 04 2010
BuildRequires: ImageMagick-tools gcc-c++ liballegro-devel libenet-devel

Requires:	%name-data = %version

%description
L++ is a single- and multiplayer Lemmings variant. It provides a networking mode for up to eight players. This allows a Lemmings experience like Amiga Lemmings or SNES Lemmings provided in the days back then.

The game sports these features:

    * Networking mode with more players and more levels than on the Amiga or SNES.
    * More lemming skills in addition to the eight standard ones.
    * Multiplayer-balancing game physics. They stay rather close to the original in most areas, but have some unique flavor here and there.
    * Exploders have knockback and send everybody flying all over the place. Perfect to dislodge enemy blockers. ;-)
    * In-game editor: Design your own levels.
    * Include your self-drawn graphics and use them as terrain, entrance hatches, exits, deadly traps, ...
    * Singleplayer mode for that old-school puzzling fun.
    * Availability for Windows and Linux: download, extract, and play.
    * For programmers: L++ is open source and free software. It should compile on a Mac or other systems as well.

%package data
Group:		Games/Puzzles
License:	public domain
Summary:	Lemmings variant game levels and other data files
BuildArch:	noarch

%description data
The %name game is Lemmings variant featuring singleplayer and networked multiplayer

THis package consists of game levels and other data files for %name.

%prep
%setup -n lpp
%patch -p0

%build

convert src/icon.ico lpp.png

cat > %name.sh <<@@@
#!/bin/sh -e
G="\$HOME/.%name"
S="%_gamesdatadir/%name"

test -d "\$G" || 
rm -f "\$G" &&
mkdir -p "\$G/data/user" "\$G/replay" && 
ln -s "\$S/bitmap" "\$S/levels" "\$G" &&
ln -s "\$S/data/bitmap" "\$S/data/sound" "\$G/data/"

cd "\$G"
exec %_gamesbindir/lpp.bin
@@@

cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Lemmings++
Comment=Lemmings variant featuring singleplayer and networked multiplayer
Exec=%name
Categories=Game;LogicGame;ArcadeGame;
Icon=%name
@@@

%make_build -C src release

%install
mkdir -p %buildroot%_gamesdatadir/%name
cp -a data bitmap levels %buildroot%_gamesdatadir/%name/
install -D %name.sh %buildroot%_gamesbindir/%name
install lpp %buildroot%_gamesbindir/lpp.bin
install lppserv %buildroot%_gamesbindir/
install -D lpp-0.png %buildroot%_miconsdir/%name.png
install -D lpp-1.png %buildroot%_niconsdir/%name.png
install -D lpp-2.png %buildroot%_liconsdir/%name.png
install -D %name.desktop %buildroot%_desktopdir/%name.desktop

%files
%attr(755,games,games) %_gamesbindir/*
%_desktopdir/*
%_iconsdir/hicolor/*/apps/*

%files data
%_gamesdatadir/%name

%changelog
* Tue Mar 22 2011 Fr. Br. George <george@altlinux.ru> 20100311-alt2
- Rebuild with allegro-4.4

* Sun Apr 04 2010 Fr. Br. George <george@altlinux.ru> 20100311-alt1
- Initial build from scratch

