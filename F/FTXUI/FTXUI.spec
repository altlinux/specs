%define oname ftxui
%define abiversion 0

Name:    FTXUI
Version: 5.0.0
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

%define common_descr \
C++ Functional Terminal User Interface \
\
A simple cross-platform C++ library for terminal based user interfaces.

%description
%common_descr

%package -n lib%oname%abiversion
Group:   Development/C++
Summary: %summary library

%description -n lib%oname%abiversion
%common_descr

%package -n lib%oname-devel
Group:   Development/C++
Summary: %summary development files and headers

%description -n lib%oname-devel
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

%files -n lib%oname%abiversion
%_libdir/lib%oname-*.so.*

%files -n lib%oname-devel
%doc *.md LICENSE
%_cmakedir/%oname
%_includedir/%oname
%_libdir/lib%oname-*.so
%_pkgconfigdir/%oname.pc

%changelog
* Wed Dec 18 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus.
