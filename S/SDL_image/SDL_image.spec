Name: SDL_image
Version: 1.2.10
Release: alt3

Summary: Simple DirectMedia Layer - image
Group: System/Libraries
License: LGPLv2+
Url: http://www.libsdl.org/projects/SDL_image/
Packager: Pavlov Konstantin <thresh@altlinux.ru>
# http://www.libsdl.org/projects/%name/release/%name-%version.tar.gz
Source0: %name-%version.tar

%def_disable static
%define libname lib%name
# must match SDL_VERSION= in configure.ac
%define SDL_ver %version

BuildRequires: libSDL-devel >= %SDL_ver
BuildRequires: libjpeg-devel libpng-devel libtiff-devel zlib-devel

%description
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.

%package -n %libname
Summary: Main library for %name
Group: System/Libraries
Requires: libSDL >= %SDL_ver

%description -n %libname
Simple DirectMedia Layer (SDL) is a cross-platform multimedia library
designed to provide fast access to the graphics frame buffer and audio
device.  This package contains a simple library for loading images of
various formats (BMP, PPM, PCX, GIF, JPEG, PNG) as SDL surfaces.

%package -n %libname-devel
Summary: Headers for developing programs that will use %name
Group: Development/C
Requires: %libname = %version-%release

%description -n %libname-devel
This package contains %name development library and header files
required to build %name-based software.

%package -n %libname-devel-static
Summary: Static libraries for developing programs that will use %name
Group: Development/C
Requires: %libname-devel = %version-%release

%description -n %libname-devel-static
This package contains %name static library required to build
statically-linked %name-based software.

%prep
%setup
# required for autoreconf
mv acinclude m4
rm m4/l*.m4
touch NEWS AUTHORS ChangeLog

%build
# required for properly linked showimage
%autoreconf
%configure \
	--disable-jpg-shared \
	--disable-png-shared \
	--disable-tif-shared \
	%{subst_enable static}
%make_build

%install
%makeinstall_std
mkdir -p %buildroot%_bindir
install -pm755 .libs/showimage %buildroot%_bindir/

%files -n %libname
%_bindir/showimage
%_libdir/*.so.*

%files -n %libname-devel
%_libdir/*.so
%_includedir/SDL/*
%_pkgconfigdir/*
%doc README CHANGES

%if_enabled static
%files -n %libname-devel-static
%_libdir/*.a
%endif

%changelog
* Fri Mar 11 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt3
- Rebuilt for debuginfo

* Wed Nov 03 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.10-alt2
- Rebuilt for soname set-versions

* Mon Jun 07 2010 Dmitry V. Levin <ldv@altlinux.org> 1.2.10-alt1
- Updated to 1.2.10 release.
- Disabled build of static library.
- Linked the library with libjpeg, libpng and libtiff.
- Packaged showimage utility.
- Packaged pkgconfig file.

* Fri Mar 06 2009 Pavlov Konstantin <thresh@altlinux.ru> 1.2.7-alt1
- 1.2.7 release.
- Get rid of post/postun ldconfig.

* Thu Feb 14 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt3
- Buffer overflow fix in RLE decompression (CVE-2008-0544).

* Fri Feb 01 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt2
- Fix GIF handling buffer overflow (CVE-2007-6697).

* Wed Aug 22 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.6-alt1
- 1.2.6 release.

* Wed Jul 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.5-alt3
- Macroize %%post and %%postun.

* Mon Mar 26 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.5-alt2
- Fixed #11194.

* Sun Feb 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.2.5-alt1
- 1.2.5 release.
- Fixed build requires.

* Fri Sep 17 2004 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.3-alt2.1
- Rebuilt with libtiff.so.4.

* Sun Dec 14 2003 Rider <rider@altlinux.ru> 1.2.3-alt2
- removed .la files from devel package

* Thu May 08 2003 Rider <rider@altlinux.ru> 1.2.3-alt1
- new version
- specfile cleanup

* Tue Oct 01 2002 Rider <rider@altlinux.ru> 1.2.2-alt3
- Automatically fixed BuildRequires.

* Mon Sep 23 2002 Rider <rider@altlinux.ru> 1.2.2-alt2
- rebuild (gcc 3.2)

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 1.2.2-alt1
- 1.2.2

* Thu May 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt2
- Rebuilt (wrong dependence on oldalsa fixed, libSDL requires libalsa2)
- Automatically added BuildRequires.
- specfile cleanups

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.2.1-alt1
- 1.2.1

* Sat Oct 20 2001 Rider <rider@altlinux.ru> 1.2.0-alt3
- BuildRequires fix

* Thu Oct 11 2001 AEN <aen@logic.ru> 1.2.0-alt2
- rebuilt with libpng.so.3

* Fri Aug 17 2001 Rider <rider@altlinux.ru> 1.2.0-alt1
- 1.2.0

* Thu Apr  5 2001 2001 Kostya Timoshenko <kt@altlinux.ru> 1.1.0-ipl5mdk
- Rebuild with SDL-1.2.0
- Moved static libraries to devel-static subpackage.

* Wed Mar 14 2001 Kostya Timoshenko <kt@petr.kz> 1.1.0-ipl4mdk
- Libification.

* Wed Dec 27 2000 Kostya Timoshenko <kt@petr.kz> 1.1.0-ipl3mdk
- Rebuild for RE

* Fri Dec  1 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.1.0-3mdk
- 1.1.0
- better new lib policy, do not generate anymore an ambiguous package
  containing binaries but with the old lib name

* Wed Nov 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.10-2mdk
- new lib policy

* Sat Nov  4 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.10-1mdk
- 1.0.10
- macros

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 1.0.9-2mdk
- automatically added BuildRequires

* Fri Jul 14 2000 Giuseppe Ghibò <ghibo@mandrakesoft.com> 1.0.9-1mdk
- updated version.
- added BuildPreReq.

* Fri Jun 23 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.0.6-1mdk
- v1.0.6

* Tue Apr 11 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.4-2mdk
- added url
- fixed group
- some minor package build fixes
- built against stable SDL version, previous was using 1.1.x devel

* Fri Feb 11 2000 Lenny Cartier <lenny@mandrakesoft.com>
- v1.0.4
- used the specfile provided by Hakan Tandogan <hakan@iconsult.com>

* Tue Jan 18 2000 Hakan Tandogan <hakan@iconsult.com>
- initial spec file
- renamed usr/bin/show to sdlshow because of conflict with mh

