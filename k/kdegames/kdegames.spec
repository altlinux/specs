%undefine __libtoolize
%define qtdir %_qt3dir
%define unstable 0
%define with_arts 0
%define _optlevel s
%define glibc_core_ver %{get_version glibc-core}

%add_findprov_lib_path %_libkde
# textrel
%add_verify_elf_skiplist %_libdir/libatlantik*.so*

Name: kdegames
Summary: KDE - Games
Version: 3.5.13.1
Release: alt1

Group: Graphical desktop/KDE
Url: http://www.kde.org/
License: GPL

Requires: %name-atlantik = %version-%release
Requires: %name-carddecks = %version-%release
%if %with_arts
Requires: %name-kasteroids = %version-%release
Requires: %name-kolf = %version-%release
%endif
Requires: %name-katomic = %version-%release
Requires: %name-kbackgammon = %version-%release
Requires: %name-kbattleship = %version-%release
Requires: %name-kblackbox = %version-%release
Requires: %name-kbounce = %version-%release
Requires: %name-kenolaba = %version-%release
Requires: %name-kfouleggs = %version-%release
Requires: %name-kgoldrunner = %version-%release
Requires: %name-kjumpingcube = %version-%release
Requires: %name-klickety = %version-%release
Requires: %name-klines = %version-%release
Requires: %name-kmahjongg = %version-%release
Requires: %name-kmines = %version-%release
Requires: %name-knetwalk = %version-%release
Requires: %name-konquest = %version-%release
Requires: %name-kpat = %version-%release
Requires: %name-kpoker = %version-%release
Requires: %name-kreversi = %version-%release
Requires: %name-ksame = %version-%release
Requires: %name-kshisen = %version-%release
Requires: %name-ksirtet = %version-%release
Requires: %name-ksmiletris = %version-%release
Requires: %name-ksnake = %version-%release
Requires: %name-ksokoban = %version-%release
Requires: %name-kspaceduel = %version-%release
Requires: %name-ktron = %version-%release
Requires: %name-ktuberling = %version-%release
Requires: %name-kwin4 = %version-%release
Requires: %name-libs = %version-%release
Requires: %name-lskat = %version-%release


Source: kdegames-%version.tar

# ALT
Patch1: 3.2.0-flags.patch
Patch2: kpat-3.5.0-fix-find-wallpaper.patch
Patch3: kdegames-3.5.0-fix-makefile.patch
Patch4: kolf-3.5.0-fix-linking.patch
Patch5: knetwalk-3.5.0-fix-start.patch
Patch6: kdegames-3.5.13-buildAutoTools.patch

# Automatically added by buildreq on Mon Apr 08 2002
BuildRequires: gcc-c++ kde-common
BuildRequires: libalsa-devel libaudiofile-devel libjpeg-devel
BuildRequires: liblcms libmng libpng-devel libqt3-devel libstdc++-devel zlib-devel
BuildRequires: fontconfig-devel, libart_lgpl-devel
BuildRequires: libmad-devel libvorbis-devel xml-utils
BuildRequires: libacl-devel libattr-devel
BuildRequires: kdelibs >= %version kdelibs-devel >= %version

%description
Games for the K Desktop Environment.

%package common
Summary: Common empty package for %name
Group: Graphical desktop/KDE
Requires: kde-common >= 3.2
Conflicts: kdegames <= 3.0
#
%description common
Common empty package for %name

%package devel
Summary: Headers files for kdegames
Group: Development/KDE and QT
Requires: kdegames-atlantik = %version-%release
%if %with_arts
Requires: kdegames-kolf = %version-%release
%endif
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description devel
Headers files needed to build applications based on kdegames applications.

%package libs
Summary: Gaming libraries for KDE
Group: System/Libraries
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description libs
KDE gaming libraries.
This package includes libkdegames
(a library providing functionality commonly needed by games)
and libkdehighscores (highscore handling library).

%package knetwalk
Group: Games/Puzzles
Summary: KDE-version of the popular NetWalk game
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description knetwalk
KDE-version of the popular NetWalk game

