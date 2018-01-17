Name: clanlib0.8
Version: 0.8.1
Release: alt6

Summary: The ClanLib Game SDK
License: LGPL
Group: System/Libraries
Url: http://www.clanlib.org/

# http://clanlib.org/~sphair/download/
Source: http://clanlib.org/download/releases-0.8/ClanLib-%version.tar.gz
Source1: launch_x11_clanapp.sh

Patch0: ClanLib-0.8.1-link-fix.patch
Patch1: ClanLib-0.8.0-doc-install.patch
Patch2: ClanLib-0.8.0-fix-pkgconfig.patch
Patch3: ClanLib-0.8.0-gcc43.patch
Patch4: clanlib-0.8.1-alt-glibc-2.16.patch
Patch5: clanlib-0.8.1-alt-libpng15.patch
Patch6: clanlib-0.8.1-alt-gcc6.patch
Patch7: clanlib-0.8.1-alt-perl.patch


Obsoletes: clanLib, lib%name
Provides: lib%name = %version

BuildRequires: gcc-c++ libGLU-devel libICE-devel libXi-devel libXmu-devel libalsa-devel
BuildRequires: libmikmod-devel libjpeg-devel libpng-devel xorg-cf-files xsltproc libvorbis-devel
BuildRequires: libSDL_gfx-devel libSDL-devel libXxf86vm-devel

%description
The ClanLib Game SDK is a crossplatform game library designed to ease the work
for game developers. The goal is to provide a common interface to classical
game problems (loading graphics eg.), so games can share as much code as
possible. Ideally anyone with small resources should be able to write
commercial quality games.

%package devel
Summary: Headers for developing programs that will use %name
Group: Development/C++
Requires: %name = %version-%release, %name-gl = %version-%release, %name-gui = %version-%release
Requires: %name-mikmod = %version-%release, %name-network = %version-%release
Requires: %name-sound = %version-%release, %name-vorbis = %version-%release
Requires: %name-sdl = %version-%release
Provides: lib%name-devel = %version
Obsoletes: lib%name-devel

%description devel
This package contains the headers that programmers will need to develop
applications which will use %name.

%package devel-static
Summary: Static libraries for developing programs that will use %name
Group: Development/C++
Requires: %name-devel = %version-%release
Provides: lib%name-devel-static = %version

%description devel-static
This package contains the static libraries that programmers will need
to develop applications which will use %name.

%package sound
Summary: ClanLib Sound module
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-sound = %version
Obsoletes: lib%name-sound

%description sound
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Sound module (clanSound).

%package sdl
Summary: ClanLib SDL module
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-sdl = %version
Obsoletes: lib%name-sdl

%description sdl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the SDL module (clanSDL).

%package vorbis
Summary: ClanLib Vorbis module
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-sound = %version-%release
Provides: lib%name-vorbis = %version
Obsoletes: lib%name-vorbis

%description vorbis
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Vorbis module (clanVorbis).

%package gl
Summary: ClanLib GL module
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-gl = %version
Obsoletes: lib%name-gl

%description gl
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the GL module (clanGL).

%package network
Summary: ClanLib Network module
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-network = %version
Obsoletes: lib%name-network

%description network
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Network module (clanNetwork).

%package gui
Summary: ClanLib Gui module
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-gui = %version
Obsoletes: lib%name-gui

%description gui
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the Gui module (clanGUI).

%package mikmod
Summary: ClanLib MikMod module
Group: System/Libraries
Requires: %name = %version-%release
Requires: %name-sound = %version-%release
Provides: lib%name-mikmod = %version
Obsoletes: lib%name-mikmod

%description mikmod
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package is the MikMod module (clanMikMod).

%package docs
Summary: ClanLib documentation
Group: System/Libraries
Requires: %name = %version-%release
Provides: lib%name-docs = %version
Obsoletes: lib%name-docs

%description docs
The ClanLib Game SDK is a crossplatform game library designed to ease the
work for game developers. This package contains the documentation.

%prep
%setup -q -n ClanLib-%version
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p2
%patch5 -p2
%patch6 -p2
%patch7 -p2

%build
echo >> acinclude.m4
autoreconf -fisv
%configure --enable-dyn --disable-debug --disable-directfb

%make_build all

