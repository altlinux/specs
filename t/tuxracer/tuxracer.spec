Name: tuxracer
Version: 0.61
Release: alt13

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Tux Racer
License: GPLv2+
# Games/Sports was Mandriva choice... well, this is "racing" game, so may share
# rpm group with racing simulators. Other logical choice - Arcade (as in desktop
# menu grouping). Ok, rpm grouping is not so important ;)
Group: Games/Sports

URL: http://tuxracer.sourceforge.net/
Source0: http://downloads.sourceforge.net/tuxracer/tuxracer-%version.tar.gz
Source1: http://downloads.sourceforge.net/tuxracer/tuxracer-data-%version.tar.gz
Source2: tuxracer-16.xpm
Source3: tuxracer-32.xpm
Source4: tuxracer-48.xpm
Source5: tuxracer.desktop
Source10: http://www.brcha.iz.rs/data/projects/RoadsOfSerbia/RoadsOfSerbia.tar.bz2
Patch3: tuxracer-0.61-gcc33.patch

# Automatically added by buildreq on Tue Dec 02 2008
BuildRequires: gcc-c++ imake libGL-devel libSDL-devel libSDL_mixer-devel libXext-devel libXi-devel libXmu-devel tcl-devel xorg-cf-files

BuildRequires: autoconf_2.5
BuildRequires: automake_1.4

Requires: %name-gamedata

%description
Tux Racer is a simple OpenGL-based racing game featuring Tux. The object of the
game is to slide down a snow- and ice-covered mountain as quickly as possible,
avoiding the trees and rocks that will slow you down.

%package gamedata
Summary: Tux Racer game data
License: GPLv2+
Group: Games/Sports
BuildArch: noarch

%description gamedata
Data files for Tux Racer racing game.

%prep
%setup -a 1 -a 10

%patch3 -p1
%set_automake_version 1.4
%set_autoconf_version 2.5

# Fix CFLAGS
%define _optlevel 3
%add_optflags %optflags_kernel %optflags_notraceback %optflags_fastmath

%build
libtoolize -i

# cosmetic: eliminate gcc warnings
subst 's/malign/falign/g' configure.in

export CPPFLAGS="-DGLX_GLXEXT_LEGACY"
%configure \
	--datadir=%_gamesdatadir/tuxracer \
	--bindir=%_gamesbindir \
	--with-data-dir=%_gamesdatadir/tuxracer \
	--with-tcl-libs=%_tcllibdir
%make_build

%install
%makeinstall datadir=%buildroot%_gamesdatadir/tuxracer bindir=%buildroot%_gamesbindir

mkdir -p %buildroot%_gamesdatadir/tuxracer
cp -a tuxracer-data-%version/* %buildroot%_gamesdatadir/tuxracer
chmod -R a+rX %buildroot%_gamesdatadir
cp -a Roads\ Of\ Serbia/ %buildroot%_gamesdatadir/tuxracer/courses/contrib/roads_of_serbia

install -pD -m644 %SOURCE2 %buildroot%_miconsdir/tuxracer.xpm
install -pD -m644 %SOURCE3 %buildroot%_niconsdir/tuxracer.xpm
install -pD -m644 %SOURCE4 %buildroot%_liconsdir/tuxracer.xpm
install -pD -m644 %SOURCE5 %buildroot%_desktopdir/tuxracer.desktop

%files
%_gamesbindir/tuxracer
%_desktopdir/*
%_niconsdir/*
%_liconsdir/*
%_miconsdir/*

%files gamedata
%_gamesdatadir/tuxracer/

%changelog
* Wed Sep 30 2009 Victor Forsyuk <force@altlinux.org> 0.61-alt13
- Fix FTBFS due to missing libtoolize call in current configure macro.

* Tue Dec 02 2008 Victor Forsyuk <force@altlinux.org> 0.61-alt12
- Renew build requirements to fix FTBFS.

* Wed Sep 10 2008 Victor Forsyuk <force@altlinux.org> 0.61-alt11
- Renew buildreqs.
- Split game data to noarch package.
- Add additional track: Roads of Serbia.

* Wed Mar 12 2008 Victor Forsyuk <force@altlinux.org> 0.61-alt10
- Rebuild with tcl 8.5.

* Tue May 17 2005 Victor Forsyuk <force@altlinux.ru> 0.61-alt9
- Saving Private Tux :) from obsolete.
- Update buildreqs.

* Sun Jan 04 2004 Anton Farygin <rider@altlinux.ru> 0.61-alt8
- gcc 3.3 build fix

* Wed Oct 01 2003 Rider <rider@altlinux.ru> 0.61-alt7
- fix build

* Tue Oct 10 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.61-alt6
- Rebuild with new tcl & gcc3.2

* Sat Jun 15 2002 Sergey Bolshakov <s.bolshakov@belcaf.com> 0.61-alt5
- rebuilt in new env

* Tue Dec 04 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.61-alt4
- Fixed permissions

* Thu Nov 19 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.61-alt3
- Fixed icons

* Fri Aug 17 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.61-alt2
- Recompiled with SDL 1.2.2
- Compiled with fixed optflags

* Thu May 31 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.61-alt1
- Build new version 0.61

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 0.60.3-ipl3mdk
- Rebuild with SDL-1.2.0

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 0.60.3-ipl2mdk
- fix BuildPreReq

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 0.60.3-ipl1mdk
- Build for RE

* Wed Dec 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.3-1mdk
- 0.60.3

* Wed Dec 20 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.1-8mdk
- recompiled to get good dependencies.

* Fri Dec  8 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.1-7mdk
- corrected BuildRequires.

* Thu Dec  7 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.1-5mdk
- added icons for the menu.

* Wed Nov 29 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.1-4mdk
- added BuildRequires on libSDL_mixer1.0-devel and libSDL1.1-devel.

* Thu Nov 16 2000 Daouda Lo <daouda@mandrakesoft.com> 0.60.1-3mdk
- rebuild with gcc 2.96
- make rpmlint happier.

* Fri Oct  6 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.60.1-2mdk
- 0.60.1

* Tue Sep 19 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.12.1-2mdk
- rebuild for latest tk.

* Sun Aug 27 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.12.1-1mdk
- first mandrake version.
