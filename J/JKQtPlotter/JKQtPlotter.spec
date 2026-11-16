#Example applications
%def_without examples

#Printer support
%def_with printer

#Unit tests
%def_with tests

%define soversion 5

%define _unpackaged_files_terminate_build 1

Name: JKQtPlotter
Version: 5.0.0
Release: alt3.beta2

Summary: Extensive C++ plotting library for Qt
License: LGPL-2.1-or-later
Group: System/Libraries

Url: https://jkriege2.github.io/JKQtPlotter/
VCS: https://github.com/jkriege2/JKQtPlotter

Source: %name-%version.tar
Patch0: JKQtPlotter-soversion.patch
Patch1: JKQtPlotter-i386-unitstr.patch

BuildRequires(pre): rpm-build-cmake

BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel

%{?_with_printer:BuildRequires: libcups-devel}
%{?_with_tests:BuildRequires: ctest}

%if_with examples
BuildRequires: libopencv-devel
BuildRequires: CImg-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
%endif

%description
JKQtPlotter is an extensive plotting framework for Qt (Qt5/Qt6),
including a feature-rich plotter widget and related components.


%package -n lib%name%soversion
Summary: JKQtPlotter runtime library for Qt6
Group: System/Libraries
Provides: lib%name = %EVR
Obsoletes: lib%name < %EVR

%description -n lib%name%soversion
Runtime shared libraries of JKQtPlotter built against Qt6.
This package is required to run applications using JKQtPlotter with Qt6.
Package name follows the library soname version (5); the "6" in file
names refers to Qt6 the library is built against.


%package -n lib%name-devel
Summary: Development files for JKQtPlotter (Qt6)
Group: Development/C++
Requires: lib%name%soversion = %EVR
Requires: qt6-base-devel
Requires: qt6-svg-devel

%description -n lib%name-devel
Header files and CMake configuration needed to develop
applications using JKQtPlotter with Qt6.


%if_with examples
%package -n %name-examples
Summary: Examples for JKQtPlotter
Group: Development/C++
Requires: lib%name%soversion = %EVR

%description -n %name-examples
Example files for JKQtPlotter.
%endif


%package -n %name-doc
Summary: Documentation for JKQtPlotter
Group: Documentation
BuildArch: noarch

%description -n %name-doc
Documentation files for JKQtPlotter.


%prep
%setup
%patch0 -p1
%patch1 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
%if_with examples
    -DCMAKE_INSTALL_BINDIR=%_libexecdir/%name/examples \
%endif
    -DCMAKE_PREFIX_PATH=%_libdir/cmake/Qt6 \
    -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF \
    -DJKQtPlotter_BUILD_TESTS:BOOL=%{with tests} \
    -DJKQtPlotter_BUILD_TOOLS:BOOL=OFF \
    -DJKQtPlotter_BUILD_EXAMPLES:BOOL=%{with examples} \
    -DJKQtPlotter_BUILD_FORCE_NO_PRINTER_SUPPORT:BOOL=%{without printer} \
    -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install

%if_with tests
# Only test binaries are installed to %%_bindir; they are run in %%check
# and must not be packaged
rm -rf %buildroot%_bindir

%check
QT_QPA_PLATFORM=offscreen %ctest
%endif


%files -n lib%name%soversion
%_libdir/libJKQT*.so.%{soversion}*

%files -n lib%name-devel
%_includedir/*
%_libdir/libJKQT*.so
%_libdir/cmake/*

%if_with examples
%files -n %name-examples
%_libexecdir/%name/examples
%endif


%files -n %name-doc
%doc %_docdir/*


%changelog
* Tue Nov 10 2026 Valentin Sokolov <sova@altlinux.org> 5.0.0-alt3.beta2
- Add missing Qt development dependencies.

* Mon Sep 21 2026 Valentin Sokolov <sova@altlinux.org> 5.0.0-alt2.beta2
- Update to version 5.0.0-beta2.
- Enable tests.
- Move rpm-build-cmake to BuildRequires(pre).
- Fix SI prefix selection for exact powers of 10 on i586 (i386-unitstr.patch).

* Thu Sep 17 2026 Valentin Sokolov <sova@altlinux.org> 5.0.0-alt2.beta1
- Repackage according to Shared Libs Policy.
- Pin library soname by setting SOVERSION in CMake (soversion.patch).

* Tue Jan 27 2026 Valentin Sokolov <sova@altlinux.org> 5.0.0-alt1.beta1
- Initial build for Sisyphus.
