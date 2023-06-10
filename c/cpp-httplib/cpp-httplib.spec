%define sover 0.12

Name: cpp-httplib
Version: 0.12.6
Release: alt1

Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
License: MIT
Group: System/Libraries

Url: https://github.com/yhirose/%name
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/yhirose/%name/archive/refs/tags/v%version/%name-%version.tar.gz
Source: %name-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: libssl-devel
BuildRequires: python3
BuildRequires: zlib-devel

%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%package -n lib%name%sover
Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
Group: System/Libraries

%description -n lib%name%sover
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%package -n lib%name-devel
Summary: Header files for lib%name
Group: Development/C++

%description -n lib%name-devel
Header files for lib%name

%prep
%setup

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DHTTPLIB_COMPILE:BOOL=TRUE
%cmake_build

%install
%cmake_install

%files -n lib%name%sover
%doc LICENSE README.md
%_libdir/libhttplib.so.*

%files -n lib%name-devel
%_libdir/cmake/httplib
%_libdir/libhttplib.so
%_includedir/httplib.h

%changelog
* Sat Jun 10 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.6-alt1
- New version 0.12.6.

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.5-alt1
- Initial build for ALT Linux
