%define _unpackaged_files_terminate_build 1
# SONAME entry lists the full version, including patch
%define abiversion 12

Name: libixwebsocket
Version: 12.0.1
Release: alt1

Summary: Websocket and http client and server library with TLS support
License: BSD-3-Clause
Group: Development/C++
Url: https://github.com/machinezone/IXWebSocket
Vcs: https://github.com/machinezone/IXWebSocket

Source: %name-%version.tar
Patch1: libixwebsocket-12.0.1-alt-fix-set-soversion.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-ninja
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: zlib-devel

%description
IXWebSocket is a C++ library for WebSocket client and server development.
It has minimal dependencies (no boost), is very simple to use and support
everything you'll likely need for websocket dev (SSL, deflate compression,
compiles on most platforms, etc...). HTTP client and server code is also
available, but it hasn't received as much testing. CORS is supported: custom
headers such as Access-Control-Allow-Origin can be set on responses through
the extra headers mechanism.

%package -n libixwebsocket%abiversion
Summary: Library libixwebsocket of ixwebsocket
Group: Development/C++

%description -n libixwebsocket%abiversion
This package contains library libuxwebsocket of IXWebSocket.

%package devel
Summary: Development files for IXWebSocket
Group: Development/C++

%description devel
This package contains development files for IXWebSocket.

%prep
%setup
%autopatch -p1
rm -rf third_party/

%build
%cmake \
  -GNinja \
  -Wno-dev \
  -DBUILD_SHARED_LIBS=ON \
  #
%cmake_build

%install
%cmake_install

%files -n libixwebsocket%abiversion
%_libdir/libixwebsocket.so.%abiversion
%_libdir/libixwebsocket.so.%version

%files devel
%_libdir/libixwebsocket.so
%_includedir/ixwebsocket
%_cmakedir/ixwebsocket
%_pkgconfigdir/ixwebsocket.pc

%changelog
* Tue Aug 25 2026 Pavel Petrykin <silverducks@altlinux.org> 12.0.1-alt1
- Initial build for Alt Linux.
