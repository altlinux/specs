%def_disable static

Name: ecore
Version: 1.2.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Serial: 1

Summary: Enlightened Core X interface library
License: BSD
Group: System/Libraries

Url: http://www.enlightenment.org/
Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildPreReq: libeet-devel >= 1.6.0
BuildPreReq: libevas-devel >= 1.2.0 libeina-devel >= 1.2.0

BuildRequires: fontconfig-devel libcurl-devel libdirectfb-devel libevas-devel
BuildRequires: libfreetype-devel libICE-devel libjpeg-devel libXcursor-devel
BuildRequires: libXdamage-devel libXinerama-devel libXp-devel libXrandr-devel
BuildRequires: libXScrnSaver-devel xorg-x11-proto-devel libXfixes-devel
BuildRequires: libXext-devel libXrender-devel libXcomposite-devel libXtst-devel
BuildRequires: libssl-devel libgcrypt-devel glib2-devel doxygen

%description
Ecore is a nice convenience library. It handles abstracting X calls so
you don't have to pass as many parameters to them. It wraps lots of
other sequences of X calls you want to do often, handles caching local
geometry of windows to save extra X traffic, abstracts X's events and
adds a timer system to be able to do timeouts, handles the core event
loops, abstracts signals into being events in the event queue, and lets
you arbitrarily add other file descriptors to the loop to listen on and
have handlers be called when they become active, and much much more.
Ecore also handles filtering events and calling idle handlers when
appropriate. Ecore is just what it says - a very complex CORE subsystem.
It is all callback based, and keeps everything abstracted - but does not
move away from normal X11 primitives like other abstractions (GDK for
example), thus keeping 100 percent compatibility with normal Xlib stuff.
The core innards of E17 rely heavily on Ecore and its ability to not just
work, but work well and optimize silently for E17.

%package -n lib%name
Summary: Enlightened Core X interface library
Group: System/Libraries

%description -n lib%name
Ecore is a nice convenience library. It handles abstracting X calls so
you don't have to pass as many parameters to them. It wraps lots of
other sequences of X calls you want to do often, handles caching local
geometry of windows to save extra X traffic, abstracts X's events and
adds a timer system to be able to do timeouts, handles the core event
loops, abstracts signals into being events in the event queue, and lets
you arbitrarily add other file descriptors to the loop to listen on and
have handlers be called when they become active, and much much more.
Ecore also handles filtering events and calling idle handlers when
appropriate. Ecore is just what it says - a very complex CORE subsystem.
It is all callback based, and keeps everything abstracted - but does not
move away from normal X11 primitives like other abstractions (GDK for
example), thus keeping 100 percent compatibility with normal Xlib stuff.
The core innards of E17 rely heavily on Ecore and its ability to not just
work, but work well and optimize silently for E17.

This package contains shared Ecore library.

%package -n lib%name-devel
Summary: Ecore headers and development libraries
Group: Development/C
Requires: lib%name = %serial:%version-%release

%description -n lib%name-devel
This package contains Ecore headers and development libraries

%package -n lib%name-devel-static
Summary: Ecore static libraries.
Group: Development/C
Requires: lib%name-devel = %serial:%version-%release

%description -n lib%name-devel-static
This package contains Ecore static libraries.

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure %{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%find_lang %name

%files -n lib%name -f %name.lang
%_libdir/libecore*.so.*
%dir %_libdir/%name/
%dir %_libdir/%name/immodules
%_libdir/%name/immodules/xim.so
%exclude %_libdir/%name/immodules/xim.la
%doc AUTHORS COPYING INSTALL README

%files -n lib%name-devel
%_libdir/libecore*.so
%_includedir/*
%_pkgconfigdir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.1-alt1
- 1.2.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.2.0-alt1
- 1.2.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.1.0-alt1
- 1.1.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.1-alt1
- 1.0.1

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt5
- updated buildreqs

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt4
- 1.0.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt3.beta2
- 1.0.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1:1.0.0-alt1.beta
- 1.0.0.beta

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.49539-alt1
- 0.9.9.49539

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.063-alt1
- 0.9.9.063

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.062-alt1
- 0.9.9.062

* Mon Dec 01 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt2
- removed obsolete %%post{,un}_ldconfig
- updated buildreqs

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1:0.9.9.050-alt1
- 0.9.9.050

* Sat Aug 09 2008 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.9.9.041-alt1.20070918.1
- Automated rebuild due to libssl.so.6 -> libssl.so.7 soname change.

* Tue Sep 18 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.041-alt1.20070918
- CVS from 20070918.

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.041-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.041-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.040-alt1.20070731
- CVS from 20070731.
- Stricted BuildRequires for eet/evas.

* Sun May 13 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.038-alt2.20070513
- CVS from 20070513.
- Fixed BuildRequires one more time.

* Thu May 10 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.038-alt2.20070509
- Removed ecore-test subpackage.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 1:0.9.9.038-alt1.20070509
- CVS from 20070509.
- Fixed BuildRequires.

* Tue Mar 27 2007 Igor Zubkov <icesik@altlinux.org> 1:0.9.9.032-alt1.20060920.1.1
- rebuild with new libcurl.so.4

* Fri Dec 29 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1:0.9.9.032-alt1.20060920.1
- Rebuilt due to libcrypto.so.4 -> libcrypto.so.6 soname change.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 1:0.9.9.032-alt1.20060920
- 20060910 -> 20060920

* Tue Sep 12 2006 Igor Zubkov <icesik@altlinux.org> 1:0.9.9.032-alt1.20060910
- update from cvs (0.9.9.026 20060412 -> 0.9.9.032 20060910)
- buildreq

* Sat Apr 15 2006 Igor Zubkov <icesik@altlinux.ru> 1:0.9.9.026-alt1.20060412
- updated from cvs

* Thu Apr 06 2006 Igor Zubkov <icesik@altlinux.ru> 1:0.9.9-alt0.1_003_20060327
- updated from cvs
- buildreq

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050524
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 1:0.9.9-alt0.1_003_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1:0.9.9-alt0.1_003_20050329
- updated from cvs.
- added serial due to version downgrade
- added local m4 to aclocal path

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre7_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre7_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre7_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 1.0.0-alt0.1_pre7_20041022
- updated from cvs.
- add ecore-test packadge
- spec cleaning
- don't build libecore-devel-static by default

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 0.0.3-alt0.1_20030613
- Updated from cvs.

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 0.0.3-alt0.1_20030315
- Updated from cvs.

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0.2-alt0.1_20021123
- Built from cvs.

* Sat Nov 23 2002 Yuri N. Sedunov <aris@altlinux.ru> 0.0.2-alt1
- First build for Sisyphus.

