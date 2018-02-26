# vim: set ft=spec: -*- mode: rpm-spec; -*-
# $Id: libffcall,v 1.5 2004/07/15 06:29:38 raorn Exp $

%def_enable static

%define	lname	ffcall
%define	version	1.10
%define	release	alt2

Name: lib%lname
Version: %version
Release: %release
Summary: Foreign Function Call Libraries
Group: System/Libraries
License: GPL
URL: http://www.haible.de/bruno/packages-ffcall.html

Source: http://www.haible.de/bruno/gnu/%lname-%version.tar.gz
Packager: Repocop Q. A. Robot <repocop@altlinux.org>

%{?_enable_static:BuildPreReq: glibc-devel-static}

%description
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

%package devel
Summary: Development headers for Foreign Function Call Libraries
Group: Development/C
Requires: %name = %version-%release

%description devel
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

This package contains development headers for FFCall libraries

%if_enabled static
%package devel-static
Summary: Development headers for Foreign Function Call Libraries
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This is a collection of four libraries which can be used to build
foreign function call interfaces in embedded interpreters.

The four packages are:

    avcall - calling C functions with variable arguments

    vacall - C functions accepting variable argument prototypes

    trampoline - closures as first-class C functions

    callback - closures with variable arguments as first-class C functions
               (a reentrant combination of vacall and trampoline)

This package contains static verions of FFCall libraries
%endif

%prep
%setup -q -n %lname-%version

%build
# SMP b0rken...
%define __nprocs 1
%{?!_enable_static:export lt_cv_prog_cc_static_works=no}
%configure \
	--enable-shared \
	%{subst_enable static}
%make_build

%install
%__mkdir_p %buildroot{%_includedir,%_libdir,%_mandir,%_datadir}
%makeinstall

%files
%doc COPYING NEWS PLATFORMS README
%_libdir/*.so.*

%files devel
%doc */*.html
%_includedir/*
%_libdir/*.so
%_mandir/man?/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%changelog
* Thu Oct 28 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10-alt2
- Rebuilt for soname set-versions

* Fri Nov 13 2009 Repocop Q. A. Robot <repocop@altlinux.org> 1.10-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * post_ldconfig for libffcall
  * postun_ldconfig for libffcall
  * postclean-05-filetriggers for spec file

* Thu Jul 15 2004 Sir Raorn <raorn@altlinux.ru> 1.10-alt1
- [1.10]
- Url updated (closes #3038)
- Explicitly enabled static

* Mon Dec 15 2003 Sir Raorn <raorn@altlinux.ru> 1.8d-alt5
- devel-static and *.la fixes

* Sun Sep 14 2003 Sir Raorn <raorn@altlinux.ru> 1.8d-alt4
- SMP build b0rken
- Some spec cleanups

* Tue Jul 30 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt3
- Libraries made shared

* Wed Jul 17 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt2
- Renamed to %name-devel

* Sat May 11 2002 Sir Raorn <raorn@altlinux.ru> 1.8d-alt1
- [1.8d]

* Mon Jan 07 2002 Sir Raorn <raorn@altlinux.ru> 1.8c-alt3
- Spec celanup

* Sat Jan 05 2002 Sir Raorn <raorn@altlinux.ru> 1.8c-alt2
- Fixed %doc for html documentation

* Sat Aug 18 2001 Sir Raorn <raorn@binec.ru>
- initial RPM release


