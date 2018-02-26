Name: xpilot
Version: 4.5.4
Release: alt3.2

Summary: An X Window System based multiplayer aerial combat game
License: GPL
Group: Games/Arcade

Url: http://xpilot.sourceforge.net
Source0: ftp://ftp.xpilot.org/pub/%name-%version.tar.bz2
Source1: %name-menu
Source2:  %name-16.png.bz2
Source3:  %name-32.png.bz2
Source4:  %name-48.png.bz2
Patch: xpilot-4.5.3-config.patch

Packager: Ilya Mashkin <oddity@altlinux.ru>

# Automatically added by buildreq on Fri Feb 24 2006
BuildRequires: imake xorg-cf-files libX11-devel libXext-devel

%description
Xpilot is an X Window System based multiplayer game of aerial combat.

The object of the game is to shoot each other down, or you can use the race mode
to just fly around.

Xpilot resembles the Commodore 64 Thrust game, which is similar to Atari's
Gravitar and Asteriods (note: this is not misspelled).

Unless you already have an xpilot server on your network, you'll need to set up
the server on one machine, and then set up xpilot clients on all of the players'
machines.

%prep
%setup -q
%patch -p0

%build
xmkmf
make Makefiles
make INSTMANDIR=%_mandir

%install
make PREFIX="%buildroot%_usr" install
make PREFIX="%buildroot%_datadir" install.man

install -m 755 -d %buildroot%_menudir/
install -m 644 %SOURCE1 %buildroot%_menudir/
install -m 755 -d %buildroot%_miconsdir/
bzcat %SOURCE2 > %buildroot%_miconsdir/%name.png
install -m 755 -d %buildroot%_iconsdir/
bzcat %SOURCE3 > %buildroot%_iconsdir/%name.png
install -m 755 -d %buildroot%_liconsdir/
bzcat %SOURCE4 > %buildroot%_liconsdir/%name.png

%files
%doc README.txt LICENSE README.txt.msub
%doc doc
%_x11bindir/*
/usr/lib/%name/*
%_x11mandir/man?/*
%_menudir/*
%_miconsdir/*.png
%_liconsdir/*.png
%_iconsdir/*.png

%changelog
* Tue Apr 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.5.4-alt3.2
- fix build

* Tue Oct 06 2008 Ilya Mashkin <oddity@altlinux.ru> 4.5.4-alt3.1
- rebuild
- update url

* Fri Feb 24 2006 Michael Shigorin <mike@altlinux.org> 4.5.4-alt3
- picked up an orphan (road companion ;-)
- spec cleanup/update for xorg7
- updated buildrequires

* Thu Oct 31 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.4-alt2
- rebuild with gcc3
- fixed menu file (xpm -> png icon)

* Wed Aug 14 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.4-alt1
- 4.5.4

* Wed Apr 03 2002 Stanislav Ievlev <inger@altlinux.ru> 4.5.0-alt1
- 4.5.0

* Mon Oct 15 2001 Stanislav Ievlev <inger@altlinux.ru> 4.4.2-alt1
- 4.4.2

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Tue Nov 28 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-8mdk
- use optflags.

* Fri Sep 15 2000 David BAUDENS <baudens@mandrakesoft.com> 4.2.0-7mdk
- Fix Title in Menu entry
- Complete macros

* Wed Aug 30 2000 Geoffrey Lee <snailtalk@mandrakesoft.com> 4.2.0-6mdk
- rebuild to use the new macros.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 4.2.0-5mdk
- automatically added BuildRequires

* Wed May 03 2000 dam's <damien@mandrakesoft.com> 4.2.0-4mdk
- Corrected menu entry.

* Tue Apr 18 2000 dam's <damien@mandrakesoft.com> 4.2.0-3mdk
- Convert gif icon to xpm.

* Mon Apr 17 2000 dam's <damien@mandrakesoft.com> 4.2.0-2mdk
- Added menu entry.

* Wed Mar 22 2000 dam's <damien@mandrakesoft.com> 4.2.0-1mdk
- updade to 4.2.0

* Fri Nov 5 1999 dam's <damien@mandrakesoft.com>
- Mandrake adaptation

* Fri Jul 30 1999 Bill Nottingham <notting@redhat.com>
- update to 4.1.0

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 6)

* Thu Dec 17 1998 Michael Maher <mike@redhat.com>
- built package for 6.0

* Thu Aug 13 1998 Jeff Johnson <jbj@redhat.com>
- add sparc
- build root

* Fri May 08 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Mon Nov  3 1997 Otto Hammersmith <otto@redhat.com>
- made exlusivearch to i386

* Thu Oct 23 1997 Marc Ewing <marc@redhat.com>
- new version
- wmconfig

* Thu Jul 31 1997 Erik Troan <ewt@redhat.com>
- built against glibc
