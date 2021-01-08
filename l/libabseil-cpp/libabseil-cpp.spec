# wait for GTEST_ALLOW_UNINSTANTIATED_PARAMETERIZED_TEST
%def_without test
Name: libabseil-cpp
Version: 20200923.2
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
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo \
%if_with test
    -DABSL_RUN_TESTS=ON -DABSL_USE_EXTERNAL_GOOGLETEST=ON \
%endif
    -DABSL_ENABLE_INSTALL=ON
%make_build

%install
%makeinstall_std

%if_with test
%check
ctest
%endif

%files devel
%doc LICENSE
%doc FAQ.md LTS.md README.md UPGRADES.md
%_libdir/libabsl_*.a
#files devel
%_includedir/absl/
%_libdir/cmake/absl/

%changelog
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
