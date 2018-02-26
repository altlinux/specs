Name: cdparanoia
Version: 10.2
Release: alt2
Serial: 1
Summary: Utility to copy digital audio cd's.
License: GPL
Group: Sound
Url: http://www.xiph.org/paranoia

Requires: lib%name = %version-%release

Source: %url/download/%name-III-%version.src.tgz
Patch0: cdparanoia-10.2-#463009.patch
Patch1: cdparanoia-10.2-endian.patch

%description
This CDDA reader distribution ('%name') reads audio from the CDROM
directly as data, with no analog step between, and writes the data to a file
or pipe as .wav, .aifc or as raw 16 bit linear PCM.

%name is a complete rewrite of Heiko Eissfeldt's 'cdda2wav' program,
and generally is much better at succeeding to read difficult discs with
cheap drives.

%package -n lib%name
Summary: Shared libraries for %name
Group: System/Libraries

%description -n lib%name
%name is a complete rewrite of Heiko Eissfeldt's 'cdda2wav' program,
and generally is much better at succeeding to read difficult discs with
cheap drives.

This package contains shared libraries for %name.

%package -n lib%name-devel
Summary: Development libraries and header files for %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: cdparanoia-devel
Obsoletes: cdparanoia-devel

%description -n lib%name-devel
%name is a complete rewrite of Heiko Eissfeldt's 'cdda2wav' program,
and generally is much better at succeeding to read difficult discs with
cheap drives.

This package contains development libraries and header files for %name.

%prep
%setup -q -n %name-III-%version
%patch0 -p3
%patch1 -p1

%build
%define _optlevel 0
%add_optflags -Wno-pointer-sign -Wno-unused -Werror-implicit-function-declaration
%configure
%make OPT="$RPM_OPT_FLAGS"

%install
mkdir -p %buildroot{%_bindir,%_libdir,%_includedir,%_man1dir}
%make install \
	BINDIR=%buildroot%_bindir \
	LIBDIR=%buildroot%_libdir \
	MANDIR=%buildroot%_mandir \
	INCLUDEDIR=%buildroot%_includedir
rm -f %buildroot%_libdir/*.a

%files
%_bindir/*
%_man1dir/*.1*

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_libdir/*.so

%changelog
* Mon Oct 25 2010 Sergey V Turchin <zerg@altlinux.org> 1:10.2-alt2
- rebuilt

* Sat Aug 08 2009 Valery Inozemtsev <shrek@altlinux.ru> 1:10.2-alt1
- 10.2

* Thu Oct 12 2006 Sergey V Turchin <zerg at altlinux dot org> IIIa9.8-alt4
- merge patches from FC
- fix compile 

* Fri Mar 24 2006 Sergey V Turchin <zerg at altlinux dot org> IIIa9.8-alt3.1
- fix libcdda_paranoia linking

* Wed Jan 19 2005 Dmitry V. Levin <ldv@altlinux.org> IIIa9.8-alt3
- Fixed compilation issues detected by gcc-3.4.3.
- Do not build static library by default.

* Wed Oct 30 2002 AEN <aen@altlinux.ru> IIIa9.8-alt2
- rebuilt with gcc-3.2

* Sat May 10 2001 Mikhail Zabaluev <mhz@altlinux.ru> IIIa9.8-alt1
- IIIa9.8
- Added devel-static subpackage.

* Thu Jan 18 2001 Dmitry V. Levin <ldv@fandra.org> IIIa9.7-ipl6mdk
- Split into three subpackages.
- Increased optimization.

* Tue Jan  2 2001 Kostya Timoshenko <kt@petr.kz>
- Build for RE

* Sat Nov 25 2000 Warly <warly@mandrakesoft.com> IIIa9.7-5mdk
- split libraries

* Fri Nov 10 2000 Warly <warly@mandrakesoft.com> IIIa9.7-4mdk
- rebuilt for glib 2.2 with gcc 2.96

* Sat Aug 05 2000 Stefan van der Eijk <s.vandereijk@chello.nl> IIIa9.7-3mdk
- macroszifications
- BM
- Geoff <snailtalk@mandrakesoft.com> post and postun for libraries

* Tue Mar 28 2000 Warly <warly@mandrakesoft.com> IIIa9.7-2mdk
- add libs
- new package devel

* Sat Mar 25 2000 Warly <warly@mandrakesoft.com> IIIa9.7-1mdk
- new group name: Sound
- IIIa9.7

* Tue Dec 14 1999 Lenny Cartier <lenny@mandrakesoft.com>
- add docs from the website

* Tue Aug 24 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- III9.6
- fix the bug that preventing to rip an ATAPI cdrom

* Fri Jul 16 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.de>
- III alpha 9.5
- fixes to spec file

* Sat May 01 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- Mandrake adaptations ;-).

* Tue Dec 22 1998 Bernhard Rosenkraenzer <bero@microsoft.sucks.eu.org>
- handle RPM_OPT_FLAGS
- bzip2 man page

* Fri Dec 11 1998 Daniel Bergstrom <noa@melody.se>
- Updated to alpha9.3

* Thu Nov 19 1998 Daniel Bergstrom <daniel@futurniture.se>
- Updated to alpha9.2

* Tue Nov 17 1998 Daniel Bergstrom <daniel@bergstrom.net>
- Upgraded to alpha9.1

* Fri Nov 13 1998 Daniel Bergstrom <daniel@bergstrom.net>
- Upgraded to alpha9

* Mon Aug 24 1998 Fryguy_ <fryguy@falsehope.com>
  [III-alpha8-1]
- Upgraded to alpha8

* Mon Jun 29 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [III-alpha7-1]
- Upgraded to alpha7
- Spec rewrited to use %name and %version macros.
- %%defattr macro in %files

* Thu Apr 30 1998 Maciej Lesniewski <nimir@kis.p.lodz.pl>
  [III-alpha6-1]
- Initial release
