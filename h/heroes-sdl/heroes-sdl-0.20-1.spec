%define _name   heroes

Name:           heroes-sdl
Version:        0.21
Release:        alt2

Summary:        Heroes - Game like Nibbles but different.
License:	GPL
Group:          Games/Arcade
URL:            http://heroes.sourceforge.net/
Source:         http://download.sourceforge.net/heroes/%_name-%version.tar.gz
Packager:	Fr. Br. George <george@altlinux.ru>

Patch1: heroes-0.21-gcc4.diff
Patch2: heroes-0.21-gcc_warning.diff
Patch3: heroes-0.21-menus.diff
Provides: heroes

Requires: heroes-data
# Automatically added by buildreq on Wed Oct 04 2006
BuildRequires: esound help2man liballegro-devel libmikmod-devel libSDL-devel libSDL_mixer-devel linux-libc-headers perl-Locale-gettext

%description
Heroes is similar to the "Tron" and "Nibbles" games of yore, but includes
many graphical improvements and new game features.  In it, you must
maneuver a small vehicle around a world and collect powerups while avoiding
obstacles, your opponents' trails, and even your own trail. Several modes
of play are available, including "get-all-the-bonuses", deathmatch, and
"squish-the-pedestrians".

%define customdocdir %_docdir/%name-%version
%define pixdir  %_datadir/pixmaps

%prep
%setup -q -n %_name-%version
%patch1 -p1
%patch2
%patch3


%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir --without-ggi --without-gii --disable-debug --enable-html-doc=%customdocdir ;
%make_build INTLLIBS=-lm
cat > %name.desktop <<@@@
[Desktop Entry]
Type=Application
Name=Heroes
Comment=Collect powerups and avoid your opponents' trails
Exec=heroes
TryExec=heroes
Icon=%name
Terminal=false
Categories=Application;Game;ArcadeGame;
StartupNotify=false
@@@

%install
%make_install DESTDIR=%buildroot install
mkdir -p %buildroot%pixdir
install -D %name.desktop %buildroot%_desktopdir/%name.desktop
install -pD -m644 misc/heroes-*.xpm %buildroot%pixdir
install -D misc/heroes-1.xpm %buildroot%_liconsdir/%name.xpm

%find_lang %name

%files -f %name.lang
%doc ABOUT-NLS ANNOUNCE AUTHORS BUGS COPYING ChangeLog ChangeLog.00 ChangeLog.01 HACKING INSTALL NEWS README THANKS TODO
%_gamesbindir/heroes
%_gamesbindir/heroeslvl
%_infodir/heroes*
%_man6dir/heroes.6*
%_man6dir/heroeslvl.6*
%_gamesdatadir/heroes/etc/heroesrc
%pixdir/heroes-*.xpm
%_desktopdir/%name.desktop
%_liconsdir/%name.xpm


%changelog
* Fri May 25 2012 Fr. Br. George <george@altlinux.ru> 0.21-alt2
- DSO list completion

* Sat Aug 08 2009 Fr. Br. George <george@altlinux.ru> 0.21-alt1
- Rebuild (closes #20429)

* Fri May 23 2008 Fr. Br. George <george@altlinux.ru> 0.21-alt0.3
- Another opensuse patch added (fixes coredump problem)

* Wed Oct 04 2006 Alex Murygin <murygin@altlinux.ru> 0.21-alt0.2
- added patches from opensuse
  heroes-0.21-gcc4.diff
  heroes-0.21-gcc_warning.diff

* Sun Mar 16 2003 Alex Murygin <murygin@altlinux.ru> 0.21-alt0.1
- First build for Sisyphus.

