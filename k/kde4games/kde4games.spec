
%def_enable ksudoku

%add_findpackage_path %_kde4_bindir
%add_python_req_skip modeltest

%define rname kdegames
Name: kde4games
%define major 4
%define minor 8
%define bugfix 3
Version: %major.%minor.%bugfix
Release: alt1

Group: Graphical desktop/KDE
Summary: KDE - Games
Url: http://games.kde.org/
License: GPL

%ifdef _kde_alternate_placement
%else
Provides: kdegames = %version-%release
Obsoletes: kdegames < %version-%release
%endif

Requires: %name-kgoldrunner = %version-%release
Requires: %name-katomic = %version-%release
Requires: %name-kblackbox = %version-%release
Requires: %name-ktuberling = %version-%release
Requires: %name-kbounce = %version-%release
Requires: %name-kspaceduel = %version-%release
Requires: %name-kreversi = %version-%release
Requires: %name-kolf = %version-%release
Requires: %name-konquest = %version-%release
Requires: %name-ksame = %version-%release
Requires: %name-kmahjongg = %version-%release
Requires: %name-kajongg = %version-%release
Requires: %name-kbattleship = %version-%release
Requires: %name-kiriki = %version-%release
%if_enabled ksudoku
Requires: %name-ksudoku = %version-%release
%endif
Requires: %name-bovo = %version-%release
Requires: %name-kjumpingcube = %version-%release
Requires: %name-klines = %version-%release
Requires: %name-kmines = %version-%release
Requires: %name-knetwalk = %version-%release
Requires: %name-kpat = %version-%release
Requires: %name-kshisen = %version-%release
Requires: %name-ksquares = %version-%release
Requires: %name-kfourinline = %version-%release
Requires: %name-lskat = %version-%release
Requires: %name-kdiamond = %version-%release
Requires: %name-kollision = %version-%release
Requires: %name-kubrick = %version-%release
Requires: %name-kblocks = %version-%release
Requires: %name-kbreakout = %version-%release
Requires: %name-ksirk = %version-%release
Requires: %name-kapman = %version-%release
Requires: %name-killbots = %version-%release
Requires: %name-bomber = %version-%release
Requires: %name-ktron = %version-%release
Requires: %name-granatier = %version-%release
Requires: %name-kigo = %version-%release
Requires: %name-palapeli = %version-%release


#Source: ftp://ftp.kde.org/pub/kde/stable/%version/src/%rname-%version.tar.bz2
Source: %rname-%version.tar
Patch1: kde4games-4.5.0-alt-find-twisted.patch

# Automatically added by buildreq on Mon Oct 20 2008 (-bi)
#BuildRequires: gcc-c++ ggz-client-libs kde4base-runtime-devel kde4libs-devel kdelibs-devel libXScrnSaver-devel libXcomposite-devel libXft-devel libXpm-devel libXt-devel libXtst-devel libXv-devel libXxf86misc-devel libxkbfile-devel nvidia_glx_177.80 rpm-build-ruby xorg-xf86vidmodeproto-devel
BuildRequires(pre): kde4libs-devel
BuildRequires: gcc-c++ libggz-devel ggz-client-libs-devel kde4base-runtime-devel
BuildRequires: libqca2-devel libsqlite3-devel libopenal-devel libsndfile-devel
BuildRequires: python-module-PyQt4 python-module-kde4 rpm-build-python
BuildRequires: kde4libs-devel >= %version

%description
Games for the K Desktop Environment.
This is a compilation of various games for KDE project
 - katomic: build complex atoms with a minimal amount of moves
 - kbattleship: battleship game with built-in game server
 - kblackbox: find atoms in a grid by shooting electrons
 - kbounce: claim areas and don't get disturbed
 - klines: place 5 equal pieces together, but wait, there are 3 new ones
 - mahjongg: a tile laying patience
 - kmines: the classical mine sweeper
 - kolf: a golf game
 - konquest: conquer the planets of your enemy
 - kpat: several patience card games
 - kreversi: the old reversi board game, also known as othello
 - ksame: collect pieces of the same color
 - kshisen: patience game where you take away all pieces
 - kspaceduel: two player game with shooting spaceships flying around a sun
 - ktuberling: kids game: make your own potato (NO french fries!)
 - kfourinline: place 4 pieces in a row
 - Lskat: lieutnant skat
%if_enabled ksudoku
 - Ksudoku: Play, create and solve sudoku grids
%endif
 - KGoldrunner: a game of action and puzzle solving.
 - KTuberling: "potato editor" game
 - Kiriki: Close of Yahtzee
 - Kjumpingcube: a tactical game for number-crunchers
 - Bovo: classic pen and paper game
 - KSquares: an implementation of the popular paper based game squares
 - Knetwalk: Turn the board pieces to get all computers connected

%package common
Summary: %name common package
Group: System/Configuration/Other
Requires: kde-common >= %major.%minor
BuildArch: noarch
%ifdef _kde_alternate_placement
%else
#Provides: kdegames-common = %version-%release
#Obsoletes: kdegames-common < %version-%release
%endif
%description common
%name common package

%package core
Summary: Core files for %name
Group: Graphical desktop/KDE
#Requires: %{get_dep kde4libs}
Requires: %name-common = %version-%release
%ifdef _kde_alternate_placement
%else
#Provides: kdegames-carddecks = %version-%release
#Obsoletes: kdegames-carddecks < %version-%release
%endif
%description core
Core files for %name

%package palapeli
Summary: Jigsaw puzzle game
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-palapeli = %version-%release
Obsoletes: kdegames-palapeli < %version-%release
%endif
%description palapeli
Palapeli is a jigsaw puzzle game. Unlike other games in that genre, you
are not limited to aligning pieces on imaginary grids. The pieces are
freely moveable. Also, Palapeli features real persistency, i.e. everything
you do is saved on your disk immediately.

