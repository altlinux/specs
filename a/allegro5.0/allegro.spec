%define oname allegro
%define _optlevel 3

%define major 5
%define minor 0
%define bugfix 5
%define sover 5.0
Name: %oname%sover
Version: %major.%minor.%bugfix
Release: alt1

Group: System/Libraries
Summary: Game programming library
License: Giftware 
URL: http://alleg.sourceforge.net
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

Source0: http://sunsite.auc.dk/allegro/%name-%version.tar
Patch0: allegro-4.0.1-allegro.h.patch
Patch1: allegro-4.1.8-allegro.h.patch

Obsoletes: %name

BuildRequires: esound-devel gcc-c++ glib2-devel libalsa-devel 
BuildRequires: libjack-devel libaudiofile-devel pkgconfig cmake
BuildRequires: libX11-devel libGL-devel libGLU-devel libXxf86dga-devel
BuildPreReq: libXtst-devel libXcomposite-devel libXcursor-devel
BuildPreReq: libXft-devel libXi-devel libXinerama-devel libXpm-devel
BuildPreReq: libXrender-devel libXrandr-devel libXt-devel libXv-devel
BuildPreReq: libXxf86misc-devel libICE-devel svgalib-devel /proc
BuildPreReq: libpng-devel zlib-devel libogg-devel libvorbis-devel
BuildPreReq: libXxf86vm-devel libXdamage-devel libXdmcp-devel
BuildPreReq: libXScrnSaver-devel libflac-devel libjpeg-devel
BuildPreReq: libopenal-devel libphysfs-devel dumb-devel
BuildPreReq: libgtk+2-devel libpixman-devel

%package -n lib%name
Group: System/Libraries
Summary: Game programming library

%package -n lib%name-devel
Group: Development/C
Summary: Game programming library development files
Requires: lib%name = %version-%release
Provides: allegro-devel = %version-%release
Obsoletes: allegro-devel

%description
Allegro is a library of functions for use in computer games.

%description -n lib%name
Allegro is a library of functions for use in computer games.

%description -n lib%name-devel
Allegro is a library of functions for use in computer games.

This package contains files needed to build programs using Allegro.

%prep
%setup

%build
mkdir Build
pushd Build

FLAGS="-pthread -fno-strict-aliasing %optflags"
FLAGS="$FLAGS %optflags_shared"
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DWANT_LINUX_CONSOLE:BOOL=ON \
	-DDOCDIR:STRING=share/doc \
	-DCMAKE_STRIP:FILEPATH="/bin/echo" \
%ifarch x86_64
	-DLIB_SUFFIX:STRING=64 \
%endif
	..
%make_build

popd

%install
%makeinstall_std -C Build

install -d %buildroot%_man3dir
install -p -m644 docs/man/* %buildroot%_man3dir

gzip CHANGES*

%files -n lib%name
%doc README.txt CHANGES* LICENSE.txt CONTRIBUTORS.txt
%_libdir/*.so.*

%files -n lib%name-devel
%doc docs/html/refman/*
%_includedir/*
%_libdir/*.so
%_man3dir/*
%_pkgconfigdir/*

%changelog
* Tue Jan 17 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.5-alt1
- Version 5.0.5

* Mon Apr 18 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.2.1-alt1
- Version 5.0.2.1

* Fri Mar 25 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1.1-alt2
- Added libXxf86vm-devel into BuildPreReq

* Tue Dec 14 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.1.1-alt1
- Version 4.4.1.1

* Wed Nov 04 2009 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1.1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for liballegro
  * postun_ldconfig for liballegro

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.2.2-alt1
- New version.
- Fixed #6444: own %%_libdir/allegro as well.

* Tue Apr 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.2.1-alt2
- Disabling asm && mmx, as it breaks binary compatibility and moves
  many-many symbols to unsharable.a library.

* Fri Jan 05 2007 Pavlov Konstantin <thresh@altlinux.ru> 4.2.1-alt1
- 4.2.1 release.
- Enabling asm && mmx.
- Disabling building static library.
- unresolved=relaxed.

* Tue May 16 2006 Pavlov Konstantin <thresh@altlinux.ru> 4.2.0-alt1
- New version.

* Thu Apr 29 2004 Sergey V Turchin <zerg at altlinux dot org> 4.1.14-alt1
- new version

* Mon Apr 28 2003 Sergey V Turchin <zerg at altlinux dot ru> 4.0.3-alt1
- 4.0.3 final

* Mon Apr 07 2003 Sergey V Turchin <zerg at altlinux dot ru> 4.0.3-alt0.1.rc3
- new version

* Fri Feb 28 2003 Sergey V Turchin <zerg@altlinux.ru> 4.0.3-alt0.1.rc1
- new version

* Wed Dec 25 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.2-alt4
- rebuild without alsa1

* Wed Oct 16 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.2-alt3
- add missing files

* Wed Oct 16 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.2-alt2
- build with gcc3.2
- build without svgalib

* Fri Aug 16 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.2-alt1
- new version

* Fri Jun 07 2002 Konstantin Volckov <goldhead@altlinux.ru> 4.0.1-alt1
- 4.0.1
- Libification
- Removed ALSA modules to another subpackage

* Tue Mar 19 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.0-alt3
- add patch0 (from cooker)

* Mon Jan 21 2002 Sergey V Turchin <zerg@altlinux.ru> 4.0.0-alt2
- fix build

* Thu Dec 20 2001 Sergey V Turchin <zerg@altlinux.ru> 4.0.0-alt1
- new version

* Fri Jul 27 2001 Sergey V Turchin <zerg@altlinux.ru> 3.9.36-alt1
- build for ALT

* Mon May 14 2001 Lenny Cartier <lenny@mandrakesoft.com>  3.9.36-1mdk
- updated to 3.9.36

* Wed Feb 28 2001 Lenny Cartier <lenny@mandrakesoft.com>  3.9.34-1mdk
- updated by Vlatko Kosturjak <kost@linux-mandrake.com> 3.9.34-1mdk
	- support for new version
	- removed patch
- use egcs

* Thu Jan 04 2001 David BAUDENS <baudens@mandrakesoft.com> 3.9.33-3mdk
- ExcludeArch: PPC
- Fix devel description
- Spec clean up

* Thu Jan 04 2001 Lenny Cartier <lenny@mandrakesoft.com> 3.9.33-2mdk
- rebuild

* Wed Sep 27 2000 Pixel <pixel@mandrakesoft.com> 3.9.33-1mdk
- initial spec
