%def_disable static

Name: libbenchmark
Version: 1.5.6
Release: alt2

Summary: A library to benchmark code snippets

License: Apache-2.0
Group: Development/C++
Url: https://github.com/google/benchmark

# Source-url: https://github.com/google/benchmark/archive/refs/tags/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: benchmark-%version.tar

Patch: benchmark-1.5.4-extbuild.patch
Patch2000: libbenchmark-e2k.patch

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sun Jul 11 2021
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgmock-devel libsasl2-3 libstdc++-devel python3-base sh4
BuildRequires: cmake gcc-c++ libgtest-devel ctest

%description
A library to benchmark code snippets, similar to unit tests.

Define a function that executes the code to measure, register it as a benchmark
function using the `BENCHMARK` macro, and ensure an appropriate `main` function
is available.

To run the benchmark, compile and link against the `benchmark` library
(libbenchmark.a/.so). If you followed the build steps above, this library will
be under the build directory you created.

%package devel
Summary: %summary; development environment
Group: Development/C++

%description devel
%summary; development environment

%package devel-static
Summary: %summary (static)
Group: Development/C++

%description devel-static
%summary (static)

%prep
%setup -n benchmark-%version
%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%cmake -DBUILD_SHARED_LIBS:BOOL=FALSE
%cmake_build
mv %_cmake__builddir/src/*.a .
rm -rf %_cmake__builddir
%cmake -DBUILD_SHARED_LIBS:BOOL=TRUE
%cmake_build

%install
%cmake_install
%if_enabled static
install *.a %buildroot/%_libdir
%endif

%check
%make_build -C %_cmake__builddir test

%files
%doc *.md
%_libdir/*.so.*

%files devel
%doc docs
%_libdir/cmake/*
%_pkgconfigdir/*
%_libdir/lib*.so
%_includedir/*

%if_enabled static
%files devel-static
%_libdir/lib*.a
%endif

%changelog
* Wed Sep 01 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt2
- disable devel-static packing, cleanup spec

* Thu Aug 19 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.6-alt1
- new version 1.5.6

* Sun Jul 11 2021 Fr. Br. George <george@altlinux.ru> 1.5.5-alt2
- Separate static library
- Introduce tests

* Fri Jul 09 2021 Vitaly Lipatov <lav@altlinux.ru> 1.5.5-alt1
- new version 1.5.5 (with rpmrb script)

* Thu Jun 10 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.5.2-alt2
- added patch for Elbrus
- corrected license

* Sun Sep 20 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.2-alt1
- new version 1.5.2 (with rpmrb script)

* Mon Aug 10 2020 Vitaly Lipatov <lav@altlinux.ru> 1.5.1-alt1
- new version 1.5.1 (with rpmrb script)

* Mon Jun 03 2019 Vitaly Lipatov <lav@altlinux.ru> 1.5.0-alt1
- new version 1.5.0 (with rpmrb script)
- skip GoogleTest using (BENCHMARK_ENABLE_GTEST_TESTS=OFF)

* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Sisyphus
