%define _unpackaged_files_terminate_build 1
%define soversion 1

Name: cppserver
Version: 1.0.6.0
Release: alt1

Summary: C++ asynchronous networking library
License: MIT
Group: Development/C++
Url: https://github.com/chronoxor/CppServer
VCS: https://github.com/chronoxor/CppServer.git

Source: %name-%version.tar
Patch: %name-%version-alt.patch

BuildRequires(pre): rpm-build-cmake
BuildRequires: gcc-c++
BuildRequires: libcppcommon-devel
BuildRequires: asio-devel
BuildRequires: libssl-devel

%description
CppServer is a C++ library providing asynchronous TCP, SSL, UDP, HTTP,
HTTPS and WebSocket servers and clients. It uses standalone Asio,
OpenSSL and CppCommon.

%package -n libcppserver%soversion
Summary: CppServer shared library
Group: System/Libraries

%description -n libcppserver%soversion
CppServer is a C++ library providing asynchronous TCP, SSL, UDP, HTTP,
HTTPS and WebSocket servers and clients. It uses standalone Asio,
OpenSSL and CppCommon.

This package contains the shared runtime library.

%package -n libcppserver-devel
Summary: Development files for CppServer
Group: Development/C++
Requires: libcppserver%soversion = %EVR

%description -n libcppserver-devel
This package contains the headers, linker symlink and pkg-config metadata
needed to develop applications using CppServer.

%prep
%setup
%autopatch -p1

%build
%cmake -DCPPSERVER_SYSTEM_DEPENDENCIES=ON
%cmake_build

%install
%cmake_install

%files -n libcppserver%soversion
%doc LICENSE
%_libdir/libcppserver.so.%soversion
%_libdir/libcppserver.so.%soversion.*

%files -n libcppserver-devel
%doc README.md
%_includedir/cppserver/
%_libdir/libcppserver.so
%_pkgconfigdir/cppserver.pc

%changelog
* Tue Nov 10 2026 Ajrat Makhmutov <rauty@altlinux.org> 1.0.6.0-alt1
- First build for ALT.
