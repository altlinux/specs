%define ver_major 42
%define _name gnome-games

Name: %_name-full
Version: %ver_major.0
Release: alt1

Summary: GNOME games
License: %gpl2plus
Group: Graphical desktop/GNOME
URL: http://live.gnome.org/GnomeGames/

BuildArch: noarch

%define aisleriot_ver 3.22.22
%define atomix_ver 3.34.0
%define glines_ver 3.32.3
%define gnect_ver 3.38.1
%define hitori_ver 3.38.4
%define iagno_ver 3.38.1
%define klotski_ver 3.38.2
%define lightsoff_ver 40.0.1
%define mahjongg_ver 3.38.3
%define mines_ver 40.1
%define nibbles_ver 3.38.2
%define quadrapassel_ver 40.2
%define robots_ver 40.0
%define swell_foop_ver 41.0
%define tali_ver 40.6
%define taquin_ver 3.38.1
%define tetravex_ver 3.38.2
# 2048
%define tiles_ver 3.38.2

Requires: %_name-2048 >= %tiles_ver
Requires: %_name-aisleriot >= %aisleriot_ver
Requires: %_name-atomix >= %atomix_ver
Requires: %_name-glchess >= %ver_major
Requires: %_name-glines >= %glines_ver
Requires: %_name-gnect >= %gnect_ver
Requires: %_name-gnibbles >= %nibbles_ver
Requires: %_name-gnobots >= %robots_ver
Requires: %_name-gnomine >= %mines_ver
Requires: %_name-gnotravex >= %tetravex_ver
Requires: %_name-gnotski >= %klotski_ver
Requires: %_name-gtali >= %tali_ver
Requires: %_name-hitori >= %hitori_ver
Requires: %_name-iagno >= %iagno_ver
Requires: %_name-lightsoff >= %lightsoff_ver
Requires: %_name-mahjongg >= %mahjongg_ver
Requires: %_name-quadrapassel >= %quadrapassel_ver
Requires: %_name-sudoku >= %ver_major
Requires: %_name-swell-foop >= %swell_foop_ver
Requires: %_name-taquin >= %taquin_ver

BuildRequires: rpm-build-licenses

%description
The %name is a virtual package that provides a collection of
simple games for your amusement.

gnome-games	simple game launcher.
Aisleriot	a collection of card games.
Glines:         color lines game, aka fiveormore.
Gnect:          four in a row game.
Gnibbles:       snake game up to four players.
Gnobots:        old bsd robots game improved.
GNOME Klotski:  game based on the not so popular Klotski.
GNOME Mine:     popular logic puzzle minesweeper.
GNOME Tali:     sort of poker with dice and less money.
Quadrapassel:   GNOME version of the popular russian game Tetris, in past quadrapassel.
Iagno:          GNOME version of the popular Othello.
Mahjongg:       GNOME version of the classic Eastern tile game, Mahjongg.
swell-foop:     in past Same GNOME, game which goal is to remove as many balls in as few moves as,
		possible.
GNOME Sudoku:   a logic game with a Japanese name.
GlChess:	a chess game which supports several chess engines.
Tetravex	a simple puzzle game based on Tetravex.

%files

%changelog
* Thu Apr 07 2022 Yuri N. Sedunov <aris@altlinux.org> 42.0-alt1
- updated versions, removed gnome-games (depends on tracker-2.0)

* Fri May 25 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0, renamed to gnome-games-full
- added real gnome-games package and aisleriot

* Wed Sep 21 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Wed Mar 30 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Mon Sep 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0
- added gnome-2048 game

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt2
- added back hitori-3.16

* Thu Mar 26 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0
- added atomix and taquin
- removed unsupported hitori

* Sun Oct 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt2
- added hitori

* Sun Sep 21 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 05 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Sep 30 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Thu Apr 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Wed Jan 09 2013 Yuri N. Sedunov <aris@altlinux.org> 3.7.2-alt1
- made virtual package after gnome-games split

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.1-alt1
- 3.6.1

* Wed Oct 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.6.0.2-alt1
- 3.6.0.2

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