%package granatier
Summary: KDE Bomberman game
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-granatier = %version-%release
Obsoletes: kdegames-granatier < %version-%release
%endif
%description granatier
KDE Bomberman game.

%package kigo
Summary: Go board game for KDE
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
Requires: gnugo
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kigo = %version-%release
Obsoletes: kdegames-kigo < %version-%release
%endif
%description kigo
Go board game for KDE.

%package kapman
Summary: A Pac-Man clone
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kapman = %version-%release
Obsoletes: kdegames-kapman < %version-%release
%endif
%description kapman
Kapman is a Pac-Man clone

%package bomber
Summary: bomber
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-bomber = %version-%release
Obsoletes: kdegames-bomber < %version-%release
%endif
%description bomber
Bomberman like game

%package killbots
Summary: KDE port of the classic BSD console game robots
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-killbots = %version-%release
Obsoletes: kdegames-killbots < %version-%release
%endif
%description killbots
Killbots is a KDE port of the classic BSD console game robots.

%package kgoldrunner
Summary: KGoldrunner, a game of action and puzzle solving
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kgoldrunner
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kgoldrunner = %version-%release
Obsoletes: kdegames-kgoldrunner < %version-%release
%endif
%description kgoldrunner
KGoldrunner, a game of action and puzzle solving.
Run through the maze, dodge your enemies, collect
all the gold and climb up to the next level.

%package katomic
Summary: Build complex atoms with a minimal amount of moves
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=katomic
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-katomic = %version-%release
Obsoletes: kdegames-katomic < %version-%release
%endif
%description katomic
katomic: build complex atoms with a minimal amount of moves

%package kblackbox
Summary: Find atoms in a grid by shooting electrons
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kblackbox
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kblackbox = %version-%release
Obsoletes: kdegames-kblackbox < %version-%release
%endif
%description kblackbox
kblackbox: find atoms in a grid by shooting electrons

%package ktuberling
Summary: KTuberling: "potato editor" game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=ktuberling
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ktuberling = %version-%release
Obsoletes: kdegames-ktuberling < %version-%release
%endif
%description ktuberling
KTuberling is a "potato editor" game intended for small
children and adults who remain young at heart. The game
has no winner; the only purpose is to make the funniest
faces you can.

%package kbounce
Summary: Claim areas and don't get disturbed
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kbounce
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kbounce = %version-%release
Obsoletes: kdegames-kbounce < %version-%release
%endif
%description kbounce
kbounce: claim areas and don't get disturbed

%package kspaceduel
Summary: Two player game with shooting spaceships flying around a sun
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kspaceduel
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kspaceduel = %version-%release
Obsoletes: kdegames-kspaceduel < %version-%release
%endif
%description kspaceduel
kspaceduel: two player game with shooting spaceships flying around a sun

%package kreversi
Summary: Old reversi board game, also known as othello
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kreversi
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kreversi = %version-%release
Obsoletes: kdegames-kreversi < %version-%release
%endif
%description kreversi
kreversi: the old reversi board game, also known as othello

%package kolf
Summary: A golf game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kolf
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kolf = %version-%release
Obsoletes: kdegames-kolf < %version-%release
%endif
%description kolf
Kolf is a miniature golf game with 2d top-down view. Courses are dynamic,
and up to 10 people can play at once in competition. Kolf comes equipped
with a variety of playgrounds and tutorial courses.

%package konquest
Summary: Conquer the planets of your enemy
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=konquest
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-konquest = %version-%release
Obsoletes: kdegames-konquest < %version-%release
%endif
%description konquest
konquest: conquer the planets of your enemy

%package ksame
Summary: Collect pieces of the same color
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=ksame
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ksame = %version-%release
Obsoletes: kdegames-ksame < %version-%release
%endif
Provides: kdegames-klickety = %version-%release
Obsoletes: kdegames-klickety < %version-%release
%description ksame
ksame: collect pieces of the same color

%package kmahjongg
Summary: A tile laying patience
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kmahjongg
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kmahjongg = %version-%release
Obsoletes: kdegames-kmahjongg < %version-%release
%endif
%description kmahjongg
Kmahjongg: a tile laying patience

%package kajongg
Summary: A tile laying patience
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kajongg
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kajongg = %version-%release
Obsoletes: kdegames-kajongg < %version-%release
%endif
%description kajongg
Kajongg: a tile laying patience

%package kbattleship
Summary: Battleship game with built-in game server
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kbattleship
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kbattleship = %version-%release
Obsoletes: kdegames-kbattleship < %version-%release
%endif
%description kbattleship
kbattleship: battleship game with built-in game server

%package kiriki
Summary: Kiriki: Close of Yahtzee
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kiriki
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kiriki = %version-%release
Obsoletes: kdegames-kiriki < %version-%release
%endif
%description kiriki
Kiriki is a dice game, written for KDE 4.
It is a clone of Gnome Tali (gtali) that is a clone of Yahtzee!

%package ksudoku
Summary: KSudoku - Play, create and solve sudoku grids
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=ksudoku
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ksudoku = %version-%release
Obsoletes: kdegames-ksudoku < %version-%release
%endif
Provides: ksudoku = %version-%release
Obsoletes: ksudoku < %version-%release
%description ksudoku
 The word Sudoku means "single number in an alloted place" in Japanese. These
are the basic rules. Every sudoku Sudoku is a square of 81 cells divided into
9 columns and 9 rows and in 9 subsquares (3x3) of 9 cells each. Solving takes
usually from 10 to 30 minutes, depending on puzzle level, your skill and
experience.
 Some cells are filled with a number at the beginnning: the remaining are to
