Name: libbenchmark
Version: 1.4.1
Release: alt1

Summary: A microbenchmark support library

Group: Development/C++
License: Apache License 2.0
Url: https://github.com/google/benchmark

# Source-url: https://github.com/google/benchmark/archive/v%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake gcc-c++

BuildRequires: libgtest-devel libgmock-devel

%description
A library to support the benchmarking of functions, similar to unit-tests.

%package devel
Summary: Development file for %name
#Requires: %name = %EVR
Group: Development/C++

%description devel
This package contains the header files for %name.

%prep
%setup
%__subst 's|lib/cmake/|%_lib/cmake/|' src/CMakeLists.txt
%__subst 's|lib/pkgconfig|%_lib/pkgconfig|' src/CMakeLists.txt
%__subst 's|set(lib_install_dir "lib/")|set(lib_install_dir "%_lib/")|' src/CMakeLists.txt
%__subst 's|/lib|/%_lib|' cmake/benchmark.pc.in

%build
%cmake -G "Unix Makefiles"
%cmake_build

%install
%cmakeinstall_std

#files
#_libdir/libbenchmark.so.*

%files devel
%_libdir/cmake/benchmark/
%_includedir/benchmark/
%_libdir/libbenchmark.a
%_libdir/libbenchmark_main.a
%_pkgconfigdir/benchmark.pc

%changelog
* Sun Feb 10 2019 Vitaly Lipatov <lav@altlinux.ru> 1.4.1-alt1
- initial build for ALT Sisyphus
