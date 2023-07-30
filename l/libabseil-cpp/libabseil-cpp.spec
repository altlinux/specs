%define _unpackaged_files_terminate_build 1

# Can't be build with packaged GTest: https://github.com/abseil/abseil-cpp/issues/1102
# And these tests are very long
%def_enable check

Name: libabseil-cpp
Version: 20230125.3
Release: alt1

Summary: C++ Common Libraries

License: Apache-2.0
Group: Development/C++
Url: https://abseil.io

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/abseil/abseil-cpp/archive/%version/abseil-cpp-%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ninja-build
BuildRequires: gcc-c++
BuildRequires: /proc

%if_enabled check
BuildRequires: libgtest-devel >= 1.13.0
BuildRequires: libgmock-devel ctest
%endif

# https://bugzilla.altlinux.org/42411
Conflicts: libclickhouse-cpp-devel <= 1.2.2-alt1

%description
Abseil is an open-source collection of C++ library code designed to augment
the C++ standard library. The Abseil library code is collected from
Google's own C++ code base, has been extensively tested and used in
production, and is the same code we depend on in our daily coding lives.

In some cases, Abseil provides pieces missing from the C++ standard; in
others, Abseil provides alternatives to the standard for special needs we've
found through usage in the Google code base. We denote those cases clearly
within the library code we provide you.

Abseil is not meant to be a competitor to the standard library; we've just
found that many of these utilities serve a purpose within our code base,
and we now want to provide those resources to the C++ community as a whole.

%package devel
Summary: Development files for %name
#Requires: %name = %EVR
Group: Development/C++

%description devel
Development headers for %name

%prep
%setup
%ifarch %e2k
# unsupported option
sed -i "/-Wvarargs/d" absl/copts/{copts.py,GENERATED_{copts.bzl,AbseilCopts.cmake}}
# EDG frontend fails at this
sed -i "/static_assert(value.empty()/{N;d}" absl/strings/internal/string_constant.h
%endif

%build
%add_optflags -fPIC
# about -DCMAKE_CXX_STANDARD=17 see https://github.com/desktop-app/tg_owt/pull/55#discussion_r599718405
%cmake \
    -DCMAKE_BUILD_TYPE:STRING=RelWithDebInfo \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_CXX_STANDARD:STRING=17 \
    -DABSL_ENABLE_INSTALL:BOOL=ON \
    -DCMAKE_POSITION_INDEPENDENT_CODE:BOOL=ON \
%if_enabled check
    -DABSL_BUILD_TESTING:BOOL=ON \
    -DABSL_USE_EXTERNAL_GOOGLETEST:BOOL=ON \
    -DABSL_FIND_GOOGLETEST:BOOL=ON \
%endif
    -GNinja
%cmake_build

%install
%cmake_install

%check
%ifarch x86_64 aarch64
ctest --test-dir %_cmake__builddir --output-on-failure --force-new-ctest-process %_smp_mflags
%else
ctest --test-dir %_cmake__builddir --output-on-failure --force-new-ctest-process %_smp_mflags ||:
%endif

%files
%_libdir/libabsl_*.so.*

%files devel
%doc LICENSE
%doc *.md
%_libdir/libabsl_*.so
#files devel
%_includedir/absl/
%_libdir/cmake/absl/
%_pkgconfigdir/*.pc

%changelog
* Sun Jul 30 2023 Vitaly Lipatov <lav@altlinux.ru> 20230125.3-alt1
- Abseil LTS branch, Jan 2023, Patch 3
- required libgtest-devel >= 1.13.0

* Mon Apr 10 2023 Alexey Shabalin <shaba@altlinux.org> 20230125.2-alt1
- 20230125.2
- switched build from static to shared libs

* Tue Aug 30 2022 Yuri N. Sedunov <aris@altlinux.org> 20211102.0-alt3
- rebuilt with -DCMAKE_POSITION_INDEPENDENT_CODE=ON
  (see https://github.com/abseil/abseil-cpp/issues/225)

* Wed Apr 20 2022 Vitaly Lipatov <lav@altlinux.ru> 20211102.0-alt2
- add Conflicts: libclickhouse-cpp-devel

* Sun Apr 10 2022 Vitaly Lipatov <lav@altlinux.ru> 20211102.0-alt1
- Abseil LTS branch, Nov 2021
- new version (20211102.0) with rpmgs script

* Wed Nov 17 2021 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 20210324.2-alt3
- fixed build for Elbrus

* Fri Sep 03 2021 Vitaly Lipatov <lav@altlinux.ru> 20210324.2-alt2
- set optflags_lto to -ffat-lto-objects

* Sun Jul 04 2021 Vitaly Lipatov <lav@altlinux.ru> 20210324.2-alt1
- Abseil LTS branch, March 2021, Patch 2
- new version 20210324.2 (with rpmrb script)

* Fri Mar 26 2021 Vitaly Lipatov <lav@altlinux.ru> 20200923.3-alt1
- new version (20200923.3) with rpmgs script
- build with -DCMAKE_CXX_STANDARD=17

* Thu Jan 28 2021 Arseny Maslennikov <arseny@altlinux.org> 20200923.2-alt2
- NMU: enable -fPIC.

* Mon Nov 02 2020 Vitaly Lipatov <lav@altlinux.ru> 20200923.2-alt1
- new version 20200923.2 (with rpmrb script)
- temp. disable test (wait for new libgtest)

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 20200225.2-alt2
- enable tests

* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 20200225.2-alt1
- initial build for ALT Sisyphus

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-2
- Don't remove buildroot in install

* Sun May 24 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-1
- Initial package.
