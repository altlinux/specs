# vim:set ft=spec:
Name: swig
Version: 2.0.4
Release: alt4

Summary: Simplified Wrapper and Interface Generator (SWIG)
License: Open Source
Group: Development/C
Url: http://www.swig.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: http://download.sourceforge.net/swig/%name-%version.tar.gz
Patch1: %name-1.3.21-alt-configure.patch
#Patch2: %name-1.3.22-runtime.patch
Patch3: %name-1.3.22-no_ansi.patch
Patch4: %name-1.3.25-runtime.patch
#Patch5: %name-1.3.39-swig-user-ruby-1.9-fixes.patch
Patch6: %name-1.3.39-alt-ruby-includes.patch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python-devel yodl chicken libracket-devel
BuildPreReq: racket R-devel libpcre-devel boost-devel
BuildPreReq: python3-devel python-tools-2to3 zlib-devel
# Automatically added by buildreq on Thu Sep 04 2008
BuildRequires: findlib gcc-c++ guile18-devel imake java-devel
BuildRequires: libXt-devel liblua5-devel libruby-devel lua5 mono-mcs
BuildRequires: perl-devel php5-devel python-devel ruby ruby-module-etc
BuildRequires: tcl-devel xorg-cf-files tidy htmldoc

Provides: %name-devel = %version
Obsoletes: %name-deve
Obsoletes: %name-runtime-guile  %name-runtime-php  %name-runtime-python  %name-runtime-perl  %name-runtime-ruby  %name-runtime-tcl

%package doc
BuildArch: noarch
Summary: SWIG documentation
Group: Books/Other
Requires: %name = %version-%release

%package runtime-guile
Group: System/Libraries
Summary: SWIG runtime guile library

%package runtime-php
Group: System/Libraries
Summary: SWIG runtime php library

%package runtime-perl
Group: System/Libraries
Summary: SWIG runtime perl library

%package runtime-python
Group: System/Libraries
Summary: SWIG runtime python library

%package runtime-ruby
Group: System/Libraries
Summary: SWIG runtime ruby library

%package runtime-tcl
Group: System/Libraries
Summary: SWIG runtime tcl library

%description
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

%description doc
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG documentation.

%description runtime-guile
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime guile library.

%description runtime-php
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime php library.

%description runtime-perl
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime perl library.

%description runtime-python
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime python library.

%description runtime-ruby
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime ruby library.

%description runtime-tcl
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime tcl library.

%prep
%setup
#patch1 -p1
#patch4 -p1
#patch5 -p2
%patch6 -p2

%build
./autogen.sh
subst 's/PYLIBDIR="lib"/PYLIBDIR="%_lib"/' configure
subst 's/PY3LIBDIR="lib"/PY3LIBDIR="%_lib"/' configure
%configure \
	--with-python=python \
	--with-python3=python3 \
	--with-boost \
	--with-pyinc=%_includedir/python%_python_version \
	--with-pylib=%_libdir/python%_python_version \
	--with-tclconfig=%_libdir
	#--with-tcl --with-python --with-perl5 --with-java --with-guile --with-ruby --with-php4

#%__subst -p 's,/usr/local/include/Py,%_includedir/python%__python_version,g' Runtime/Makefile
# SMP incompatible
# no `all' target
%make
%make docs
#%make runtime
#pushd Runtime
#%make
#popd
bzip2 -9fk CHANGES TODO

%install
%makeinstall_std \
	M4_INSTALL_DIR=%buildroot%_datadir/aclocal
