Summary: GPL rendition of old Arcade Volleyball game
Name: gav
Version: 0.8.0
Release: alt4.qa2
URL: http://gav.sourceforge.net
Source: %name-%version.tar.gz
Patch: %name.patch
Patch1: %name-%version-fix.patch
Patch2: %name-%version-desktop.patch
Patch3: %name-%version-gcc4.patch
License: GPL
Group: Games/Sports 

Summary(ru_RU.KOI8-R): Аркадный волейбол

# due to .desktop
Requires: /usr/bin/sound_wrapper

# Automatically added by buildreq on Mon Mar 06 2006
BuildRequires: esound gcc-c++ libSDL-devel libSDL_image-devel libSDL_net-devel libstdc++-devel 

%description
An SDL-based rendition of an old favorite CGA game featuring
two characters playing a volleyball-like game. This "revamped"
version is supposed to support theming, multiplayer games,
different input devices and networking.

%description -l ru_RU.KOI8-R
SDL версия старой популярной CGA игры, в которой двое играют
в некое подобие волейбола. Текущая версия поддерживает скины,
сетевую игру, различные устройства управления.


%prep
%setup -q
%patch -p1
%patch1 -p1
%patch2 -p1
%patch3 -p0

%build
make depend
%make

%install
%__mkdir_p %buildroot{%_gamesbindir,%_gamesdatadir}
%makeinstall ROOT=%buildroot

# Icon
%__install -p -m644 -D package/%name.png  %buildroot%_miconsdir/%name.png

# desktop-file
%__install -p -m644 -D package/%name.desktop  %buildroot%_desktopdir/%name.desktop


%files
%_gamesbindir/*
%_gamesdatadir/*
%_desktopdir/%name.desktop
%_miconsdir/%name.png
%doc README CHANGELOG 

%changelog
* Tue Apr 12 2011 Igor Vlasenko <viy@altlinux.ru> 0.8.0-alt4.qa2
- NMU: .desktop files should use /usr/bin/sound_wrapper

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.8.0-alt4.qa1
- NMU (by repocop): the following fixes applied:
  * update_menus for gav
  * postclean-05-filetriggers for spec file

* Fri May 19 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.8.0-alt4
- gcc4 compatible

* Mon Mar 06 2006 Eugene V. Horohorin <genix@altlinux.ru> 0.8.0-alt3
- menu file changed with gav.desktop
- buildreq updated
- gav.desktop fix

* Mon Nov 28 2005 Eugene V. Horohorin <genix@altlinux.ru> 0.8.0-alt2
- patch of Alex Plehanov applyed (options a saved now, a lot of small fixes)

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.8.0-alt1.1
- Rebuilt with libstdc++.so.6.

* Tue Apr 27 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.8.0-alt1
- updated to version 0.8.0
- updated russian descriptions
- thanks to Michael Shigorin:
	+ menu file repair (use soundwrapper)
	+ spec cleanups 
	

* Thu Apr 01 2004 Eugene V. Horohorin <genix@altlinux.ru> 0.7.3-alt1
- implementation build

