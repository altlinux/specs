%define _unpackaged_files_terminate_build 1
%define libgslver 28
%define libgslcblasver 0

Name: gsl
Version: 2.8
Release: alt2
Summary: The GNU Scientific Library for numerical analysis
License: GPLv3
Group: Development/Other
URL: https://www.gnu.org/software/gsl/gsl.html
VCS: https://git.savannah.gnu.org/git/gsl.git
Source: %name-%version.tar
Patch0: gsl-2.7-alt-build.patch
Conflicts: lib%name-devel < %EVR
BuildRequires: ghostscript-module-X ghostscript-utils
# explicitly added texinfo for info files
BuildRequires: texinfo
BuildRequires: python3-module-sphinx python3-module-sphinx-sphinx-build-symlink python3-module-sphinx_rtd_theme

%package -n libgslcblas%libgslcblasver
Summary: BLAS Shared librairy for GNU Scientific Library
Group: System/Libraries
Conflicts: libgsl < 2.8-alt1

%package -n libgsl%libgslver
Summary: Shared librairy for GNU Scientific Library (GSL)
Group: System/Libraries
Obsoletes: libgsl

%package -n lib%name-devel
Summary: Development environment for GNU Scientific Library (GSL)
Group: Development/C
Requires: libgsl%libgslver = %EVR
Requires: libgslcblas%libgslcblasver = %EVR

%package -n lib%name-doc
Summary: book for Scientific Library
Group: Documentation
BuildArch: noarch

%package -n lib%name-info
Summary: Info pages for Scientific Library
Group: Documentation
BuildArch: noarch
Conflicts: %name < %EVR

%package -n lib%name-examples
Summary: Examples sources for using with Scientific Library
Group: Documentation
BuildArch: noarch

%description
The %name package is part of the GNU Scientific Library (GSL). The GSL is a
collection of routines for numerical analysis, written in C.  The GSL is
in alpha development.  It now includes a random number suite, an FFT
package, simulated annealing and root finding.  In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

Install the %name package if you need utilities for high-level scientific
numerical analysis.

%description -n libgslcblas%libgslcblasver
The libgslcblas package is part of the GNU Scientific Library (GSL).
The GNU Scientific Library (GSL) is a collection of routines for numerical
computing. The routines have been written from scratch in C, and present a
modern Applications Programming Interface (API) for C programmers,
allowing wrappers to be written for very high level languages.

Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains shared library required for run GSL-based software.

%description -n libgsl%libgslver
The libgsl package is part of the GNU Scientific Library (GSL).
The GNU Scientific Library (GSL) is a collection of routines for numerical
computing. The routines have been written from scratch in C, and present a
modern Applications Programming Interface (API) for C programmers,
allowing wrappers to be written for very high level languages.

Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains shared library required for run GSL-based software.

%description -n libgsl-devel
The libgsl-devel package is part of the GNU Scientific Library (GSL).
The GNU Scientific Library (GSL) is a collection of routines for numerical
computing. The routines have been written from scratch in C, and present a
modern Applications Programming Interface (API) for C programmers,
allowing wrappers to be written for very high level languages.

Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains shared libs and include headers required for development.

%description -n lib%name-doc
book for developers

%description -n lib%name-info
Info pages for GSL

%description -n lib%name-examples
Sources of examples for using with GSL

%prep
%setup
%patch0 -p1

%build
%autoreconf
%configure
%make_build

%install
%makeinstall

