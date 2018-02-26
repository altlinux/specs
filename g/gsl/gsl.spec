Name: gsl
Version: 1.15
Release: alt2.bzr20120122

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Summary: The GNU Scientific Library for numerical analysis
License: GPL
Group: Development/Other
URL: http://www.gnu.org/software/gsl/gsl.html

# bzr branch http://bzr.savannah.gnu.org/r/gsl/trunk/
Source: %name-%version.tar
Requires: lib%name = %version-%release
Conflicts: lib%name-devel < %version-%release

# Automatically added by buildreq on Wed Jun 06 2007
BuildRequires: ghostscript-module-X ghostscript-utils

#BuildPreReq: texlive-latex-recommended texlive-generic-recommended

%package -n lib%name
Summary: Shared librairies for Scientific Library
Group: System/Libraries

%package -n lib%name-devel
Summary: Development environment for Scientific Library
Group: Development/C
Requires: lib%name = %version-%release

%package -n lib%name-devel-static
Summary: Development environment for Scientific Library
Group: Development/C
Requires: lib%name-devel = %version-%release

%package -n lib%name-doc
Summary: book for Scientific Library
Group: Documentation
BuildArch: noarch

%package -n lib%name-info
Summary: Info pages for Scientific Library
Group: Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

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

%description -n lib%name
The lib%name package is part of the GNU Scientific Library (GSL). The GSL is a
collection of routines for numerical analysis, written in C.  The GSL is
in alpha development.  It now includes a random number suite, an FFT
package, simulated annealing and root finding.  In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains shared library required for run GSL-based software.

%description -n lib%name-devel
The lib%name-devel package is part of the GNU Scientific Library (GSL). The GSL is a
collection of routines for numerical analysis, written in C.  The GSL is
in alpha development.  It now includes a random number suite, an FFT
package, simulated annealing and root finding.  In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains shared libs and include headers required for development.

%description -n lib%name-devel-static
The lib%name-devel package is part of the GNU Scientific Library (GSL). The GSL is a
collection of routines for numerical analysis, written in C.  The GSL is
in alpha development.  It now includes a random number suite, an FFT
package, simulated annealing and root finding.  In the future, it will
include numerical and Monte Carlo integration and special functions.
Linking against the GSL allows programs to access functions which can
handle many of the problems encountered in scientific computing.

This package contains static libs.

%description -n lib%name-doc
book for developers

%description -n lib%name-info
Info pages for GSL

%description -n lib%name-examples
Sources of examples for using with GSL

%prep
%setup

%build
./autogen.sh
%configure
sed -i 's|\(GSL_MINOR_VERSION.*\)+|\1|' gsl_version.h
%make_build

pushd doc
    #make ps
    #ps2pdf gsl-ref.ps
		%make gsl-ref.html
popd

%install
%makeinstall

install -d %buildroot%_docdir/lib%name-%version/examples
#install -m644 doc/gsl-ref.pdf %buildroot%_docdir/lib%name-%version
cp -fR doc/gsl-ref.html %buildroot%_docdir/lib%name-%version/
install -p -m644 doc/examples/* %buildroot%_docdir/lib%name-%version/examples
bzip2 ChangeLog
bzip2 NEWS
install -p -m644 ChangeLog.* NEWS.* AUTHORS README THANKS TODO \
	DONE VOLUNTEERS NOTES \
	%buildroot%_docdir/lib%name-%version

%files
%_bindir/*
%exclude %_bindir/%name-config
%_man1dir/*
%exclude %_man1dir/%name-config.1*

%files -n lib%name
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/AUTHORS
%_libdir/*.so.*

%files -n lib%name-devel
%_bindir/%name-config
%_libdir/*.so
%_libdir/pkgconfig/*
%_includedir/*
%_datadir/aclocal/*
%_man1dir/%name-config.1*
%_man3dir/*

#files -n lib%name-devel-static
#_libdir/*.a

%files -n lib%name-doc
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/*
%exclude %_docdir/lib%name-%version/AUTHORS
%exclude %_docdir/lib%name-%version/examples

%files -n lib%name-info
%_infodir/*.info*

%files -n lib%name-examples
%doc %dir %_docdir/lib%name-%version
%doc %_docdir/lib%name-%version/examples

%changelog
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