%package kgoldrunner
Summary: A game of action and puzzle solving
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kgoldrunner
KGoldrunner, a game of action and puzzle solving.
Run through the maze, dodge your enemies,
collect all the gold and climb up to the next level.

%package atlantik
Summary: Monopoly like games client for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description atlantik
Monopoly like games client for KDE

%package carddecks
Summary: Card decks for KDE games
Group: Games/Cards
Requires: %name-common = %version-%release
#
%description carddecks
Several different collections of card images for use by KDE games.

%package kenolaba
Summary: The Abalone board game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kenolaba
An implementation of the Abalone board game for KDE.
You can play both against the computer and against human players.

%if %with_arts
%package kasteroids
Summary: Asteroids game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kasteroids
An Asteroids-like game for KDE. Shoot the asteroids before they hit you!
%endif

%package katomic
Summary: Katomic - a game for KDE
Group: Games/Puzzles
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description katomic
The aim of Atomic Entertainment is to build chemical molecules using basic
atoms you are given.  The molecule being built is shown in a frame in the main
window.

Clicking on an atom will cause arrows to appear beside it.  These arrows
show the direction the atom can be moved. After an arrow is clicked, the atom
will move in this direction until it reaches the next border or another atom. Iftwo atoms touch each other with the corresponding connectors, they form a
molecule. The atoms can only be moved one at a time.

%package kbackgammon
Summary: A Backgammon game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kbackgammon
A Backgammon game for KDE.

%package kbattleship
Summary: A Battleship game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kbattleship
A Battleship game for KDE. kbattleship can be played both against the computer
and against other human players.

%package kblackbox
Summary: A strategy game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kblackbox
A strategy game for KDE. Can you find out where the hidden balls are?

%package kfouleggs
Summary: A falling blocks game - arrange the blocks by color
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kfouleggs
A falling blocks game for KDE.
Arranging the falling blocks by color will make them disappear.

%package kbounce
Summary: A KDE game: Try catching the bouncing balls
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kbounce
A KDE game: Try catching the bouncing balls!

%package kjumpingcube
Summary: A strategy game. Try to make all fields show your color!
Group: Games/Strategy
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kjumpingcube
A strategy game. Try to make all fields show your color!
kjumpingcube can be played both against the computer and against other
human players.

%package klickety
Summary: klickety game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description klickety
klickety game for KDE

%package klines
Summary: A strategy game: Try to arrange the marbles by color!
Group: Games/Strategy
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description klines
A strategy game: Try to arrange the marbles by color!

%package kmahjongg
Summary: A Mahjongg game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmahjongg
A Majhongg game for KDE.
Make 2 identical blocks disappear.

%package kmines
Summary: A minefield game for KDE
Group: Games/Strategy
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kmines
A minefield game for KDE - find all mines without blowing up!

%if %with_arts
%package kolf
Summary: KDE Golf miniature arcade
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kolf
KDE Golf miniature arcade
%endif

%package konquest
Summary: A conquest game for KDE
Group: Games/Strategy
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description konquest
A multiplayer strategy game for KDE - try to conquer all galaxies.

%package kpat
Summary: Some solitaire games for KDE
Group: Games/Cards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kpat
Some solitaire card games for KDE

%package kpoker
Summary: A Poker game for KDE
Group: Games/Cards
Requires: %name-common = %version-%release
#
%description kpoker
A Poker game for KDE

%package kreversi
Summary: A Reversi (Flip Side) game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kreversi
A Reversi (Flip Side) game for KDE

%package ksame
Summary: A strategy game for KDE - connect as many balls of the same color as possible
Group: Games/Strategy
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksame
A strategy game for KDE - connect as many balls of the same color as possible

%package kshisen
Summary: Shisen Sho (a Mahjongg-like game) for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kshisen
Shisen Sho (a Mahjongg-like game) for KDE

