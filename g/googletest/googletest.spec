%define sover 0

Name: googletest
Version: 1.8.0
Release: alt3

Summary: Google's framework for writing C++ tests
License: BSD
Group: Development/C++

Url: https://github.com/%name/googletest

# https://github.com/google/%name/archive/release-%version.tar.gz
Source: %name-release-%version.tar.gz
Patch0: %name-soname-alt.patch
Patch1: %name-lib64-alt.patch

# Automatically added by buildreq on Thu Apr 06 2017 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel perl python-base
BuildRequires: cmake gcc-c++

%description
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgtest%sover
Summary: Google's framework for writing C++ tests
Group: Development/C++
Provides: libgtest = %EVR
Obsoletes: libgtest

%description -n libgtest%sover
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgtest-devel
Summary: Development environment for gtest
Group: Development/C++

%description -n libgtest-devel
Development environment for gtest

%package -n libgmock%sover
Summary: Google C++ Mocking Framework
Group: Development/C++
Requires: libgtest%sover = %EVR
Provides: libgmock = %EVR
Obsoletes: libgmock

%description -n libgmock%sover
Google's framework for writing and using C++ mock classes on a variety
of platforms (Linux, Mac OS X, Windows, Windows CE, Symbian, etc).
Inspired by jMock, EasyMock, and Hamcrest, and designed with C++'s
specifics in mind, it can help you derive better designs of your
system and write better tests.

%package -n libgmock-devel
Summary: Development environment for gmock
Group: Development/C++
Requires: libgtest-devel = %EVR

%description -n libgmock-devel
Development environment for gmock

%prep
%setup -n %name-release-%version
%patch0 -p1
%if "%_lib" == "lib64"
%patch1 -p1
%endif

%build

# Generate gtest-config
pushd googletest
%autoreconf
%configure
popd

%__mkdir_p %_target_platform
pushd %_target_platform

cmake .. \
	-DCMAKE_INSTALL_PREFIX:PATH=%prefix \
	-DCMAKE_C_FLAGS:STRING='%optflags' \
	-DCMAKE_CXX_FLAGS:STRING='%optflags' \
	-DCMAKE_BUILD_TYPE:STRING="Release" \
	-DBUILD_SHARED_LIBS:BOOL=TRUE

popd

%make_build -C %_target_platform

%install
%makeinstall_std -C %_target_platform
%__install -Dp -m0644 googletest/m4/gtest.m4 %buildroot%_aclocaldir/gtest.m4
%__install -Dp -m0755 googletest/scripts/gtest-config %buildroot%_bindir/gtest-config

%files -n libgtest%sover
%doc googletest/CHANGES googletest/CONTRIBUTORS googletest/LICENSE
%_libdir/libgtest.so.*
%_libdir/libgtest_main.so.*

%files -n libgtest-devel
%_bindir/gtest-config
%_libdir/libgtest.so
%_libdir/libgtest_main.so
%_includedir/gtest
%_aclocaldir/gtest.m4

%files -n libgmock%sover
%doc googlemock/CHANGES googlemock/CONTRIBUTORS googlemock/LICENSE
%_libdir/libgmock.so.*
%_libdir/libgmock_main.so.*

%files -n libgmock-devel
%_libdir/libgmock.so
%_libdir/libgmock_main.so
%_includedir/gmock

%changelog
* Thu Apr 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 1.8.0-alt3
- fix packaging on 64bit arches other than x86_64

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


