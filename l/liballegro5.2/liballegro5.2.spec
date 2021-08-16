%define oname allegro5
%define _optlevel 3

%define major 5.2
%define minor 6
%define bugfix 0
%define sover 5.2

Name: liballegro5.2
Version: %major.7
Release: alt1

Summary: Game programming library

Group: System/Libraries
License: Giftware
URL: https://liballeg.org/

# Source-url: https://github.com/liballeg/allegro5/archive/%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: libalsa-devel dumb-devel libflac-devel libfreetype-devel
BuildRequires: libICE-devel libjpeg-devel libpng-devel
BuildRequires: libtheora-devel libvorbis-devel
BuildRequires: libXcursor-devel libXext-devel libXxf86vm-devel
BuildRequires: libXrandr-devel libXinerama-devel libXpm-devel
BuildRequires: libGL-devel libGLU-devel
BuildRequires: libopenal-devel libphysfs-devel
BuildRequires: libpulseaudio-devel libopus-devel libopusfile-devel libwebp-devel
BuildRequires: libfreeimage-devel libenet-devel



%package devel
Group: Development/C
Summary: Game programming library development files
Requires: %name = %EVR
Provides: liballegro5-devel = %version-%release
Provides: liballegro-devel = %version-%release
Conflicts: liballegro5.0-devel

%description
Allegro is a library of functions for use in computer games.

%description devel
Allegro is a library of functions for use in computer games.

This package contains files needed to build programs using Allegro.

%prep
%setup

%build
%cmake -DWANT_DOCS=OFF
%cmake_build

%install
%cmakeinstall_std

#install -d %buildroot%_man3dir
#install -p -m644 docs/man/* %buildroot%_man3dir

%files
%doc README.txt LICENSE.txt CONTRIBUTORS.txt
%_libdir/*.so.*

%files devel
%_includedir/*
%_libdir/*.so
#%_man3dir/*
%_pkgconfigdir/*

%changelog
* Mon Aug 16 2021 Vitaly Lipatov <lav@altlinux.ru> 5.2.7-alt1
- new version 5.2.7 (with rpmrb script)
- build with gtk3
- add BR: libfreeimage-devel libenet-devel

* Fri Oct 16 2020 Vitaly Lipatov <lav@altlinux.ru> 5.2.6.0-alt1
- new version (5.2.6.0) with rpmgs script
- rewrite spec, build allegro5.2 (ALT bug 38513)

* Fri Nov 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.10-alt1
- Version 5.0.10

* Fri Feb 01 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.8-alt2
- Version 5.0.8

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.5-alt2
- Rebuilt with libpng15

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
