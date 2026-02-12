#Example applications
%def_without examples

#Printer support
%def_with printer


Name: JKQtPlotter
Version: 5.0.0
Release: alt1.beta1

Summary: Extensive C++ plotting library for Qt
License: LGPL-2.1-or-later
Group: System/Libraries

Url: https://jkriege2.github.io/JKQtPlotter/
VCS: https://github.com/jkriege2/JKQtPlotter

Source: %name-%version.tar

BuildRequires: rpm-build-cmake
BuildRequires(pre): cmake

BuildRequires: gcc-c++
BuildRequires: qt6-base-devel
BuildRequires: qt6-svg-devel

%{?_with_printer:BuildRequires: libcups-devel}

%if_with examples
BuildRequires: libopencv-devel
BuildRequires: CImg-devel
BuildRequires: libXext-devel
BuildRequires: libXrandr-devel
%endif

%description
JKQtPlotter is an extensive plotting framework for Qt (Qt5/Qt6),
including a feature-rich plotter widget and related components.


%package -n lib%name
Summary: JKQtPlotter runtime library for Qt6
Group: System/Libraries

%description -n lib%name
Runtime shared libraries of JKQtPlotter built against Qt6.
This package is required to run applications using JKQtPlotter with Qt6.


%package -n lib%name-devel
Summary: Development files for JKQtPlotter (Qt6)
Group: Development/C++
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files and CMake configuration needed to develop
applications using JKQtPlotter with Qt6.


%if_with examples
%package -n %name-examples
Summary: Examples for JKQtPlotter
Group: Development/C++
Requires: lib%name = %version-%release

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

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
%if_with examples
    -DCMAKE_INSTALL_BINDIR=%_libexecdir/%name/examples \
%endif
    -DCMAKE_PREFIX_PATH=%_libdir/cmake/Qt6 \
    -DJKQtPlotter_BUILD_DECORATE_LIBNAMES_WITH_BUILDTYPE:BOOL=OFF \
    -DJKQtPlotter_BUILD_TESTS:BOOL=OFF \
    -DJKQtPlotter_BUILD_TOOLS:BOOL=OFF \
    -DJKQtPlotter_BUILD_EXAMPLES:BOOL=%{with examples} \
    -DJKQtPlotter_BUILD_FORCE_NO_PRINTER_SUPPORT:BOOL=%{without printer} \
    -DBUILD_SHARED_LIBS=ON
%cmake_build


%install
%cmake_install


%files -n lib%name
%_libdir/libJKQT*6.so.*

%files -n lib%name-devel
%_includedir/jkqt*
%_libdir/libJKQT*6.so
%_libdir/cmake/JKQTPlotter*6*

%if_with examples
%files -n %name-examples
%_libexecdir/%name/examples
%endif

%files -n %name-doc
%doc %_docdir/*


%changelog
* Tue Jan 27 2026 Valentin Sokolov <sova@altlinux.org> 5.0.0-alt1.beta1
- Initial build for Sisyphus.