%define _unpackaged_files_terminate_build 1

Name: oneDPL
Version: 2022.13.0
Release: alt1

Summary: oneAPI DPC++ Library for parallel C++ programming
Summary(ru_RU.UTF-8): Библиотека oneAPI DPC++ для параллельного программирования на C++
License: Apache-2.0 WITH LLVM-exception
Group: Development/C++
Url: https://github.com/uxlfoundation/oneDPL
Vcs: https://github.com/uxlfoundation/oneDPL.git

Source: %name-%version.tar
Patch0: %name-%version-cmake-destdir.patch
Patch1: %name-%version-for-loop-signed-stride.patch
Patch2: %name-%version-histogram-bin-scale.patch

BuildRequires(pre): rpm-macros-cmake
BuildPreReq: cmake >= 3.11
BuildPreReq: ctest
BuildPreReq: gcc-c++
BuildPreReq: tbb-devel >= 2021

%description
oneDPL is an implementation of the oneAPI specification for the oneDPL
component. It provides C++17 parallel algorithms and related facilities for
host processors and SYCL devices.

%description -l ru_RU.UTF-8
oneDPL — реализация спецификации oneAPI для компонента oneDPL. Библиотека
предоставляет параллельные алгоритмы C++17 и связанные средства для центральных
процессоров и устройств SYCL.

%package devel
Summary: Development files for oneAPI DPC++ Library
Summary(ru_RU.UTF-8): Файлы разработки библиотеки oneAPI DPC++
Group: Development/C++

%description devel
This package contains the header-only oneDPL library and CMake package files
required to develop applications with oneDPL.

%description devel -l ru_RU.UTF-8
Пакет содержит заголовочную библиотеку oneDPL и файлы пакета CMake, необходимые
для разработки приложений с oneDPL.

%prep
%setup
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DONEDPL_BACKEND=tbb

%install
%cmake_install

%check
%cmake_build --target build-onedpl-tests
%ctest

%files devel
%doc LICENSE.txt README.md third-party-programs.txt
%_includedir/oneapi/
%_libdir/cmake/oneDPL/
%_docdir/oneDPL/

%changelog
* Wed Sep 16 2026 Georgij Tsarin <crystarm@altlinux.org> 2022.13.0-alt1
- Initial build for Sisyphus.
