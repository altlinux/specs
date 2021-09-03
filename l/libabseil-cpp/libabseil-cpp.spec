%global optflags_lto %optflags_lto -ffat-lto-objects

%def_without test
Name: libabseil-cpp
Version: 20210324.2
Release: alt2

Summary: C++ Common Libraries

License: Apache-2.0
Group: Development/C++
Url: https://abseil.io

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/abseil/abseil-cpp/archive/%version/abseil-cpp-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: libgtest-devel libgmock-devel ctest

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

%build
%add_optflags "-fPIC"
# about -DCMAKE_CXX_STANDARD=17 see https://github.com/desktop-app/tg_owt/pull/55#discussion_r599718405
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_CXX_STANDARD=17 \
%if_with test
    -DBUILD_TESTING=ON -DABSL_USE_EXTERNAL_GOOGLETEST=ON \
%endif
    -DABSL_ENABLE_INSTALL=ON
%make_build

%install
%makeinstall_std

%check
ctest

%files devel
%doc LICENSE
%doc *.md
%_libdir/libabsl_*.a
#files devel
%_includedir/absl/
%_libdir/cmake/absl/
%_pkgconfigdir/*.pc

%changelog
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
