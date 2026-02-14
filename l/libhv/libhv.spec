%define _unpackaged_files_terminate_build 1
%define soname 0
%define _common_libdir /usr/lib

Name: libhv
Version: 1.3.4
Release: alt1

Summary: A c/c++ network library for developing TCP/UDP/SSL/HTTP/WebSocket/MQTT client/server
License: BSD-3-Clause
Group: Development/Tools
Url: https://github.com/ithewei/libhv
Vcs: https://github.com/ithewei/libhv.git

ExcludeArch: %ix86

Source: %name-%version.tar

Patch: %name-%version-%release.patch

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: openssl-devel

%description
libhv is a c/c++ network library for developing TCP/UDP/SSL/HTTP/WebSocket/MQTT
client/server.  Like libevent, libev, and libuv, libhv provides event-loop with
non-blocking IO and timer, but simpler api and richer protocols.

%package -n libhv%soname
Summary: Dynamic libraries for libhv
Group: Development/Tools

%description -n libhv%soname
The runtime shared library for libhv.

%package devel
Summary: Development files for libhv
Group: Development/C++

%description devel
Development files for building applications that use libhv.

%prep
%setup -q
%autopatch -p1

%build
%cmake \
    -DSOVERSION=%soname \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_OPENSSL=ON \
    -DCMAKE_C_FLAGS="-fno-lto" \
    -DCMAKE_CXX_FLAGS="-fno-lto"

%cmake_build

%install
%cmake_install
rm -f %buildroot%_common_libdir/libhv_static.a

%files -n libhv%soname
%doc LICENSE
%_libdir/libhv.so.%soname

%files devel
%_libdir/libhv.so
%_common_libdir/cmake/libhv/*.cmake
%_includedir/hv/

%changelog
* Wed Jan 14 2026 Grant Makyan <karonus@altlinux.org> 1.3.4-alt1
- Init for ALT.
