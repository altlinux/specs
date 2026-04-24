%define soname 0
%define szsoname 2

Name: libaec
Version: 1.1.6
Release: alt1

Summary: Adaptive Entropy Coding library
License: BSD-2-Clause
Group: System/Libraries
Url: https://gitlab.dkrz.de/k202009/libaec
VCS: https://gitlab.dkrz.de/k202009/libaec

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: ctest
BuildRequires: gcc-c++

%description
Libaec provides fast lossless compression of 1 up to 32 bit wide
signed or unsigned integers (samples). The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations. While floating point representations are not directly
supported, they can also be efficiently coded by grouping exponents
and mantissa.

Libaec implements Golomb-Rice coding as defined in the Space Data
System Standard documents 121.0-B-2 and 120.0-G-2.

Libaec includes a drop-in replacement for the SZIP library.

%package -n libaec%soname
Summary: Adaptive Entropy Coding library
Group: System/Libraries

%description -n libaec%soname
Libaec provides fast lossless compression of 1 up to 32 bit wide
signed or unsigned integers (samples). The library achieves best
results for low entropy data as often encountered in space imaging
instrument data or numerical model output from weather or climate
simulations.

This package contains the shared library.

%package -n libsz%szsoname
Epoch: 1
Summary: SZIP library replacement using libaec
Group: System/Libraries

%description -n libsz%szsoname
This package provides a free drop-in replacement for the SZIP
compression library. It is a compatibility library that provides
the SZIP API using the libaec implementation.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: libsz%szsoname = %EVR

%description devel
This package contains development files for %name - headers
and CMake configuration files needed to build applications using libaec.

%prep
%setup

%build
%cmake \
	-DCMAKE_BUILD_TYPE=RelWithDebInfo \
	-DBUILD_SHARED_LIBS:BOOL=ON \
	-DBUILD_STATIC_LIBS:BOOL=OFF

%cmake_build

%install
%cmake_install

%check
%ctest

%files -n libaec%soname
%doc README.md CHANGELOG.md
%_libdir/libaec.so.%{soname}
%_libdir/libaec.so.%{soname}.*

%files -n libsz%szsoname
%doc doc/README.SZIP
%_libdir/libsz.so.%{szsoname}
%_libdir/libsz.so.%{szsoname}.*

%files devel
%_includedir/libaec.h
%_includedir/szlib.h
%_libdir/libaec.so
%_libdir/libsz.so
%_libdir/cmake/libaec/

%changelog
* Tue Apr 21 2026 Anton Farygin <rider@altlinux.org> 1.1.6-alt1
- 1.1.4 -> 1.1.6

* Thu Dec 04 2025 Anton Farygin <rider@altlinux.com> 1.1.4-alt1
- initial build for ALT Linux
