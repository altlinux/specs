%define _oldname gnome2-games
%define ver_major 3.4
%define extradata_ver_major 3.2
%define extradata_ver %extradata_ver_major.0
%def_without extradata
%def_enable clutter
%def_enable introspection
%def_disable static
#  swell-foop, lightsoff
%def_enable staging

Name: gnome-games
Version: %ver_major.2
Release: alt2

Summary: GNOME games
License: %gpl2plus
Group: Graphical desktop/GNOME
URL: http://www.gnome.org/

Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
Source1: ftp://ftp.gnome.org/pub/gnome/sources/%name-extra-data/%extradata_ver_major/%name-extra-data-%extradata_ver.tar.xz
Patch: %name-3.3.92-gir.patch
# https://launchpadlibrarian.net/106290229/04_fix-segfault.patch
Patch1: %name-glines-3.4.2-segfault.patch

Obsoletes: %_oldname < 2.14
Provides: %_oldname = %version-%release

%define gtk_ver 3.3.11
%define gnome_common_ver 2.16.0

Requires: %name-glines = %version-%release
Requires: %name-gnect = %version-%release
Requires: %name-gnibbles = %version-%release
Requires: %name-gnobots = %version-%release
Requires: %name-quadrapassel = %version-%release
Requires: %name-gnomine = %version-%release
Requires: %name-gnotravex = %version-%release
Requires: %name-gnotski = %version-%release
Requires: %name-gtali = %version-%release
Requires: %name-iagno = %version-%release
Requires: %name-mahjongg = %version-%release
%{?_enable_staging:Requires: %name-swell-foop = %version-%release}
Requires: %name-sudoku = %version-%release
Requires: %name-glchess = %version-%release
%{?_enable_staging:Requires: %name-lightsoff = %version-%release}

BuildPreReq: rpm-build-licenses

# From configure.in
BuildPreReq: intltool >= 0.35.0
BuildPreReq: libstdc++-devel gcc-c++
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: librsvg-devel >= 2.32.0
BuildPreReq: libcairo-gobject-devel >= 1.0
BuildPreReq: gstreamer-devel >= 0.10.11
BuildRequires: libcanberra-gtk3-devel
BuildPreReq: libclutter-devel >= 1.0 libclutter-gtk3-devel >= 0.9.8
BuildRequires: gnome-common >= %gnome_common_ver yelp-tools xmllint itstool
BuildRequires: python-devel python-modules-compiler python-module-pygobject-devel
BuildRequires: guile18-devel libSM-devel libgcrypt-devel libcheck-devel libsqlite3-devel libGLU-devel zlib-devel
BuildRequires: vala >= 0.15.1 vala-tools
# GObject introspection support
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel libclutter-gir-devel libjson-glib-gir-devel}

%description
GNOME (GNU Network Object Model Environment) is a user-friendly set of
applications and desktop tools to be used in conjunction with a window
manager for the X Window System.  GNOME is similar in purpose and scope
to CDE and KDE, but GNOME is based completely on free software.
The gnome-games package containes a collection of simple games for your
amusement.

		games which are easy to play with the aid of a mouse.
Glines:         color lines game, aka fiveormore
Gnect:          four in a row game
Gnibbles:       snake game up to four players
Gnobots:        old bsd robots game improved
GNOME Klotski:  game based on the not so popular Klotski
GNOME Mine:     popular logic puzzle minesweeper
GNOME Tali:     sort of poker with dice and less money
Quadrapassel:   GNOME version of the popular russian game Tetris, in past quadrapassel
Iagno:          GNOME version of the popular Othello
Mahjongg:       GNOME version of the classic Eastern tile game, Mahjongg
swell-foop:     in past Same GNOME, game which goal is to remove as many balls in as few moves as,
		possible
GNOME Sudoku:   a logic game with a Japanese name
GlChess:	a chess game which supports several chess engines.

%package common
Summary: Common files for GNOME games
Group: Graphical desktop/GNOME
BuildArch: noarch
Obsoletes: %_oldname-common < 2.14
Provides: %_oldname-common = %version-%release
Obsoletes: %name-xbill
Obsoletes: %name-freecell
Obsoletes: %name-gataxx
Obsoletes: %name-blackjack
Obsoletes: libgdkcardimage

%description common
This package contains common files needed to run GNOME games.

%package glines
Summary: A version of the color lines program
Group: Games/Boards
Obsoletes: %_oldname-glines < 2.14
PreReq: %name-common = %version-%release

