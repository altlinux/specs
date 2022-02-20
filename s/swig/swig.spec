%def_with boost
%def_with caml
%def_with doc
#def_with java
%def_with lua
%def_with perl5
#def_with python
%def_with python3
%def_with R
%def_with ruby
%def_with scheme
%def_with tcl

# vim:set ft=spec:
Name: swig
Version: 4.0.2
Release: alt2
Epoch: 1

Summary: Simplified Wrapper and Interface Generator (SWIG)
License: Open Source
Group: Development/C
Url: https://github.com/swig/swig

# Source-url: https://github.com/swig/swig/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Upstream patches
Patch10: swig-4.0.2-Fix-overload_simple_cast-test-with-Python-3.10.patch

%def_enable testsuite

%{?_with_boost:BuildPreReq: boost-devel}
%{?_with_caml:BuildPreReq: ocaml-findlib}
%{?_with_doc:BuildPreReq: yodl tidy htmldoc}
%{?_with_java:BuildPreReq: java-devel}
%{?_with_lua:BuildPreReq: liblua5-devel lua5}
%{?_with_perl5:BuildPreReq: perl-devel libpcre-devel}
%{?_with_python:BuildPreReq: python-devel}
%{?_with_python3:BuildPreReq: rpm-build-python3 python3-devel python-tools-2to3}
%{?_with_R:BuildPreReq: R-devel}
%{?_with_ruby:BuildPreReq: libruby-devel ruby ruby-module-etc}
%{?_with_scheme:BuildPreReq: chicken guile22-devel}
%ifarch %ix86 x86_64
%{?_with_scheme:BuildPreReq: libracket-devel racket}
%endif
%{?_with_tcl:BuildPreReq: tcl-devel}

BuildRequires: gcc-c++
BuildRequires: libXt-devel imake xorg-cf-files
BuildRequires: zlib-devel

%if_enabled testsuite
BuildRequires: perl(Math/BigInt.pm)
%endif

Provides: %name-devel = %version
Obsoletes: %name-deve
Obsoletes: %name-runtime-guile   %name-runtime-python  %name-runtime-perl  %name-runtime-ruby  %name-runtime-tcl
Requires: %name-data = %EVR

%package data
BuildArch: noarch
Summary: SWIG data files
Group: Development/C
Conflicts: %name < %EVR

%package doc
BuildArch: noarch
Summary: SWIG documentation
Group: Books/Other
Requires: %name = %EVR

%package runtime-guile
Group: System/Libraries
Summary: SWIG runtime guile library

%package runtime-perl
Group: System/Libraries
Summary: SWIG runtime perl library
Requires: %name = %EVR

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

%description data
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG data files.

%description runtime-guile
SWIG takes an interface description file written in a combination of C/C++
and special directives and produces interfaces to Perl, Python, and Tcl.
It allows scripting languages to use C/C++ code with minimal effort.

This package contains SWIG runtime guile library.

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
%autopatch -p1

%build
./autogen.sh
sed -i 's/PYLIBDIR="lib"/PYLIBDIR="%_lib"/' configure
sed -i 's/PY3LIBDIR="lib"/PY3LIBDIR="%_lib"/' configure
%configure \
	%{?_with_python:--with-python=python} \
	%{?_with_python3:--with-python3=python3} \
	%{?_with_caml:--with-ocamlc=ocamlc} \
	%{subst_with boost} \
	%{subst_with java} \
	%{subst_with perl5} \
	%{subst_with ruby} \
	%{subst_with tcl} \
	--with-pyinc=%_includedir/python%_python3_version \
	--with-pylib=%_libdir/python%_python3_version \
	--with-tclconfig=%_libdir
	#--with-tcl --with-python --with-perl5 --with-java --with-guile --with-ruby

#%__subst -p 's,/usr/local/include/Py,%_includedir/python%__python_version,g' Runtime/Makefile
# SMP incompatible
# no `all' target
%make_build
#%make docs
#%make runtime
#pushd Runtime
#%make
#popd
xz -9fk CHANGES TODO

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

%if_enabled testsuite
%check
%__make check PY3=1
%endif

%files
%_bindir/*
#%_datadir/aclocal/%name.m4
%_includedir/*
%dir %docdir
%docdir/[A-Z][A-Z]*

%files doc
%dir %docdir
%docdir/[A-Z][a-z]*
#%_man1dir/*

%files data
%_datadir/%{name}

#%files runtime-guile
#%_libdir/libswigguile*.so*
#%doc CHANGES.current LICENSE

#files runtime-perl
#_libdir/libswigpl*.so*
#doc CHANGES.current LICENSE

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
* Sat Feb 19 2022 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt2
- fix build with python 3.10

* Wed Jan 05 2022 Anton Midyukov <antohami@altlinux.org> 1:4.0.2-alt1
- new version (4.0.2) with rpmgs script
- enable testsuite
- disable python testsuite
- disable java testsuite

* Wed Apr 17 2019 Michael Shigorin <mike@altlinux.org> 1:3.0.12-alt8
- introduced explicit knobs for languages
- minor spec cleanup (needs much more attention)

* Fri Mar 08 2019 Anton Farygin <rider@altlinux.ru> 1:3.0.12-alt7
- cleanup spec (removed php5  buildrequires)

* Tue Jan 22 2019 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0.12-alt6
- NMU: additional fixes for code generated for python and gcc-8.

* Mon Dec 03 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0.12-alt5
- NMU: fixed code generated for python >= 2.3 and gcc-8.

* Wed Jul 11 2018 Andrey Cherepanov <cas@altlinux.org> 1:3.0.12-alt4.1
- (NMU) Rebuild with new Ruby autorequirements.
- Build with racket only on %%ix86 and x86_64.

* Tue Sep 26 2017 Evgeny Sinelnikov <sin@altlinux.ru> 1:3.0.12-alt4
- Fix import package (https://github.com/swig/swig/issues/769)

* Thu Jul 27 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1:3.0.12-alt3
- Removed mono dependencies

* Wed Apr 26 2017 Sergey Bolshakov <sbolshakov@altlinux.ru> 1:3.0.12-alt2
- rebuilt with guile22

* Sun Jan 29 2017 Yuri N. Sedunov <aris@altlinux.org> 1:3.0.12-alt1
- 3.0.12
- removed obsolete patches
- updated lua* build dependencies
- built with boost-1.63

* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1:3.0.8-alt1
- Version 3.0.8

* Thu Aug 13 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.7-alt1
- Version 3.0.7

* Wed Jul 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.6-alt1
- Version 3.0.6 (ALT #31128)

* Sat Apr 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.5-alt1
- Version 3.0.5

* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.2-alt1
- Version 3.0.2

* Wed Sep 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt2
- Added perl support

* Fri May 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:3.0.0-alt1
- Version 3.0.0

* Wed Dec 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.11-alt1
- Version 2.0.11

* Fri Jul 26 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.10-alt1
- Version 2.0.10

* Thu Apr 25 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.9-alt1
- Version 2.0.9

* Sun Feb 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1:2.0.8-alt1
- Back to version 2.0.8

* Thu Jan 31 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.9-alt1
- Version 2.0.9

* Fri Aug 31 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.8-alt1
- Version 2.0.8

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
