Name: cpputest
Version: 4.0
Release: alt1

Summary: Unit testing and mocking framework for C/C++

Group: Development/Other
License: BSD
Url: https://cpputest.github.io

Source: %name-%version.tar
Patch: cpputest-4.0-alt-fix-cmake-install-path.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: gcc-c++ cmake ctest

%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}

%description
CppUTest is a C /C++ based unit xUnit test framework for unit testing
and for test-driving your code. It is written in C++ but is used in C
and C++ projects and frequently used in embedded systems but it works
for any C/C++ project.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other

%description -n lib%name-devel
The %name-devel package contains C++ header files for developing
applications that use %name.

%package -n lib%name-devel-static
Summary: Static libraries for %name
Group: Development/Other
Requires: lib%name-devel = %EVR

%description -n lib%name-devel-static
The %name-devel-static package contains static libraries for %name.

%prep
%setup
%autopatch -p2

%build
%cmake
%cmake_build

%install
%cmake_install

%check
export LD_LIBRARY_PATH=$(pwd)/%_cmake__builddir
%cmake_build --target test

%files -n lib%name-devel
%doc README.md README_CppUTest_for_C.txt
%doc COPYING
%_includedir/*
%_libdir/cmake/CppUTest
%_pkgconfigdir/*.pc

%files -n lib%name-devel-static
%_libdir/*.a

%changelog
* Mon Nov 7 2022 Vladimir Didenko <cow@altlinux.ru> 4.0-alt1
- initial build for Sisyphus
