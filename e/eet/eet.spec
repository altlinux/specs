%def_disable tests
%def_disable static

Name: eet
Version: 1.6.1
%ifdef beta
Release: alt1.%beta
%else
Release: alt1
%endif

Summary: Library for speedy data storage, retrieval and compression.
License: BSD
Group: Graphical desktop/Enlightenment
URL: http://www.enlightenment.org/

Source: http://download.enlightenment.org/releases/%name-%version.tar.bz2

BuildRequires: libeina-devel >= 1.2.0 libjpeg-devel libgnutls-devel libgcrypt-devel zlib-devel
%{?_enable_static:BuildPreReq: glibc-devel-static}
%{?_enable_tests:BuildRequires: libcheck-devel}

%description
Eet is a tiny library designed to write an arbitary set of chunks of data
to a file and optionally compress each chunk (very much like a zip file)
and allow fast random-access reading of the file later on. It does not
do zip as a zip itself has more complexity than is needed, and it was much
simpler to impliment this once here.

It also can encode and decode data structures in memory, as well as image
data for saving to eet files or sending across the network to other
machines, or just writing to arbitary files on the system. All data is
encoded ina platform independant way and can be written and read by any
architecture.

%package -n lib%name
Summary: Eet library
Group: System/Libraries

%description -n lib%name
Eet is a tiny library designed to write an arbitary set of chunks of data
to a file and optionally compress each chunk (very much like a zip file)
and allow fast random-access reading of the file later on. It does not
do zip as a zip itself has more complexity than is needed, and it was much
simpler to impliment this once here.

It also can encode and decode data structures in memory, as well as image
data for saving to eet files or sending across the network to other
machines, or just writing to arbitary files on the system. All data is
encoded ina platform independant way and can be written and read by any
architecture.

This package contains shared Eet library.

%package -n lib%name-devel
Summary: Eet headers and development libraries
Group: Development/C
Requires: lib%name = %version-%release

%description -n lib%name-devel
This package contains Eet headers and development libraries

%package -n lib%name-devel-static
Summary: Eet static libraries
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
This package contains static libraries

%package -n lib%name-utils
Summary: Utils for eet library
Group: Graphical desktop/Enlightenment
Requires: lib%name = %version-%release

%description -n lib%name-utils
Utils for operate with Eet data

%prep
%ifdef beta
%setup -q -n %name-%version.%beta
%else
%setup -q
%endif

%build
%autoreconf
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	%{subst_enable static} \
	%{subst_enable tests}

%make_build

# tmpnam used
%check
%{?_enable_tests:%make check}

%install
%make_install DESTDIR=%buildroot install

%files -n lib%name
%_libdir/*.so.*

%files -n lib%name-devel
%_includedir/*
%_pkgconfigdir/*
%_libdir/*.so

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files -n lib%name-utils
%_bindir/*

%changelog
* Mon Jun 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Fri May 11 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Dec 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.5.0-alt1
- 1.5.0

* Sat May 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1

* Wed Mar 09 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt5
- updated buildreqs

* Sun Jan 30 2011 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt4
- 1.4.0 release

* Thu Nov 18 2010 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt3.beta2
- 1.4.0.beta2

* Tue Nov 09 2010 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt2.beta
- rebuild for update dependencies

* Fri Oct 29 2010 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1.beta
- 1.4.0.beta

* Mon Jun 07 2010 Yuri N. Sedunov <aris@altlinux.org> 1.3.0-alt1
- 1.3.0

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2
- gnutls support enabled

* Fri Jul 24 2009 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1 (closes #20863)
- updated buildreqs
- removed obsolete %%post{,un}_ldconfig calls
- fixed source url

* Sat Oct 18 2008 Yuri N. Sedunov <aris@altlinux.org> 1.1.0-alt1
- 1.1.0 release

* Thu Apr 03 2008 Igor Androsov <blake@altlinux.org> 0.9.99900-alt1.20080410
- CVS from 20080410
- * Change Group to (Graphical desktop/Enlightenment)
- + Add libeet-utils package with eet

* Mon Sep 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.10.041-alt1.20070917
- CVS from 20070917.

* Thu Sep 06 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.10.041-alt1.20070905
- CVS from 20070905.

* Tue Jul 31 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.10.040-alt1.20070731
- CVS from 20070731.

* Wed May 09 2007 Pavlov Konstantin <thresh@altlinux.ru> 0.9.10.038-alt1.20070509
- CVS from 20070509.
- Fixed buildrequires.

* Wed Sep 20 2006 Igor Zubkov <icesik@altlinux.org> 0.9.10.032-alt1.20060920
- 20060910 -> 20060920

* Sun Sep 10 2006 Igor Zubkov <icesik@altlinux.org> 0.9.10.032-alt1.20060910
- update from cvs (0.9.10.026 20060412 -> 0.9.10.032 20060910)
- buildreq

* Wed Apr 12 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.10.026-alt1.20060412
- update from cvs
- add manual pages

* Mon Apr 03 2006 Igor Zubkov <icesik@altlinux.ru> 0.9.10-alt0.1_003_20060327.1
- update from cvs
- buildreq

* Thu Feb 02 2006 ALT QA Team Robot <qa-robot@altlinux.org> 0.9.10-alt0.1_003_20050530.1
- Rebuilt for new pkg-config dependencies.

* Mon May 30 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050530
- updated from cvs.

* Tue May 24 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050524
- updated from cvs.

* Mon May 16 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050516
- updated from cvs.

* Sat May 14 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050514
- updated from cvs.

* Thu Apr 28 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050428
- updated from cvs.
- minor spec fixes.

* Mon Apr 25 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050425
- updated from cvs.

* Thu Apr 21 2005 Denis Klykvin <nikon@altlinux.ru> 0.9.10-alt0.1_003_20050421
- updated from cvs

* Tue Mar 29 2005 Alex Murygin <murygin@altlinux.ru> 0.9.10-alt0.1_003_20050329
- updated from cvs.

* Sat Jan 22 2005 Alex Murygin <murygin@altlinux.ru> 0.9.9-alt0.1_20050122
- updated from cvs.

* Tue Dec 28 2004 Alex Murygin <murygin@altlinux.ru> 0.9.9-alt0.1_20041228
- updated from cvs.

* Fri Dec 17 2004 Alex Murygin <murygin@altlinux.ru> 0.9.9-alt0.1_20041216
- updated from cvs.

* Sun Oct 24 2004 Alex Murygin <murygin@altlinux.ru> 0.9.9-alt0.1_20041022
- updated from cvs.
- spec cleaning
- don't build libeet-devel-static by default

* Fri Jun 13 2003 Alex Murygin <murygin@altlinux.ru> 0.0.1-alt0.1_20030613
- Updated from cvs.

* Sat Mar 15 2003 Alex Murygin <murygin@altlinux.ru> 0.0.1-alt0.1_20030315
- first spec for Sisyphus

