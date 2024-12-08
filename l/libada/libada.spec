%define oname ada

Name: libada
Version: 2.9.2
Release: alt1

Summary: WHATWG-compliant and fast URL parser written in modern C++

License: Apache-2.0
Group: System/Libraries
Url: https://github.com/ada-url/ada

Packager: Vitaly Lipatov <lav@altlinux.ru>

# Source-url: https://github.com/ada-url/ada/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++

%description
Ada is a fast and spec-compliant URL parser written in C++.
WHATWG-compliant and fast URL parser,
part of Node.js, Clickhouse, Redpanda, Kong, Telegram and Cloudflare Workers.

%package devel
Summary: Development files for %oname
Requires: %name = %EVR
Group: Development/C

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %oname.

%prep
%setup

%build
%cmake \
    -DCMAKE_BUILD_TYPE=RelWithDebInfo \
    -DBUILD_SHARED_LIBS=yes \
    -DADA_TOOLS=no \
    -DADA_BENCHMARKS=no \
    -DADA_TESTING=no \
    %nil
%cmake_build

%install
%cmake_install

%check
#ctest

%files
%_libdir/lib%oname.so.*

%files devel
%doc LICENSE*
%doc README.md
%_libdir/lib%oname.so
%_libdir/cmake/%oname/
%_includedir/%oname/
%_includedir/ada.h
%_includedir/ada_c.h

%changelog
* Sun Dec 08 2024 Vitaly Lipatov <lav@altlinux.ru> 2.9.2-alt1
- initial build for ALT Sisyphus