%package ksirtet
Summary: A falling blocks game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksirtet
Make the falling blocks disappear by arranging them in lines

%package ksmiletris
Summary: A falling blocks game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksmiletris
Make the falling blocks disappear - finding out how to do it is half the
fun. ;)

%package ksnake
Summary: A snake game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksnake
A snake game for KDE - collect all apples, but don't crash into the walls!

%package ksokoban
Summary: A Sokoban (move chests to the correct location) game for KDE
Group: Games/Puzzles
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ksokoban
A Sokoban (move chests to the correct location) game for KDE

%package kspaceduel
Summary: A space duel game for KDE
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kspaceduel
A space duel game for KDE.
kspaceduel can be played both against other humans and against the computer.

%package ktron
Summary: A Tron game for KDE - make the opponent crash into a wall first!
Group: Games/Arcade
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktron
A Tron game for KDE - make the opponent crash into a wall first!
ktron can be played both against other humans and against the computer.

%package ktuberling
Summary: Create a potato man
Group: Toys
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description ktuberling
Create a potato man - place eyes, nose, mouth, eyebrows etc. on a potato.

%package kwin4
Summary: Connect 4 game for KDE
Group: Games/Boards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description kwin4
An implementation of the Connect 4 board game for KDE

%package lskat
Summary: A card game for KDE, based on the German "Offiziersskat" game
Group: Games/Cards
Requires: %{get_dep kdelibs}
Requires: %name-common = %version-%release
#
%description lskat
Lt. Skat is a card game for KDE, based on the German "Offiziersskat" game,
a 2 player variant of the Skat game.
lskat can be played against the computer.

%prep
%setup -q  -n kdegames-%version
#%patch1 -p1
%patch2 -p1
%patch3 -p1
#%patch4 -p1
%patch5 -p1
%patch6 -p1

cp -Rp /usr/share/libtool/aclocal/libtool.m4 admin/libtool.m4.in
cp -Rp /usr/share/libtool/config/ltmain.sh admin/ltmain.sh
make -f admin/Makefile.common cvs ||:

%build
rm -rf %buildroot
export QTDIR=%qtdir
export KDEDIR=%prefix

export PATH=$QTDIR/bin:$KDEDIR/bin:$PATH

export LD_LIBRARY_PATH=$QTDIR/%_lib:$KDEDIR/%_lib:$LD_LIBRARY_PATH
export LDFLAGS="-L%buildroot/%_libdir -L%buildroot/%_libdir/kde3 -L%_libdir"
#add_optflags -I%_includedir/tqtinterface

%K3configure \
    --bindir=%_gamesbindir \
    --enable-closure \
    --disable-gcc-hidden-visibility \
%if %unstable
    --enable-debug=full \
%else
    --disable-debug \
%endif
%if %with_arts
    --with-arts \
%else
    --without-arts \
%endif
    --enable-final \
    --enable-highscore-dir=%_localstatedir/games

%make_build
%make_build -C atlantik
%make_build apidox

%install
%if %unstable
%set_strip_method none
%endif
export PATH=%_bindir:$PATH

#K3install

%__mkdir_p %buildroot/%_gamesbindir
%make install \
    DESTDIR=%buildroot \
    bindir=%_gamesbindir
%make DESTDIR=%buildroot install-apidox

[ -f %buildroot/%_K3xdg_apps/knetwalk.desktop ] \
  || install -m 0644 knetwalk/src/knetwalk.desktop %buildroot/%_K3xdg_apps/knetwalk.desktop

%__mkdir_p %buildroot/%_localstatedir/games/
>%buildroot/%_localstatedir/games/knetwalk.scores
>%buildroot/%_localstatedir/games/kbounce.scores
>%buildroot/%_localstatedir/games/ksirtet.scores
>%buildroot/%_localstatedir/games/kmines.scores
>%buildroot/%_localstatedir/games/klickety.scores
>%buildroot/%_localstatedir/games/kfouleggs.scores
>%buildroot/%_localstatedir/games/kreversi.scores

%files
%files common

