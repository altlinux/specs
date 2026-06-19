%define _unpackaged_files_terminate_build 1

%def_without check

%define sover 1
%define libname libliquid%{sover}
Name: liquid-dsp
Version: 1.8.0
Release: alt1

Summary: Digital Signal Processing Library for Software-Defined Radios
License: MIT
Group: Development/C++
Url: https://liquidsdr.org
VCS: https://github.com/jgaeddert/liquid-dsp

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: ctest

%description
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP
modules that do no rely on external dependencies or cumbersome
frameworks.

%package -n %{libname}
Summary: Digital signal processing library for software-defined radios
Group: Development/C++
Obsoletes: libliquid < %{version}
Provides: libliquid = %{version}

%description -n %{libname}
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP
modules that do no rely on external dependencies or cumbersome
frameworks.

%package devel
Summary: Development files for the liquid-dsp library
Group: Development/C++
Requires: %{libname} = %{version}
Obsoletes: libliquid-devel < %{version}
Provides: libliquid-devel = %{version}

%description devel
liquid-dsp is a signal processing library for software-defined
radios written in C. Its purpose is to provide a set of extensible DSP
modules that do no rely on external dependencies or cumbersome
frameworks.

This subpackage contains libraries and header files for developing
applications that want to make use of libliquid.

%prep
%setup
sed -i 's|DESTINATION lib$|DESTINATION "lib${LIB_SUFFIX}"|' CMakeLists.txt

%build
%cmake \
       -DENABLE_SIMD=OFF \
       -DBUILD_EXAMPLES=OFF
%cmake_build

%install
%cmake_install

%check
%ctest

%files -n %libname
%doc LICENSE CHANGELOG.md README.rst
%_libdir/libliquid.so.%{sover}
%_libdir/libliquid.so.%{sover}.*

%files devel
%doc LICENSE examples
%dir %_includedir/liquid
%_includedir/liquid/*
%_libdir/libliquid.so
%dir %_libdir/cmake/liquid
%_libdir/cmake/liquid/*.cmake
%_libdir/pkgconfig/liquid-dsp.pc

%changelog
* Fri Jun 19 2026 Nikolay Strelkov <snk@altlinux.org> 1.8.0-alt1
- New version 1.8.0.

* Sun Jun 08 2025 Nikolay Strelkov <snk@altlinux.org> 1.7.0-alt1
- Initial build for Sisyphus
