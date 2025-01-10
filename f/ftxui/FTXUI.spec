%define abiversion 0

Name:    ftxui
Version: 5.1.0
Release: alt1

Summary: Functional Terminal (X) User interface
License: MIT
Group:   Development/C++
Url:     https://github.com/ArthurSonzogni/FTXUI

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: ctest
BuildRequires: gcc-c++
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(benchmark)
Provides:      FTXUI = %EVR
Obsoletes:     FTXUI < %EVR
%define common_descr A simple cross-platform C++ library for terminal based user interfaces.

%description
%common_descr

%package -n lib%name%abiversion
Group:   Development/C++
Summary: %summary library

%description -n lib%name%abiversion
%common_descr

%package -n lib%name-devel
Group:   Development/C++
Summary: %summary development files and headers

%description -n lib%name-devel
%common_descr

%prep
%setup

%build
%cmake -DBUILD_SHARED_LIBS=ON \
       -DFTXUI_BUILD_DOCS=ON \
       -DFTXUI_BUILD_TESTS=ON
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n lib%name%abiversion
%_libdir/lib%name-*.so.*

%files -n lib%name-devel
%doc *.md LICENSE
%_cmakedir/%name
%_includedir/%name
%_libdir/lib%name-*.so
%_pkgconfigdir/%name.pc

%changelog
* Thu Jan 09 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Wed Dec 18 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus.