be filled by the player using numbers from 1 to 9, without repeating a number
twice on each column, row or subsuquare (each of them must contain only
one 1, one 2, one 3, and so on). The game requires logic and patience.
The numerals in Sudoku puzzles are used for convenience (for example in 16x16
board we use letters): arithmetic relationships between numbers are irrelevant.
 This program supports also 16x16 games with numbers from 1 to 16 and 256
cells with 16 cols, rows and subsquares! (if normal sudoku are not enough for
you).
 More information at http://en.wikipedia.org/wiki/Sudoku

%package bovo
Summary: Bovo: classic pen and paper game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=bovo
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-bovo = %version-%release
Obsoletes: kdegames-bovo < %version-%release
%endif
%description bovo
Bovo is a KDE 4 game, modeled upon a classic pen and paper game,
where you try to connect five in a row prior to your opponent.

%package kjumpingcube
Summary: kjumpingcube: a tactical game for number-crunchers
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kjumpingcube
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kjumpingcube = %version-%release
Obsoletes: kdegames-kjumpingcube < %version-%release
%endif
%description kjumpingcube
KJumpingCube is a tactical one or two-player game. The playing field
consists of squares that contains points which can be increased. By
this you can gain more fields and finally win the board over.

%package klines
Summary: Place 5 equal pieces together, but wait, there are 3 new ones
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=klines
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-klines = %version-%release
Obsoletes: kdegames-klines < %version-%release
%endif
%description klines
klines: place 5 equal pieces together, but wait, there are 3 new ones

%package kmines
Summary: The classical mine sweeper
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kmines
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kmines = %version-%release
Obsoletes: kdegames-kmines < %version-%release
%endif
%description kmines
kmines: the classical mine sweeper

%package knetwalk
Summary: Turn the board pieces to get all computers connected
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=knetwalk
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-knetwalk = %version-%release
Obsoletes: kdegames-knetwalk < %version-%release
%endif
%description knetwalk
Turn the board pieces to get all computers connected.

%package kpat
Summary: Several patience card games
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kpat
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kpat = %version-%release
Obsoletes: kdegames-kpat < %version-%release
%endif
%description kpat
kpat: several patience card games

%package kshisen
Summary: Patience game where you take away all pieces
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kshisen
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kshisen = %version-%release
Obsoletes: kdegames-kshisen < %version-%release
%endif
%description kshisen
Kshisen: patience game where you take away all pieces

%package ksquares
Summary: KSquares: an implementation of the popular paper based game squares
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=ksquares
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ksquares = %version-%release
Obsoletes: kdegames-ksquares < %version-%release
%endif
%description ksquares
KSquares is an implementation of the popular paper based game squares.
You must draw lines to complete squares, the player with the most s
quares wins.

%package kfourinline
Summary: Place 4 pieces in a row
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kfourinline
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kfourinline = %version-%release
Obsoletes: kdegames-kfourinline < %version-%release
%endif
%description kfourinline
kfourinline: place 4 pieces in a row

%package lskat
Summary: Lieutnant skat
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=lskat
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-lskat = %version-%release
Obsoletes: kdegames-lskat < %version-%release
%endif
%description lskat
lskat: lieutnant skat

%package kdiamond
Summary: Three-in-a-row game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kdiamond
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kdiamond = %version-%release
Obsoletes: kdegames-kdiamond < %version-%release
%endif
%description kdiamond
KDiamond is a three-in-a-row game (much like Bejeweled) for the KDE 4 desktop.

%package kollision
Summary: A simple ball dodging game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kollision
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kollision = %version-%release
Obsoletes: kdegames-kollision < %version-%release
%endif
%description kollision
A simple ball dodging game

%package kubrick
Summary: Game based on Rubik's Cube
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kubrick = %version-%release
Obsoletes: kdegames-kubrick < %version-%release
%endif
%description kubrick
Kubrick, a game based on Rubik's Cube

%package kblocks
Summary: Single player falling blocks puzzle game
Group: Graphical desktop/KDE
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kblocks = %version-%release
Obsoletes: kdegames-kblocks < %version-%release
%endif
%description kblocks
Single player falling blocks puzzle game

%package kbreakout
Summary: kbreakout
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=kbreakout
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-kbreakout = %version-%release
Obsoletes: kdegames-kbreakout < %version-%release
%endif
%description kbreakout
Single player falling blocks puzzle game

%package ksirk
Summary: Single player falling blocks puzzle game
Group: Graphical desktop/KDE
Url: http://games.kde.org/game.php?game=ksirk
Requires: kde4games-core = %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ksirk = %version-%release
Obsoletes: kdegames-ksirk < %version-%release
%endif
%description ksirk
KsirK is a computerized version of a well known strategy board game.
KsirK is a multi-player network-playable game with an AI. The goal
of the game is simply to conquer the World... It is done by attacking
your neighbours with your armies.

%package -n libkdegames4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkdegames4
KDE 4 library.

%package -n libkmahjongglib4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkmahjongglib4
KDE 4 library.

%package -n libkolfprivate4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkolfprivate4
KDE 4 library.

%package -n libkggzgames4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkggzgames4
KDE 4 library.

%package -n libkggzmod4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkggzmod4
KDE 4 library.

%package -n libkggznet4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkggznet4
KDE 4 library.

%package -n libiris4_ksirk
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libiris4_ksirk
KDE 4 library.

%package -n libpala4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libpala4
KDE 4 library.

%package -n libkcardgame4
Summary: KDE 4 library
Group: System/Libraries
Requires: %name-common = %version-%release
%description -n libkcardgame4
KDE 4 library.

