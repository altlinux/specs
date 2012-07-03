Name: hedgewars
Version: 0.9.17
Release: alt1

Summary: Game with heavily armed fighting hedgehogs
License: GPL
Group: Games/Strategy
URL: http://www.hedgewars.org/

Packager: Anton Farygin <rider@altlinux.ru>

Source0: %name-%version.tar
Patch0: %name-%version-%release.patch

# Automatically added by buildreq on Fri Mar 13 2009

BuildRequires: gcc-c++ cmake libqt4-devel libSDL-devel libSDL_ttf-devel libSDL_mixer-devel libSDL_image-devel libSDL_net-devel fpc ghc-binary ghc-network-bytestring 
BuildRequires: ghc-bytestring-show ghc-deepseq
BuildRequires: ghc-stm ghc-regex-base ghc-mtl ghc-binary ghc-regex-compat ghc-parsec ghc ghc-utf8-string ghc-network ghc-regex-posix ghc-dataenc ghc-hslogger
BuildRequires: liblua5-devel

%description
Each player controls a team of several hedgehogs. During the course of the 
game, players take turns with one of their hedgehogs. They then use whatever 
tools and weapons are available to attack and kill the opponents' hedgehogs, 
thereby winning the game. Hedgehogs may move around the terrain in a variety 
of ways, normally by walking and jumping but also by using particular tools 
such as the "Rope" or "Parachute", to move to otherwise inaccessible areas. 

Each turn is time-limited to ensure that players do not hold up the game 
with excessive thinking or moving.
A large variety of tools and weapons are available for players during the 
game: Grenade, Cluster Bomb, Bazooka, UFO, Shotgun, Desert Eagle, Fire Punch, 
Baseball Bat, Dynamite, Mine, Rope, Pneumatic pick, Parachute. Most weapons, 
when used, cause explosions that deform the terrain, removing circular chunks. 

The landscape is an island floating on a body of water, or a restricted cave 
with water at the bottom. A hedgehog dies when it enters the water (either 
by falling off the island, or through a hole in the bottom of it), it is 
thrown off either side of the arena or when its health is reduced, 
typically from contact with explosions, to zero (the damage dealt to the 
attacked hedgehog or hedgehogs after a player's or CPU turn is shown only 
when all movement on the battlefield has ceased).

%prep
%setup -q
%patch0 -p1

%build
PATH="/usr/lib/qt4/bin/:$PATH" cmake -DCMAKE_INSTALL_PREFIX="%_prefix" -DWITH_SERVER=1 -DDATA_INSTALL_DIR=%_datadir  CMakeLists.txt
%make_build VERBOSE=true

%install
%make_install DESTDIR=%buildroot install

mkdir -p %buildroot%_datadir/applications/

cat <<EOF >%buildroot%_datadir/applications/%name.desktop
[Desktop Entry]
Name=%name
Comment=Strategy action game
Exec=hedgewars
Terminal=false
Type=Application
StartupNotify=true
Categories=Game;ActionGame;StrategyGame;
EOF


%files
%doc README
%_bindir/*
%_datadir/%name/
%_datadir/applications/*.desktop

%changelog
* Sun Nov 20 2011 Anton Farygin <rider@altlinux.ru> 0.9.17-alt1
- new version

* Sun Sep 18 2011 Anton Farygin <rider@altlinux.ru> 0.9.16-alt1
- new version

* Sat Feb 12 2011 Anton Farygin <rider@altlinux.ru> 0.9.15-alt1
- new version

* Wed Sep 29 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt2
- rebuild in new environment

* Sun Apr 04 2010 Anton Farygin <rider@altlinux.ru> 0.9.13-alt1
- new version

* Wed Mar 10 2010 Anton Farygin <rider@altlinux.ru> 0.9.12-alt2
- fixed build with new fpc-2.4.0

* Sun Nov 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.12-alt1
- new version

* Mon May 25 2009 Anton Farygin <rider@altlinux.ru> 0.9.11-alt1
- new version

* Tue Apr 14 2009 Anton Farygin <rider@altlinux.ru> 0.9.10-alt1
- new version

* Sun Mar 15 2009 Anton Farygin <rider@altlinux.ru> 0.9.9-alt2
- build hedgewars-server too

* Mon Jan 26 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.9-alt1
- 0.9.9

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1.1
- Fix summary

* Sat Jan 10 2009 Ilya Mashkin <oddity@altlinux.ru> 0.9.8-alt1
- 0.9.8

* Mon Nov 03 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.7-alt1
- 0.9.7

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 0.9.6-alt1
- 0.9.6

* Sun Jun 22 2008 Igor Zubkov <icesik@altlinux.org> 0.9.4-alt1
- build for Sisyphus