%files knetwalk
%attr(2711, root, games) %_gamesbindir/knetwalk
%config(noreplace) %attr(664, games, games) %_localstatedir/games/knetwalk.scores
%_K3apps/knetwalk
%_kde3_iconsdir/*/*/apps/knetwalk.*
%_K3xdg_apps/knetwalk.desktop

%files kgoldrunner
%_gamesbindir/kgoldrunner
%_K3apps/kgoldrunner
%_kde3_iconsdir/*/*/apps/kgoldrunner.png
%doc %_K3doc/en/kgoldrunner
%_K3xdg_apps/KGoldrunner.desktop

%files libs
%_libdir/libkdegames.so*
%_K3apps/kdegames
%_kde3_iconsdir/*/*/actions/roll.*
%_kde3_iconsdir/*/*/actions/highscore.*
%_kde3_iconsdir/*/*/actions/endturn.*
%_kde3_iconsdir/*/*/actions/lastmoves.*
%_kde3_iconsdir/*/*/actions/legalmoves.*
%_K3apps/carddecks/cards-default
%dir %_K3apps/carddecks/decks
%_K3apps/carddecks/decks/deck0.*

%files carddecks
%_K3apps/carddecks
%exclude %_K3apps/carddecks/cards-default
%exclude %_K3apps/carddecks/decks/deck0.*

%files atlantik
%_gamesbindir/atlantik
%_libdir/libatlant*.so*
%_libdir/kde3/kio_atlantik.so*
%_K3apps/atlantik
%_K3services/atlantik.protocol
%doc %_K3doc/en/atlantik
%_kde3_iconsdir/*/*/*/atlantik.png
%_K3xdg_apps/atlantik.desktop

%files kenolaba
%_gamesbindir/kenolaba
%_K3xdg_apps/kenolaba.desktop
%_K3apps/kenolaba
%_kde3_iconsdir/*/*/apps/kenolaba*
%doc %_K3doc/en/kenolaba

%if %with_arts
%files kasteroids
%_gamesbindir/kasteroids
%_K3xdg_apps/kasteroids.desktop
%_K3apps/kasteroids
%_kde3_iconsdir/*/*/apps/kasteroids*
%doc %_K3doc/en/kasteroids
%endif

%files katomic
%_gamesbindir/katomic
%_K3xdg_apps/katomic.desktop
%_K3apps/katomic
%_kde3_iconsdir/*/*/apps/katomic*
%doc %_K3doc/en/katomic

%files kbackgammon
%_gamesbindir/kbackgammon
%_K3xdg_apps/kbackgammon.desktop
%_K3apps/kbackgammon
%_kde3_iconsdir/*/*/apps/kbackgammon*
%doc %_K3doc/en/kbackgammon

%files kbattleship
%_K3apps/zeroconf/_kbattleship._tcp
%_K3apps/kbattleship
%_kde3_iconsdir/*/*/apps/kbattleship*
%_gamesbindir/kbattleship
%doc %_K3doc/en/kbattleship
%_K3xdg_apps/kbattleship.desktop

%files kblackbox
%_gamesbindir/kblackbox
%_K3xdg_apps/kblackbox.desktop
%_K3apps/kblackbox
%_kde3_iconsdir/*/*/apps/kblackbox*
%doc %_K3doc/en/kblackbox

%files kfouleggs
%attr(2711, root, games) %_gamesbindir/kfouleggs
%config(noreplace) %attr(664, games, games) %_localstatedir/games/kfouleggs.scores
%_K3cfg/kfouleggs.kcfg
%_K3xdg_apps/kfouleggs.desktop
%_K3apps/kfouleggs
%_kde3_iconsdir/*/*/*/kfouleggs.*
%doc %_K3doc/en/kfouleggs

%files kbounce
%attr(2711, root, games) %_gamesbindir/kbounce
%config(noreplace) %attr(664, games, games) %_localstatedir/games/kbounce.scores
%_K3xdg_apps/kbounce.desktop
%_K3apps/kbounce
%_kde3_iconsdir/*/*/apps/kbounce*
%doc %_K3doc/en/kbounce