%package ktron
Summary: Simple Tron clone
Group: Graphical desktop/KDE
URL: http://games.kde.org/game.php?game=ktron
Requires: kde4games-core = %version-%release
Provides: kde4games-kdesnake = %version-%release
Obsoletes: kde4games-kdesnake < %version-%release
%ifdef _kde_alternate_placement
%else
Provides: kdegames-ktron = %version-%release
Obsoletes: kdegames-ktron < %version-%release
%endif
%description ktron
Well known from the famous movie, KTron is a popular computer 
game for two players. In a fast action sequence both players 
have to move and avoid colliding with any walls, the opponent 
as well as the own path. The player colliding first looses the 
game.

KSnake Race is a fast action game where you steer a snake 
which has to eat food. While eating the snake grows. But 
once a player collides with the other snake or the wall 
the game is lost. This becomes of course more and more 
difficult the longer the snakes grow.

%package devel
Summary: Headers files for %name
Group: Development/KDE and QT
Requires: kde4libs-devel
%description devel
Headers files needed to build applications based on kdegames applications.


%prep
%setup -q -n %rname-%version
%patch1 -p1


%build
NOBUILDPKGS=
%if_enabled ksudoku
%else
NOBUILDPKGS+=" -DBUILD_ksudoku=FALSE"
%endif
%K4build


%install
%K4install
if ! [ -f %buildroot/%_sysconfdir/ggz.modules.d/kdegames ]
then
    mkdir -p %buildroot/%_sysconfdir/ggz.modules.d/
    touch %buildroot/%_sysconfdir/ggz.modules.d/kdegames
fi


%files
%files common
%doc README
%_K4xdg_mime/kpatience.xml
%config %_sysconfdir/ggz.modules.d/kdegames

%files core
%_K4apps/kdegames
%_K4apps/carddecks
%_K4apps/kmahjongglib
%_K4iconsdir/oxygen/*/actions/lastmoves.*
%_K4iconsdir/oxygen/*/actions/legalmoves.*
%_K4conf/kcardtheme.knsrc
#%exclude %_sysconfdir/ggz.modules

%files kajongg
%ifdef _kde_alternate_placement
%_kde4_bindir/kajongg
%_kde4_bindir/kajonggserver
%_kde4_xdg_apps/kajongg.desktop
%_kde4_iconsdir/hicolor/*/apps/kajongg.*
%_kde4_iconsdir/hicolor/*/actions/games-kajongg-law.*
%else
%_K4bindir/kajongg
%_K4bindir/kajonggserver
%_K4xdg_apps/kajongg.desktop
%_K4iconsdir/hicolor/*/apps/kajongg.*
%_K4iconsdir/hicolor/*/actions/games-kajongg-law.*
%endif
%_K4apps/kajongg
%_K4doc/*/kajongg

%files palapeli
%ifdef _kde_alternate_placement
%_kde4_bindir/palapeli
%_kde4_xdg_apps/palapeli.desktop
%_kde4_iconsdir/hicolor/*/apps/palapeli.*
%_kde4_iconsdir/hicolor/*/mimetypes/application-x-palapeli.*
%else
%_K4bindir/palapeli
%_K4xdg_apps/palapeli.desktop
%_K4iconsdir/hicolor/*/apps/palapeli.*
%_K4iconsdir/hicolor/*/mimetypes/application-x-palapeli.*
%endif
%_K4lib/palapeli_*.so
%_K4lib/palathumbcreator.so
%_K4apps/palapeli
%_K4srv/ServiceMenus/palapeli_servicemenu.desktop
%_K4srv/palapeli_*.desktop
%_K4srv/palathumbcreator.desktop
%_K4srvtyp/libpala-slicerplugin.desktop
%_K4xdg_mime/palapeli-mimetypes.xml
%_K4conf/palapeli-collectionrc
%_K4doc/*/palapeli

%files kigo
%ifdef _kde_alternate_placement
%_kde4_bindir/kigo
%_kde4_xdg_apps/kigo.desktop
%_kde4_iconsdir/hicolor/*/*/kigo.*
%else
%_K4bindir/kigo
%_K4xdg_apps/kigo.desktop
%_K4iconsdir/hicolor/*/*/kigo.*
%endif
%_K4apps/kigo
%_K4cfg/kigo.kcfg
%_K4conf/kigo-games.knsrc
%_K4conf/kigo.knsrc
%_K4doc/*/kigo

%files granatier
%ifdef _kde_alternate_placement
%_kde4_bindir/granatier
%_kde4_xdg_apps/granatier.desktop
%_kde4_iconsdir/hicolor/*/*/granatier.*
%else
%_K4bindir/granatier
%_K4xdg_apps/granatier.desktop
%_K4iconsdir/hicolor/*/*/granatier.*
%endif
%_K4apps/granatier
%_K4cfg/granatier.kcfg
%_K4doc/*/granatier

%files ktron
%ifdef _kde_alternate_placement
%_kde4_bindir/ktron
%_kde4_xdg_apps/ktron.desktop
%_kde4_iconsdir/hicolor/*/*/ktron.png
%else
%_K4bindir/ktron
%_K4xdg_apps/ktron.desktop
%_K4iconsdir/hicolor/*/*/ktron.png
%endif
%_K4apps/ktron
%_K4cfg/ktron.kcfg
%_K4conf/ktron.knsrc
%_K4doc/en/ktron
#
%ifdef _kde_alternate_placement
%_kde4_bindir/kdesnake
%_kde4_xdg_apps/kdesnake.desktop
%_kde4_iconsdir/hicolor/*/*/kdesnake.*
%else
%_K4bindir/kdesnake
%_K4xdg_apps/kdesnake.desktop
%_K4iconsdir/hicolor/*/*/kdesnake.*
%endif

