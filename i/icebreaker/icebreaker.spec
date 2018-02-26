Name: icebreaker
Version: 1.9.7
Release: alt2.1
Epoch: 1

Summary: An addictive action-puzzle game involving bouncing penguins
License: GPL
Group: Games/Arcade

Url: http://www.mattdm.org/icebreaker/
Source0: %name-%version.tgz
Source1: %name.desktop
Source2: %name.16.xpm
Source3: %name.32.xpm
Source4: %name.48.xpm
Patch0: icebreaker-makefile.patch
Patch1: icebreaker-1.9.7-alt-buffer.patch
Packager: Michael Shigorin <mike@altlinux.org>

BuildRequires: libSDL-devel libSDL_mixer-devel
BuildRequires: xorg-libs aalib esound libSDL-devel libSDL_mixer-devel
BuildRequires: libalsa2 libaudiofile libogg libslang libsmpeg libvorbis

%description
So, uh, there's a bunch of penguins on an iceberg in Antarctica.
You have been selected to catch them so they can be shipped to Finland
where they are essential to a secret plot for world domination.

%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%define _optlevel 3
%add_optflags %optflags_kernel %optflags_notraceback %optflags_fastmath
%make_build OPTIMIZE="$RPM_OPT_FLAGS -finline-functions" prefix=%prefix highscoredir=%_localstatedir/games

%install
mkdir -p %buildroot/%_gamesdatadir/icebreaker
touch icebreaker.scores
install -pDm664 icebreaker.scores %buildroot/%_localstatedir/games/icebreaker.scores
install -pDm755 icebreaker %buildroot/%_gamesbindir/icebreaker
install -pm644 *.wav *.bmp *.ibt %buildroot/%_gamesdatadir/icebreaker/
install -pD %SOURCE1 %buildroot/%_desktopdir/%name.desktop
install -pDm644 %SOURCE2 %buildroot/%_miconsdir/%name.xpm
install -pDm644 %SOURCE3 %buildroot/%_niconsdir/%name.xpm
install -pDm644 %SOURCE4 %buildroot/%_liconsdir/%name.xpm

%files
%doc README TODO LICENSE ChangeLog
%attr(2711,root,games) %_gamesbindir/icebreaker
%_gamesdatadir/icebreaker
%attr(664,games,games) %_localstatedir/games/icebreaker.scores
%_desktopdir/%name.desktop
%_miconsdir/icebreaker.xpm
%_niconsdir/icebreaker.xpm
%_liconsdir/icebreaker.xpm

%changelog
* Tue Apr 26 2011 Andrey Cherepanov <cas@altlinux.org> 1:1.9.7-alt2.1
- Remove aRts support

* Wed Jul 22 2009 Michael Shigorin <mike@altlinux.org> 1:1.9.7-alt2
- applied repocop patch
- spec fixup/cleanup

* Mon Jul 20 2009 Michael Shigorin <mike@altlinux.org> 1:1.9.7-alt1
- 1.9.7
- (hopefully) fixed a few buffer overflows found by new gcc

* Thu Dec 04 2008 Michael Shigorin <mike@altlinux.org> 1:1.9.5-alt3
- applied repocop patch
- s/Serial:/Epoch:/

* Wed Sep 24 2008 Michael Shigorin <mike@altlinux.org> 1:1.9.5-alt2
- buildreq
- spec cleanup
- replaced Debian menufile with fd.o one (PLD+ru+uk)

* Tue Feb 04 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.9.5-alt1
- new version

* Mon Oct 28 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.2.1-alt5
- rebuild with gcc3.2

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.2.1-alt4
- fix binary permissions

* Mon Jan 21 2002 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt3
- fix icons

* Wed Sep 12 2001 Sergey V Turchin <zerg@altlinux.ru> 1.2.1-alt2
- new version

* Fri Aug 17 2001 Stanislav Ievlev <inger@altlinux.ru> 1.09-alt2
- Rebuilt with new SDL.

* Fri Jul 27 2001 Sergey V Turchin <zerg@altlinux.ru> 1.09-alt1
- new version

* Thu Jul 05 2001 Sergey V Turchin <zerg@altlinux.ru> 1.0-alt1
- build for ALT

* Fri May 18 2001 François Pons <fpons@mandrakesoft.com> 1.0-4mdk
- update to use libSDL 1.2.

* Tue Dec 19 2000 François Pons <fpons@mandrakesoft.com> 1.0-3mdk
- updated build requires with new library name.

* Wed Nov 15 2000 David BAUDENS <baudens@mandrakesoft.com> 1.0-2mdk
- BuildRequires: SDL_mixer-devel
- Fix %%postun

* Fri Oct 27 2000 François Pons <fpons@mandrakesoft.com> 1.0-1mdk
- added menu entries.
- initial release.

* Thu Oct 5 2000 Matthew Miller <mattdm@mattdm.org>
- looks good to me. one-point-oh

* Tue Oct 3 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.995
- better make process

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.99 :)

* Mon Oct 2 2000 Matthew Miller <mattdm@mattdm.org>
- updated to 0.98

* Fri Sep 15 2000 Matthew Miller <mattdm@mattdm.org>
- first package
