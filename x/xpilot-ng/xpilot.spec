Name: xpilot-ng
Version: 4.7.3
Release: alt2.1

Summary: An X Window System based multiplayer aerial combat game
License: GPL
Group: Games/Arcade
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://xpilot.sourceforge.net
Source0: %name-%version.tar.gz
Source2: xpilot-16.png.bz2
Source3: xpilot-32.png.bz2
Source4: xpilot-48.png.bz2
Patch: xpilot-ng-4.7.3-alt-getline.patch

# Automatically added by buildreq on Fri Jan 15 2010 (-bi)
BuildRequires: imake libGL-devel libSDL-devel libSDL_image-devel libSDL_ttf-devel libXext-devel libXt-devel libexpat-devel libopenal-devel xorg-cf-files zlib-devel libGLU-devel libICE-devel libSM-devel libX11-devel xorg-xextproto-devel xorg-xproto-devel

#BuildRequires: xorg-x11-devel libexpat-devel libSDL-devel libSDL_ttf-devel libSDL_image-devel libopenal-devel

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
%patch -p1 -b .getline

%build
#xmkmf
#make Makefiles
#make INSTMANDIR=%_mandir
%configure \
	--enable-sound \
	--enable-dbe \
	--enable-mbx \
	--enable-select-sched

%make

%install
%makeinstall_std install


mkdir -p $RPM_BUILD_ROOT%_desktopdir
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}-server.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Xpilot server
Icon=%{name}
Exec=%{name}-server
Terminal=true
Categories=Game;ArcadeGame;
EOF
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}-sdl.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Xpilot SDL
Icon=%{name}
Exec=%{name}-sdl -join
Terminal=false
Categories=Game;ArcadeGame;
EOF
cat > $RPM_BUILD_ROOT%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Version=1.0
Type=Application
Name=Xpilot SDL
Icon=%{name}
Exec=%{name}-x11 -join
Terminal=false
Categories=Game;ArcadeGame;
EOF

install -m 755 -d %buildroot%_miconsdir/
bzcat %SOURCE2 > %buildroot%_miconsdir/%name.png
install -m 755 -d %buildroot%_niconsdir/
bzcat %SOURCE3 > %buildroot%_niconsdir/%name.png
install -m 755 -d %buildroot%_liconsdir/
bzcat %SOURCE4 > %buildroot%_liconsdir/%name.png

%files
%doc README NEWS
%doc mapconvert.py
%_bindir/xpilot-ng-replay
%_bindir/xpilot-ng-sdl
%_bindir/xpilot-ng-server
%_bindir/xpilot-ng-x11
%_bindir/xpilot-ng-xp-mapedit
%_datadir/%name
%_mandir/man?/*
%_desktopdir/*
%_miconsdir/*.png
%_liconsdir/*.png
%_niconsdir/*.png

%changelog
* Wed Oct 26 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.7.3-alt2.1
- Rebuild with Python-2.7

* Sat Mar 26 2011 Igor Vlasenko <viy@altlinux.ru> 4.7.3-alt2
- converted debian menu to freedesktop

* Mon Jan 24 2011 Ilya Mashkin <oddity@altlinux.ru> 4.7.3-alt1
- 4.7.3
- update xpilot-ng-4.7.3-alt-getline.patch

* Fri Jan 15 2010 Igor Vlasenko <viy@altlinux.ru> 4.7.2-alt1
- new version (renamed to xpilot-ng) 

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
