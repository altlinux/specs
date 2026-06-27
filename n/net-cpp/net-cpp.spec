%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

# TODO do something related to C++17 support in gtest and this code
%def_without check

Name: net-cpp
Version: 3.2.2
Release: alt1

Summary: A simple yet beautiful networking API for C++14
License: LGPL-3.0-only
Group: System/Libraries
Url: https://gitlab.com/ubports/development/core/lib-cpp/net-cpp

Source: %name-%version.tar

# sync with version 3.2.2 from Debian unstable
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-cmake

BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: doxygen
BuildRequires: /usr/bin/dot
BuildRequires: boost-devel
BuildRequires: pkgconfig(libcurl)
BuildRequires: pkgconfig(jsoncpp)
BuildRequires: pkgconfig(process-cpp)
BuildRequires: boost-asio-devel
BuildRequires: pkgconfig(gtest)

%description
%summary

%package -n lib%{name}
Summary: C++14 library for networking purposes - runtime library
Group: System/Libraries

%description -n lib%{name}
Net-Cpp is a simple and straightforward networking library for C++14.

This package includes the net-cpp runtime libraries.

%package -n lib%{name}-doc
Summary: Documentation files for libnet-cpp-devel
Group: Documentation
BuildArch: noarch

%description -n lib%{name}-doc
Net-Cpp is a simple and straightforward networking library for C++14.

This package includes the documentation files for the libnet-cpp
development.

%package -n lib%{name}-devel
Summary: C++14 library for networking purposes - development headers
Group: Development/C++
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
Net-Cpp is a simple and straightforward networking library for C++11.

This package includes all the development headers and libraries for
net-cpp.

%prep
%setup
%patch -p1
sed -i "s/-std=c++17/-std=c++14/" CMakeLists.txt

%build
%cmake \
       -DBUILD_TESTING=Off
%cmake_build

%install
%cmake_install

%check
%ctest -j1 -VV -E "http_client_test"

%files -n lib%{name}
%doc AUTHORS ChangeLog COPYING
%_libdir/libnet-cpp.so.2
%_libdir/libnet-cpp.so.3.?.?

%files -n lib%{name}-devel
%_libdir/libnet-cpp.so
%_includedir/core/location.h
%_includedir/core/net/error.h
%_includedir/core/net/http/client.h
%_includedir/core/net/http/content_type.h
%_includedir/core/net/http/error.h
%_includedir/core/net/http/header.h
%_includedir/core/net/http/method.h
%_includedir/core/net/http/request.h
%_includedir/core/net/http/response.h
%_includedir/core/net/http/status.h
%_includedir/core/net/http/streaming_client.h
%_includedir/core/net/http/streaming_request.h
%_includedir/core/net/uri.h
%_includedir/core/net/visibility.h
%_pkgconfigdir/net-cpp.pc

%files -n lib%{name}-doc
%dir %_datadir/doc/net-cpp
%_datadir/doc/net-cpp/*

%changelog
* Sat Jun 27 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.2-alt1
- New version 3.2.2.

* Sun Mar 15 2026 Nikolay Strelkov <snk@altlinux.org> 3.2.1-alt1
- New version 3.2.1.

* Sat Nov 15 2025 Nikolay Strelkov <snk@altlinux.org> 3.2.0-alt2
- Applied repocop fix for arch-dep-package-consists-of-usr-share

* Sat Sep 13 2025 Nikolay Strelkov <snk@altlinux.org> 3.2.0-alt1
- New version 3.2.0.

* Sun Jul 27 2025 Nikolay Strelkov <snk@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
