Name: octave
Version: 3.4.0
Release: alt2.1

%define docdir %_defaultdocdir/%name-%version

Summary: GNU Octave -- a high-level language for numerical computations
License: GPLv3
Group: Sciences/Mathematics
Url: http://www.octave.org
Packager: Paul Wolneykien <manowar@altlinux.ru>

BuildRequires: flex gcc-c++ gcc-fortran libcurl-devel libfftw3-devel libglpk-devel
BuildRequires: libhdf5-devel liblapack-goto-devel libncurses-devel libpcre-devel
BuildRequires: libreadline-devel libstdc++-devel libtinfo-devel libX11-devel libXext-devel
BuildRequires: libSM-devel libICE-devel liblcms-devel bzlib-devel libltdl-devel
BuildRequires: libGraphicsMagick-c++-devel libGL-devel libGLU-devel libfreetype-devel
BuildRequires: libftgl-devel zlib-devel desktop-file-utils gnuplot less
BuildRequires: texlive-base-bin texlive-generic-recommended

Source: %name-%version-%release.tar

Requires: gnuplot

%package devel
Summary: GNU Octave -- development part
Group: Development/C
Requires: %name = %version-%release

%package doc
Summary: GNU Octave -- documentation
Group: Development/Other
BuildArch: noarch

%description
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

Octave has extensive tools for solving common numerical linear algebra
problems, finding the roots of nonlinear equations, integrating
ordinary functions, manipulating polynomials, and integrating ordinary
differential and differential-algebraic equations. It is easily
extensible and customizable via user-defined functions written in
Octave's own language, or using dynamically loaded modules written in
C++, C, Fortran, or other languages.

%description devel
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

This package contains development libraries and header files.

%description doc
GNU Octave is a high-level language, primarily intended for numerical
computations. It provides a convenient command line interface for
solving linear and nonlinear problems numerically, and for performing
other numerical experiments using a language that is mostly compatible
with Matlab. It may also be used as a batch-oriented language.

This package contains extra documentation for GNU Octave.

%define _libexecdir %_libdir

%prep
%setup

%build
%add_optflags $(pkg-config hdf5-seq --cflags)
%autoreconf
%configure --with-blas=goto2 \
    --enable-dl --enable-shared \
    --disable-static --disable-rpath \
    --enable-lite-kernel --enable-picky-flags
#smp-unaware
%make_build

%install
%makeinstall

mkdir -p %buildroot%_datadir/octave/packages %buildroot%_libdir/octave/packages

pushd doc
mkdir -p %buildroot%docdir
find interpreter/octave.html liboctave/liboctave.html -type f | cpio -pmdv %buildroot%docdir
install -pm0644 faq/OctaveFAQ.pdf interpreter/octave.pdf \
    liboctave/liboctave.pdf refcard/refcard-a4.pdf %buildroot%docdir
popd
gzip -c ChangeLog > %buildroot%docdir/ChangeLog.gz
install -pm0644 BUGS COPYING NEWS* PROJECTS README README.Linux %buildroot%docdir

# Install the filetrigger for packages:
install -pm0755 -D altlinux/%name.filetrigger %buildroot%_rpmlibdir/%name.filetrigger

%check
%make_build check

%files
%dir %docdir
%docdir/BUGS
%docdir/COPYING
%docdir/NEWS*
%docdir/PROJECTS
%docdir/README
%docdir/README.Linux
%docdir/ChangeLog.gz

%_bindir/octave
%_bindir/octave-%version
%_bindir/octave-config
%_bindir/octave-config-%version

