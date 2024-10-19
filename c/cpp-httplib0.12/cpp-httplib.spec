%define oname cpp-httplib
%define sover 0.12

Name: %oname%sover
Version: 0.12.6
Release: alt2

Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
License: MIT
Group: System/Legacy libraries

Url: https://github.com/yhirose/%oname
Packager: Nazarov Denis <nenderus@altlinux.org>

# https://github.com/yhirose/%oname/archive/refs/tags/v%version/%oname-%version.tar.gz
Source: %oname-%version.tar

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libbrotli-devel
BuildRequires: libssl-devel
BuildRequires: python3
BuildRequires: zlib-devel

%description
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%package -n lib%oname%sover
Summary: A C++11 single-file header-only cross platform HTTP/HTTPS library.
Group: System/Legacy libraries

%description -n lib%oname%sover
A C++11 single-file header-only cross platform HTTP/HTTPS library.

%prep
%setup -n %oname-%version

%build
%cmake \
	-DBUILD_SHARED_LIBS:BOOL=TRUE \
	-DHTTPLIB_COMPILE:BOOL=TRUE
%cmake_build

%install
%cmake_install

%__rm -rf %buildroot%_libdir/cmake/httplib
%__rm -rf %buildroot%_libdir/libhttplib.so
%__rm -rf %buildroot%_includedir/httplib.h

%files -n lib%oname%sover
%doc LICENSE README.md
%_libdir/libhttplib.so.*

%changelog
* Sat Oct 19 2024 Nazarov Denis <nenderus@altlinux.org> 0.12.6-alt2
- Build as legacy library

* Sat Jun 10 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.6-alt1
- New version 0.12.6.

* Tue May 30 2023 Nazarov Denis <nenderus@altlinux.org> 0.12.5-alt1
- Initial build for ALT Linux
