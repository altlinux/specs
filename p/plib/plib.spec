Name: plib
Version: 1.8.5
Release: alt2

Summary: Steve's Portable Game Library
License: LGPL
Group: Development/C++
Url: http://plib.sourceforge.net/

Source0: http://plib.sourceforge.net/dist/%name-%version.tar.gz

Patch1: plib-1.8.4-alt-shared.patch
Patch2: plib-1.8.4-alt-fix-unresolved.patch
Patch5: plib-1.8.4-alt-makefile.patch

Packager: Igor Zubkov <icesik@altlinux.org>

# Automatically added by buildreq on Thu May 15 2008
BuildRequires: gcc-c++ libaudio-devel libGL-devel libICE-devel libSM-devel libX11-devel libXext-devel libXi-devel libXmu-devel

%description
Write games and other realtime interactive applications that are 100 percent
portable across a wide range of hardware and operating systems.

%package devel
Summary: Development libraries and header files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
Development libraries and header files for %name.

%prep
%setup -q
%patch1 -p1
%patch2 -p1
%patch5 -p1

%build
%autoreconf
%configure \
	--disable-static
%make_build

%install
%make DESTDIR=%buildroot install

%files
%doc AUTHORS ChangeLog KNOWN_BUGS NOTICE README TODO-1.6 TODO-2.0 TODO_AFTER135
%_libdir/*.so.*

%files devel
%_libdir/*.so
%_includedir/%name

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.8.5-alt2
- Rebuilt for soname set-versions
- Fixed underlinking of libraries

* Wed Dec 10 2008 Valery Inozemtsev <shrek@altlinux.ru> 1.8.5-alt1
- NMU:
  * updated to 1.8.5
  * updated build dependencies

* Thu May 15 2008 Igor Zubkov <icesik@altlinux.org> 1.8.4-alt8
- buildreq

* Fri Jun 08 2007 Igor Zubkov <icesik@altlinux.org> 1.8.4-alt7
- run ldconfig after install and uninstall

* Thu May 25 2006 Igor Zubkov <icesik@altlinux.ru> 1.8.4-alt6
- try 2 to fix build in hasher

* Thu May 18 2006 Igor Zubkov <icesik@altlinux.ru> 1.8.4-alt5
- sync with SuSE plib-1.8.4-19
- fix rebuild with gcc 4.1

* Sat May 06 2006 Igor Zubkov <icesik@altlinux.ru> 1.8.4-alt4
- fix unresolved symbols

* Mon Nov 28 2005 Igor Zubkov <icesik@altlinux.ru> 1.8.4-alt3
- add docs
- fix build

* Thu May 12 2005 Stanislav Ievlev <inger@altlinux.org> 1.8.4-alt2
- fixed building in hasher

* Tue Feb 08 2005 Stanislav Ievlev <inger@altlinux.org> 1.8.4-alt1
- 1.8.4

* Tue Sep 21 2004 Stanislav Ievlev <inger@altlinux.org> 1.8.3-alt1
- 1.8.3

* Thu Dec 04 2003 Stanislav Ievlev <inger@altlinux.org> 1.6.0-alt3.1
- rebuild without .la files

* Tue Sep 16 2003 Stanislav Ievlev <inger@altlinux.ru> 1.6.0-alt3
- fix build in hasher

* Thu Dec 19 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.0-alt2
- fix #0001718 and #0001717

* Wed Oct 02 2002 Stanislav Ievlev <inger@altlinux.ru> 1.6.0-alt1
- 1.6.0
- split into devel and devel-static subpackages

* Mon Sep 24 2001 Sergey V Turchin <zerg@altlinux.ru> 1.5.1-alt1
- 1.5.1

* Wed Sep 19 2001 Sergey V Turchin <zerg@altlinux.ru> 1.4.2-alt2
- fix provides

* Tue Sep 18 2001 Sergey V Turchin <zerg@altlinux.ru> 1.4.2-alt1
- build for ALT

* Thu Aug 30 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.4.2-1mdk
- 1.4.2

* Mon Jun 25 2001  Daouda Lo <daouda@mandrakesoft.com> 1.4.1-1mdk
- release 1.4.1

* Fri Jun 22 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.4.0-1mdk
- version 1.4.0

* Mon Mar 05 2001 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-5mdk
- rh patches

* Fri Jan  5 2001 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0-4mdk
- rebuild

* Thu Sep 14 2000 Lenny Cartier <lenny@mandrakesoft.com> 1.2.0-3mdk
- clean spec

* Thu Aug 24 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0-2mdk
- added Packager tag
- removed hardcoded -O6

* Mon Jul  3 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.2.0-1mdk
- 1.2.0 stable release

* Thu Jun 29 2000 Guillaume Cottenceau <gc@mandrakesoft.com> 1.0.20-1mdk
- first Mandrake Package