%files kjumpingcube
%_gamesbindir/kjumpingcube
%_K3cfg/kjumpingcube.kcfg
%_K3xdg_apps/kjumpingcube.desktop
%_K3apps/kjumpingcube
%_kde3_iconsdir/*/*/apps/kjumpingcube*
%doc %_K3doc/en/kjumpingcube

%files klickety
%attr(2711, root, games) %_gamesbindir/klickety
%config(noreplace) %attr(664, games, games) %_localstatedir/games/klickety.scores
%_K3apps/klickety
%_kde3_iconsdir/*/*/apps/klickety.*
%doc %_K3doc/en/klickety
%_K3xdg_apps/klickety.desktop

%files klines
%_gamesbindir/klines
%_K3cfg/klines.kcfg
%_K3xdg_apps/klines.desktop
%_K3apps/klines
%_kde3_iconsdir/*/*/apps/klines*
%doc %_K3doc/en/klines

%files kmahjongg
%_gamesbindir/kmahjongg
%_K3cfg/kmahjongg.kcfg
%_K3apps/kmahjongg
%_kde3_iconsdir/*/*/apps/kmahjongg*
%doc %_K3doc/en/kmahjongg/
%_K3xdg_apps/kmahjongg.desktop

%files kmines
%attr(2711, root, games) %_gamesbindir/kmines
%config(noreplace) %attr(664, games, games) %_localstatedir/games/kmines.scores
%_K3xdg_apps/kmines.desktop
%_K3apps/kmines
%_kde3_iconsdir/*/*/apps/kmines*
%doc %_K3doc/en/kmines

%if %with_arts
%files kolf
%_gamesbindir/kolf
%_libdir/libkdeinit_kolf.so*
%_libdir/libkolf.so*
%_libdir/kde3/kolf.so*
%_K3apps/kolf
%_K3mimelnk/application/x-kolf.desktop
%_K3mimelnk/application/x-kourse.desktop
%doc %_K3doc/en/kolf
%_K3xdg_apps/kolf.desktop
%_kde3_iconsdir/*/*/*/kolf.png
%endif

%files konquest
%_gamesbindir/konquest
%_K3xdg_apps/konquest.desktop
%_K3apps/konquest
%_kde3_iconsdir/*/*/apps/konquest*
%doc %_K3doc/en/konquest

%files kpat
%_gamesbindir/kpat
%_K3xdg_apps/kpat.desktop
%_K3apps/kpat
%_kde3_iconsdir/*/*/apps/kpat*
%doc %_K3doc/en/kpat

%files kpoker
%_gamesbindir/kpoker
%_K3xdg_apps/kpoker.desktop
%_K3apps/kpoker
%_kde3_iconsdir/*/*/apps/kpoker*
%doc %_K3doc/en/kpoker

%files kreversi
%attr(2711, root, games) %_gamesbindir/kreversi
%config(noreplace) %attr(664, games, games) %_localstatedir/games/kreversi.scores
%_K3cfg/kreversi.kcfg
%_K3xdg_apps/kreversi.desktop
%_K3apps/kreversi
%_kde3_iconsdir/*/*/apps/kreversi*
%doc %_K3doc/en/kreversi

%files ksame
%_gamesbindir/ksame
%_K3xdg_apps/ksame.desktop
%_K3apps/ksame
%_kde3_iconsdir/*/*/apps/ksame*
%doc %_K3doc/en/ksame

%files kshisen
%_gamesbindir/kshisen
%_K3cfg/kshisen.kcfg
%_K3xdg_apps/kshisen.desktop
%_K3apps/kshisen
%_kde3_iconsdir/*/*/apps/kshisen*
%doc %_K3doc/en/kshisen

