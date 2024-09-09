%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1
%define soversion 11
%set_verify_elf_method strict

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%def_enable static

Name: libconfig
Version: 1.7.3
Release: alt1
Summary: C/C++ Configuration File Library
License: LGPLv2.1+
Group: System/Libraries
Url: https://hyperrealm.github.io/libconfig
VCS: https://github.com/hyperrealm/libconfig.git

Source: %name-%version.tar

# Automatically added by buildreq on Sat Oct 08 2011
# optimized out: libstdc++-devel
BuildRequires: flex gcc-c++
# explicitly added texinfo for info files
BuildRequires: texinfo

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

%package -n libconfig%soversion
Summary: C Configuration File Library
Group: System/Libraries

%description -n libconfig%soversion
libconfig is the C binding for libconfig library.

%package -n libconfig-devel
Summary: Header files for %name
Group: Development/Other
Requires: libconfig%soversion = %EVR

%description -n libconfig-devel
Header files for %name library.

%package -n libconfig-c++%soversion
Summary: C++ Configuration File Library
Group: System/Libraries
# doesn't require base, common code included in library

%description -n libconfig-c++%soversion
libconfig++ is the C++ binding for libconfig library.

%package -n libconfig-c++-devel
Summary: Header files for libconfig++ library
Group: Development/Other
Requires: libconfig-c++%soversion = %EVR
Requires: %name-devel = %EVR
Requires: libstdc++-devel

%description -n libconfig-c++-devel
Header files for libconfig++ library.

%if_enabled static
%package -n libconfig-devel-static
Summary: Static library files for %name
Group: Development/Other
Requires: %name-devel = %EVR
Requires: glibc-devel-static

%description -n libconfig-devel-static
Static library files for %name.

%package -n libconfig-c++-devel-static
Summary: Static library files for libconfig++
Group: Development/Other
Requires: %name-c++-devel = %EVR
Requires: libstdc++-devel-static

%description -n libconfig-c++-devel-static
Static library files for libconfig++.
%endif

%prep
%setup
rm -rf examples/Makefile*
rm -rf examples/*/Makefile*
rm -rf examples/*/*.vcproj
sed -i '/examples.*Makefile/d' configure.ac

%build
%add_optflags -D_FILE_OFFSET_BITS=64

%autoreconf
%configure \
	%{subst_enable static} \
	--disable-examples
%make_build

%install
%makeinstall_std

%files -n libconfig%soversion
%doc AUTHORS ChangeLog README NEWS TODO
%_libdir/libconfig.so.%soversion
%_libdir/libconfig.so.%soversion.*

%files -n libconfig-devel
%doc examples/
%_libdir/libconfig.so
%_includedir/libconfig.h
%_pkgconfigdir/libconfig.pc
%_infodir/libconfig.info*
%_libdir/cmake/libconfig++/libconfig++Config.cmake
%_libdir/cmake/libconfig/libconfigConfig.cmake

%files -n libconfig-c++%soversion
%_libdir/libconfig++.so.*

%files -n libconfig-c++-devel
%_libdir/libconfig++.so
%_includedir/libconfig.h++
%_pkgconfigdir/libconfig++.pc

%if_enabled static
%files -n libconfig-devel-static
%_libdir/libconfig.a

%files -n libconfig-c++-devel-static
%_libdir/libconfig++.a
%endif

%changelog
* Thu Sep 05 2024 Andrey Kovalev <ded@altlinux.org> 1.7.3-alt1
- Updated to upstream version 1.7.3.
- Built according to shared libs policy.

* Fri Oct 08 2021 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5-alt3
- Fixed build with LTO.

* Fri Jun 08 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.5-alt2
- NMU: rebuilt to regenerate ABI.

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.5-alt1.1
- NMU: added BR: texinfo

* Mon Sep 28 2015 Michael Shigorin <mike@altlinux.org> 1.5-alt1
- new version 1.5

* Fri Jun 12 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.4.9-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Thu Jun 19 2014 Michael Shigorin <mike@altlinux.org> 1.4.9-alt1
- new version 1.4.9

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