rm -f %buildroot%_libdir/*.a

%files
%_bindir/*
%exclude %_bindir/%name-config
%_man1dir/*
%exclude %_man1dir/%name-config.1*

%files -n libgsl%libgslver
%doc AUTHORS
%_libdir/libgsl.so.%libgslver
%_libdir/libgsl.so.%libgslver.*

%files -n libgslcblas%libgslcblasver
%_libdir/libgslcblas.so.%libgslcblasver
%_libdir/libgslcblas.so.%libgslcblasver.*

%files -n lib%name-devel
%doc ChangeLog NEWS README THANKS TODO DONE VOLUNTEERS NOTES
%_bindir/%name-config
%_libdir/*.so
%_pkgconfigdir/*
%_includedir/*
%_datadir/aclocal/*
%_man1dir/%name-config.1*
%_man3dir/*

%files -n lib%name-info
%_infodir/*.info*

%files -n lib%name-examples
%doc doc/examples

%changelog
* Sun Jul 14 2024 Anton Farygin <rider@altlinux.ru> 2.8-alt2
- Added copflict with libgs < 2.8 (Fixes: #50901)

* Wed May 29 2024 Anton Farygin <rider@altlinux.ru> 2.8-alt1
- 2.7 -> 2.8

* Thu Jul 29 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 2.7-alt1
- Updated to upstream version 2.7.

* Mon Apr 13 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6-alt1
- Updated to upstream version 2.6.

* Mon Sep 10 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 2.5-alt1
- Updated to upstream version 2.5.

* Mon Aug 28 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.4-alt1
- Updated to upstream version 2.4.
- Cleaned up spec.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.16-alt1.git20150121.1
- NMU: added BR: texinfo

* Wed Mar 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1.git20150121
- New snapshot

* Sat Jul 05 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1.git20140602
- New snapshot

* Wed Nov 13 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.16-alt1.bzr20131023
- Version 1.16

* Tue Jun 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15.90-alt1.bzr20130614
- Version 1.15.90

* Mon Feb 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt2.bzr20130127
- New snapshot

* Wed Sep 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt2.bzr20120912
- New snapshot

* Sun Jun 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt2.bzr20120122
- Fixed Cflags in pkg-config file

* Fri Feb 24 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1.bzr20120122
- New snapshot

* Thu Dec 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1.bzr20111116
- New snapshot

* Mon Sep 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.15-alt1.bzr20110830
- Version 1.15

* Thu Apr 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.90-alt1.bzr20110416.1
- gsl/gsl_errno.h: added definition of struct FILE

* Wed Apr 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14.90-alt1.bzr20110416
- Version 1.14.90
- Disabled devel-static package

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.bzr20101012.2
- gsl_version.h: fixed GSL_MINOR_VERSION (thnx led@)

* Thu Feb 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.bzr20101012.1
- Rebuilt for dewbuginfo

* Wed Oct 20 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.bzr20101012
- New snapshot

* Tue Jun 22 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.14-alt1.bzr20100613
- Version 1.14

* Tue Nov 24 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt2.git20091014
- New snapshot

* Mon Nov 09 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.13-alt1
- Version 1.13
- Rebuilt with texlive instead of tetex

* Mon Jul 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt3
- Removed spare requirements for doc packages
- Owned doc dir for all packages with docs (ALT #20657)

* Thu Jul 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt2.1
- Added missing doc files

* Thu Jul 02 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt2
- Moved some files between packages and added examples (ALT #20657)

* Tue Jun 30 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12-alt1
- Version 1.12

* Fri Feb 29 2008 Stanislav Ievlev <inger@altlinux.org> 1.10-alt1
- 1.10

* Wed Jun 06 2007 Stanislav Ievlev <inger@altlinux.org> 1.9-alt1
- 1.9
- add subpackage with book

* Tue Jun 27 2006 Stanislav Ievlev <inger@altlinux.org> 1.8-alt1
- 1.8

* Mon Apr 03 2006 Stanislav Ievlev <inger@altlinux.org> 1.7-alt1
- 1.7
- fixed linking

* Wed Aug 18 2004 Stanislav Ievlev <inger@altlinux.org> 1.5-alt1
- 1.5

* Thu Dec 04 2003 Stanislav Ievlev <inger@altlinux.org> 1.4-alt1.1
- rebuild without .la files

* Fri Sep 12 2003 Stanislav Ievlev <inger@altlinux.ru> 1.4-alt1
- 1.4

* Tue Mar 11 2003 Stanislav Ievlev <inger@altlinux.ru> 1.3-alt1
- 1.3

* Mon Nov 11 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt2
- rebuild with gcc3

* Mon Jul 29 2002 Stanislav Ievlev <inger@altlinux.ru> 1.2-alt1
- 1.2

* Mon Apr 01 2002 Stanislav Ievlev <inger@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Fri Nov 16 2001 Stanislav Ievlev <inger@altlinux.ru> 1.0-alt1
- 1.0

* Tue Sep 25 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9.3-alt2
- Fixed requirements.

* Fri Sep 21 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9.3-alt1
- 0.9.3

* Mon Sep 03 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9.2-alt1
- 0.9.2

* Wed Jul 11 2001 Stanislav Ievlev <inger@altlinux.ru> 0.9-alt1
- 0.9

* Fri Jun 01 2001 Stanislav Ievlev <inger@altlinux.ru> 0.8-alt1
- 0.8

* Wed Apr 11 2001 Stanislav Ievlev <inger@altlinux.ru> 0.7-alt1
- Up to 0.7 . devel-static package

* Wed Jan 17 2001 Dmitry V. Levin <ldv@fandra.org> 0.6-ipl1mdk
- RE adaptions.
- Fixed texinfo documentation.

* Wed Dec 06 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.6-1mdk
- new release
- fix build on PPC
- new lib scheme

* Fri Jul 28 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.5-3mdk
- BM
- split out devel

* Tue Apr 18 2000 John Buswell <johnb@mandrakesoft.com> 0.5-2mdk
- Fixed distribution tag

* Thu Mar 30 2000 John Buswell <johnb@mandrakesoft.com> 0.5-1mdk
- 0.5
- Fixed groups
- spec-helper

* Mon Nov 24 1999 Camille Begnis <camille@mandrakesoft.com>
- added %%defattr and SMP compilation
- updated url and ftp source

* Tue Aug 16 1999 Bernhard Rosenkraenzer <bero@linux-mandrake.com>
- 0.4.1

* Tue Jul 06 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Build for new environment (Rel: 5mdk).

* Wed May 19 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>

- Remove the ldconfig hack of bero.

* Tue May 11 1999 Bernhard Rosenkraenzer <bero@mandrakesoft.com>
- Mandrake adaptions
- make ldconfig in %post and %preun -p

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com>
- auto rebuild in the new build environment (release 2)

* Thu Mar 11 1999 Bill Nottingham <notting@redhat.com>
- update to 0.3f
- add patches to fix glibc-2.1 compilation, doc oddity

* Thu Feb 25 1999 Bill Nottingham <notting@redhat.com>
- new summary/description, work around automake oddity

* Tue Jan 12 1999 Michael K. Johnson <johnsonm@redhat.com>
- libtoolize for arm

* Thu Sep 10 1998 Cristian Gafton <gafton@redhat.com>
- spec file fixups

* Sat May 9 1998 Michael Fulbright <msf@redhat.com>
- started with package for gmp from Toshio Kuratomi <toshiok@cats.ucsc.edu>
- cleaned up file list
- fixed up install-info support
