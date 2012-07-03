Name: lmarbles
Version: 1.0.8
Release: alt1.qa1
Serial: 1

Group: Games/Puzzles
Summary: Atomix-style arcade game
License: GPL
Url: http://lgames.sourceforge.net/index.php?project=LMarbles
Packager: Ilya Mashkin <oddity@altlinux.ru>
Provides: marbles = %serial:%version-%release
Obsoletes: marbles <= %serial:%version-%release

Source0: %name-%version.tar.gz
#
Source5: %{name}16.xpm
Source6: %{name}32.xpm
Source7: %{name}48.xpm

# Automatically added by buildreq on Fri Jul 02 2004 (-bi)
BuildRequires: libSDL-devel libSDL_mixer-devel desktop-file-utils

%description
Marbles is very similar to Atomix and was heavily inspired by it.
Goal is to create a more or less complex figure out of single
marbles within a time limit to reach the next level.
Sounds easy? Well, there is a problem: If a marble starts to move it
will not stop until it hits a wall or marble. And to make it even
more interesting there are obstacles like arrows,
crumbling walls and teleports!

%prep
%setup -q


%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --localstatedir=%_localstatedir/games
%make_build

%install
%make install DESTDIR=%buildroot
touch %buildroot/%_localstatedir/games/%name.prfs

mkdir -p %buildroot/%_menudir/

# todo: report category ArcadeGame to upstream
# move and fix desktop file
desktop-file-install --dir %buildroot%_desktopdir --delete-original \
	--add-category ArcadeGame %buildroot%_gamesdatadir/applications/%name.desktop

# fix desktop file
sed -i -e 's,^Icon=.*,Icon=%name,' %buildroot%_desktopdir/%name.desktop

install -D -m644 %SOURCE6 %buildroot/%_niconsdir/%name.xpm
install -D -m644 %SOURCE5 %buildroot/%_miconsdir/%name.xpm
install -D -m644 %SOURCE7 %buildroot/%_liconsdir/%name.xpm

%files
%doc AUTHORS ChangeLog TODO src/manual
%attr(2711, root, games) %_gamesbindir/*
%attr(664, games, games) %_localstatedir/games/%name.prfs
%_datadir/games/lmarbles
%_desktopdir/%name.desktop
%_datadir/games/icons/lmarbles48.gif
%_niconsdir/*.xpm
%_miconsdir/*
%_liconsdir/*
%doc %_man6dir/*

%changelog
* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.8-alt1.qa1
- NMU: converted menu to desktop file

* Sat Oct 31 2009 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.8-alt1
- 1.0.8

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.7-alt2
- remove old macros
- fix icons locations

* Thu Sep 25 2008 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.7-alt1.1
- rebuild
- update requires

* Fri Jul 02 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.0.7-alt1
- new version
- fix rpm/menu section

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.6-alt1
- new version

* Wed Oct 23 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.5-alt1
- new version
- build with gcc3.2

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.4-alt1
- new version
- fix binary permissions

* Wed Mar 27 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.2-alt1
- new version

* Wed Jan 23 2002 Sergey V Turchin <zerg@altlinux.ru> 010307-alt1
- build for ALT

* Mon Jan 21 2002 Stefan van der Eijk <stefan@eijk.nu> 010307-5mdk
- BuildRequires

* Wed Nov 07 2001 François Pons <fpons@mandrakesoft.com> 010307-4mdk
- added url tag.

* Tue Jul 03 2001 François Pons <fpons@mandrakesoft.com> 010307-3mdk
- build release, updated distrution tag.

* Fri May 18 2001 François Pons <fpons@mandrakesoft.com> 010307-2mdk
- update to use libSDL 1.2.

* Fri Apr 27 2001 François Pons <fpons@mandrakesoft.com> 010307-1mdk
- created patch to install man pages correctly (uggly).
- update to 010307.

* Fri Jan 13 2001 David BAUDNS <baudens@mandrakesoft.com> 001211-2mdk
- BuildRequires: libSDL1.1-devel

* Wed Dec 20 2000 François Pons <fpons@mandrakesoft.com> 001211-1mdk
- initial release