%_datadir/%name
%_libdir/%name-%version/*.so*
%exclude %_libdir/%name-%version/*.la*
%_libexecdir/%name

%_infodir/octave.info*
%_infodir/OctaveFAQ.info*
%_infodir/liboctave.info*

%_man1dir/*

%_desktopdir/*.desktop

%_rpmlibdir/%name.filetrigger

%files devel
%_includedir/%name-%version
%_bindir/mkoctfile
%_bindir/mkoctfile-%version

%files doc
%docdir/*.pdf
%docdir/interpreter
%docdir/liboctave

%changelog
* Thu Sep 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2.1
- Rebuilt with libhdf5-7

* Tue Jul 05 2011 Paul Wolneykien <manowar@altlinux.ru> 3.4.0-alt2
- Remove the curl/types.h inclusion.

* Tue Apr 26 2011 Paul Wolneykien <manowar@altlinux.ru> 3.4.0-alt1
- Octave v3.4.0.

* Mon Apr 25 2011 Paul Wolneykien <manowar@altlinux.ru> 3.2.4-alt2.2
- Add filetrigger for packages.

* Thu Apr 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.4-alt2.1
- Built with GotoBLAS2 instead of ATLAS

* Mon Apr 11 2011 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.4-alt2
- rebuilt with recent ftgl

* Tue Dec 07 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.4-alt1
- 3.2.4 released

* Sun Jan 24 2010 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.3-alt2
- explicitly claim ownership of %%docdir

* Fri Nov 20 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.2.3-alt1
- 3.2.3 released

* Sun May 10 2009 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.5-alt1
- 3.0.5 released

* Sat Dec  6 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt2
- obsolete by filetriggers macros removed

* Mon Sep 15 2008 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.2-alt1
- 3.0.2 released

* Sun Dec 23 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 3.0.0-alt1
- 3.0.0 released

* Sat Nov 24 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.17-alt2
- octave headers separated to devel subpackage
- redundant reqs on emacsen filtered out

* Thu Nov 15 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.17-alt1
- 2.9.17 released

* Mon Aug 13 2007 Sergey Bolshakov <sbolshakov@altlinux.ru> 2.9.13-alt1
- 2.9.13 released

* Thu Dec 25 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.52-alt1
- New version

* Tue May 06 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.47-alt1
- new version

* Wed Jan 01 2003 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.40-alt1
- new unstable version

* Tue Oct 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.37-alt2
- postscript and html printable docs added, build deps fixed

* Tue Oct 29 2002 Vitaly Lugovsky <vsl@altlinux.ru> 2.1.37-alt1
- new version (unstable)

* Sun Jan 14 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Sep 13 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-6mdk
- Rebuild with r-path (octave lib ont in /usr/lib/)

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 2.0.16-5mdk
- automatically added BuildRequires

* Wed Jul 26 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-4mdk
- Macros, BM, add multiple icons sizes

* Wed Apr 12 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-3mdk
- strip oct file
- add menu entry

* Tue Mar 21 2000 Vincent Saugey <vince@mandrakesoft.com> 2.0.16-2mdk
- corrected for new groups

* Thu Mar 09 2000 Lenny Cartier <lenny@mandrakesoft.com>
- mandrake build
- v2.0.16

* Fri Oct 23 1998 Jeff Johnson <jbj@redhat.com>
- update to 2.0.13.90

* Thu Jul  9 1998 Jeff Johnson <jbj@redhat.com>
- repackage in powertools.

* Thu Jun 11 1998 Andrew Veliath <andrewtv@usa.net>
- Add %%attr, build as user.

* Mon Jun 1 1998 Andrew Veliath <andrewtv@usa.net>
- Add BuildRoot, installinfo, require gnuplot, description from
  Octave's web page, update to Octave 2.0.13.
- Adapt from existing spec file.

* Tue Dec  2 1997 Otto Hammersmith <otto@redhat.com>
- removed libreadline stuff from the file list

* Mon Nov 24 1997 Otto Hammersmith <otto@redhat.com>
- changed configure command to put things in $RPM_ARCH-rehat-linux,
  rather than genereated one... was causing problems between building
  on i686 build machine.

* Mon Nov 17 1997 Otto Hammersmith <otto@redhat.com>
- moved buildroot from /tmp to /var/tmp

* Mon Sep 22 1997 Mike Wangsmo <wanger@redhat.com>
- Upgraded to version 2.0.9 and built for glibc system

* Thu May 01 1997 Michael Fulbright <msf@redhat.com>
- Updated to version 2.0.5 and changed to build using a BuildRoot