%files kapman
%ifdef _kde_alternate_placement
%_kde4_bindir/kapman
%_kde4_xdg_apps/kapman.desktop
%_kde4_iconsdir/hicolor/*/apps/kapman.*
%else
%_K4bindir/kapman
%_K4xdg_apps/kapman.desktop
%_K4iconsdir/hicolor/*/apps/kapman.*
%endif
%_K4apps/kapman/
%_K4snd/kapman/
%_K4doc/en/kapman

%files bomber
%ifdef _kde_alternate_placement
%_kde4_bindir/bomber
%_kde4_xdg_apps/bomber.desktop
%_kde4_iconsdir/hicolor/*/apps/bomber.*
%else
%_K4bindir/bomber
%_K4xdg_apps/bomber.desktop
%_K4iconsdir/hicolor/*/apps/bomber.*
%endif
%_K4apps/bomber/
%_K4cfg/bomber.kcfg
%_K4doc/*/bomber

%files killbots
%ifdef _kde_alternate_placement
%_kde4_bindir/killbots
%_kde4_xdg_apps/killbots.desktop
%_kde4_iconsdir/hicolor/*/apps/killbots.*
%else
%_K4bindir/killbots
%_K4xdg_apps/killbots.desktop
%_K4iconsdir/hicolor/*/apps/killbots.*
%endif
%_K4apps/killbots/
%_K4cfg/killbots.kcfg
%_K4doc/*/killbots/

%files kgoldrunner
%ifdef _kde_alternate_placement
%_kde4_bindir/kgoldrunner
%_kde4_xdg_apps/KGoldrunner.desktop
%_kde4_iconsdir/hicolor/*/apps/kgoldrunner.png
%else
%_K4bindir/kgoldrunner
%_K4xdg_apps/KGoldrunner.desktop
%_K4iconsdir/hicolor/*/apps/kgoldrunner.png
%endif
%_K4conf/kgoldrunner.knsrc
%_K4apps/kgoldrunner/
%_K4doc/*/kgoldrunner

%files katomic
%ifdef _kde_alternate_placement
%_kde4_bindir/katomic
%_kde4_xdg_apps/katomic.desktop
%_kde4_iconsdir/hicolor/*/apps/katomic.png
%else
%_K4bindir/katomic
%_K4xdg_apps/katomic.desktop
%_K4iconsdir/hicolor/*/apps/katomic.png
%endif
%_K4doc/*/katomic
%_K4apps/katomic
%_K4conf_update/katomic-*
%_K4conf/katomic.knsrc

%files kblackbox
%ifdef _kde_alternate_placement
%_kde4_bindir/kblackbox
%_kde4_xdg_apps/kblackbox.desktop
%_kde4_iconsdir/hicolor/*/apps/kblackbox.png
%else
%_K4bindir/kblackbox
%_K4xdg_apps/kblackbox.desktop
%_K4iconsdir/hicolor/*/apps/kblackbox.png
%endif
%_K4apps/kblackbox/
%_K4doc/*/kblackbox

%files ktuberling
%ifdef _kde_alternate_placement
%_kde4_bindir/ktuberling
%_kde4_xdg_apps/ktuberling.desktop
%_kde4_iconsdir/hicolor/*/apps/ktuberling.*
%_kde4_iconsdir/hicolor/*/mimetypes/application-x-tuberling.*
%else
%_K4bindir/ktuberling
%_K4xdg_apps/ktuberling.desktop
%_K4iconsdir/hicolor/*/apps/ktuberling.*
%_K4iconsdir/hicolor/*/mimetypes/application-x-tuberling.*
%endif
%_K4apps/ktuberling/
%_K4doc/*/ktuberling

%files kbounce
%ifdef _kde_alternate_placement
%_kde4_bindir/kbounce
%_kde4_xdg_apps/kbounce.desktop
%_kde4_iconsdir/hicolor/*/apps/kbounce.*
%else
%_K4bindir/kbounce
%_K4xdg_apps/kbounce.desktop
%_K4iconsdir/hicolor/*/apps/kbounce.*
%endif
%_K4apps/kbounce/
%_K4doc/*/kbounce

%files kspaceduel
%ifdef _kde_alternate_placement
%_kde4_bindir/kspaceduel
%_kde4_xdg_apps/kspaceduel.desktop
%_kde4_iconsdir/hicolor/*/apps/kspaceduel.png
%else
%_K4bindir/kspaceduel
%_K4xdg_apps/kspaceduel.desktop
%_K4iconsdir/hicolor/*/apps/kspaceduel.png
%endif
%_K4apps/kspaceduel/
%_K4doc/*/kspaceduel
%_K4cfg/kspaceduel.kcfg

%files kreversi
%ifdef _kde_alternate_placement
%_kde4_bindir/kreversi
%_kde4_xdg_apps/kreversi.desktop
%_kde4_iconsdir/hicolor/*/apps/kreversi.png
%else
%_K4bindir/kreversi
%_K4xdg_apps/kreversi.desktop
%_K4iconsdir/hicolor/*/apps/kreversi.png
%endif
%_K4apps/kreversi/
%_K4doc/*/kreversi

%files kolf
%ifdef _kde_alternate_placement
%_kde4_bindir/kolf
%_kde4_xdg_apps/kolf.desktop
%_kde4_iconsdir/hicolor/*/apps/kolf.png
%else
%_K4bindir/kolf
%_K4xdg_apps/kolf.desktop
%_K4iconsdir/hicolor/*/apps/kolf.png
%endif
%_K4apps/kolf/
%_K4doc/*/kolf

