Name: libabseil-cpp
Version: 20200225.2
Release: alt1

Summary: C++ Common Libraries

License: ASL 2.0
Group: Development/C++
Url: https://abseil.io

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/abseil/abseil-cpp/archive/%version/abseil-cpp-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++

#BuildRequires: libgtest-devel ctest

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
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo
# -DABSL_RUN_TESTS=ON
%make_build

%install
%makeinstall_std

#check
#ctest

%files devel
%doc LICENSE
%doc FAQ.md LTS.md README.md UPGRADES.md
%_libdir/libabsl_*.a
#files devel
%_includedir/absl/
%_libdir/cmake/absl/

%changelog
* Sun Aug 23 2020 Vitaly Lipatov <lav@altlinux.ru> 20200225.2-alt1
- initial build for ALT Sisyphus

* Wed May 27 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-2
- Don't remove buildroot in install

* Sun May 24 2020 Rich Mattes <richmattes@gmail.com> - 20200225.2-1
- Initial package.
