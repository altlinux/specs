%def_disable static
%define major 1.6
%define oname fox

Name: libfox
Version: %major.55
Release: alt1

Summary: The FOX C++ GUI Toolkit shared libraries

License: LGPL
Group: System/Libraries
Url: http://www.fox-toolkit.org/fox.html

# ftp://ftp.fox-toolkit.org/pub/%oname-%version.tar.gz
Source: %oname-%version.tar
Patch1: %oname-%version-alt-build.patch

# Automatically added by buildreq on Wed Jul 15 2009
BuildRequires: bzlib-devel gcc-c++ imake libGL-devel libICE-devel
BuildRequires: libXcursor-devel libXext-devel libXft-devel
BuildRequires: libXrandr-devel libjpeg-devel libpng-devel libtiff-devel
BuildRequires: xorg-cf-files libXfixes-devel libXi-devel
BuildRequires: libGLU-devel

%description
FOX is a C++-Based Library for Graphical User Interface Development
FOX supports modern GUI features, such as Drag-and-Drop, Tooltips, Tab
Books, Tree Lists, Icons, Multiple-Document Interfaces (MDI), timers,
idle processing, automatic GUI updating, as well as OpenGL/Mesa for
3D graphics.  Subclassing of basic FOX widgets allows for easy
extension beyond the built-in widgets by application writers.

%package devel
Summary: Development files and documentation for the FOX GUI toolkit.
Group: Development/C++
Requires: %name = %version-%release

%description devel
The fox-devel package contains the files necessary to develop applications
using the FOX GUI toolkit: the header files, the reswrap resource compiler,
manual pages, and HTML documentation.

%package doc
Summary: Documentation files for the FOX GUI toolkit
Group: Development/C++
BuildArch: noarch

%description doc
The package contains HTML documentation.

%if_enabled static
%package devel-static
Summary: A version of the FOX GUI toolkit for static linking
Group: Development/C++
Requires: %name-devel = %version-%release

%description devel-static
The fox-static package contains the files necessary to link applications
to the FOX GUI toolkit statically (rather than dynamically). Statically
linked applications do not require the library to be installed on the system
running the application.
%endif

%package examples
Summary: FOX example applications
Group: Development/Other
Requires: %name = %version-%release
Provides: %oname-examples
Obsoletes: %oname-examples
Obsoletes: %{name}14-examples

%description examples
The fox-example-apps package contains executables for several FOX-based
applications, including Adie, calculator and PathFinder.

%prep
%setup -n %oname-%version
%patch1 -p2
subst 's|FXFile::getExecPath(),"Adie.stx"|"%_datadir/fox-examples/","Adie.stx"|g' \
	adie/Adie.cpp

%build
%autoreconf
%add_optflags -frtti
%configure  --with-opengl=opengl \
			--enable-threadsafe \
			--with-xft \
			--with-xrandr \
			--with-xim \
			--with-shape \
			--with-xshm \
			--with-xcursor \
			--with-xrender \
			--with-cups \
			--enable-release \
			%{subst_enable static}

%make_build

%install
%makeinstall

mv %buildroot%_docdir/%oname-%major %buildroot%_docdir/%name-doc-%major

# remove non-packaged files
rm -rf %buildroot%_prefix/%name
mkdir -p %buildroot/%_datadir/fox-examples
mv %buildroot/%_bindir/Adie.stx %buildroot/%_datadir/fox-examples

mv %buildroot%_bindir/calculator %buildroot%_bindir/fox-calculator

