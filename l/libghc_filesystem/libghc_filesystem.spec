%def_with test

Name: libghc_filesystem
Version: 1.5.14
Release: alt1

Summary: An implementation of C++17 std::filesystem for C++11 /C++14/C++17/C++20

License: MIT
Group: Development/C++
Url: https://github.com/gulrak/filesystem

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/gulrak/filesystem/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

BuildRequires: libgtest-devel libgmock-devel ctest

%description
An implementation of C++17 std::filesystem for C++11 /C++14/C++17/C++20.

%package devel
Summary: An implementation of C++17 std::filesystem for C++11 /C++14/C++17/C++20
Group: Development/C++

%description devel
An implementation of C++17 std::filesystem for C++11 /C++14/C++17/C++20.

%prep
%setup

%build
%cmake_insource -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DCMAKE_CXX_STANDARD=17 \
%if_with test
    -DGHC_FILESYSTEM_BUILD_TESTING=ON \
%endif
    %nil

%make_build

%install
%makeinstall_std

%check
ctest

%files devel
%doc LICENSE README.md
%_includedir/ghc/
%_libdir/cmake/ghc_filesystem

%changelog
* Sat Mar 18 2023 Vitaly Lipatov <lav@altlinux.ru> 1.5.14-alt1
- initial build for ALT Sisyphus
