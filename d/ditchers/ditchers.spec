Name:		ditchers
Version:	1.2
Release:	alt4
Group:		Games/Arcade
Summary:	Underground tanks dig tunnels in the soil and destroys opponents
Source:		%name-%version.tar.gz
Source1:	beach.tar.gz
Source2:	bunker.tar.gz
Source3:	cutover.tar.gz
Source4:	sand.tar.gz
Patch:		ditchers.1.0.4.1.patch
Patch1:		ditchers-1.2.tinyxml.patch
URL:		http://ditchers.sourceforge.net
License:	BSD

Requires:	%name-data

# Automatically added by buildreq on Mon Jun 21 2010
BuildRequires: boost-filesystem-devel gcc-c++ libSDL_gfx-devel libSDL_image-devel libSDL_mixer-devel libSDL_net-devel libguichan-devel liblua5-devel libpng-devel tinyxml-devel

BuildRequires:	libguichan-devel > 0.8.0

%description
Ditchers is an action game based on principles of the legendary game
Tunneler. Underground tanks dig tunnels in the soil and their goal is to
find and destroy the opponent using a variety of weapons.

Features:

Multiplayer

Many players can participate in a game at once. At one computer, two
people can play in splitscreen and with any number of artificial
players. Network game is also available.

Network

While the game is perfectly playable at one computer it is also possible
to play over network. A small server application is included so any
number of clients may connect and play. The server can maintain any
number of games simultaneously.

Artificial players

AI players (bots) are available in the game. Furthermore, these bots
work according to AI scripts and it is possible to alter these scripts
or to create new ones. The game can be also run with no human players to
spectate how able scripted AI players are.

%package data
Summary: Data files for %name 
Group: Games/Arcade
Buildarch: noarch
%description data
Data files for %name, %summary

%prep
%setup -n %name
%patch -p1 -b .orig
%patch1 -p3

for N in */*.desktop; do
  sed -i 's/.png//
  s@/usr/share/games@%_gamesdatadir@g' $N;
done

cat > %name.sh <<@@@
#!/bin/sh
cd %_gamesdatadir/%name
%_gamesbindir/ditcher.bin
@@@

gzip -d  %name.6.gz

sed -i 's|^\(CFLAGS.*\)|\1 -g -DBOOST_FILESYSTEM_VERSION=2|' \
	ditcher/Makefile ditchs/Makefile

( cd ditcher/data/maps
tar xf %SOURCE1
tar xf %SOURCE2
tar xf %SOURCE3
tar xf %SOURCE4 )

%build
%make_build -C ditcher
%make_build -C ditchs

%install
mkdir -p %buildroot%_gamesdatadir/%name
cp -r ditcher/*.png ditcher/data %buildroot%_gamesdatadir/%name
install -D -m755 ditcher/ditcher %buildroot%_gamesbindir/ditcher.bin
install -D -m755 %name.sh %buildroot%_gamesbindir/ditcher
install -D -m755 ditchs/ditchs %buildroot%_gamesbindir/ditchs
install -D %name.6 %buildroot%_man6dir/%name.6
for N in ditcher ditchs; do
  install -D $N/$N.desktop %buildroot%_desktopdir/$N.desktop
  install -D $N/$N.png %buildroot%_liconsdir/$N.png
done

%files
%doc */*.txt
%dir %_gamesdatadir/%name
%_gamesbindir/*
%_desktopdir/*
%_liconsdir/*
%_man6dir/*

%files data
%_gamesdatadir/%name/*

%changelog
* Thu May 24 2012 Fr. Br. George <george@altlinux.ru> 1.2-alt4
- DSO list completion

* Thu Apr 05 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.3
- Rebuilt with Boost 1.49.0

* Sun Dec 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.2
- Rebuilt with Boost 1.48.0

* Fri Jul 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt3.1
- Rebuilt with Boost 1.47.0

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 1.2-alt3
- Upstream level collection added

* Tue Jun 21 2011 Fr. Br. George <george@altlinux.ru> 1.2-alt2
- Patch up to new tinyxml

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.2
- Rebuilt with Boost 1.46.1 and for debuginfo

* Thu Dec 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.2-alt1.1
- rebuild with new icu44 and/or boost by request of git.alt administrator

* Sun Aug 29 2010 Fr. Br. George <george@altlinux.ru> 1.2-alt1
- Version up

* Mon Jun 21 2010 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Version up

* Mon May 24 2010 Fr. Br. George <george@altlinux.ru> 1.0.4.1-alt1
- New version

* Wed May 12 2010 Fr. Br. George <george@altlinux.ru> 0-alt1
- Initial build from scratch

