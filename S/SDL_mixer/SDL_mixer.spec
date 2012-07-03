Name: SDL_mixer
Version: 1.2.11
Release: alt5
Summary: Simple DirectMedia Layer - mixer
Group: System/Libraries
License: LGPLv2+
Url: http://www.libsdl.org/projects/SDL_mixer/

Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires: gcc-c++ libSDL-devel libvorbis-devel libflac-devel libmikmod-devel
BuildRequires: libmad-devel

%description
SDL_mixer is a sample multi-channel audio mixer library.  It supports
any number of simultaneously playing channels of 16 bit stereo audio,
plus a single channel of music, mixed by the popular MikMod MOD,
Timidity MIDI, FLAC, Ogg Vorbis, and SMPEG MP3 libraries.

%package -n lib%name
Summary: Main library for %name
Group: System/Libraries
Requires: timidity-instruments
Provides: %name = %version-%release

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

%package -n lib%name-devel
Summary: Header files for developing programs that will use %name
Group: Development/C
Requires: lib%name = %version-%release
Provides: %name-devel = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package utils
Summary: %name utilities for playing various types of sound files.
Group: System/Libraries
Requires: lib%name = %version-%release

%description utils
This package contains the %name console utilities for playing various
types of sound files using %name.

%prep
%setup
%patch -p1

cat acinclude/* > aclocal.m4

%build
autoconf
%configure \
	--enable-music-mp3-mad-gpl \
	--disable-music-mp3-shared \
	--disable-music-ogg-shared \
	--disable-music-flac-shared \
	--disable-music-mod-shared \
	--disable-static
# get rid of RPATH
sed -ri 's/^(hardcode_libdir_flag_spec|runpath_var)=.*/\1=/' libtool
%make_build

%install
%makeinstall_std

%files utils
%_bindir/playmus
%_bindir/playwave

%files -n lib%name
%doc CHANGES README
%_libdir/lib*.so.*

%files -n lib%name-devel
%_libdir/*.so
%_includedir/SDL
%_pkgconfigdir/*.pc

%changelog
* Wed Feb 29 2012 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt5
- replaced by smpeg to mad

* Tue Dec 27 2011 Dmitry V. Levin <ldv@altlinux.org> 1.2.11-alt4
- Added SDL_mixer-utils subpackage (by Igor Vlasenko).

* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.11-alt3
- Rebuilt for debuginfo

* Fri Nov 19 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.11-alt2
- Minor specfile cleanup.
- Rebuilt for soname set-versions.

* Tue Dec 15 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.11-alt1
- 1.2.11

* Fri Nov 13 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.9-alt2
- disabled smpeg on arm

* Tue Oct 20 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Sat Mar 14 2009 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt4
- rebuild

* Mon Nov 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt3
- disabled esd support

* Mon Nov 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt2
- fixed timidity config path/name (close #17846)
- added requires timidity-instruments

* Sun Jul 22 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.8-alt1
- 1.2.8

* Sat Jan 20 2007 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt2
- enable OGG support for %%ix86

* Wed Dec 20 2006 Valery Inozemtsev <shrek@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Feb 08 2005 Anton Farygin <rider@altlinux.ru> 1.2.6-alt2
- updated build requires
- enabled internal libmikmod (#6060)

* Tue Jan 25 2005 Anton Farygin <rider@altlinux.ru> 1.2.6-alt1
- new version

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 1.2.4-alt5
- .la files removed from lib%name-devel package

* Wed Oct 23 2002 Grigory Milev <week@altlinux.ru> 1.2.4-alt4
- rebuild with new directfb

* Tue Oct 01 2002 Rider <rider@altlinux.ru> 1.2.4-alt3
- BuildRequires fix (auto)

* Mon Sep 23 2002 Rider <rider@altlinux.ru> 1.2.4-alt2
- rebuild (gcc 3.2)

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2.4-alt1.1
- rebuild with new vorbis

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.4-alt1
- 1.2.4

* Wed May 22 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt2
- Rebuilt (wrong dependence on oldalsa fixed, SDL requires libalsa2) 
- Automatically added BuildRequires.
- specfile cleanups

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Fri Apr  6 2001 Kostya Timoshenko <kt@altlinux.ru> 1.1.0-ipl5mdk
- Rebuild with SDL-1.2.0
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 1.1.0-ipl4mdk
- Libification.

* Tue Jan 16 2001 Kostya Timoshenko <kt@petr.kz> 1.1.0-ipl3mdk
- adding SDL_mixer-fix-timidity-path.patch

* Tue Dec 26 2000 Kostya Timoshenko <kt@petr.kz> 1.1.0-ipl2mdk
- Build for RE

* Fri Dec  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.0-1mdk
- 1.1.0
- better new lib policy, do not generate anymore an ambiguous package
  containing binaries but with the old lib name

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-4mdk
- macros
- against cool new libogg and libvorbis
- new lib policy
- split package for binaries

* Thu Nov  2 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.6-3mdk
- rebuild against newest oggvorbis to get vorbis support

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.6-2mdk
- automatically added BuildRequires

* Mon Jul 03 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0.6-1mdk
- new release

* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.5-1mdk
- change buildrequires
- v1.0.5

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-4mdk
- Use makeinstall macros.

* Tue May 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0.4-3mdk
- Fix macros with new libtoolize.
- Use %-configure.

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.4-2mdk
- added url
- fixed group
- some minor package build fixes

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- v1.0.4
- used specfile provided by Hakan Tandogan <hakan@iconsult.com>

* Tue Jan 18 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
