# vim: set ft=spec: -*- rpm-spec -*-

Name: cppunit
Version: 1.12.1
Release: alt2

Summary: C++ port of the famous JUnit framework for unit testing
License: LGPL
Group: Development/C++
Url: http://sourceforge.net/projects/cppunit

Source: %name-%version.tar
Patch: %name-%version-%release.patch
Packager: Alexey I. Froloff <raorn@altlinux.org>

# Automatically added by buildreq on Thu Oct 05 2006
BuildRequires: doxygen gcc-c++

%description
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%package devel
Summary: C++ port of the famous JUnit framework for unit testing
Group: Development/C++
Requires: %name = %version-%release
Obsoletes: %name-gcc2-devel, %name-gcc3-devel, %name-common-devel
Provides: %name-gcc2 = %version-%release, %name-gcc3 = %version-%release, %name-common-devel = %version-%release

%description devel
CppUnit is the C++ port of the famous JUnit framework for unit
testing.

%prep
%setup -q
%patch -p1

%build
%autoreconf
%configure \
	--disable-static \
	--docdir=%_docdir/%name-%version
%make_build

%install
%makeinstall_std

%files
%_libdir/lib*.so.*

%files devel
%_bindir/*
%_includedir/cppunit/
%_libdir/lib*.so
%_datadir/aclocal/*
%_man1dir/*
%_pkgconfigdir/%name.pc
%doc %_docdir/%name-%version/*

%changelog
* Sat Mar 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.12.1-alt2
- Rebuilt for debuginfo

* Mon Nov 09 2009 Alexey I. Froloff <raorn@altlinux.org> 1.12.1-alt1
- [1.12.1]
- spec cleanup

* Mon Jan 21 2008 Sir Raorn <raorn@altlinux.ru> 1.12.0-alt2
- Fix build with new autoconf

* Thu Oct 05 2006 Sir Raorn <raorn@altlinux.ru> 1.12.0-alt1
- [1.12.0]
- Updated BuildRequires

* Tue Jan 18 2005 ALT QA Team Robot <qa-robot@altlinux.org> 1.10.2-alt1.1
- Rebuilt with libstdc++.so.6.

* Mon Sep 06 2004 Alexey Voinov <voins@altlinux.ru> 1.10.2-alt1
- new version (1.10.2)

* Sat May 08 2004 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt6
- remove requirements on gcc3.2 
- buildreqs fixed

* Mon Mar 15 2004 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt5
- build fixed (*.la removed)
- multiply g++ support completely removed
- little spec clean up

* Tue Jul 08 2003 Alexey Voinov <voins@altlinux.ru> 1.8.0-alt4.2
- fixed version number for gcc3.2

* Tue Sep 10 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt4.1
- fixed version number for gcc3.2
(this is temporary release)

* Mon Aug 19 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt4
- added macros to control compilers version for which to build library
- spec rewrite: subpackages rearranged, files rearranged
- use gcc-version specific directories instead of update-alternatives
- buildreqs fixed

* Mon Jun 10 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt3
- buildreqs fixed

* Thu Jun 06 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt2
- fixed names of .so in update-alternatives
- fixed permissions on cppunit-config*
- added cppunit/ui include directory

* Sun May 26 2002 Alexey Voinov <voins@voins.program.ru> 1.8.0-alt1
- new version (1.8.0)

* Mon May 20 2002 Alexey Voinov <voins@voins.program.ru> 1.6.2-alt0.2
- support for gcc-3.x.x/gcc-2.x.x
- support for alternatives

* Thu Dec 13 2001 Alexey Voinov <voins@voins.program.ru> 1.6.2-alt0.1
- initial build 