%install
%makeinstall \
	BIN_PREFIX=%buildroot%_bindir \
	LIB_PREFIX=%buildroot%_libdir \
	INC_PREFIX=%buildroot%_includedir \
	TARGET_PREFIX=%buildroot%_libdir/ClanLib \
	MAN_PREFIX=%buildroot%_mandir \
	HTML_PREFIX=%buildroot%_docdir/clanlib-%version

%__install -pD -m644 README CREDITS CODING_STYLE ascii-logo %buildroot%_docdir/clanlib-%version
%__install -pD -m755 %SOURCE1 %buildroot%_bindir/launch_x11_clanapp


%files
%dir %_docdir/clanlib-%version
%_docdir/clanlib-%version/README
%_docdir/clanlib-%version/CREDITS
%_bindir/launch_x11_clanapp
%_libdir/libclanCore-*.so.*
%_libdir/libclanSignals-*.so.*
%_libdir/libclanApp-*.so.*
%_libdir/libclanDisplay-*.so.*

%files devel
%dir %_docdir/clanlib-%version
%_docdir/clanlib-%version/CODING_STYLE
%_docdir/clanlib-%version/ascii-logo
%_libdir/*.so
%_includedir/*
%_pkgconfigdir/*

%files devel-static
%_libdir/*.a

%files docs
%dir %_docdir/clanlib-%version
%_docdir/clanlib-%version/*.html
%_docdir/clanlib-%version/Overview
%_docdir/clanlib-%version/Reference
%_docdir/clanlib-%version/Tutorial

%files mikmod
%_libdir/libclanMikMod-*.so.*

%files network
%_libdir/libclanNetwork-*.so.*

%files vorbis
%_libdir/libclanVorbis-*.so.*

%files gl
%_libdir/libclanGL-*.so.*

%files sound
%_libdir/libclanSound-*.so.*

%files sdl
%_libdir/libclanSDL-*.so.*

%files gui
%_libdir/libclanGUI-*.so.*
%_libdir/libclanGUIStyleSilver-*.so.*

%changelog
* Wed Jan 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt6
- Fixed build with new perl.

* Wed Oct 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.8.1-alt5
- Fixed build with new toolchain.

* Mon Dec 03 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt4.1
- Fixed build with glibc 2.16 and libpng15

* Mon Mar 28 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt4
- Updated Buildreqs
- Added strict dependencies between subpackages, as suggested by rpm

* Tue Jan 18 2011 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt3
- Rebuilt for set-provides

* Thu Aug 27 2009 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt2
- Updated patch to fix build on new gcc & coreutils

* Sun Nov 23 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.1-alt1
- Updated to new version

* Tue Jan 15 2008 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt4
- Fix build with new autotools

* Sat Oct 07 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt3
- Fixed weird autoconf bug (no newline at end of acinclude.m4 file)

* Sat Sep 23 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt2
- Fixed pkgconfig libdir variable.
- Added missing Tutorial to docs

* Wed Sep 20 2006 Damir Shayhutdinov <damir@altlinux.ru> 0.8.0-alt1
- New version
- Fixed buildreqs

* Mon Feb 27 2006 Stanislav Ievlev <inger@altlinux.org> 0.6.5-alt1.5
- fixed buildreqs

* Thu Jan 20 2005 Stanislav Ievlev <inger@altlinux.org> 0.6.5-alt1.4
- fixed buileing with gcc3.4

* Mon Oct 13 2003 Alexey Tourbin <at@altlinux.ru> 0.6.5-alt1.3
- fixed %name-docs package (missing files, reported by UlfR)

* Tue Sep 16 2003 Alexey Tourbin <at@altlinux.ru> 0.6.5-alt1.2
- custom optimization dropped
- buildreq re-applied (fixes build in the hasher)

* Fri Jun 20 2003 Stanislav Ievlev <inger@altlinux.ru> 0.6.5-alt1.1
- rebuild with new liblua4

* Wed Apr 30 2003 Rider <rider@altlinux.ru> 0.6.5-alt1
- aclocal & automake fixes
- specfile cleanup
- new version
- build requires update

* Wed Oct 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.6.3-alt2
- Rebuilt in new environment
- Some cpec cleanup

* Wed Aug 28 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.6.3-alt1
- 0.6.3
- Build with lua
- Added clanlib-lua * clanlib-devel-static packages

* Wed Jul 31 2002 Stanislav Ievlev <inger@altlinux.ru> 0.5.4-alt1.1
- rebuild with new vorbis
- directfb temporary disabled

* Thu Jan 23 2002 Konstantin Volckov <goldhead@altlinux.ru> 0.5.4-alt1
- 0.5.4
- Fixed requires in -devel package

* Tue Nov 28 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.5.1-alt1
- 0.5.1

* Thu Oct 11 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt3
- Rebuilt with libpng.so.3

* Thu Aug 30 2001 Dmitry V. Levin <ldv@altlinux.ru> 0.5.0-alt2
- Specfile cleanup (no more lib*lib's).

* Wed Aug 29 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.5.0-alt1
- 0.5.0
- Some spec cleanup
- Added optimization
- Added lib%name-gl package

* Sat Jun 30 2001 Stefan van der Eijk <stefan@eijk.nu> 0.5.0-2mdk
- BuildRequires:	freetype-devel --> freetype2-devel
- Removed BuildRequires:	XFree86-devel, zlib-devel

* Tue Jun 26 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.5.0-1mdk
- release 0.5.0

* Thu Apr 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-25mdk
- don't block forever on a busy dsp (patch #5)

* Fri Mar 30 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-24mdk
- use no-omit-frame-pointer to workaround g++ exceptions bug

* Thu Mar 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-23mdk
- remove explicit requires on requires, silly me

* Fri Mar  9 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-22mdk
- recompile without svgalib

* Fri Feb 16 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-21mdk
- do not put the launch_x11_clanapp script in the lib package!
- provides devel-lib with version
- put subpackages' devel files in generic devel package

* Mon Feb 12 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-20mdk
- fix BuildRequires (libbzip2-devel, thx to Jeff)

* Fri Dec  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-19mdk
- fix BuildRequires

* Tue Nov 28 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-18mdk
- new lib policy

* Tue Nov  7 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-17mdk
- provides ClanLib for compatibility

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-16mdk
- rebuild to have correct deps (e.g. sucking libraries linked to themselves)
- change name to clanlib (e.g. uppercase names suck)
- rebuild against lowercased hermes

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-15mdk
- really recompile against newest libstdc++

* Fri Nov  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-14mdk
- recompile against newest libstdc++

* Mon Oct 16 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-13mdk
- fix no-newline-at-end-of-some-sourcefiles that bothers gcc-2.96

* Mon Oct 16 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.4.4-12mdk
- Fix gcc2.96 compilation;

* Sun Sep 17 2000 David BAUDENS <baudens@mandrakesoft.com> 0.4.4-11mdk
- Don't use i386 code on non i386 compatibles archs
- Let configure do is job on PPC (and really don't use i386 code)

* Fri Sep 15 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-10mdk
- rebuild against fixed XFree-4 by fredl

* Fri Sep  8 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-9mdk
- fixed BuildRequires: removed ClanLib-devel, added XFree86-static-libs,
  ImageMagick >= 5.0.0
- removed nasty static -march=pentium, /me sucks

* Wed Sep  6 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-8mdk
- added the optional force of x11 target (envvar CLANLIB_FORCE_X11_DISPLAY)
- added a script to launch clanlib apps with force x11 target

* Wed Aug 30 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-7mdk
- added more documentation in subpackages

* Wed Aug 23 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-6mdk
- automatically added packager tag

* Wed Aug 23 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.4-5mdk
- corrected BuildRequires for archs other than ix86.

* Tue Aug 08 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.4.4-4mdk
- automatically added BuildRequires

* Tue Aug  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-3mdk
- not 100%% sure with the 2mdk

* Mon Jul 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-2mdk
- integrated patch to ImageMagick stuff from the clanlib-devel mailing
  list, thanks to the help of Ingo Ruhnke <grumbel@gmx.de>; it was a
  contribution from Matt Kimball <mkimball@veriomail.com>

* Mon Jul 31 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 0.4.4-1mdk
- took SRPM from ClanLib web site
- Mandrake adaptations
- ugly: take the Magick stuff from CVS to compile with ImageMagick 5
- mega headache; had to redefine CXXFLAGS to remove -mcpu=pentiumpro
