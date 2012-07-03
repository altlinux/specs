Name: trophy
Version: 2.0.3
Release: alt1

Summary: Trophy is a 2D car racing action game
License: GPLv2
Group: Games/Sports

Url: http://trophy.sourceforge.net/
Source: http://downloads.sourceforge.net/trophy/trophy-%version.tar.gz
Source2: trophy.16.png
Source3: trophy.32.png
Source4: trophy.48.png
Source5: trophy.desktop
Patch: trophy-1.1.6-asneeded.patch

# Automatically added by buildreq on Fri Nov 26 2010
BuildRequires: clanlib0.8-devel gcc-c++ libGLU-devel

Requires: trophy-gamedata = %version

%description
Trophy is a single-player racing game. Even though the goal is basically to
finish the laps as the first, Trophy is an action game which offers much more
than just a race. Lots of extras enable "unusual" features for races such as
shooting, putting mines and many others.

%package gamedata
Summary: Game data for Trophy
Group: Games/Sports
# We split game data to separate package to make it noarch and thus save
# bandwidth and space on distribution media.
BuildArch: noarch

%description gamedata
Game data for Trophy car racing game.

%prep
%setup
#%patch -p1

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
%makeinstall_std

install -pD -m644 %SOURCE2 %buildroot%_miconsdir/trophy.png
install -pD -m644 %SOURCE3 %buildroot%_niconsdir/trophy.png
install -pD -m644 %SOURCE4 %buildroot%_liconsdir/trophy.png
install -pD -m644 %SOURCE5 %buildroot%_desktopdir/trophy.desktop

%files
%_gamesbindir/*
%_desktopdir/*
%_miconsdir/*.png
%_niconsdir/*.png
%_liconsdir/*.png

%files gamedata
%_gamesdatadir/*
%_man6dir/*

%changelog
* Fri Mar 16 2012 Victor Forsiuk <force@altlinux.org> 2.0.3-alt1
- 2.0.3

* Sat Jan 28 2012 Victor Forsiuk <force@altlinux.org> 2.0.0-alt1
- 2.0.0

* Tue Jun 28 2011 Victor Forsiuk <force@altlinux.org> 1.1.7-alt1
- 1.1.7

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.1.6-alt1
- 1.1.6
- Renew build requirements (libGLU-devel was optimized out and lost due to
  changes in dependency chain).

* Tue Dec 02 2008 Victor Forsyuk <force@altlinux.org> 1.1.5-alt2
- Renew build requirements to fix FTBFS.

* Wed Aug 20 2008 Victor Forsyuk <force@altlinux.org> 1.1.5-alt1
- Adopted package from an orphanage.
- Split (huge!) game data to noarch package.

* Mon Feb 27 2006 Stanislav Ievlev <inger@altlinux.org> 1.1.3-alt4.1
- fixed icons path

* Fri Jan 21 2005 Stanislav Ievlev <inger@altlinux.org> 1.1.3-alt4
- fixed build with gcc3.4

* Fri Aug 06 2004 Stanislav Ievlev <inger@altlinux.org> 1.1.3-alt3
- move to sports from arcade group

* Tue Sep 30 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.3-alt2
- fix building in hasher

* Wed Jun 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1.1.3-alt1
- 1.1.3

* Mon Oct 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.7-alt2
- Rebuilt in new environment

* Thu Aug 29 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.7-alt1
- 1.0.7
- Rebuild with clanlib 0.6.3

* Wed Jan 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0.6-alt3
- Recompiled with ClanLib 0.5.4

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.6-alt2
- Recompiled with ClanLib 0.5.1

* Thu Aug 30 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0.6-alt1
- 1.0.6
- Added optimization

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 1.0.1-ipl9mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Wed Feb 21 2001 Kostya Timoshenko <kt@petr.kz> 1.0.1-ipl8mdk
- add 48x48 icon
- add designal manual
- fix requires on launch_x11_clanapp

* Wed Jan 31 2001 Kostya Timoshenko <kt@petr.kz> 1.0.1-ipl7mdk
- fix hermes-devel -> libhermes-devel in BuildPreReq.

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz>
- Build for RE
