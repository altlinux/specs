%define sover 1
%define libname libultrahdr%sover
Name: libultrahdr
Version: 1.4.0
Release: alt2
Summary: Library for handling Ultra HDR image format
License: Apache-2.0
Group: System/Libraries
Url: https://github.com/google/libultrahdr
Source: %name-%version.tar
Patch0: %name-%version-%release.patch

BuildRequires: gcc-c++
BuildRequires: cmake ctest
BuildRequires: pkgconfig
BuildRequires: libjpeg-devel


%description
libultrahdr is a library providing encoding and decoding functionality
for the Ultra HDR image format, which combines SDR and HDR in a single image file.

%package -n %libname
Summary: Shared library for %name
Group: System/Libraries

%description -n %libname
This package contains shared library files for %name.

%package tools
Summary: Ultra HDR command-line utility
Group: Graphics
Requires: %libname = %EVR

%description tools
This package contains the ultrahdr_app command-line utility for encoding and decoding
Ultra HDR images.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %libname = %EVR

%description devel
This package contains header files and libraries needed for developing
applications using %name.

%prep
%setup
%patch0 -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=%prefix \
    -DBUILD_SHARED_LIBS:BOOL=on \
    -DCMAKE_INSTALL_LIBDIR=%_libdir

%cmake_build

%install
%cmakeinstall_std
rm -f %buildroot/%_libdir/*.a


%files -n %libname
%doc README.md LICENSE
%_libdir/*.so.%{sover}
%_libdir/*.so.%{sover}.*

%files tools
%_bindir/ultrahdr_app

%files devel
%_includedir/*
%_libdir/*.so
%_libdir/pkgconfig/*.pc

%changelog
* Wed Apr 22 2026 Anton Farygin <rider@altlinux.org> 1.4.0-alt2
- fixed build with gcc 15

* Mon Mar 17 2025 Anton Farygin <rider@altlinux.ru> 1.4.0-alt1
- initial build for ALT Linux