mkdir -p %buildroot%_includedir
cp -aL Source/Swig/*.h Source/DOH/*.h Source/Include/*.h \
	%buildroot%_includedir/
# symlinks
#__rm -fv Examples/perl Examples/test-suite/perl Examples/GIFPlot/Php4

%define docdir %_docdir/%name-%version
rm -rf %buildroot%docdir
mkdir -p %buildroot%docdir
install -p -m644 ANNOUNCE CHANGES* COPYRIGHT LICENSE* README RELEASENOTES TODO* \
	%buildroot%docdir/
cp -a Examples Doc %buildroot%docdir/

#pushd Runtime
#%make_install install DESTDIR=%buildroot
#popd

%files
%_bindir/*
#%_datadir/aclocal/%name.m4
%_includedir/*
%_datadir/%{name}
%dir %docdir
%docdir/[A-Z][A-Z]*

%files doc
%dir %docdir
%docdir/[A-Z][a-z]*
%_man1dir/*

#%files runtime-guile
#%_libdir/libswigguile*.so*
#%doc CHANGES.current LICENSE

#%files runtime-php
#%_libdir/libswigphp*.so*
#%doc CHANGES.current LICENSE

#%files runtime-perl
#%_libdir/libswigpl*.so*
#%doc CHANGES.current LICENSE

#%files runtime-python
#%_libdir/libswigpy*.so*
#%doc CHANGES.current LICENSE

#%files runtime-ruby
#%_libdir/libswigrb*.so*
#%doc CHANGES.current LICENSE

#%files runtime-tcl
#%_libdir/libswigtcl*.so*
#%doc CHANGES.current LICENSE

%changelog
* Tue Apr 10 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt4
- Rebuilt without pike7.8-devel

* Wed Apr 04 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt3
- Built with Python 3 support

* Tue Aug 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt2
- Fixed for asdict

* Sun Aug 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.4-alt1
- Version 2.0.4

* Mon Mar 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.2-alt1
- Version 2.0.2

* Mon Nov 08 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1
- Version 2.0.1

* Wed Jul 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0-alt1
- Version 2.0.0 (ALT #23734)

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.40-alt2
- Fixed previous error (build with old sources)

* Sun Feb 07 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.40-alt1
- Version 1.3.40

* Fri Nov 06 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.39-alt1.1
- Rebuilt with python 2.6

* Fri Jul 03 2009 Alexey I. Froloff <raorn@altlinux.org> 1.3.39-alt1
- [1.3.39]

* Tue Nov 25 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.36-alt2
- rebuild with php5-devel in buildreq

* Thu Sep 04 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.36-alt1
- new version
- fixed build req

* Mon Mar 17 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.34-alt1
- new version

* Mon Feb 18 2008 Gleb Stiblo <ulfr@altlinux.ru> 1.3.31-alt2
- Remove python version from build requirements.
  (Thanks to Grigory Batalov <bga@altlinux.ru>)

* Fri Dec 15 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.3.31-alt1
- new version

* Tue May 23 2006 Gleb Stiblo <ulfr@altlinux.ru> 1.3.29-alt1
- new version

* Fri Dec 09 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.27-alt1
- new version

* Thu Nov 17 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.25-alt2
- x86_64 build bug fixed

* Wed Aug 10 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.25-alt1
- new upstream release

* Wed Mar 30 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.24-alt2
- gcc3.3 depends fixed

* Thu Jan 06 2005 Gleb Stiblo <ulfr@altlinux.ru> 1.3.24-alt1
- new version
- debian patch for runtime libs

* Sun Aug 22 2004 Dmitry V. Levin <ldv@altlinux.org> 1.3.21-alt6
- Updated build dependencies.
- Packaged docs in separate subpackage.
- Packaged other runtime libraries in separate subpackages,
  resurrected %%post/%%postun scripts.

* Fri Jun 11 2004 Gleb Stiblo <ulfR@altlinux.ru> 1.3.21-alt5
- libswigpy moved to swig-runtime-python

* Thu Jun 10 2004 Gleb Stiblo <ulfR@altlinux.ru> 1.3.21-alt4
- libswigpy.so added for subversion-python

* Fri Jun 04 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.3.21-alt3
- removed runtime libraries
- swig and swing-devel merged

* Thu Jun 03 2004 Gleb Stiblo <ulfr@altlinux.ru> 1.3.21-alt2
- rebuild with new python building scheme

* Wed Jan 14 2004 Alexey Tourbin <at@altlinux.ru> 1.3.21-alt1
- 1.3.21
- built with python23

* Thu Nov 27 2003 Alexey Tourbin <at@altlinux.ru> 1.3.19-alt2
- do not package .la files
- post/postun ldconfig scripts added
- static libraries not packaged by default

* Thu Nov 13 2003 Alexey Tourbin <at@altlinux.ru> 1.3.19-alt1
- updated to 1.3.19

* Thu Oct 17 2002 Rider <rider@altlinux.ru> 1.3.16-alt1
- 1.3.16

* Wed Aug 14 2002 Rider <rider@altlinux.ru> 1.3.14-alt1
- 1.3.14
- specfile cleanup
- BuildRequires fix

* Sat Feb 09 2002 Rider <rider@altlinux.ru> 1.3.11-alt1
- 1.3.11

* Fri Jan 04 2002 Rider <rider@altlinux.ru> 1.3a5-alt1
- 1.3a5

* Sat Jan 13 2001 AEN <aen@logic.ru>
- RE  adaptation
- build with pythin 2.0

* Fri Nov 17 2000 David BAUDENS <baudens@mandrakesoft.com> 1.3a3-2mdk
- Rebuild with gcc-2.96 & glibc-2.2

* Wed Jul 19 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.3a3-1mdk
- BM.
- Clean up specs.
- 1.3a3.

* Tue Jun 20 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.1p5-5mdk
- Use makeinstall macros.

* Mon Apr 10 2000 Francis Galiegue <fg@mandrakesoft.com> 1.1p5-4mdk
- Provides: swig

* Mon Apr  3 2000 Pixel <pixel@mandrakesoft.com> 1.1p5-3mdk
- rebuild with new perl
- cleanup

* Wed Mar 22 2000 Francis Galiegue <fg@mandrakesoft.com> 1.1p5-2mdk
- Rebuilt on kenobi
- Don't use prefix

* Fri Mar 10 2000 Francis Galiegue <francis@mandrakesoft.com> 1.1p5-1mdk
- First RPM for Mandrake