%description glines
Glines, is the Gnome port of the once popular Windows game called Color
Lines. The game's objective is to align as often as possible five balls
or more of the same color causing them to disappear, play as long as
possible, and be #1 in the High Scores.

%package gnect
Summary: Four in a row game
Group: Games/Boards
Obsoletes: %_oldname-gnect < 2.14
PreReq: %name-common = %version-%release

%description gnect
Gnect is a four-in-a-row game for the GNOME Project. The object of the
game is to build a line of four of your marbles while trying to stop
your opponent (human or computer) building a line of his or her own. A
line can be horizontal, vertical or diagonal.

%package gnibbles
Summary: A cute little game that has no description
Group: Games/Boards
Obsoletes: %_oldname-gnibbles < 2.14
PreReq: %name-common = %version-%release

%description  gnibbles
Gnibbles is a game where the user controls a snake. The snake moves
around the board, eating diamonds while avoiding the walls placed around
it.

%package gnobots
Summary: Second Gnome version of robots game for BSD games collection
Group: Games/Boards
Obsoletes: %_oldname-gnobots < 2.14
Obsoletes: %name-gnobots2 < 2.15
Provides: %name-gnobots2 = %version-%release
PreReq: %name-common = %version-%release

%description gnobots
GNOME Robots II is a development of the original Gnome Robots game which
was itself based on the text based robots game which can be found on a
number of UNIX systems, and comes with the BSD games package on Linux
systems.

%package quadrapassel
Summary: A tetris clone.
Group: Games/Boards
Obsoletes: %_oldname-gnometris < 2.14
Obsoletes: %name-gnometris
PreReq: %name-common = %version-%release

%description quadrapassel
GNOME version of the popular russian game Tetris.

%package gnomine
Summary: Classic find the mines in the minefield game
Group: Games/Boards
Obsoletes: %_oldname-gnomine < 2.14
PreReq: %name-common = %version-%release

%description gnomine
GNOME Mines is a variation of the popular logic puzzle minesweeper.

%package gnotravex
Summary: A game based on Tetravex.
Group: Games/Boards
Obsoletes: %_oldname-gnotravex < 2.14
PreReq: %name-common = %version-%release

%description gnotravex
GNOME Tetravex is a simple puzzle where pieces must be positioned so
that the same numbers are touching each other. Your game is timed, these
times are stored in a system-wide scoreboard.

%package gnotski
Summary: Derivative game from Klotski.
Group: Games/Boards
Obsoletes: %_oldname-gnotski < 2.14
PreReq: %name-common = %version-%release

%description gnotski
Gnome Klotski is a small game for GNOME. The idea is originally
from a game called "Klotski".

%package gtali
Summary: Gnome version of Yahtzee Dice Game
Group: Games/Boards
Obsoletes: %_oldname-gtali < 2.14
PreReq: %name-common = %version-%release

%description gtali
Gnome Tali is a sort of poker with dice and less money. You roll five
dice three times and try to create the best hand. Your two rerolls may
include any or all of your dice.

%package iagno
Summary: Gnome version of Othello (Reversi) board game
Group: Games/Boards
Obsoletes: %_oldname-iagno < 2.14
PreReq: %name-common = %version-%release

%description iagno
Iagno is a computer version of the game Reversi, more popularly called
Othello.

%package lightsoff
Summary: Lights Off is a puzzle game
Group: Games/Boards
PreReq: %name-common = %version-%release
Requires: %name-gir = %version-%release
Requires: seed

%description lightsoff
Lights Off is a puzzle game, where the objective is to turn off all of
the tiles on the board. Each click toggles the state of the clicked tile
and its non-diagonal neighbors

%package mahjongg
Summary: Classic Chinese Tile Game
Group: Games/Boards
Obsoletes: %_oldname-mahjongg < 2.14
PreReq: %name-common = %version-%release

%description mahjongg
Gnome Mahjongg, or Mahjongg for short, is a solitaire (one player)
version of the classic Eastern tile game, Mahjongg.

%package swell-foop
Summary: The "Same Game" puzzle
Group: Games/Boards
Obsoletes: %_oldname-same < 2.14
Obsoletes: %name-same
PreReq: %name-common = %version-%release

%description swell-foop
The objective of same-gnome is to remove as many balls from the playing
area in as few moves as possible.

%package sudoku
Summary: GNOME Sudoku game
Group: Games/Boards
BuildArch: noarch
PreReq: %name-common = %version-%release

%description sudoku
Sudoku is a logic game with a Japanese name that has recently exploded
in popularity.

