%define cvs_date 20080410

Name: edb
Version: 1.0.5.042
Release: alt5.%cvs_date

Summary: Enlightenment Database Access Library
License: BSD-like
Group: Graphical desktop/Enlightenment
Url: http://www.enlightenment.org/
Source: %name-%version.tar.bz2
Patch: edb-1.0.5.042-alt-link.patch

%def_disable static
%{?_enable_static:BuildPreReq: glibc-devel-static}

BuildRequires: gtk+-devel libncurses-devel zlib-devel

%description
Edb is a database abstraction layer to Berkeley Databases. Edb contains the
source for DB 2.7.7, thus freezing the database format on disk, making sure it
will never become incompatible (as is a habit of the DB interface in libc). Edb
wraps this with a convenience and optimization API layer, making database
access easy, fast and consistent. It handles typing of information in the
database and much more.

%package -n lib%name
Summary: Graphical desktop/Enlightenment
Group: System/Libraries

%description -n lib%name
Edb is a database abstraction layer to Berkeley Databases. Edb contains the
source for DB 2.7.7, thus freezing the database format on disk, making sure it
will never become incompatible (as is a habit of the DB interface in libc). Edb
wraps this with a convenience and optimization API layer, making database
access easy, fast and consistent. It handles typing of information in the
database and much more.

This package contains shared library required for %name-based software.

%package -n lib%name-devel
Summary: Include files for development with Enlightenment Database Access Library
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
Edb is a simple, clean high-level db access/storage library.

This package contains include files required for development %name-based software.

%package -n lib%name-devel-static
Summary: Static library for development with Enlightenment Database Access Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
Edb is a simple, clean high-level db access/storage library.

This package contains static library required for development statically linked
%name-based software.

%package -n %{name}_ed
Summary: Edb command-line editor
Group: Graphical desktop/Enlightenment
Requires: lib%name = %version-%release
Conflicts: %name-utils

%description -n %{name}_ed
A command-line db editor for Edb

%package -n %{name}_gtk_ed
Summary: Edb GTK+ editor
Group: Graphical desktop/Enlightenment
Requires: lib%name = %version-%release
Conflicts: %name-utils

%description -n %{name}_gtk_ed
A GTK+ gui db editor for Edb

%package -n %{name}_vt_ed
Summary: Edb curses editor
Group: Graphical desktop/Enlightenment
Requires: lib%name = %version-%release
Conflicts: %name-utils

%description -n %{name}_vt_ed
A curses db editor for Edb

%prep
%setup -q -n %name
%patch -b .link

%build
export NOCONFIGURE=yes
sh autogen.sh

%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	--enable-cxx \
	%{subst_enable static}
%make_build

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*
%doc AUTHORS COPYING COPYING-PLAIN README src/LICENSE

%files -n lib%name-devel
%_libdir/pkgconfig/edb.pc
%_libdir/*.so
%_includedir/*

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n %{name}_ed
%_bindir/%{name}_ed

%files -n %{name}_gtk_ed
%_bindir/%{name}_gtk_ed

%files -n %{name}_vt_ed
%_bindir/%{name}_vt_ed

%changelog
* Mon May 21 2012 Yuri N. Sedunov <aris@altlinux.org> 1.0.5.042-alt5.20080410
- fixed build

* Fri Mar 11 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.5.042-alt4.20080410
- rebuild for debuginfo

* Sat Nov 06 2010 Yuri N. Sedunov <aris@altlinux.org> 1.0.5.042-alt3.20080410
- rebuild for set-version

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.0.5.042-alt2.20080410
- removed obsolete %%post{,un}_ldconfig calls

* Thu Apr 03 2008 Igor Androsov <blake@altlinux.org> 1.0.5.042-alt1.20080410
- CVS from 20080403
- * Change group to Graphical desktop/Enlightenment

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5.008-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5.008-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5.007-alt1.20070731
- CVS from 20070731.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.0.5.007-alt1.20070509
- CVS from 20070509.
- Fix BuildRequires.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 1.0.5.007-alt1.20060920
- 20060910 -> 20060920

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 1.0.5.007-alt1.20060910
- update from cvs (1.0.5.007 20060412 -> 1.0.5.007-alt1.20060910)
- buildreq

* Wed Apr 12 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.5.007-alt1.20060412
- updated from cvs

* Mon Apr 03 2006 Igor Zubkov <icesik@altlinux.ru> 1.0.5-alt2_002_20060327.1
- updated from cvs
- buildreq

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 1.0.5-alt2_002_20050530.1
- Rebuilt for new pkg-config dependencies.

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050524
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 1.0.5-alt2_002_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 1.0.5-alt2_002_20050329
- updated from cvs.

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 1.0.5-alt1_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 1.0.5-alt1_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 1.0.5-alt1_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 1.0.5-alt1_20041022
- updated from cvs.
- packadge edb-utils splitted to edb_ed edb_gtk_ed edb_vt_et
- spec cleaning
- don't build libedb-devel-static by default

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 1.0.3-alt4_20030613
- Updated from cvs.

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 1.0.3-alt4_20030315
- Updated from cvs.
- Add --enable-cxx

* Sun Nov 24 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt3_20021123
- Updated from cvs.

* Wed Oct 16 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt2
- Rebuild with gcc-3.2

* Thu Apr 04 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.3-alt1
- 1.0.3 

* Thu Apr 12 2001 Dmitry V. Levin <ldv@altlinux.ru> 1.0.2-alt2
- Libification.

* Tue Apr 3 2001 AEN <aen@logic.ru> 1.0.2-alt1
- first spec for Sisyphus
