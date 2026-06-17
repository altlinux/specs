%define abiversion 7
%def_disable static

Name:    ftxui
Version: %abiversion.0.0
Release: alt1

Summary: Functional Terminal (X) User interface
License: MIT
Group:   Development/C++
Url:     https://github.com/ArthurSonzogni/FTXUI

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: ctest
BuildRequires: gcc-c++
%if_enabled static
BuildRequires: pkgconfig(gtest)
BuildRequires: pkgconfig(benchmark)
%endif
Provides:      FTXUI = %EVR
Obsoletes:     FTXUI < %EVR

%define common_descr A simple cross-platform C++ library for terminal based user interfaces.

%if_enabled static
%{?optflags_lto:%global optflags_lto %optflags_lto -ffat-lto-objects}
%endif

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

%package -n lib%name-devel-static
Group:   Development/C++
Summary: %summary static libraries.
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
%common_descr

%prep
%setup

%build
%cmake  \
       -DFTXUI_BUILD_DOCS=ON \
%if_enabled static
       -DFTXUI_BUILD_TESTS=ON
%else
       -DBUILD_SHARED_LIBS=ON
%endif

%cmake_build

%install
%cmake_install

%if_enabled static
%check
%ctest
%endif

%if_enabled static
%files -n lib%name-devel-static
%_libdir/lib%name-*.a
%else
%files -n lib%name%abiversion
%_libdir/lib%name-*.so.%{abiversion}*
%endif

%files -n lib%name-devel
%doc *.md LICENSE
%_cmakedir/%name
%_includedir/%name
%if_disabled static
%_libdir/lib%name-*.so
%endif
%_pkgconfigdir/%name.pc

%changelog
* Mon Jun 15 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 7.0.0-alt1
- 6.1.0 -> 7.0.0 (Closes: #58570).

* Wed Apr 30 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.1.0-alt1
- 6.0.0 -> 6.1.0.

* Fri Mar 28 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 6.0.0-alt1
- 5.1.0 -> 6.0.0.

* Thu Jan 09 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 5.1.0-alt1
- 5.0.0 -> 5.1.0.

* Wed Dec 18 2024 Sergey Gvozdetskiy <serjigva@altlinux.org> 5.0.0-alt1
- Initial build for Sisyphus.
