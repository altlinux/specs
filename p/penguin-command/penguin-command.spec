Name: penguin-command
Version: 1.6.11
Release: alt1.qa1

Summary: A clone of the classic Missile Command game
Summary(ru_RU.UTF-8): Клон классической игры Missile Command
License: GPLv2
Group: Games/Arcade
Url: http://www.linux-games.com/penguin-command/index.html
Packager: Aleksandr Blokhin 'Sass' <sass@altlinux.ru>

Source: http://www.linux-games.com/penguin-command/%name-%version.tar.gz
Source1: %name.png.tar.bz2
Source2: %name.desktop

# Automatically added by buildreq on Wed Jun 18 2008 (-bi)
BuildRequires: libSDL-devel libSDL_image-devel libSDL_mixer-devel zlib-devel

%description
This is a clone of the classic "Missile Command" Game, but it has better
graphics and music. The gameplay has only been slightly modified. Penguin
Command is completely licensed under the GPL, excluding the music.

%description -l ru_RU.UTF-8
Это клон классической игры Missile Command, имеющий лучшую графику и звуковое 
сопровождение, чем у оригинала. Также несколько отличается сценарий игры.
Penguin Command, за исключением музыки, распространяется на условиях лицензии GPL.

%prep
%setup -a1

%build
%configure --bindir=%_gamesbindir --datadir=%_gamesdatadir
%make_build

%install
%makeinstall bindir=$RPM_BUILD_ROOT%_gamesbindir \
	     datadir=$RPM_BUILD_ROOT%_gamesdatadir

%__install -p -D -m644 %name.16.png $RPM_BUILD_ROOT%_miconsdir/%name.png
%__install -p -D -m644 %name.32.png $RPM_BUILD_ROOT%_niconsdir/%name.png
%__install -p -D -m644 %name.48.png $RPM_BUILD_ROOT%_liconsdir/%name.png

%__install -Dp -m 0644 %SOURCE2 %buildroot%_desktopdir/%name.desktop

%find_lang %name

%files -f %name.lang
%doc README NEWS AUTHORS ChangeLog
%dir %_gamesdatadir/%name
%dir %_gamesdatadir/%name/gfx
%dir %_gamesdatadir/%name/sound
%_gamesbindir/%name
%_gamesdatadir/%name/gfx
%_gamesdatadir/%name/sound
%_desktopdir/%name.desktop
%_niconsdir/%name.png
%_miconsdir/%name.png
%_liconsdir/%name.png
%_man6dir/*

%changelog
* Tue Nov 24 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.6.11-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for penguin-command
  * postclean-05-filetriggers for spec file

* Fri Jun 20 2008 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.6.11-alt1
- 1.6.11
- updated Buildrequires

* Sun Jan 16 2005 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.6.8-alt1
- 1.6.8

* Mon Jun 21 2004 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.6.6-alt1
- 1.6.6

* Tue Dec 17 2002 Aleksandr Blokhin 'Sass' <sass@altlinux.ru> 1.6.5-alt1
- Initial release for Sisyphus based on spec from MDK
