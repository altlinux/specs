Name: lbreakout2
Version: 2.6.5
Release: alt2

Summary: Breakout-style arcade game
License: GPL
Group: Games/Arcade

Url: http://lgames.sourceforge.net
Source0: http://ftp1.sourceforge.net/lgames/%name-%version.tar.gz
Source1: %name.desktop
Source2: %name.watch
Source5: %name.16.xpm
Source6: %name.32.xpm
Source7: %name.48.xpm
Source8: lbreakout2.6
Source9: lbreakout2server.6
Patch0: 10-ball-turbo-key-pref.patch
Patch1: spelling-fixes.patch
Packager: Ilya Mashkin <oddity@altlinux.ru>

Requires: %name-data = %version-%release

Summary(ru_RU.UTF-8): игра отбивай-и-разбивай со стильной графикой

# Automatically added by buildreq on Tue Sep 09 2008 (-bi)
BuildRequires: libSDL-devel libSDL_mixer-devel libpng-devel

%description
LBreakout is a classical Breakout game and this means (if you like Breakout ;-)
it is a lot of fun to play!
If you never ever played such a game you can check out the manual for more
information, take a look at the screenshots and last but not least... play it!

%description -l ru_RU.UTF-8
lbreakout2 -- игра, подобная классическим играм жанра breakout и xboing,
с улучшенными графическими эффектами. В нижней части экрана вы управляете
битой и вам нужно отбивать шарики так, чтобы они попали в находящиеся
сверху блоки и разбили их.

Код lbreakout2 отличается от lbreakout. Те, кто играл в lbreakout,
возможно, захотят установить и эту версию.

%package data
Summary: %name levels
License: GPL
Group: Games/Arcade
BuildArch: noarch

%description data
This package contains levels for %name

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%configure \
    --bindir=%_gamesbindir \
    --datadir=%_gamesdatadir \
    --localstatedir=%_localstatedir/games \
    --with-docdir=%_docdir/%name-%version/html
%make_build

%install
%makeinstall_std doc_dir=%_docdir/%name-%version/

rm -rf %buildroot/%_docdir/%name
rm -f %buildroot%_bindir/%name{,server}

rm -rf html
cp -ar docs html
rm -f html/Makefile*

install -pDm644 %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -pDm644 %SOURCE5 %buildroot/%_miconsdir/%name.xpm
install -pDm644 %SOURCE6 %buildroot/%_niconsdir/%name.xpm
install -pDm644 %SOURCE7 %buildroot/%_liconsdir/%name.xpm
install -pDm644 %SOURCE8 %buildroot/%_man6dir/lbreakout2.6
install -pDm644 %SOURCE9 %buildroot/%_man6dir/lbreakout2server.6

mkdir -p %buildroot%_datadir/locale
mv %buildroot%_gamesdatadir/locale/* %buildroot%_datadir/locale/
%find_lang %name

%files -f %name.lang
%doc README TODO AUTHORS ChangeLog
%doc html
%attr(2711,root,games) %_gamesbindir/%name
%_gamesbindir/%{name}server
%config(noreplace) %attr(664,games,games) %_localstatedir/games/*
%_desktopdir/%name.desktop
%_miconsdir/%name.xpm
%_niconsdir/%name.xpm
%_liconsdir/%name.xpm
%_datadir/games/applications/%name.desktop
%_datadir/games/icons/*48.gif
%_man6dir/*

%files data
%_datadir/games/%name

# TODO:
# - add .desktop for server (NB: http://secunia.com/advisories/9134/)

%changelog
* Thu Jul 27 2017 Michael Shigorin <mike@altlinux.org> 2.6.5-alt2
- dropped weird auto BR: rpm-build-haskell
- dropped beta macro (looks like there gonna be none)
- added debian patches, manpages, watch file, and Russian description
- minor spec cleanup

* Sun Dec 20 2015 Ilya Mashkin <oddity@altlinux.ru> 2.6.5-alt1
- 2.6.5

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.6.4-alt1.1
- Rebuilt with libpng15

* Sat Jun 30 2012 Ilya Mashkin <oddity@altlinux.ru> 2.6.4-alt1
- 2.6.4

* Thu Mar 10 2011 Ilya Mashkin <oddity@altlinux.ru> 2.6.3-alt1
- 2.6.3

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 2.6-alt0.7
- 2.6beta-7
- added Icon to desktop file (thx shrek@)
- fixed translations installation, sort of

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 2.5.2-alt1
- 2.5.2
- introduced noarch data subpackage
- fixed icons installation
- spec cleanup

* Sat Dec 06 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt5
- added Packager:

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt4
- applied repocop patch
- minor spec cleanup

* Tue Nov 18 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt3
- enabled sound support (#17925, thx horror@)

* Tue Sep 09 2008 Michael Shigorin <mike@altlinux.org> 2.5-alt2
- fixed build (buildreq)
- replaced Debian menu file with PLD-based desktop one
- spec cleanup
- me as a Packager:

* Wed Aug 11 2004 Sergey V Turchin <zerg at altlinux dot org> 2.5-alt1
- new version

* Wed Jun 30 2004 Sergey V Turchin <zerg at altlinux dot org> 2.5-alt0.2.beta8
- new beta

* Mon Jul 14 2003 Sergey V Turchin <zerg at altlinux dot org> 2.5-alt0.1.beta3
- 2.5beta-3

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 2.4.1-alt1
- new version

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 2.4-alt1
- new version

* Thu Nov 14 2002 Sergey V Turchin <zerg@altlinux.ru> 2.4-alt0.1.beta
- new version
- build with gcc3.2

* Mon Aug 19 2002 Sergey V Turchin <zerg@altlinux.ru> 2.3.2-alt1
- new version

* Thu Aug 15 2002 Sergey V Turchin <zerg@altlinux.ru> 2.3.1-alt1
- new version

* Wed Aug 14 2002 ZerG <zerg@altlinux.ru> 2.3-alt1
- new version
- add more levelpacks

* Wed Mar 27 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2.2-alt2
- add Hommage levelset

* Wed Feb 27 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2.2-alt1
- new version
- add levelpack "Bombs"

* Fri Feb 08 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2.1-alt1
- new version
- add 2 new levelpacks

* Mon Jan 28 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt1
- new version
- add BeOS-4ever levelpack

* Wed Jan 23 2002 Sergey V Turchin <zerg@altlinux.ru> 2.2-alt0.pre.2
- new version

* Tue Jan 08 2002 Sergey V Turchin <zerg@altlinux.ru> 2.1.2-alt1
- new version
- fix menu entry

* Sat Dec 29 2001 Sergey V Turchin <zerg@altlinux.ru> 2.1.1-alt1
- new version

* Wed Nov 28 2001 Sergey V Turchin <zerg@altlinux.ru> 2.0-alt0.2.pre2
- new version

* Thu Nov 08 2001 Sergey V Turchin <zerg@altlinux.ru> 2.0-alt0.1.beta
- initial spec