%package glchess
Summary: A chess game for GNOME
Group: Games/Boards
PreReq: %name-common = %version-%release
# Add chess to requirements to be sure it is possible to play with computer
Requires: chess

%description glchess
A chess game which supports several chess engines, with 2D and optionally
3D support if OpenGL is present.

%package gir
Summary: GObject introspection support for the GNOME games
Group: System/Libraries
Requires: %name-common = %version-%release

%description gir
GObject introspection data for the GNOME games

%package gir-devel
Summary: GObject introspection devel data for the GNOME games
Group: System/Libraries
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GNOME games

%prep
%setup -a1
%patch -b .gir
%patch1

# fix extra-data install paths
#subst 's|\(pixmapdir = \$(datadir)/\)gnome-games/|\1|
#	s|\(themedir = \$(datadir)/\)gnome-games/|\1|' %name-extra-data-%extradata_ver/*/Makefile.am

%build
%autoreconf
%configure \
    --disable-schemas-compile \
    --enable-setgid \
    --with-scores-group=games \
    --with-scores-user=games \
    %{subst_enable static} \
    %{subst_enable introspection} \
    %{subst_enable staging}

%make_build

# build gnome-games-extra-data
pushd %name-extra-data-%extradata_ver
%autoreconf
%configure
%make_build
popd

%install
%makeinstall_std

%if_with extradata
# install gnome-games-extra-data
pushd %name-extra-data-%extradata_ver
%makeinstall_std
popd
%endif

%define games quadrapassel lightsoff gnect gnomine swell-foop mahjongg gtali gnotravex gnotski glines iagno gnobots2 gnibbles gnome-sudoku glchess

%find_lang --with-gnome %name %games

%files

%files common -f %name.lang
%dir %_datadir/%name
%config %_datadir/glib-2.0/schemas/org.gnome.Games.WindowState.gschema.xml
%doc AUTHORS TODO NEWS

%files glines -f glines.lang
%attr(2711,root,games) %_bindir/glines
%_datadir/glines/
#%_datadir/%name/glines
%_desktopdir/glines.desktop
%_iconsdir/hicolor/*x*/apps/glines.png
%_iconsdir/hicolor/scalable/apps/glines.svg
%_man6dir/glines*
%config %_datadir/glib-2.0/schemas/org.gnome.glines.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/glines*

%files gnect -f gnect.lang
%attr(-,root,games) %_bindir/gnect
%_desktopdir/gnect.desktop
%_datadir/gnect/
%_iconsdir/hicolor/*x*/apps/gnect.png
%_iconsdir/hicolor/scalable/apps/gnect.svg
%_man6dir/gnect*
%config %_datadir/glib-2.0/schemas/org.gnome.gnect.gschema.xml

%files gnibbles -f gnibbles.lang
%attr(2711,root,games) %_bindir/gnibbles
%_desktopdir/gnibbles.desktop
%_datadir/gnibbles/
%_iconsdir/hicolor/*x*/apps/gnibbles.png
%_iconsdir/hicolor/scalable/apps/gnibbles.svg
%_man6dir/gnibbles*
%config %_datadir/glib-2.0/schemas/org.gnome.gnibbles.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gnibbles*

%files gnobots -f gnobots2.lang
%attr(2711,root,games) %_bindir/gnobots2
%_desktopdir/gnobots2.desktop
%_datadir/gnobots2/
#%_datadir/%name/gnobots2
%_iconsdir/hicolor/*x*/apps/gnobots2.png
%_iconsdir/hicolor/scalable/apps/gnobots2.svg
%_iconsdir/hicolor/*x*/actions/teleport-random.png
%_iconsdir/hicolor/*x*/actions/teleport.png
%_man6dir/gnobots2*
%config %_datadir/glib-2.0/schemas/org.gnome.gnobots2.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gnobots2*

%files quadrapassel -f quadrapassel.lang
%attr(2711,root,games) %_bindir/quadrapassel
%_desktopdir/quadrapassel.desktop
%_datadir/quadrapassel/
%_iconsdir/hicolor/*x*/apps/quadrapassel.png
%_iconsdir/hicolor/scalable/apps/quadrapassel.svg
%_man6dir/quadrapassel*
%config %_datadir/glib-2.0/schemas/org.gnome.quadrapassel.gschema.xml
%config(noreplace) %attr(0664,root,games) %_localstatedir/games/quadrapassel*

