%define oname allegro
%define _optlevel 3

%def_disable static
%set_verify_elf_method unresolved=relaxed,textrel=relaxed

%define major 4
%define minor 4
%define bugfix 3
%define sover 4.4
Name: %oname%sover
Version: %major.%minor.%bugfix.1
Release: alt2

Group: System/Libraries
Summary: Game programming library
License: Giftware 
URL: http://alleg.sourceforge.net

Source0: http://sunsite.auc.dk/allegro/%name-%version.tar
Patch4: allegro-4.4-no-degree-symbol.patch

Obsoletes: %name
Conflicts: lib%oname-svgalib < %version-%release

BuildRequires: esound-devel gcc-c++ glib2-devel libalsa-devel 
BuildRequires: libjack-devel libaudiofile-devel pkgconfig cmake
BuildRequires: libX11-devel libGL-devel libGLU-devel libXxf86dga-devel
BuildPreReq: libXtst-devel libXcomposite-devel libXcursor-devel
BuildPreReq: libXft-devel libXi-devel libXinerama-devel libXpm-devel
BuildPreReq: libXrender-devel libXrandr-devel libXt-devel libXv-devel
BuildPreReq: libXxf86misc-devel libICE-devel
BuildPreReq: libpng-devel zlib-devel libogg-devel libvorbis-devel
BuildPreReq: libXxf86vm-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%package -n lib%name
Group: System/Libraries
Summary: Game programming library

%package -n lib%oname-devel
Group: Development/C
Summary: Game programming library development files
Requires: lib%name = %version-%release
Provides: allegro-devel = %version-%release
Obsoletes: allegro-devel

%description
Allegro is a library of functions for use in computer games.

%description -n lib%name
Allegro is a library of functions for use in computer games.

%description -n lib%oname-devel
Allegro is a library of functions for use in computer games.

This package contains files needed to build programs using Allegro.

%prep
%setup
%patch4 -p2

%build
mkdir Build
pushd Build

FLAGS="-fno-strict-aliasing %optflags %optflags_shared"
cmake \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_CXX_FLAGS:STRING="$FLAGS" \
	-DCMAKE_C_FLAGS:STRING="$FLAGS" \
	-DCMAKE_VERBOSE_MAKEFILE:BOOL=ON \
	-DWANT_LINUX_CONSOLE:BOOL=ON \
	-DWANT_LINUX_VGA:BOOL=OFF \
	-DDOCDIR:STRING=share/doc \
	-DINFODIR:STRING=share/info \
%if "%_lib" == "lib64"
	-DLIB_SUFFIX:STRING=64 \
%endif
	..
%make_build

popd

%install
%makeinstall_std -C Build modulebasedir=%buildroot/%_libdir/allegro

install -Dpm 644 allegro.cfg %buildroot%_sysconfdir/allegrorc
install -pm 755 tools/x11/xfixicon.sh %buildroot%_bindir
install -m 755 Build/docs/makedoc %buildroot%_bindir/allegro-makedoc
install -dm 755 %buildroot%_datadir/allegro
install -pm 644 keyboard.dat language.dat %buildroot%_datadir/allegro

%files -n lib%name
%dir %_libdir/allegro
%dir %_libdir/allegro/%major.%minor.%bugfix
%_libdir/*.so.*
%_libdir/allegro/%major.%minor.%bugfix/alleg-dga2.so
%_libdir/allegro/%major.%minor.%bugfix/modules.lst
%_libdir/allegro/%major.%minor.%bugfix/alleg-alsadigi.so
%_libdir/allegro/%major.%minor.%bugfix/alleg-alsamidi.so
%_libdir/allegro/%major.%minor.%bugfix/alleg-jack.so
%_libdir/allegro/%major.%minor.%bugfix/alleg-fbcon.so
#_libdir/allegro/%major.%minor.%bugfix/alleg-vga.so
%_sysconfdir/allegrorc
%_datadir/allegro

%files -n lib%oname-devel
%dir %_datadir/doc/%oname-%major.%minor.%bugfix
%doc %_datadir/doc/%oname-%major.%minor.%bugfix/*
%_bindir/*
%_includedir/*
%_libdir/*.so
%_infodir/*
%_pkgconfigdir/*

%changelog
* Wed Aug 30 2023 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.3.1-alt2
- fix build with pw jack substitute

* Wed Oct 27 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.3.1-alt1
- 4.4.3.1 (closes: 41206)

* Wed Jul 21 2021 Michael Shigorin <mike@altlinux.org> 4.4.2-alt7.1
- E2K: fix build (reapply sem@'s solution for alt5)

* Thu Jan 28 2021 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.2-alt7
- FTBFS fixed

* Mon Nov 26 2018 Leontiy Volodin <lvol@altlinux.org> 4.4.2-alt6
- Fixed build

* Mon Apr 09 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.2-alt5
- drop svgalib plugin

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 4.4.2-alt4.qa1.1
- NMU: added BR: texinfo

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 4.4.2-alt4.qa1
- NMU: rebuilt for updated dependencies.

* Thu Oct 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt4
- Rebuilt with libpng15

* Thu Mar 01 2012 Sergey Bolshakov <sbolshakov@altlinux.ru> 4.4.2-alt3
- rebuilt on arm

* Thu Jul 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt2
- Added allegro-makedoc (inspired by viy@)

* Tue Jul 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.4.2-alt1
- Version 4.4.2
- Added liballeggl.so (ALT #25915)

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