%files ksirtet
%attr(2711, root, games) %_gamesbindir/ksirtet
%config(noreplace) %attr(664, games, games) %_localstatedir/games/ksirtet.scores
%_K3cfg/ksirtet.kcfg
%_K3xdg_apps/ksirtet.desktop
%_K3apps/ksirtet
%_kde3_iconsdir/*/*/apps/ksirtet*
%doc %_K3doc/en/ksirtet

%files ksmiletris
%_gamesbindir/ksmiletris
%_K3xdg_apps/ksmiletris.desktop
%_K3apps/ksmiletris
%_kde3_iconsdir/*/*/apps/ksmiletris*
%doc %_K3doc/en/ksmiletris/

%files ksnake
%_gamesbindir/ksnake
%_K3cfg/ksnake.kcfg
%_K3xdg_apps/ksnake.desktop
%_K3apps/ksnake
%_kde3_iconsdir/*/*/apps/ksnake*
%doc %_K3doc/en/ksnake

%files ksokoban
%_gamesbindir/ksokoban
%_K3xdg_apps/ksokoban.desktop
%_kde3_iconsdir/*/*/apps/ksokoban*
%doc %_K3doc/en/ksokoban

%files kspaceduel
%_gamesbindir/kspaceduel
%_K3cfg/kspaceduel.kcfg
%_K3xdg_apps/kspaceduel.desktop
%_K3apps/kspaceduel
%_kde3_iconsdir/*/*/apps/kspaceduel*
%doc %_K3doc/en/kspaceduel

%files ktron
%_gamesbindir/ktron
%_K3cfg/ktron.kcfg
%_K3xdg_apps/ktron.desktop
%_K3apps/ktron
%_kde3_iconsdir/*/*/apps/ktron*
%doc %_K3doc/en/ktron

%files ktuberling
%_gamesbindir/ktuberling
%_K3xdg_apps/ktuberling.desktop
%_K3apps/ktuberling
%_kde3_iconsdir/*/*/apps/ktuberling*
%_K3mimelnk/application/x-tuberling.desktop
%doc %_K3doc/en/ktuberling

%files kwin4
%_gamesbindir/kwin4*
%_K3cfg/kwin4.kcfg
%_K3xdg_apps/kwin4.desktop
%_K3apps/kwin4
%_kde3_iconsdir/*/*/apps/kwin4*
%doc %_K3doc/en/kwin4

%files lskat
%_gamesbindir/lskat*
%_K3xdg_apps/lskat.desktop
%_K3apps/lskat
%_kde3_iconsdir/*/*/apps/lskat*
%doc %_K3doc/en/lskat