%files konquest
%ifdef _kde_alternate_placement
%_kde4_bindir/konquest
%_kde4_xdg_apps/konquest.desktop
%_kde4_iconsdir/hicolor/*/apps/konquest.png
%else
%_K4bindir/konquest
%_K4xdg_apps/konquest.desktop
%_K4iconsdir/hicolor/*/apps/konquest.png
%endif
%_K4apps/konquest/
%_K4doc/*/konquest

%files ksame
%ifdef _kde_alternate_placement
%_kde4_bindir/klickety
%_kde4_xdg_apps/ksame.desktop
%_kde4_xdg_apps/klickety.desktop
%_kde4_iconsdir/hicolor/*/apps/ksame.*
%_kde4_iconsdir/hicolor/*/apps/klickety.*
%else
%_K4bindir/klickety
%_K4xdg_apps/ksame.desktop
%_K4xdg_apps/klickety.desktop
%_K4iconsdir/hicolor/*/apps/ksame.*
%_K4iconsdir/hicolor/*/apps/klickety.*
%endif
%_K4apps/klickety
%_K4doc/*/klickety
%_K4conf_update/klickety*

%files kmahjongg
%ifdef _kde_alternate_placement
%_kde4_bindir/kmahjongg
%_kde4_xdg_apps/kmahjongg.desktop
%_kde4_iconsdir/hicolor/*/apps/kmahjongg.*
%else
%_K4bindir/kmahjongg
%_K4xdg_apps/kmahjongg.desktop
%_K4iconsdir/hicolor/*/apps/kmahjongg.*
%endif
%_K4apps/kmahjongg/
%_K4doc/*/kmahjongg
%_K4cfg/kmahjongg.kcfg

%files kbattleship
%ifdef _kde_alternate_placement
%_kde4_bindir/kbattleship
%_kde4_xdg_apps/kbattleship.desktop
%_kde4_iconsdir/hicolor/*/apps/kbattleship.png
%else
%_K4bindir/kbattleship
%_K4xdg_apps/kbattleship.desktop
%_K4iconsdir/hicolor/*/apps/kbattleship.png
%endif
%_K4apps/kbattleship/
%_K4srv/kbattleship.protocol
%_K4doc/*/kbattleship

%files kiriki
%ifdef _kde_alternate_placement
%_kde4_bindir/kiriki
%_kde4_xdg_apps/kiriki.desktop
%_kde4_iconsdir/hicolor/*/apps/kiriki.png
%else
%_K4bindir/kiriki
%_K4xdg_apps/kiriki.desktop
%_K4iconsdir/hicolor/*/apps/kiriki.png
%endif
%_K4apps/kiriki/
%_K4doc/*/kiriki

%if_enabled ksudoku
%files ksudoku
%ifdef _kde_alternate_placement
%_kde4_bindir/ksudoku
%_kde4_xdg_apps/ksudoku.desktop
%_kde4_iconsdir/hicolor/*/apps/ksudoku.*
%else
%_K4bindir/ksudoku
%_K4xdg_apps/ksudoku.desktop
%_K4iconsdir/hicolor/*/apps/ksudoku.*
%endif
%_K4apps/ksudoku/
%_K4conf/ksudokurc
%_K4doc/*/ksudoku
%else
%exclude %_K4doc/*/ksudoku
%endif

%files bovo
%ifdef _kde_alternate_placement
%_kde4_bindir/bovo
%_kde4_xdg_apps/bovo.desktop
%_kde4_iconsdir/hicolor/*/apps/bovo.*
%else
%_K4bindir/bovo
%_K4xdg_apps/bovo.desktop
%_K4iconsdir/hicolor/*/apps/bovo.*
%endif
%_K4apps/bovo/
%_K4doc/*/bovo

%files kjumpingcube
%ifdef _kde_alternate_placement
%_kde4_bindir/kjumpingcube
%_kde4_xdg_apps/kjumpingcube.desktop
%_kde4_iconsdir/hicolor/*/apps/kjumpingcube.png
%else
%_K4bindir/kjumpingcube
%_K4xdg_apps/kjumpingcube.desktop
%_K4iconsdir/hicolor/*/apps/kjumpingcube.png
%endif
%_K4apps/kjumpingcube/
%_K4cfg/kjumpingcube.kcfg
%_K4doc/*/kjumpingcube

%files klines
%ifdef _kde_alternate_placement
%_kde4_bindir/klines
%_kde4_xdg_apps/klines.desktop
%_kde4_iconsdir/hicolor/*/apps/klines.png
%else
%_K4bindir/klines
%_K4xdg_apps/klines.desktop
%_K4iconsdir/hicolor/*/apps/klines.png
%endif
%_K4apps/klines/
%_K4doc/*/klines
%_K4cfg/klines.kcfg

%files kmines
%ifdef _kde_alternate_placement
%_kde4_bindir/kmines
%_kde4_xdg_apps/kmines.desktop
%_kde4_iconsdir/hicolor/*/apps/kmines.png
%else
%_K4bindir/kmines
%_K4xdg_apps/kmines.desktop
%_K4iconsdir/hicolor/*/apps/kmines.png
%endif
%_K4apps/kmines/
%_K4conf/kmines.knsrc
%_K4doc/*/kmines

%files knetwalk
%ifdef _kde_alternate_placement
%_kde4_bindir/knetwalk
%_kde4_xdg_apps/knetwalk.desktop
%_kde4_iconsdir/hicolor/*/apps/knetwalk.*
%else
%_K4bindir/knetwalk
%_K4xdg_apps/knetwalk.desktop
%_K4iconsdir/hicolor/*/apps/knetwalk.*
%endif
%_K4apps/knetwalk/
%_K4doc/*/knetwalk

