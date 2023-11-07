%define oname benchmark

Name: lib%oname
Version: 1.7.1
Release: alt1.2

Summary: A library to benchmark code snippets

License: Apache-2.0
Group: Development/C++
Url: https://github.com/google/benchmark

# Source-url: https://github.com/google/benchmark/archive/refs/tags/v%version.tar.gz
Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: %oname-%version.tar
Provides: google-%name = %EVR

Patch: benchmark-1.5.4-extbuild.patch
Patch2000: libbenchmark-e2k.patch

BuildRequires(pre): rpm-macros-cmake

# Automatically added by buildreq on Sun Jul 11 2021
# optimized out: cmake-modules glibc-kernheaders-generic glibc-kernheaders-x86 libgmock-devel libsasl2-3 libstdc++-devel python3-base sh4
BuildRequires: cmake gcc-c++ libgtest-devel ctest ninja-build
# some tests query CPU info via /proc
BuildRequires: /proc

%ifarch %ix86
# XXX: i387 doubles have extended precision (mantissa is 80 bits), so results
# of calculations might differ from those obtained with strictly IEEE-754
# doubles (with 53-bit mantissa). This is why StatisticsTest.CV fails on i586
# (the problem can be reproduced on x86_64 by forcing i387 for floating point
# arithmetics with `-mfpmath=387` GCC flag).
# To avoid the problem force SSE on 32-bit x86:
%add_optflags -msse -mfpmath=sse
%endif

%description
A library to benchmark code snippets, similar to unit tests.

Define a function that executes the code to measure, register it as a benchmark
function using the `BENCHMARK` macro, and ensure an appropriate `main` function
is available.

To run the benchmark, compile and link against the `benchmark` library
(libbenchmark.a/.so). If you followed the build steps above, this library will
be under the build directory you created.

%package devel
Summary: %summary development environment
Group: Development/C++
Requires: lib%oname = %EVR

%description devel
%summary development environment.

%prep
%setup -n %oname-%version
#%%patch -p1
%ifarch %e2k
%patch2000 -p1
%endif

%build
%cmake \
  -G Ninja \
  -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
  -DGIT_VERSION=%version \
  -DBUILD_SHARED_LIBS:BOOL=ON \
  -DBENCHMARK_ENABLE_TESTING:BOOL=ON \
  -DBENCHMARK_USE_BUNDLED_GTEST:BOOL=OFF \
  -DBENCHMARK_ENABLE_GTEST_TESTS:BOOL=ON \
  -DBENCHMARK_ENABLE_INSTALL:BOOL=ON \
  -DBENCHMARK_DOWNLOAD_DEPENDENCIES:BOOL=OFF \
%ifarch %e2k
  -DBENCHMARK_ENABLE_WERROR:BOOL=OFF \
%endif
  %nil
%cmake_build

%install
%cmake_install
rm -rf %buildroot%_defaultdocdir

%check
ctest --test-dir %_cmake__builddir --output-on-failure --force-new-ctest-process %_smp_mflags

%files
%doc *.md
%_libdir/*.so.*

%files devel
%doc docs
%_libdir/cmake/*
%_pkgconfigdir/*
%_libdir/lib*.so
%_includedir/*

%changelog
* Mon Oct 16 2023 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.7.1-alt1.2
- NMU: fixed FTBFS on LoongArch (some tests need /proc).
  While at it worked around Statistics.CV test failure on i586.

* Wed May 03 2023 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.7.1-alt1.1
- e2k: patch update, werror off

* Tue May 02 2023 Alexey Shabalin <shaba@altlinux.org> 1.7.1-alt1
- new version 1.7.1

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
