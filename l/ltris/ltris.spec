Name: ltris
Version: 1.0.18
Release: alt1
Serial: 1

Group: Games/Arcade
Summary: Nice tetris clone
URL: http://lgames.sourceforge.net/index.php?project=LTris
License: GPL
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://download.sourceforge.net/lgames/ltris-%version.tar.gz

#BuildRequires: XFree86-libs aalib esound libSDL-devel libSDL_mixer-devel
#BuildRequires: libalsa libarts libaudiofile libogg libslang libsmpeg libvorbis

# Automatically added by buildreq on Wed Jun 30 2004 (-bi)
BuildRequires: esound libSDL-devel libSDL_mixer-devel desktop-file-utils

%description
o Tetris clone using SDL
o Sound
o Menu
o Controls can be redefined
o Block preview
o Starting level between 0 and 9
o Various backgrounds
o HighScores
o Nice graphics
o Smooth gameplay
o Cool effects (transparency, animations)
o Two player mode
o Two game modes

%prep
%setup -q

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --localstatedir=%{_localstatedir}/games
%make_build

%install
%make install DESTDIR=%buildroot

install -D -m644 icons/%{name}16.xpm $RPM_BUILD_ROOT%_miconsdir/%name.xpm
install -D -m644 icons/%{name}32.xpm $RPM_BUILD_ROOT%_niconsdir/%name.xpm
install -D -m644 icons/%{name}48.xpm $RPM_BUILD_ROOT%_liconsdir/%name.xpm

# todo: report category BlocksGame to upstream
# move and fix desktop file
desktop-file-install --dir %buildroot%_desktopdir --delete-original \
	--add-category BlocksGame %buildroot%_gamesdatadir/applications/%name.desktop

# fix desktop file
sed -i -e 's,^Icon=.*,Icon=%name,' %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang

%doc README AUTHORS ChangeLog TODO
%attr(2711, root, games) %_gamesbindir/*
%attr(-, games, games) %_localstatedir/games/%name.hscr
%_gamesdatadir/%name
%_desktopdir/%name.desktop
%_niconsdir/%name.xpm
%_miconsdir/%name.xpm
%_liconsdir/%name.xpm

%changelog
* Sat Jun 30 2012 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.18-alt1
- 1.0.18

* Tue Aug 30 2011 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.17-alt1
- 1.0.17

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1:1.0.16-alt1.qa1
- NMU: converted menu to desktop file

* Sat Mar 05 2011 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.16-alt1
- 1.0.16

* Sun Sep 26 2010 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.15-alt1
- 1.0.15

* Sat Dec 26 2009 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.14-alt1
- 1.0.14

* Sat Oct 31 2009 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.13-alt1
- 1.0.13

* Sat Sep 19 2009 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.12-alt2
- remove old macros
- fix icons locations

* Mon Sep 01 2008 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.12-alt1
- new version 1.0.12

* Wed Jun 30 2004 Sergey V Turchin <zerg at altlinux dot org> 1:1.0.7-alt1
- new version

* Tue Oct 07 2003 Sergey V Turchin <zerg at altlinux dot org> 1:1.0.5-alt1
- new version

* Thu Jan 16 2003 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.4-alt1
- new version

* Wed Oct 23 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt2
- rebuild with gcc3.2

* Fri Aug 09 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.3-alt1
- new version
- fix binary permissions

* Thu Jun 13 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.2-alt1
- new version

* Tue Jan 15 2002 Sergey V Turchin <zerg@altlinux.ru> 1:1.0.1-alt1
- new version

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 010310-alt1
- new version

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 001115-ipl2mdk
- fix BuildPreReq

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 001115-ipl1mdk
- Build for RE

* Wed Dec 20 2000 Pixel <pixel@mandrakesoft.com> 001115-1mdk
- new version

* Tue Nov 07 2000 David BAUDENS <baudens@mandrakesoft.com> 001017-3mdk
- ExcludeArch: ppc

* Tue Nov  7 2000 Pixel <pixel@mandrakesoft.com> 001017-2mdk
- rebuild
- longtitle
- capitalize summary

* Wed Oct 18 2000 Pixel <pixel@mandrakesoft.com> 001017-1mdk
- new version

* Wed Oct  4 2000 Pixel <pixel@mandrakesoft.com> 000705-2mdk
- new icons (thanks to the author Michael Speck)

* Fri Sep 29 2000 Pixel <pixel@mandrakesoft.com> 000705-1mdk
- initial spec