%files kpat
%ifdef _kde_alternate_placement
%_kde4_bindir/kpat
%_kde4_xdg_apps/kpat.desktop
%_kde4_iconsdir/hicolor/*/apps/kpat.*
%else
%_K4bindir/kpat
%_K4xdg_apps/kpat.desktop
%_K4iconsdir/hicolor/*/apps/kpat.*
%endif
#%_K4apps/kconf_update/kpat_update_cardwidth.upd
%_K4apps/kpat
%_K4doc/*/kpat
%_K4cfg/kpat.kcfg
%_K4conf/kpat.knsrc

%files kshisen
%ifdef _kde_alternate_placement
%_kde4_bindir/kshisen
%_kde4_xdg_apps/kshisen.desktop
%_kde4_iconsdir/hicolor/*/apps/kshisen.png
%else
%_K4bindir/kshisen
%_K4xdg_apps/kshisen.desktop
%_K4iconsdir/hicolor/*/apps/kshisen.png
%endif
%_K4apps/kshisen/
%_K4snd/kshisen
%_K4cfg/kshisen.kcfg
%_K4doc/*/kshisen

%files ksquares
%ifdef _kde_alternate_placement
%_kde4_bindir/ksquares
%_kde4_xdg_apps/ksquares.desktop
%_kde4_iconsdir/hicolor/*/apps/ksquares.png
%else
%_K4bindir/ksquares
%_K4xdg_apps/ksquares.desktop
%_K4iconsdir/hicolor/*/apps/ksquares.png
%endif
%_K4apps/ksquares/
%_K4cfg/ksquares.kcfg
%_K4doc/*/ksquares

%files kfourinline
%ifdef _kde_alternate_placement
%_kde4_bindir/kfourinline
%_kde4_bindir/kfourinlineproc
%_kde4_xdg_apps/kfourinline.desktop
%_kde4_iconsdir/hicolor/*/apps/kfourinline.png
%else
%_K4bindir/kfourinline
%_K4bindir/kfourinlineproc
%_K4xdg_apps/kfourinline.desktop
%_K4iconsdir/hicolor/*/apps/kfourinline.png
%endif
%_K4apps/kfourinline/
%_K4doc/*/kfourinline
%_K4cfg/kwin4.kcfg

%files lskat
%ifdef _kde_alternate_placement
%_kde4_bindir/lskat
%_kde4_xdg_apps/lskat.desktop
%_kde4_iconsdir/hicolor/*/apps/lskat.png
%else
%_K4bindir/lskat
%_K4xdg_apps/lskat.desktop
%_K4iconsdir/hicolor/*/apps/lskat.png
%endif
%_K4apps/lskat/
%_K4doc/*/lskat

%files kdiamond
%ifdef _kde_alternate_placement
%_kde4_bindir/kdiamond
%_kde4_xdg_apps/kdiamond.desktop
%_kde4_iconsdir/hicolor/*/*/kdiamond.*
%else
%_K4bindir/kdiamond
%_K4xdg_apps/kdiamond.desktop
%_K4iconsdir/hicolor/*/*/kdiamond.*
%endif
%_K4apps/kdiamond/
%_K4conf/kdiamond.knsrc
%_K4snd/KDiamond-Stone-*.ogg
%_K4doc/*/kdiamond

%files kollision
%ifdef _kde_alternate_placement
%_kde4_bindir/kollision
%_kde4_xdg_apps/kollision.desktop
%_kde4_iconsdir/hicolor/*/apps/kollision.*
%else
%_K4bindir/kollision
%_K4xdg_apps/kollision.desktop
%_K4iconsdir/hicolor/*/apps/kollision.*
%endif
%_K4apps/kollision/
%_K4iconsdir/oxygen/*/apps/kollision.*
%_K4doc/*/kollision

%files kubrick
%ifdef _kde_alternate_placement
%_kde4_bindir/kubrick
%_kde4_xdg_apps/kubrick.desktop
%_kde4_iconsdir/hicolor/*/apps/kubrick.*
%else
%_K4bindir/kubrick
%_K4xdg_apps/kubrick.desktop
%_K4iconsdir/hicolor/*/apps/kubrick.*
%endif
%_K4apps/kubrick/
%_K4doc/*/kubrick

%files kblocks
%ifdef _kde_alternate_placement
%_kde4_bindir/kblocks
%_kde4_xdg_apps/kblocks.desktop
%_kde4_iconsdir/hicolor/*/apps/kblocks.*
%else
%_K4bindir/kblocks
%_K4xdg_apps/kblocks.desktop
%_K4iconsdir/hicolor/*/apps/kblocks.*
%endif
%_K4apps/kblocks/
%_K4cfg/kblocks.kcfg
%_K4conf/kblocks.knsrc
%_K4doc/en/kblocks

