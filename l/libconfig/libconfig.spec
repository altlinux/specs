%def_enable static

Name: libconfig
Version: 1.4.8
Release: alt2

Summary: C/C++ Configuration File Library
License: LGPLv2.1+
Group: System/Libraries

Url: http://www.hyperrealm.com/main.php?s=libconfig
Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: flex gcc-c++

%description
Libconfig is a simple library for manipulating structured configuration
files, like this one: test.cfg. This file format is more compact and
more readable than XML. And unlike XML, it is type-aware, so it is not
necessary to do string parsing in application code.

Libconfig is very compact thus well-suited for memory constrained
systems like handheld devices.

The library includes bindings for both the C and C++ languages. It works
on POSIX-compliant UNIX systems (GNU/Linux, Mac OS X, Solaris, FreeBSD)
and Windows (2000, XP and later).

%package devel
Summary: Header files for %name
Group: Development/Other
Requires: %name = %version-%release

%description devel
Header files for %name library.

%package c++
Summary: C++ Configuration File Library
Group: System/Libraries
# doesn't require base, common code included in library

%description c++
libconfig++ is the C++ binding for libconfig library.

%package c++-devel
Summary: Header files for libconfig++ library
Group: Development/Other
Requires: %name-c++ = %version-%release
Requires: %name-devel = %version-%release
Requires: libstdc++-devel

%description c++-devel
Header files for libconfig++ library.

%if_enabled static
%package devel-static
Summary: Static library files for %name
Group: Development/Other
Requires: %name-devel = %version-%release
Requires: glibc-devel-static

%description devel-static
Static library files for %name.

%package c++-devel-static
Summary: Static library files for libconfig++
Group: Development/Other
Requires: %name-c++-devel = %version-%release
Requires: libstdc++-devel-static

%description c++-devel-static
Static library files for libconfig++.
%endif

%prep
%setup
rm -rf examples/Makefile*
rm -rf examples/*/Makefile*
rm -rf examples/*/*.vcproj
sed -i '/examples.*Makefile/d' configure.ac
%autoreconf

%build
%configure \
	%{subst_enable static} \
	--disable-examples
%make_build

%install
%makeinstall_std

%files
%doc AUTHORS ChangeLog README NEWS TODO
%_libdir/libconfig.so.*
#_bindir/libconfig_tests

%files devel
%doc examples/
%_libdir/libconfig.so
%_includedir/libconfig.h
%_pkgconfigdir/libconfig.pc
%_infodir/libconfig.info*

%files c++
%_libdir/libconfig++.so.*

%files c++-devel
%_libdir/libconfig++.so
%_includedir/libconfig.h++
%_pkgconfigdir/libconfig++.pc

%if_enabled static
%files devel-static
%_libdir/libconfig.a

%files c++-devel-static
%_libdir/libconfig++.a
%endif

%changelog
* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.4.8-alt2
- whoops, forgot to commit the tested spec changes

* Sat Oct 08 2011 Michael Shigorin <mike@altlinux.org> 1.4.8-alt1
- 1.4.8 (thx fedorawatch)
- dropped libconfig_tests from main subpackage
  (no more installed by upstream makefile)

* Mon Apr 18 2011 Michael Shigorin <mike@altlinux.org> 1.4.7-alt1
- 1.4.7 (thx led@)

* Mon Apr 18 2011 Michael Shigorin <mike@altlinux.org> 1.4.6-alt4
- introduced conditional static library build, enabled by default

* Mon Mar 21 2011 Michael Shigorin <mike@altlinux.org> 1.4.6-alt3
- fixed packaging soname links in c++ subpackage (closes: #25266)
  + thanks snejok@ for investigation/report

* Thu Feb 24 2011 Michael Shigorin <mike@altlinux.org> 1.4.6-alt2
- separated libconfig++ so main package doesn't require libstdc++
  (based on PLD r1.3 by qboosh@)
- added libconfig_tests to main package (too small for utils, eh?)

* Thu Feb 24 2011 Michael Shigorin <mike@altlinux.org> 1.4.6-alt1
- 1.4.6
- spec/description cleanup
- dropped Packager: (proper maintainer is welcome)

* Mon Nov 01 2010 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt2
- Rebuilt for soname set-versions

* Mon Jan 04 2010 Andrey Rahmatullin <wrar@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Tue Nov 24 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.4-alt1
- 1.4

* Wed Aug 26 2009 Andrey Rahmatullin <wrar@altlinux.ru> 1.3.2-alt1
- 1.3.2

* Sun Dec 28 2008 Vitaly Lipatov <lav@altlinux.ru> 1.3.1-alt1
- new version 1.3.1 (with rpmrb script)

* Mon Jan 07 2008 Vitaly Lipatov <lav@altlinux.ru> 1.2.1-alt1
- new version 1.2.1 (with rpmrb script)

* Wed Oct 24 2007 Vitaly Lipatov <lav@altlinux.ru> 1.2-alt1
- new version 1.2 (with rpmrb script)

* Fri Aug 04 2006 Vitaly Lipatov <lav@altlinux.ru> 0.9-alt0.1
- initial build for ALT Linux Sisyphus
