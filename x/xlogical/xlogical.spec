Name: xlogical
Version: 1.0
Release: alt8
Serial: 1
Summary: SDL logical arcade game
Summary(ru_RU.KOI8-R): Логическая игра под управлением SDL
License: GPL
Group: Games/Arcade
Url: http://changeling.ixionstudios.com/xlogical/
Packager: Fr. Br. George <george@altlinux.ru>

Source0: %name-%version-8.tar.bz2
Source2: %{name}16.xpm
Source3: %{name}32.xpm
Source4: %{name}48.xpm
Source5: %name.desktop

Patch1: %name-gcc41-compile.patch
Patch2: %name-1.0-8-gcc44.patch

# Automatically added by buildreq on Thu Nov 04 2010
BuildRequires: gcc-c++ libSDL_image-devel libSDL_mixer-devel

%description
This is a puzzle game based on a game by Rainbow Arts called Logical! which
was released on the Commodore Amiga in 1980's.  It requires parallel thinking
and quick reflexes.

%description -l ru_RU.KOI8-R
Это развивающая игра, основанная на игре компании Rainbow Arts под названием
Logical! и выпущенной для Commodere Amiga в 1980 году. Развивает параллельное
мышление и реакцию. Великолепная графика и прекрасный звук надолго отвлечет
вас и/или ваших детей от повседневных забот.

%prep
%setup -q -n %name-%version-8
#set_automake_version 1.4
#set_autoconf_version 2.5

%patch1 -p0
%patch2 -p1

%build
%autoreconf
%configure --localstatedir=%_localstatedir/games
%make_build CXXFLAGS="$RPM_OPT_FLAGS"

%install
install -pD -m2711 %name %buildroot%_x11bindir/%name
%makeinstall -C images install datadir=%buildroot%_datadir prefix=%buildroot%prefix
%makeinstall -C music install datadir=%buildroot%_datadir prefix=%buildroot%prefix
%makeinstall -C sound install datadir=%buildroot%_datadir prefix=%buildroot%prefix
install -pD -m660 %name.scores %buildroot%_localstatedir/games/%name/%name.scores
install -pD -m644 %name.levels %buildroot%_datadir/%name/%name.levels
install -pD -m644 %name.properties %buildroot%_datadir/%name/%name.properties
install -pD -m644 %SOURCE2 %buildroot%_miconsdir/%name.xpm
install -pD -m644 %SOURCE3 %buildroot%_iconsdir/%name.xpm
install -pD -m644 %SOURCE4 %buildroot%_liconsdir/%name.xpm
install -pD -m644 %SOURCE5 %buildroot%_datadir/applications/%name.desktop

%files
%attr(2711,root,games) %_x11bindir/%name
%attr(770,root,games) %dir %_localstatedir/games/%name
%attr(660,root,games) %dir %_localstatedir/games/%name/%name.scores
%_datadir/%name
%_datadir/applications/*
%_miconsdir/*
%_liconsdir/*
%_iconsdir/*.xpm
%doc ChangeLog README TODO NEWS AUTHORS

%changelog
* Fri Nov 05 2010 Fr. Br. George <george@altlinux.ru> 1:1.0-alt8
- Serial added because of alt* < ipl7mdk*

* Thu Nov 04 2010 Fr. Br. George <george@altlinux.ru> 1.0-alt8
- Version up

* Mon Dec 18 2006 Fr. Br. George <george@altlinux.ru> 1.0-ipl7mdk.4
- Fix-up rebuild

* Thu Aug 10 2006 Eugene V. Horohorin <genix@altlinux.ru> 1.0-ipl7mdk.3
- gcc4.1 compatible (thanks mike@)
- replace menu-file with desktop one

* Wed Jun 22 2005 Eugene V. Horohorin <genix@altlinux.ru> 1.0-ipl7mdk.2
- #4623 bug fix
- build requires fix

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.0-ipl7mdk.1
- Rebuilt with libstdc++.so.6.

* Tue Sep 30 2003 Rider <rider@altlinux.ru> 1.0-ipl7mdk
- build requires fix

* Fri Oct 25 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.0-ipl6mdk
- Rebuilt in new environment
- Added patch for gcc3

* Sat Apr 13 2002 Dmitry V. Levin <ldv@alt-linux.org> 1.0-ipl5mdk
- Fixed hardly broken package permissions.
- Fixed tag translation specifications.
- Added missing directories to %%files lists.

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 1.0-ipl4mdk
- build with new SDL
- Fixed CFLAGS
- Some spec cleanup

* Wed Apr 10 2001 Rider <rider@altlinux.ru>
- build with SDL 1.2.0

* Mon Mar 19 2001 Rider <rider@altlinux.ru>
- 1.0-6

* Sun Jan 21 2001 Rider <rider@linux.ru.net>
- initial spec file for RE
