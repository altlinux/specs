Name: xtux
Version: 20030306
Release: alt5

Summary: X11 client server network game featuring opensource mascots
License: GPL
Group: Games/Arcade

Url: http://xtux.sf.net

Packager: Andrey Rahmatullin <wrar@altlinux.ru>

Source: %name-src-%version.tar.gz
# from PLD
Source1: %name.desktop
Source2: %name-48.png
Source3: %name-32.png
Source4: %name-16.png
Patch0: %name-20030306-pld-makefile-optflags.patch
Patch1: %name-20030306-pld-newgame-fix.patch
Patch2: %name-20030306-debian-disable-ggz.patch

BuildPreReq: libXpm-devel

Requires: fonts-bitmap-75dpi
Requires: %name-data = %version-%release

%description
XTux Arena is a client server network game for X11 featuring
opensource mascots, like Linus, RMS, GNOME, KDE, and of course tux.
Players can compete in a multiplayer deathmatch mode (called holywar)
or play against the computer (cooperative multiplayer supported) in a
mission against Microsoft.


%package data
Summary: Data files for XTux
Group: Games/Arcade
BuildArch: noarch

%description data
XTux Arena is a client server network game for X11 featuring
opensource mascots, like Linus, RMS, GNOME, KDE, and of course tux.

This package contains data files needed to play XTux.


%prep
%setup -n %name
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%make_build DATADIR=%_gamesdatadir/%name OPTFLAGS="%optflags"

%install
mkdir -p %buildroot{%_gamesdatadir,%_gamesbindir,%_menudir}
install -pD -m755 xtux tux_serv %buildroot%_gamesbindir
cp -R data %buildroot%_gamesdatadir/%name
install -pD -m644 %SOURCE1 %buildroot%_desktopdir/%name.desktop
install -pD -m644 %SOURCE2 %buildroot%_liconsdir/%name.png
install -pD -m644 %SOURCE3 %buildroot%_niconsdir/%name.png
install -pD -m644 %SOURCE4 %buildroot%_miconsdir/%name.png


%files
%_gamesbindir/*
%_desktopdir/%name.desktop
%_liconsdir/%name.png
%_miconsdir/%name.png
%_niconsdir/%name.png
%doc doc scripts AUTHORS CHANGELOG README README.GGZ

%files data
%_gamesdatadir/%name


%changelog
* Mon Nov 17 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20030306-alt5
- remove update_*/clean_* invocations

* Mon Aug 04 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20030306-alt4
- add 16x16 and 32x32 pixmaps
- split noarch data package
- fix desktop file according to desktop-file-validate

* Sun Mar 09 2008 Andrey Rahmatullin <wrar@altlinux.ru> 20030306-alt3
- remove menu file
- fix desktop file location
- add update_menus call
- fix icon file location
- ad Url
- update buildreqs
- disable GGZ (Debian)
- add Requires: fonts-bitmap-75dpi

* Sun Oct 24 2004 Andrey Rahmatullin <wrar@altlinux.ru> 20030306-alt2
- fix menu section

* Mon Oct 11 2004 Andrey Rahmatullin <wrar@altlinux.ru> 20030306-alt1
- initial build