%files gnomine -f gnomine.lang
%attr(2711,root,games) %_bindir/gnomine
%_desktopdir/gnomine.desktop
%_datadir/gnomine/
%_iconsdir/hicolor/*x*/apps/gnomine.png
%_man6dir/gnomine*
%config %_datadir/glib-2.0/schemas/org.gnome.gnomine.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gnomine*

%files gnotravex -f gnotravex.lang
%attr(2711,root,games) %_bindir/gnotravex
%_desktopdir/gnotravex.desktop
%_datadir/gnotravex/
%_iconsdir/hicolor/*x*/apps/gnotravex.png
%_iconsdir/hicolor/scalable/apps/gnotravex.svg
%_man6dir/gnotravex*
%config %_datadir/glib-2.0/schemas/org.gnome.gnotravex.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gnotravex*

%files gnotski -f gnotski.lang
%attr(2711,root,games) %_bindir/gnotski
%_desktopdir/gnotski.desktop
%_datadir/gnotski/
%_iconsdir/hicolor/*x*/apps/gnotski.png
%_iconsdir/hicolor/scalable/apps/gnotski.svg
%_man6dir/gnotski*
%config %_datadir/glib-2.0/schemas/org.gnome.gnotski.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gnotski*

%files gtali -f gtali.lang
%attr(2711,root,games) %_bindir/gtali
%_desktopdir/gtali.desktop
%_datadir/gtali/
%_iconsdir/hicolor/*x*/apps/gtali.png
%_iconsdir/hicolor/scalable/apps/gtali.svg
%_man6dir/gtali*
%config %_datadir/glib-2.0/schemas/org.gnome.gtali.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/gtali*

%files iagno -f iagno.lang
%attr(-,root,games) %_bindir/iagno
%_desktopdir/iagno.desktop
%_datadir/iagno
#%_datadir/%name/iagno
%_iconsdir/hicolor/*x*/apps/iagno.png
#%_iconsdir/hicolor/scalable/apps/iagno.svg
%_man6dir/iagno*
%config %_datadir/glib-2.0/schemas/org.gnome.iagno.gschema.xml

%if_enabled staging
%files lightsoff -f lightsoff.lang
%attr(-,root,games) %_bindir/lightsoff
%_desktopdir/lightsoff.desktop
%_datadir/lightsoff/
%_iconsdir/hicolor/scalable/apps/lightsoff.svg
%config %_datadir/glib-2.0/schemas/org.gnome.lightsoff.gschema.xml
%endif

%files mahjongg -f mahjongg.lang
%attr(2711,root,games) %_bindir/mahjongg
%_desktopdir/mahjongg.desktop
%_datadir/mahjongg
#%_datadir/%name/mahjongg
%_iconsdir/hicolor/*x*/apps/mahjongg.png
%_iconsdir/hicolor/scalable/apps/mahjongg.svg
%_man6dir/mahjongg*
%config %_datadir/glib-2.0/schemas/org.gnome.mahjongg.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/mahjongg*

%if_enabled staging
%files swell-foop -f swell-foop.lang
%attr(-,root,games) %_bindir/swell-foop
%_desktopdir/swell-foop*
%_datadir/%name/swell-foop/
%_iconsdir/hicolor/*x*/apps/swell-foop.png
%_iconsdir/hicolor/scalable/apps/swell-foop.svg
%config %_datadir/glib-2.0/schemas/org.gnome.swell-foop.gschema.xml
%config(noreplace) %attr(0664,games,games) %_localstatedir/games/swell-foop.*
%endif

%files sudoku -f gnome-sudoku.lang
%attr(-,root,games) %_bindir/gnome-sudoku
%_desktopdir/gnome-sudoku.desktop
%_datadir/gnome-sudoku/
%python_sitelibdir_noarch/gnome_sudoku
%_iconsdir/hicolor/*x*/apps/gnome-sudoku.png
%_iconsdir/hicolor/scalable/apps/gnome-sudoku.svg
%_man6dir/gnome-sudoku*
%config %_datadir/glib-2.0/schemas/org.gnome.gnome-sudoku.gschema.xml

%files glchess -f glchess.lang
%attr(-,root,games) %_bindir/glchess
%_desktopdir/glchess.desktop
%_datadir/glchess/
%_iconsdir/hicolor/*x*/apps/glchess.png
%_iconsdir/hicolor/scalable/apps/glchess.svg
%_man6dir/glchess*
%config %_datadir/glib-2.0/schemas/org.gnome.glchess.gschema.xml