%files devel
%_includedir/*
%_K3doc/en/kdegames-%version-apidocs

%changelog
* Sun Oct 14 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13.1-alt1
- Release TDE version 3.5.13.1

* Sat Oct 06 2012 Roman Savochenko <rom_as@altlinux.ru> 3.5.13-alt1
- TDE 3.5.13 release build

* Tue Aug 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.10-alt1
- new version

* Tue Feb 26 2008 Sergey V Turchin <zerg at altlinux dot org> 3.5.9-alt1
- new version

* Wed Oct 17 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.8-alt1
- new version

* Thu May 24 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.7-alt1
- new version

* Mon Jan 29 2007 Sergey V Turchin <zerg at altlinux dot org> 3.5.6-alt1
- new version

* Tue Oct 17 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.5-alt1
- new version

* Mon Sep 04 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.4-alt1
- new version

* Mon Jun 19 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt2
- bump release to push incoming@ALT

* Tue Jun 06 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.3-alt1
- new version

* Mon Apr 03 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.2-alt1
- new version

* Thu Feb 02 2006 Sergey V Turchin <zerg at altlinux dot org> 3.5.1-alt1
- new version

* Thu Dec 29 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt2
- fix starting knetwalk

* Fri Dec 09 2005 Sergey V Turchin <zerg at altlinux dot org> 3.5.0-alt1
- new version
- sgid kbounce and knetwalk for shared hiscores

* Tue Oct 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt2
- sgid games for ksirtet,kmines,kfouleggs,klickety for shared hiscores
- add one desk background to libs subpackage

* Tue Jun 07 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.1-alt1
- new version

* Fri Apr 01 2005 Sergey V Turchin <zerg at altlinux dot org> 3.4.0-alt1
- new version

* Tue Jan 11 2005 Sergey V Turchin <zerg at altlinux dot org> 3.3.2-alt1
- rebuild

* Wed Jan 05 2005 ZerG <zerg@altlinux.ru> 3.3.2-alt0.0.M24
- new version

* Thu Oct 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.1-alt1
- new version

* Sat Oct 02 2004 Sergey V Turchin <zerg at altlinux dot org> 3.3.0-alt1
- new version

* Tue Jul 06 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt3
- fix package sign

* Mon Jul 05 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt2
- fix kpat find wallpaper when no kdeartwork wallpapers

* Mon Jun 07 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.3-alt1
- new version

* Mon Apr 12 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.2-alt1
- new version

* Tue Mar 16 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.1-alt1
- update code from KDE_3_2_BRANCH 

* Thu Mar 04 2004 Sergey V Turchin <zerg at altlinux dot org> 3.2.0-alt1
- new version
- update code from KDE_3_2_BRANCH 

* Fri Dec 05 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt2
- remove *.la files

* Thu Sep 18 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.4-alt1
- update code from cvs

* Wed Aug 20 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt1
- update code from cvs

* Tue Jul 22 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.3-alt0.1
- update code from cvs

* Tue Jul 01 2003 Sergey V Turchin <zerg at altlinux dot org> 3.1.2-alt2
- update code from cvs

* Wed May 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.2-alt1
- update code from cvs KDE_3_1_BRANCH

* Tue Apr 29 2003 Sergey V Turchin <zerg at altlinux dot ru> 3.1.1-alt2
- update code from cvs KDE_3_1_BRANCH
- add MDK patches

* Mon Mar 31 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.1-alt1
- update code from cvs KDE_3_1_BRANCH

* Wed Jan 29 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt3
- update code from cvs KDE_3_1_0_RELEASE

* Thu Jan 09 2003 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt2
- update code from cvs

* Thu Nov 28 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt1
- update from cvs

* Wed Nov 06 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc2
- rc2

* Mon Nov 04 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.20.rc1
- rc1
- increase %%release to easy check dependencies

* Fri Oct 25 2002 Sergey V Turchin <zerg@altlinux.ru> 3.1.0-alt0.2
- update from cvs

* Tue Sep 10 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt2
- sync patches with cooker
- rebuild with gcc3.2 && objprelink

* Tue Aug 20 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.3-alt1
- update from cvs

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.2-alt1
- new version

* Fri Jun 07 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0.1-alt1
- new version
- split

* Mon Apr 29 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt3
- move to /usr

* Tue Apr 09 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt2
- fix requires

* Mon Apr 08 2002 Sergey V Turchin <zerg@altlinux.ru> 3.0-alt1
- build for ALT

* Thu Apr 04 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Fix update menu

* Tue Mar 26 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

* Thu Mar 21 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc3.1mdk
- RC3

* Sat Mar 16 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.rc2.4mdk
- RC2

* Wed Feb 13 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.4mdk
- Fix BuildRequires for 8.2

* Sat Feb 09 2002 David BAUDENS <baudens@mandrakesoft.com> 3.0-0.beta2.3mdk
- Fix ./configure
- Enable debug
- Set unstable macro to 1

* Fri Feb 08 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.2mdk
- fix spec file

* Sun Jan 27 2002 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta2.1mdk
- beta2

* Thu Dec 20 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.3mdk
- Rename to allow KDE 2 & 3 to be installed in same time

* Sat Dec 08 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-0.beta1.3mdk
- kde 3.0 beta1

* Fri Nov 30 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-2mdk
- Improve spec file

* Sat Nov 24 2001 Laurent MONTEL <lmontel@mandrakesoft.com> 3.0-1mdk
- kde 3.0

