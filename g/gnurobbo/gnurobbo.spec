Name:    gnurobbo
Version: 0.66
Release: alt2

Summary: GNU Robbo - It's popular Atari XE/XL game ported to Linux
License: GPL
URL: http://gnurobbo.sourceforge.net

Group: Games/Arcade

Source: %name-%version-source.tar.gz
Source1: %name.16.png
Source2: %name.32.png
Source3: %name.48.png
Source4: %name.desktop

Patch1: Makefile.patch

Packager: Evgeny V. Shishkov <shev@altlinux.org>

Summary(ru_RU.UTF8): GNU Robbo - популярная игра ATARI XE/XL портированная в Linux

# Automatically added by buildreq on Fri Dec 11 2009
BuildRequires: libSDL_image-devel libSDL_mixer-devel libSDL_ttf-devel libSDL-devel

%description
This is ATARI XE/XL game ported to Linux. This game was very popular and was one of the greatest ATARI games.
You can see similarities to sokoban, but this game has more features like shooting, unfriendly animals....

%description -l ru_RU.UTF-8
GNU Robbo - ATARI XE / XL игра портированеая на Linux. Эта игра была одной из величайших игр и была очень популярна на ATARI.
Вы можете увидеть сходство с sokoban, но эта игра имеет больше функций, таких как стрельба, злые животные...

%prep
%setup -n %name-%version
%patch1 -p1
%__subst 's,PACKAGE_DATA_DIR?=./data,PACKAGE_DATA_DIR?=%buildroot%_gamesdatadir/$(TARGET),' Makefile
%__subst 's,-DPACKAGE_DATA_DIR=\\"$(PACKAGE_DATA_DIR)\\",-DPACKAGE_DATA_DIR=\\"%_gamesdatadir/$(TARGET)\\",' Makefile
%__subst 's,#define DEFAULT_LOCALE\ \"en_GB\",#define DEFAULT_LOCALE\ \"ru_RU\",' locales.h

%build
%make_build

%install

%makeinstall BINDIR=%buildroot%_gamesbindir \
DOCDIR=%buildroot%_docdir/%name

#PACKAGE_DATA_DIR=%buildroot%_gamesdatadir/%name \

%__install -pD -m644 %SOURCE1 %buildroot%_miconsdir/%name.png
%__install -pD -m644 %SOURCE2 %buildroot%_niconsdir/%name.png
%__install -pD -m644 %SOURCE3 %buildroot%_liconsdir/%name.png
%__install -pD -m644 %SOURCE4 %buildroot%_desktopdir/%name.desktop

%files
%defattr(-, root, root)
%_gamesbindir/*
%_gamesdatadir/%name
%_desktopdir/%name.desktop
%doc README COPYING ChangeLog LICENSE-sound LICENSE-ttf NEWS
%_miconsdir/%name.png
%_niconsdir/%name.png
%_liconsdir/%name.png

%changelog
* Wed May 30 2012 Evgeny V Shishkov <shev@altlinux.org> 0.66-alt2
- add Makefile.patch

* Tue Nov 30 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.66-alt1
- new version 0.66

* Wed Jan 20 2010 Evgeny V. Shishkov <shev@altlinux.org> 0.65.6-alt1
- new version 0.65.6

* Fri Dec 25 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.65-alt2
- set default locale ru_RU

* Fri Dec 25 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.65-alt1
- new version 0.65

* Mon Dec 14 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.64-alt2
- fix PACKAGE_DATA_DIR in Makefile (error: Couldn't open levels folder)

* Fri Dec 11 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.64-alt1
- new version 0.64
- update buildreq
- remove makefile.patch

* Thu Mar 19 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.62-alt1
- new version 0.62
- update makefile.patch

* Tue Mar 10 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.61-alt3
- fix .desktop file

* Thu Mar 05 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.61-alt2
- fix PACKAGE_DATA_DIR (error: Couldn't open levels folder)

* Tue Mar 03 2009 Evgeny V. Shishkov <shev@altlinux.org> 0.61-alt1
- new version 0.61
    # Added graphical skin support
    # Added a newly created graphical skin: Tronic
    # 15 additional levels converted from RobboVII
    # 32 additional levels converted from RobboVIII
    # 32 additional levels converted from RobboIX
    # Added in-game help and a demo version
    # Added reconfigurable options
    # Added reconfigurable controls
    # Added analogue and digital joystick support
    # Added centering of game within any resolution
    # Added support for different locales
    # Added a Polish translation
    # Many bug fixes 

* Mon Nov 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.57-alt3
- remove update_menus, clean_menus from spec file
    (update_menus repocop test)

* Thu Jul 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.57-alt2
- change niconsdir macros

* Thu Apr 24 2008 Evgeny V. Shishkov <shev@altlinux.org> 0.57-alt1
- Initial build
