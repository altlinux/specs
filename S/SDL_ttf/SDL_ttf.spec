Name: SDL_ttf
Version: 2.0.10
Release: alt2

Summary: Simple DirectMedia Layer - Sample TrueType Font Library
License: LGPLv2+
Group: System/Libraries
Url: http://www.libsdl.org/projects/SDL_ttf/
# http://www.libsdl.org/projects/%name/release/%name-%version.tar.gz
Source: %name-%version.tar

# Automatically added by buildreq on Mon Aug 22 2011
# optimized out: libGL-devel libGLU-devel libX11-devel xorg-xproto-devel
BuildRequires: libSDL-devel libfreetype-devel zlib-devel

%description
This is a sample library which allows you to use TrueType fonts in your SDL
applications. It comes with an example program "showfont" which displays an
example string for a given TrueType font file.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n lib%name
Summary: Main library for %name
Group: System/Libraries

%description -n lib%name
This package contains the library needed to run programs dynamically
linked with %name.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%package -n lib%name-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains the headers that programmers will need to develop
applications which will use %name.

Warning! TrueType font decoding is under patent, and software using this
library may be in violation of this patent. Use at your own risk! See
http://www.freetype.org/ for details.

%prep
%setup

%build
%configure --disable-static
%make_build

%install
%makeinstall_std

%files -n lib%name
%_libdir/*.so.*
%doc CHANGES README

%files -n lib%name-devel
%_libdir/*.so
%_includedir/SDL/*
%_pkgconfigdir/*.pc

%changelog
* Mon Aug 22 2011 Dmitry V. Levin <ldv@altlinux.org> 2.0.10-alt2
- Fixed build.

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 2.0.10-alt1
- 2.0.9 -> 2.0.10

* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt4
- Rebuilt for debuginfo

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt3
- Rebuilt for soname set-versions

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 2.0.9-alt2
- Get rid of post/postun ldconfig.

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.9-alt1
- 2.0.9 release.

* Wed Jul 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.8-alt3
- Macroize %%post and %%postun.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 2.0.8-alt2
- Fixed BuildRequires.
- Added packager field.

* Mon May 22 2006 Anton Farygin <rider@altlinux.ru> 2.0.8-alt1
- new version
- fixed build with new freetype

* Fri Oct 29 2004 Anton Farygin <rider@altlinux.ru> 2.0.6-alt3
- build fix

* Fri Jul 02 2004 ALT QA Team Robot <qa-robot@altlinux.org> 2.0.6-alt2.1
- Rebuilt.

* Thu May 08 2003 Rider <rider@altlinux.ru> 2.0.6-alt1
- new version

* Mon Sep 23 2002 Rider <rider@altlinux.ru> 2.0.5-alt2
- rebuild (gcc 3.2)

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 2.0.5-alt1
- 2.0.5

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 2.0.4-alt2
- Rebuilt (wrong dependence on oldalsa fixed, SDL requires libalsa2) 
- Automatically added BuildRequires.
- specfile cleanups

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 2.0.4-alt1
- 2.0.4

* Wed Apr 11 2001 Kostya Timoshenko <kt@altlinux.ru> 1.2.2-ipl3mdk
- Rebuild with SDL-1.2.0
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 1.2.2-ipl2mdk
- Libification.

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz> 1.2.2-ipl1mdk
- Rebuild for RE

* Fri Dec  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.2-1mdk
- follow new lib policy
- 1.2.2

* Wed Aug 30 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.2.1-1mdk
- updated to version 1.2.1.
- updated URL.

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.2-2mdk
- automatically added BuildRequires

* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.2-1mdk
- v1.0.2

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.1-2mdk
- added url
- fixed group
- some minor package build fixes
- built against stable SDL version, previous was using 1.1.x devel

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- used specfile provided by Hakan Tandogan <hakan@iconsult.com>

* Sun Jan 16 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
