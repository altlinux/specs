%define _unpackaged_files_terminate_build 1
# change libcares package name according to SharedLibsPolicy in future
%define soname 2

Name: c-ares
Version: 1.33.1
Release: alt1

Summary: A library that performs asynchronous DNS operations
License: MIT
Group: System/Libraries

Url: http://c-ares.haxx.se/
Source: %url/download/c-ares-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
# need for test/configure
BuildRequires: gcc-c++
BuildRequires: libgtest-devel

%description
c-ares is a C library that performs DNS requests and name resolves
asynchronously. This package contains little utilities built with
this library.

%package -n libcares
Summary: A library that performs asynchronous DNS operations
Group: System/Libraries

%description -n libcares
c-ares is a C library that performs DNS requests and name resolves
asynchronously. c-ares is a fork of the library named 'ares', written
by Greg Hudson at MIT.

%package -n libcares-devel
Summary: Libraries, includes, etc. to develop applications used c-ares
Group: System/Libraries
Requires: libcares = %version-%release

%description -n libcares-devel
This package contains the header files and libraries links needed to
compile applications or shared objects that use c-ares.

%prep
%setup -n c-ares-%version
%patch0 -p1

%build
%cmake -DCMAKE_INSTALL_LIBDIR:PATH="%_libdir" -DCARES_BUILD_TESTS:BOOL=ON
%cmake_build

%install
%cmake_install

%check
%_cmake__builddir/bin/arestest --gtest_filter='-*.Live*:LibraryTest.GetTCPSock'

%files
%_bindir/*
%_man1dir/*

%files -n libcares
%_libdir/*.so.%soname
%_libdir/*.so.%soname.*

%files -n libcares-devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*.pc
%_libdir/cmake/%name
%_man3dir/*

%changelog
* Mon Aug 26 2024 Anton Farygin <rider@altlinux.ru> 1.33.1-alt1
- 1.33.1

* Fri Aug 16 2024 Anton Farygin <rider@altlinux.ru> 1.33.0-alt1
- 1.33.0

* Tue Jul 09 2024 Anton Farygin <rider@altlinux.ru> 1.32.1-alt1
- 1.32.1

* Sun Jun 09 2024 Anton Farygin <rider@altlinux.ru> 1.30.0-alt1
- 1.30.0

* Thu Apr 04 2024 Anton Farygin <rider@altlinux.ru> 1.28.1-alt1
- 1.28.1

* Sun Mar 03 2024 Anton Farygin <rider@altlinux.ru> 1.27.0-alt1
- 1.27.0

* Sat Jan 27 2024 Anton Farygin <rider@altlinux.ru> 1.26.0-alt1
- 1.26.0

* Thu Jan 11 2024 Anton Farygin <rider@altlinux.ru> 1.25.0-alt1
- 1.25.0

* Wed Jul 05 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.1-alt1
- 1.19.1 (Fixes: CVE-2023-31124, CVE-2023-31130, CVE-2023-31147, CVE-2023-32067)

* Mon Apr 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.19.0-alt2
- switch to build with cmake
- backport patch for fix memory leak in ares_send

* Sat Feb 04 2023 Anton Farygin <rider@altlinux.ru> 1.19.0-alt1
- 1.19.0 (Fixes: CVE-2022-4904)

* Thu Nov 25 2021 Anton Farygin <rider@altlinux.ru> 1.18.1-alt1
- 1.18.1
- enabled tests

* Wed Aug 11 2021 Anton Farygin <rider@altlinux.ru> 1.17.2-alt1
- 1.17.2 (Fixes: CVE-2021-3672)

* Tue Jul 27 2021 Anton Farygin <rider@altlinux.ru> 1.17.1-alt2
- fixed tools install in c-ares package

* Mon Nov 23 2020 Anton Farygin <rider@altlinux.ru> 1.17.1-alt1
- 1.17.1

* Tue Nov 17 2020 Anton Farygin <rider@altlinux.ru> 1.16.1-alt2
- added 0d252eb commit from upstream to resolve security issue (fixes: CVE-2020-8277)

* Fri May 15 2020 Anton Farygin <rider@altlinux.ru> 1.16.1-alt1
- 1.16.1

* Tue Mar 31 2020 Anton Farygin <rider@altlinux.ru> 1.16.0-alt1
- 1.16.0

* Thu Nov 15 2018 Anton Farygin <rider@altlinux.ru> 1.15.0-alt1
- 1.15.0

* Tue May 15 2018 Anton Farygin <rider@altlinux.ru> 1.14.0-alt1
- 1.14.0 

* Tue Aug 08 2017 Anton Farygin <rider@altlinux.ru> 1.13.0-alt1
- 1.13.0 with these security fixes:
        * CVE-2016-5180 - Heap-based buffer overflow in the ares_create_query function.
        * CVE-2017-1000381 - NAPTR parser out of bounds access.

* Wed Aug 03 2016 Vitaly Lipatov <lav@altlinux.ru> 1.11.0-alt1
- new version 1.11.0 (with rpmrb script)

* Wed Sep 10 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.0-alt1
- Version 1.10.0

* Tue Dec 27 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt2
- Fix RPATH issue.

* Sat Aug 20 2011 Victor Forsiuk <force@altlinux.org> 1.7.5-alt1
- 1.7.5

* Tue Dec 14 2010 Victor Forsiuk <force@altlinux.org> 1.7.4-alt1
- 1.7.4

* Fri Nov 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt2
- Rebuilt for soname set-versions.

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 1.7.3-alt1
- 1.7.3

* Fri Mar 26 2010 Victor Forsiuk <force@altlinux.org> 1.7.1-alt1
- 1.7.1

* Tue Dec 22 2009 Victor Forsyuk <force@altlinux.org> 1.7.0-alt1
- 1.7.0

* Thu Dec 11 2008 Victor Forsyuk <force@altlinux.org> 1.6.0-alt1
- 1.6.0

* Wed Nov 26 2008 Victor Forsyuk <force@altlinux.org> 1.5.3-alt2
- Removed obsolete %%post* scripts.

* Fri Sep 12 2008 Victor Forsyuk <force@altlinux.org> 1.5.3-alt1
- 1.5.3

* Thu Jun 12 2008 Victor Forsyuk <force@altlinux.org> 1.5.2-alt1
- Initial build.
