Name: googletest
Version: 1.13.0
Release: alt1

Summary: Google's framework for writing C++ tests
License: BSD-3-Clause
Group: Development/C++

Url: https://github.com/google/%name

# https://github.com/google/%name/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++

%description
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgtest
Summary: Google's framework for writing C++ tests
Group: Development/C++
Provides: libgtest0
Obsoletes: libgtest0 <= 1.10.0 

%description -n libgtest
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgtest-devel
Summary: Development environment for gtest
Group: Development/C++
Requires: libgmock-devel = %EVR

%description -n libgtest-devel
Development environment for gtest

%package -n libgmock
Summary: Google C++ Mocking Framework
Group: Development/C++
Provides: libgmock0
Obsoletes: libgmock0 <= 1.10.0

%description -n libgmock
Google's framework for writing and using C++ mock classes on a variety
of platforms (Linux, Mac OS X, Windows, Windows CE, Symbian, etc).
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, it can help you derive better designs of your
system and write better tests.

%package -n libgmock-devel
Summary: Development environment for gmock
Group: Development/C++

%description -n libgmock-devel
Development environment for gmock

%prep
%setup

%build
%ifarch %e2k
# googletest/src/gtest.cc:2806 wrt testing::<unnamed>::TestNameIs::operator()
%add_optflags -Wno-error=unused-function
# error: unrecognized argument to attribute "optimize"
sed -i 's/__attribute__((optimize("no-optimize-sibling-calls")))//' \
	googletest/include/gtest/internal/gtest-port.h
%endif
%cmake -DBUILD_SHARED_LIBS:BOOL=TRUE -Dgmock_build_tests:BOOL=TRUE
%cmake_build

%install
%cmake_install

%check
%make -C %_cmake__builddir test

%files -n libgtest
%doc CONTRIBUTORS LICENSE googletest/README.md
%_libdir/libgtest.so.*
%_libdir/libgtest_main.so.*

%files -n libgtest-devel
%_libdir/libgtest.so
%_libdir/libgtest_main.so
%_libdir/cmake/GTest
%_pkgconfigdir/gtest.pc
%_pkgconfigdir/gtest_main.pc
%_includedir/gtest

%files -n libgmock
%doc CONTRIBUTORS LICENSE googlemock/README.md
%_libdir/libgmock.so.*
%_libdir/libgmock_main.so.*

%files -n libgmock-devel
%_libdir/libgmock.so
%_libdir/libgmock_main.so
%_pkgconfigdir/gmock.pc
%_pkgconfigdir/gmock_main.pc
%_includedir/gmock

%changelog
* Wed Jan 25 2023 Nazarov Denis <nenderus@altlinux.org> 1.13.0-alt1
- Version 1.13.0

* Sat Sep 10 2022 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.12.1-alt1.1
- Fixed build for Elbrus

* Fri Jul 01 2022 Nazarov Denis <nenderus@altlinux.org> 1.12.1-alt1
- Version 1.12.1

* Mon Jun 06 2022 Nazarov Denis <nenderus@altlinux.org> 1.11.0-alt1.3
- Set GCC version 11

* Thu Jul 08 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.0-alt1.2
- Add requires on libgmock-devel for libgtest-devel (ALT #40408)

* Wed Jun 23 2021 Michael Shigorin <mike@altlinux.org> 1.11.0-alt1.1
- E2K: ftbfs workaround

* Sat Jun 12 2021 Nazarov Denis <nenderus@altlinux.org> 1.11.0-alt1
- Version 1.11.0

* Sat Jun 27 2020 Nazarov Denis <nenderus@altlinux.org> 1.10.0-alt1
- Version 1.10.0 (ALT #38645)

* Sat Jan 26 2019 Nazarov Denis <nenderus@altlinux.org> 1.8.1-alt1
- Version 1.8.1 (ALT #35575)

* Fri Jan 18 2019 Leontiy Volodin <lvol@altlinux.org> 1.8.0-alt6
- Removed ubt macros

* Tue Jan 15 2019 Leontiy Volodin <lvol@altlinux.org> 1.8.0-alt5%ubt
- Fixed ubt macros in spec

* Wed May 02 2018 Nazarov Denis <nenderus@altlinux.org> 1.8.0-alt4%ubt
- Change URL (ALT #34874)

* Thu Apr 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.0-alt3
- fix packaging on 64bit arches other than x86_64

* Tue Apr 18 2017 Nazarov Denis <nenderus@altlinux.org> 1.8.0-alt1.M80P.1
- Build for branch p8

* Thu Apr 06 2017 Nazarov Denis <nenderus@altlinux.org> 1.8.0-alt2
- Add soname
- Add gtest-config

* Wed Apr 05 2017 Nazarov Denis <nenderus@altlinux.org> 1.8.0-alt1
- Version 1.8.0

* Tue Jun 16 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 1.7.0-alt1.1
- Rebuilt for gcc5 C++11 ABI.

* Tue Oct 15 2013 Fr. Br. George <george@altlinux.ru> 1.7.0-alt1
- Autobuild version bump to 1.7.0

* Tue Jul 05 2011 Fr. Br. George <george@altlinux.ru> 1.6.0-alt1
- Autobuild version bump to 1.6.0
- Rename spec and directory to confirm project name
- Resurrect make install killed by upstream

* Wed Mar 30 2011 Fr. Br. George <george@altlinux.ru> 1.5.0-alt1
- Initial build from scratch


