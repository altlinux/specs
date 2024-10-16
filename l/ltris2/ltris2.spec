Name: ltris2
Version: 2.0.2
Release: alt1

Group: Games/Arcade
Summary: Nice tetris clone
URL: http://lgames.sourceforge.net/index.php?project=LTris
License: GPLv2+
Packager: Ilya Mashkin <oddity@altlinux.ru>

Source0: http://download.sourceforge.net/lgames/ltris2-%version.tar.gz
Patch1: ltris-1.0.19-inlines.patch

Patch2: fix_sdl_test.patch
Patch3: icon_fix.patch

BuildRequires: esound libSDL2-devel libSDL2_mixer-devel desktop-file-utils automake sysconftool ImageMagick libSDL2_ttf-devel libSDL2_image-devel gcc gcc-c++
Obsoletes: ltris < 2
Provides: ltris


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
#patch1 -p1
#patch2 -p1
#patch3 -p1
###convert ltris48.gif ltris.png
#cp ltris48.png ltris.png

%build
autoreconf -f -i
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --localstatedir=%{_localstatedir}/games
%make_build

%install
%make install DESTDIR=%buildroot

#install -D -m644 icons/%{name}16.xpm $RPM_BUILD_ROOT%_miconsdir/%name.xpm
#install -D -m644 icons/%{name}32.xpm $RPM_BUILD_ROOT%_niconsdir/%name.xpm
#install -D -m644 icons/%{name}48.xpm $RPM_BUILD_ROOT%_liconsdir/%name.xpm

# todo: report category BlocksGame to upstream
# move and fix desktop file
desktop-file-install --dir %buildroot%_desktopdir --delete-original \
	--add-category BlocksGame %buildroot%_gamesdatadir/applications/%name.desktop

# fix desktop file
sed -i -e 's,^Icon=.*,Icon=%name,' %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang

%doc README TODO
%attr(2711, root, games) %_gamesbindir/*
%attr(-, games, games) %_localstatedir/games/%name.hscr
%_gamesdatadir/%name
%_datadir/games/icons/hicolor/256x256/apps/ltris2.png
%_desktopdir/%name.desktop
#_niconsdir/%name.xpm
#_miconsdir/%name.xpm
#_liconsdir/%name.xpm

%changelog
* Wed Oct 16 2024 Ilya Mashkin <oddity@altlinux.ru> 2.0.2-alt1
- 2.0.2

* Mon Jun 10 2024 Ilya Mashkin <oddity@altlinux.ru> 1:1.3.2-alt1
- 1.3.2

* Sun Apr 28 2024 Ilya Mashkin <oddity@altlinux.ru> 1:1.3.1-alt1
- 1.3.1

* Thu Mar 14 2024 Ilya Mashkin <oddity@altlinux.ru> 1:1.3-alt1
- 1.3

* Sat Feb 24 2024 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.8-alt1
- 1.2.8

* Tue Sep 12 2023 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.7-alt1
- 1.2.7

* Fri Oct 14 2022 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.6-alt1
- 1.2.6

* Wed Jun 22 2022 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.5-alt1
- 1.2.5

* Tue Apr 19 2022 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.4-alt1
- 1.2.4

* Sat May 01 2021 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.3-alt1
- 1.2.3

* Wed Feb 10 2021 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.2-alt2
- add ltris.png
- build with gcc10

* Wed Feb 10 2021 Ilya Mashkin <oddity@altlinux.ru> 1:1.2.2-alt1
- 1.2.2

* Fri Feb 26 2016 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.19-alt2
- fix build

* Tue Nov 12 2013 Ilya Mashkin <oddity@altlinux.ru> 1:1.0.19-alt1
- 1.0.19

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