%if_enabled introspection
%files gir
%_libdir/%name/*.so.*
%_libdir/girepository-1.0/*

%files gir-devel
%_libdir/%name/*.so
%_datadir/gir-1.0/*
%exclude %_libdir/%name/*.la
%endif

%changelog
* Sat Jun 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt2
- fixed glines crash (GNOME bug #675628)

* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Mon Apr 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1
- moved org.gnome.Games.WindowState.gschema.xml to -common subpackage (ALT #27227)

* Tue Mar 27 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.2.0-alt1.1
- Rebuild with Python-2.7

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0

* Tue May 24 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 19 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Apr 19 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt4
- updated buildreqs

* Thu Mar 03 2011 Alexey Shabalin <shaba@altlinux.ru> 2.32.1-alt3
- updated buildreqs
- used new rpm-build-gir to find dependencies in *.js files

* Mon Jan 17 2011 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt2
- backported some patches from 2.91.x (in particulary fixed lightsoff,
  swell-foop crash)

* Tue Nov 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.1-alt1
- 2.32.1

* Mon Oct 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.32.0-alt1
- 2.32.0

* Tue Jun 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.2-alt1
- 2.30.2

* Tue May 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.1-alt1
- 2.30.1

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt2
- rebuild with new gnome-games-extradata

* Mon Mar 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.30.0-alt1
- 2.30.0

* Tue Mar 09 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.92-alt1
- 2.29.92

* Sat Mar 06 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt2
- fixed permissions for %_bindir/swell-foop
- added lightsoff into gnome-games virtual package
- rebuild using rpm-build-gir

* Fri Feb 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.29.91-alt1
- 2.29.91
- removed obsolete blackjack
- gnometris ranamed to quadrapassel and same-gnome to swell-foop
- new game -- lightsoff
- new gnome-games-gir{,-devel} subpackages

* Tue Feb 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt2
- build sudoku and glchess as noarch

* Thu Dec 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Tue Oct 20 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1

* Mon Sep 21 2009 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Mon Aug 17 2009 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90

* Tue Jun 30 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.3-alt1
- 2.26.3

* Tue May 19 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.2-alt1
- 2.26.2
- updated buildreqs

* Tue Apr 14 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.1-alt1
- 2.26.1

* Wed Mar 18 2009 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0
- updated buildreqs
- prepared to buid clutter-based lightsoff game (requires libclutter >= 0.8.8)

* Tue Jan 13 2009 Yuri N. Sedunov <aris@altlinux.org> 2.24.3-alt1
- 2.24.3

* Tue Nov 25 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.2-alt1
- 2.24.2
- removed obsolete %%post* scripts

* Tue Nov 04 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1.1-alt1
- 2.24.1.1
- don't package useless %%_libdir/gnome-games/gnome-games-render-cards
- build gnome-games-common as noarch

* Tue Oct 21 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.1-alt1
- 2.24.1

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.24.0-alt1
- 2.24.0

* Mon Jun 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.22.3-alt1
- 2.22.3

* Wed Apr 16 2008 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.22.1.1-alt1
- new version: 2.22.1.1

* Tue Mar 18 2008 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.22.0-alt1
- new version: 2.22.0

* Tue Dec 18 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.20.2-alt1
- new version: 2.20.2
- fixed a bug with gnome-games-common preun scriptlet

* Mon Nov 26 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.20.1-alt1
- new version: 2.20.1
- GlChess now requires python-module-pygtkglext (fixed #12872)
- do not skip usage of python req/prov autofind for sudoku subpackage

* Thu Sep 20 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.20.0.1-alt1
- new version: 2.20.0.1

* Tue Sep 18 2007 Egor Vyscrebentsov <evyscr@altlinux.ru> 2.18.2.1-alt1
- new version: 2.18.2.1
  + added GlChess
  + added Sudoku
  + removed Gataxx
- removed old patches
- prevented score files to be replaced while upgrading the package
- cleared sgid attribute on blackjack (fixed #12793)
- corrected .desktop categories for GTali and Iagno (fixed #12824)

* Thu Jul 05 2007 Igor Zubkov <icesik@altlinux.org> 2.16.3-alt2
- add Packager tag
- fix rebuild

* Fri Feb 02 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.3-alt1
- new version 2.16.3 (with rpmrb script)

* Sun Jan 21 2007 Alexey Rusakov <ktirf@altlinux.org> 2.16.2-alt1
- new version 2.16.2 (with rpmrb script)

* Sun Oct 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt2
- fixed a bug in gnome-games-gnobots install scripts

* Sat Oct 07 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.16.1-alt1
- new version (2.16.1)
- updated dependencies

* Thu Jul 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.15.5-alt1
- new version 2.15.5.
- updated filelists
- renamed gnome-games-gnobots2 into gnome-games-gnobots

* Sun Jul 02 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2.1-alt1
- new version 2.14.2.1 (with rpmrb script)

* Thu Jun 15 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Sun Apr 16 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.14.1-alt1
- new version (2.14.1)
- the package has been renamed from gnome2-games to gnome-games
- spec cleanup (bless --disable-schemas-install)
- added --disable-scrollkeeper to configure call, though it seems unfunctional yet.

* Sat Mar 04 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.8-alt2
- removed dangling Requires: gnome2-games-stones.

* Mon Feb 27 2006 Alexey Rusakov <ktirf@altlinux.ru> 2.13.8-alt1
- new version (2.13.8)
- buildreqs revised, spec cleanup
- removed Debian menu stuff
- no more GNOME Stones.

* Thu Nov 03 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt2
- Gnobots menu item has been moved from Arcade to Boards.

* Tue Oct 04 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.1-alt1
- new version

* Fri Sep 30 2005 Alexey Rusakov <ktirf@altlinux.ru> 2.12.0-alt1
- 2.12.0

* Mon Jun 13 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.1-alt1
- 2.10.1

* Fri Mar 11 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1.1
- rebuild against new python (2.4)

* Mon Mar 07 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.10.0-alt1
- 2.10.0

* Wed Mar 02 2005 Yuri N. Sedunov <aris@altlinux.ru> 2.9.7-alt1
- 2.9.7

* Thu Oct 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.1-alt1
- 2.8.1

* Mon Sep 13 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.8.0-alt1
- 2.8.0
- obsoletes libgdkcardimage.

* Thu Jun 24 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.2-alt1
- 2.6.2
- move BlackJack to Amusement/Cards in menu.

* Thu Jun 17 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1.1
- move gtali to Games/Boards (close #4351).
- fix sol (close #4370).
- fixed gnotravex menu.

* Wed Apr 21 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.1-alt1
- 2.6.1

* Thu Apr 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.6.0.1-alt1
- 2.6.0.1

* Mon Feb 23 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.7-alt1
- 2.5.7

* Mon Feb 16 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.5.6-alt1
- 2.5.6

* Wed Jan 28 2004 Yuri N. Sedunov <aris@altlinux.ru> 2.4.2-alt1
- 2.4.2
- do not package .la files.
- do not build libgdkcardimage-devel-static by default.

* Mon Oct 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.1-alt1
- 2.4.1

* Sat Sep 20 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.4.0-alt1
- 2.4.0

* Wed Aug 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.90-alt1
- 2.3.90

* Tue Aug 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.7-alt1
- 2.3.7

* Fri Jul 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.5-alt1
- 2.3.5

* Wed Jul 02 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.4-alt1
- 2.3.4

* Wed Jun 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.3-alt1
- 2.3.3
- new blackjack game.

* Mon May 19 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.3.2-alt1
- 2.3.2
- Obsoletes: xbill, freecell

* Thu Mar 13 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.1-alt1
- 2.2.1

* Tue Feb 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt3
- gnect schemas fixed. (#2152).

* Thu Jan 30 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt2
- fixed menus.
- libgdkcardimage requires newest libgnomeui.

* Tue Jan 21 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.2.0-alt1
- 2.2.0
- remove conflict gnome-xbill with original xBill game.

* Sat Jan 04 2003 Yuri N. Sedunov <aris@altlinux.ru> 2.1.5-alt1
- 2.1.5

* Fri Dec 20 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.4-alt1
- 2.1.4

* Tue Nov 26 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.3-alt1
- 2.1.3

* Sat Nov 02 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.2-alt1
- 2.1.2

* Wed Oct 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.1-alt1
- 2.1.1

* Sat Oct 05 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.1.0-alt1
- 2.1.0

* Mon Sep 30 2002 Stanislav Ievlev <inger@altlinux.ru> 2.0.4-alt1.2
- gnome2-games-mahjongg-2.0.4-alt1.1.i586.rpm: bad permisions in suid/sgid files

* Sun Sep 29 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1.1
- gnome2-games virtual package installs all games.
- gconf2_install macro used for schemas installation.
- scrollkeeper >= 0.3.11 added to requires list.

* Thu Sep 19 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt1
- 2.0.4
- each game splitted in separate package.

* Sun Jul 07 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.1-alt1
- First build games for for GNOME2.
