Name: googletest
Version: 1.8.0
Release: alt1

Summary: Google's framework for writing C++ tests
License: BSD
Group: Development/C++

Url: https://github.com/%name/googletest

# https://github.com/google/%name/archive/release-%version.tar.gz
Source: %name-release-%version.tar.gz
Patch: %name-lib64-alt.patch

# Automatically added by buildreq on Wed Apr 05 2017 (-bi)
# optimized out: cmake-modules elfutils libstdc++-devel perl python-base
BuildRequires: cmake gcc-c++

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

%description -n libgtest
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgtest-devel
Summary: Development environment for %name
Group: Development/C++
Requires: libgtest = %EVR

%description -n libgtest-devel
Development environment for %name

%package -n libgmock
Summary: Google's framework for writing C++ tests
Group: Development/C++
Requires: libgtest = %EVR

%description -n libgmock
Google's framework for writing C++ tests on a variety of platforms
(Linux, Mac OS X, Windows, Cygwin, Windows CE, and Symbian). Based on
the xUnit architecture. Supports automatic test discovery, a rich set of
assertions, user-defined assertions, death tests, fatal and non-fatal
failures, value- and type-parameterized tests, various options for
running the tests, and XML test report generation.

%package -n libgmock-devel
Summary: Development environment for %name
Group: Development/C++
Requires: libgmock = %EVR
Requires: libgtest-devel = %EVR

%description -n libgmock-devel
Development environment for %name

%prep
%setup -n %name-release-%version
%ifarch x86_64
%patch0 -p1
%endif

%build
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

%files -n libgtest
%doc googletest/CHANGES googletest/CONTRIBUTORS googletest/LICENSE
%_libdir/libgtest.so
%_libdir/libgtest_main.so

%files -n libgtest-devel
%_includedir/gtest
%_aclocaldir/gtest.m4

%files -n libgmock
%doc googlemock/CHANGES googlemock/CONTRIBUTORS googlemock/LICENSE
%_libdir/libgmock.so
%_libdir/libgmock_main.so

%files -n libgmock-devel
%_includedir/gmock

%changelog
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