%files
%_libdir/*.so.*
%doc AUTHORS README

%files doc
%_docdir/%name-doc-%major/

%files devel
%doc ADDITIONS INSTALL TRACING
%_bindir/%oname-config
%_bindir/reswrap
%_bindir/shutterbug
%_includedir/*
%_libdir/*.so
%_man1dir/reswrap.*
%_man1dir/shutterbug.*
%_pkgconfigdir/*.pc

%if_enabled static
%files -n lib%name-devel-static
%_libdir/*.a
%endif

%files examples
%_bindir/adie
%_bindir/PathFinder
%_bindir/fox-calculator
%_datadir/fox-examples
%_man1dir/adie.*
%_man1dir/PathFinder.*
%_man1dir/calculator.*

%changelog
* Wed Nov 15 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.55-alt1
- Updated to upstream version 1.6.55.

* Fri Apr 19 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 1.6.46-alt3.qa1
- NMU: rebuilt for updated dependencies.

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.46-alt3
- Rebuilt with libpng15

* Sat Sep 15 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.46-alt2
- Avoid conflict with qt-at-spi

* Thu Sep 13 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.46-alt1
- Version 1.6.46

* Tue Dec 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.44-alt1
- Version 1.6.44

* Thu Mar 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.43-alt1
- Version 1.6.43

* Wed Mar 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.36-alt3
- Fixed build
- Rebuilt for debuginfo

* Wed Jul 15 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.36-alt2
- update buildreq (ALT#20773)

* Sun Jul 12 2009 Vitaly Lipatov <lav@altlinux.ru> 1.6.36-alt1
- new version 1.6.36 (with rpmrb script)

* Sat Nov 29 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.34-alt1
- new version 1.6.34 (with rpmrb script)
- update buildreq

* Sat Jun 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.33-alt2
- build with xft, xrandr, xim, shape, xshm, cups support
- enable threadsafe, add -ftti to CFLAGS

* Sun May 04 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.33-alt1
- new version 1.6.33 (with rpmrb script)

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.6.31-alt1
- new version 1.6.31 (with rpmrb script)

* Wed Jul 18 2007 Vitaly Lipatov <lav@altlinux.ru> 1.6.27-alt1
- new version 1.6.27 (with rpmrb script)

* Sat Dec 30 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.20-alt0.1
- new version 1.6.20 (with rpmrb script)

* Tue Jul 18 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.8-alt0.1
- new version 1.6.8 (with rpmrb script)

* Mon Jun 26 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.6-alt0.1
- new version 1.6.6 (with rpmrb script)

* Tue Jun 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.4-alt0.1
- new version 1.6.4 (with rpmrb script)

* Wed Apr 05 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.2-alt0.1
- new version 1.6.2 (with rpmrb script)

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt0.2
- split html doc to doc package, update buildreqs
- add obsoletes for fox 1.4 examples

* Sun Apr 02 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.1-alt0.1
- new version 1.6.1
- add autoreconf, fix linking

* Wed Mar 22 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.2
- release 1.6.0

* Thu Feb 09 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.1rc3
- new version (RC3)
- rename source package, spec to libfox

* Mon Feb 06 2006 Vitaly Lipatov <lav@altlinux.ru> 1.6.0-alt0.1
- new version

* Sun Dec 18 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.27-alt1
- new version

* Tue Nov 22 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.24-alt1
- new version
- change packager

* Sun Oct 30 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.21-alt1
- NMU: new version

* Thu Oct 27 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.20-alt1
- NMU: new version

* Thu Sep 08 2005 Vitaly Lipatov <lav@altlinux.ru> 1.4.17-alt1
- NMU: new version
- fix bug #5362
- fix Adie.stx place

* Tue Jan 18 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.2.13-alt1
- 1.2.13

* Tue Jul 20 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.7-alt1
- 1.2.7

* Tue Jun 08 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.3-alt1
- 1.2.3

* Sat May 22 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.2.1-alt1
- new stable version.

* Wed May 12 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.1.53-alt1
- jump to development branch.

* Fri Mar 05 2004 Yuri N. Sedunov <aris@altlinux.ru> 1.0.51-alt1
- new version.

* Thu Dec 11 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.48-alt1
- new version.
- do not package .la files.
- do not build libfox-devel-static subpackage by default.

* Wed Nov 12 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.47-alt1
- 1.0.47

* Tue Jun 24 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.41-alt1
- 1.0.41

* Wed Feb 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 1.0.32-alt1
- 1.0.32

* Mon Oct 14 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.26-alt1
- 1.0.26
- %%files section fixed for lib%name-devel package.

* Mon Sep 09 2002 Yuri N. Sedunov <aris@altlinux.ru> 1.0.22-alt1
- Adopted for Sisyphus.
- 1.0.22 

* Tue Oct 10 2000 David Sugar <dyfet@ostel.com> 0.99.132-3
- rtti forced for rpm build specs that use -fno-rtti.

* Fri Mar 24 2000 José Romildo Malaquias <romildo@iceb.ufpo.b> 0.99.122-1
- new version

* Fri Mar 24 2000 José Romildo Malaquias <romildo@iceb.ufpo.b> 0.99.119-1
- new version

* Sun Mar 05 2000 José Romildo Malaquias <romildo@iceb.ufpo.b>
- some adaptations

* Tue Nov 10 1998 René van Paassen <M.M.vanPaassen@lr.tudelft.nl>
- initial package