%files kbreakout
%ifdef _kde_alternate_placement
%_kde4_bindir/kbreakout
%_kde4_xdg_apps/kbreakout.desktop
%_kde4_iconsdir/hicolor/*/apps/kbreakout.png
%else
%_K4bindir/kbreakout
%_K4xdg_apps/kbreakout.desktop
%_K4iconsdir/hicolor/*/apps/kbreakout.png
%endif
%_K4apps/kbreakout/
%_K4doc/*/kbreakout

%files ksirk
%ifdef _kde_alternate_placement
%_kde4_bindir/ksirk
%_kde4_bindir/ksirkskineditor
%_kde4_xdg_apps/ksirk.desktop
%_kde4_xdg_apps/ksirkskineditor.desktop
%_kde4_iconsdir/hicolor/*/apps/ksirk.*
%_kde4_iconsdir/locolor/*/apps/ksirk.*
%else
%_K4bindir/ksirk
%_K4bindir/ksirkskineditor
%_K4xdg_apps/ksirk.desktop
%_K4xdg_apps/ksirkskineditor.desktop
%_K4iconsdir/hicolor/*/apps/ksirk.*
%_K4iconsdir/locolor/*/apps/ksirk.*
%endif
%_K4conf/ksirk.knsrc
%_K4cfg/ksirksettings.kcfg
%_K4cfg/ksirkskineditorsettings.kcfg
%_K4apps/ksirk/
%_K4apps/ksirkskineditor/
%_K4doc/en/ksirk
%_K4doc/en/ksirkskineditor

%files -n libkdegames4
%_K4libdir/libkdegames.so.*
%files -n libkmahjongglib4
%_K4libdir/libkmahjongglib.so.*
%files -n libkolfprivate4
%_K4libdir/libkolfprivate.so.*
%files -n libkggzgames4
%_K4libdir/libkggzgames.so.*
%files -n libkggzmod4
%_K4libdir/libkggzmod.so.*
%files -n libkggznet4
%_K4libdir/libkggznet.so.*
%files -n libiris4_ksirk
%_K4libdir/libiris_ksirk.so.*
%files -n libpala4
%_K4libdir/libpala.so.*
%files -n libkcardgame4
%_K4libdir/libkcardgame.so

%files devel
%_K4apps/cmake/modules/*
%_K4libdir/libpala
%_K4link/*.so
%_K4includedir/*

%changelog
* Thu May 03 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.3-alt1
- new version

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt0.M60P.1
- built for M60P

* Thu Apr 12 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.2-alt1
- new version

* Wed Apr 04 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt0.M60P.1
- built for M60P

* Tue Mar 13 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.1-alt1
- new version

* Fri Jan 27 2012 Sergey V Turchin <zerg@altlinux.org> 4.8.0-alt1
- new version

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt0.M60P.1
- build for M60P

* Mon Dec 05 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.4-alt1
- new version

* Mon Nov 07 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt1.1
- Rebuild with Python-2.7

* Thu Nov 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt0.M60P.1
- built for M60P

* Wed Nov 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.3-alt1
- new version

* Tue Oct 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt0.M60T.1
- built for M60T

* Mon Oct 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.2-alt1
- new version

* Sun Sep 18 2011 Sergey V Turchin <zerg@altlinux.org> 4.7.1-alt1
- new version

* Wed Jul 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.5-alt1
- new version

* Fri Jun 10 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.4-alt1
- new version
- move kmahjongglib data to core subpackage (ALT#25679)

* Fri May 06 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.3-alt1
- new version

* Fri Apr 08 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.2-alt1
- new version

* Thu Mar 03 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.1-alt1
- new version

* Wed Feb 16 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt2
- obsolete kdegames-klickety

* Wed Feb 02 2011 Sergey V Turchin <zerg@altlinux.org> 4.6.0-alt1
- new version

* Wed Jan 19 2011 Sergey V Turchin <zerg@altlinux.org> 4.5.5-alt1
- new version

* Wed Dec 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.4-alt1
- new version

* Tue Nov 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt3
- fix conflict with kdegames-kblackbox (ALT#24671)

* Tue Nov 23 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt2
- obsolete kdegames

* Wed Nov 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.3-alt1
- new version

* Thu Oct 07 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.2-alt1
- new version

* Wed Sep 01 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.1-alt1
- new version

* Mon Aug 09 2010 Sergey V Turchin <zerg@altlinux.org> 4.5.0-alt1
- new version

* Thu Jul 08 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt0.M51.1
- built for M51

* Mon Jul 05 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.5-alt1
- new version

* Thu Jun 03 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt0.M51.1
- built for M51

* Wed Jun 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.4-alt1
- new version

* Thu May 13 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt0.M51.1
- built for M51

* Wed May 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.3-alt1
- new version

* Wed Apr 21 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt0.M51.1
- built for M51

* Tue Mar 30 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.2-alt1
- new version

* Tue Mar 02 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.1-alt1
- new version

* Fri Feb 12 2010 Sergey V Turchin <zerg@altlinux.org> 4.4.0-alt1
- new version

* Thu Jan 28 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.95-alt1
- new version

* Mon Jan 25 2010 Sergey V Turchin <zerg@altlinux.org> 4.3.90-alt1
- new version

* Tue Dec 15 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt0.M51.1
- built for M51

* Tue Dec 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.4-alt1
- new version

* Mon Nov 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt0.M51.1
- built for M51

* Thu Nov 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.3-alt1
- new version

* Mon Oct 12 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.2-alt1
- new version

* Tue Sep 01 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.1-alt1
- new version

* Wed Aug 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.3.0-alt1
- 4.3.0

* Thu Jul 23 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.98-alt1
- 4.2.98

* Fri Jul 17 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.96-alt1
- 4.2.96

* Mon Jun 22 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt0.M50.1
- built for M50

* Tue Jun 09 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.4-alt1
- new version

* Tue May 05 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.3-alt1
- new version

* Mon Apr 06 2009 Sergey V Turchin <zerg@altlinux.org> 4.2.2-alt1
- new version

* Thu Mar 05 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.1-alt1
- new version

* Wed Jan 28 2009 Sergey V Turchin <zerg at altlinux dot org> 4.2.0-alt1
- new version

* Tue Jan 20 2009 Sergey V Turchin <zerg at altlinux dot org> 4.1.96-alt1
- new version

* Fri Nov 07 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.3-alt1
- new version

* Tue Oct 21 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt2
- fix requires

* Mon Oct 20 2008 Sergey V Turchin <zerg at altlinux dot org> 4.1.2-alt1
- initial specfile

