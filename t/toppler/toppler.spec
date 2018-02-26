Name: toppler
Version: 1.1.5
Release: alt1

Group: Games/Arcade
Summary: Dangerously ascent of the tower.
Summary(ru_RU.UTF8): Опасное восхождение на башню.
Url: http://toppler.sourceforge.net
License: GPL

Source0: %name-%version.tar.gz
Source2: %name.16.png
Source3: %name.32.png
Source4: %name.48.png

Packager: Evgeny V. Shishkov <shev@altlinux.org>

# Automatically added by buildreq on Wed Mar 21 2012
BuildRequires: gcc-c++ libSDL-devel libSDL_mixer-devel zlib-devel

%description
In this game you have to help a cute little green animal switch off some kind of "evil" mechanism.
The "power off switch" is hidden somewhere in high towers. On your way to the target you need to avoid a lot of 
strange robots that guard the tower.

%description -l ru_RU.UTF-8
В этой игре вы должны помочь зеленому животному выключить "злой" механизм. "Выключатель" находится на высокой башне. 
По пути к цели нужно избегать много странных охранников башни.

%prep
%setup -q

%build
#aclocal; automake; autoconf
%configure \
	--bindir=%_gamesbindir \
	--datadir=%_gamesdatadir \
	--localstatedir=%_localstatedir/games
%make_build

%install
%makeinstall \
    bindir=%buildroot/%_gamesbindir \
    datadir=%buildroot/%_gamesdatadir \
    localedir=%buildroot/%_datadir/locale \
    localstatedir=%buildroot/%_localstatedir/games

install -m755 -d %buildroot%_desktopdir/
cat > %buildroot%_desktopdir/%{name}.desktop <<EOF
[Desktop Entry]
Encoding=UTF-8
X-Desktop-File-Install-Version=0.2
Name=Tower Toppler
Type=Application
Comment=A clone of the 'Nebulus' game on old 8 and 16 bit machines.
Comment[ru]=Клон игры 'Nebulus', популярная на старых 8 и 16-битных машинах.
Exec=%_gamesbindir/%name
Icon=%name
Categories=Game;ArcadeGame;
EOF

mkdir -p %buildroot/%_iconsdir/hicolor/{16x16,32x32,48x48}/apps
install -m 644 %SOURCE2 %buildroot/%_iconsdir/hicolor/16x16/apps/%name.png
install -m 644 %SOURCE3 %buildroot/%_iconsdir/hicolor/32x32/apps/%name.png
install -m 644 %SOURCE4 %buildroot/%_iconsdir/hicolor/48x48/apps/%name.png

%find_lang %name

%files -f %name.lang
%_gamesbindir/*
%_gamesdatadir/%name/*
%_desktopdir/%{name}.desktop
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png
%_localstatedir/games/%name
%doc %_man6dir/*
%doc AUTHORS README COPYING ChangeLog NEWS

%changelog
* Wed Mar 21 2012 Evgeny V Shishkov <shev@altlinux.org> 1.1.5-alt1
- new version 1.1.5
- update .desktop file
- remove patches

* Mon Apr 18 2011 Igor Vlasenko <viy@altlinux.ru> 1.1.3-alt5.qa1
- NMU: converted menu to desktop file

* Thu Aug 06 2009 Evgeny V. Shishkov <shev@altlinux.org> 1.1.3-alt5
- add patch leveledit.patch (overflow destination buffer). Thank Alexey Tourbin.

* Thu Apr 30 2009 Evgeny V. Shishkov <shev@altlinux.org> 1.1.3-alt4
- Fixed build with new libtool

* Mon Nov 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 1.1.3-alt3
- remove update_menus, clean_menus from spec file
    (update_menus repocop test)

* Mon Oct 27 2008 Evgeny V. Shishkov <shev@altlinux.org> 1.1.3-alt2
- add patch highscore-gcc4.3.patch

* Thu Sep 11 2008 Evgeny V. Shishkov <shev@altlinux.org> 1.1.3-alt1
- new version 1.1.3
- new packager :)

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.6-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Aug 17 2004 Sergey V Turchin <zerg at altlinux dot org> 1.0.6-alt1
- new version
- fix icons placement

* Fri Nov 21 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.3-alt1
- new version

* Mon Oct 06 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt2
- fix build

* Tue Jun 10 2003 Sergey V Turchin <zerg at altlinux dot org> 1.0.2-alt1
- new version

* Thu Apr 03 2003 Sergey V Turchin <zerg@altlinux.ru> 1.0.0-alt1
- new version

* Thu Jan 16 2003 Sergey V Turchin <zerg@altlinux.ru> 0.98.4-alt1
- new version

* Fri Nov 22 2002 Sergey V Turchin <zerg@altlinux.ru> 0.98.0-alt1
- new version

* Wed Oct 02 2002 Sergey V Turchin <zerg@altlinux.ru> 0.97.1-alt1
- new version
- build with gcc3.2

* Sat May 18 2002 Sergey V Turchin <zerg@altlinux.ru> 0.96-alt2
- rebuild with new alsa

* Thu Feb 21 2002 Sergey V Turchin <zerg@altlinux.ru> 0.96-alt1
- new version

* Tue Jan 29 2002 Sergey V Turchin <zerg@altlinux.ru> 0.73-alt1
- new version

* Mon Jan 21 2002 Sergey V Turchin <zerg@altlinux.ru> 0.71-alt1
- initial spec
