%define _unpackaged_files_terminate_build 1

%define libname amqpcpp
%define abiversion 4

Name:    amqp-cpp
Version: 4.3.27
Release: alt2

Summary: C++ library for asynchronous non-blocking communication with RabbitMQ
License: Apache-2.0
Group:   Development/C++
Url:     https://github.com/CopernicaMarketingSoftware/AMQP-CPP

Source: %name-%version.tar

BuildRequires(pre): cmake
BuildRequires: gcc-c++
BuildRequires: libssl-devel

%description
AMQP-CPP is a C++ library for communicating with a RabbitMQ message broker.
The library can be used to parse incoming data from,
and generate frames to, a RabbitMQ server.

%package -n lib%name%abiversion
Summary: C++ library for asynchronous non-blocking communication with RabbitMQ
Group: System/Libraries

%description -n lib%name%abiversion
AMQP-CPP is a C++ library for communicating with a RabbitMQ message broker.
The library can be used to parse incoming data from,
and generate frames to, a RabbitMQ server.

%package -n lib%name-devel
Summary: Developer files for lib%name
Group: Development/C++
Requires: lib%name%abiversion = %EVR

%description -n lib%name-devel
The lib%name-devel package contains libraries and header files for
developing applications that use lib%name%abiversion.

%prep
%setup

%build
# Fix install cmakedir
sed -i 's|DESTINATION cmake|DESTINATION ${CMAKE_INSTALL_LIBDIR}/cmake|' CMakeLists.txt

%cmake -DAMQP-CPP_BUILD_SHARED=ON \
       -DAMQP-CPP_LINUX_TCP=ON
%cmake_build

%install
%cmakeinstall_std

%files -n lib%name%abiversion
%doc *.md LICENSE
%_libdir/lib%libname.so.%{abiversion}*

%files -n lib%name-devel
%_cmakedir/*
%_includedir/*.h
%_includedir/%libname
%_pkgconfigdir/%libname.pc
%_libdir/lib%libname.so

%changelog
* Wed Mar 11 2026 Nikita Shmatko <nash@altlinux.org> 4.3.27-alt2
- Minor specfile fixes.

* Wed Oct 29 2025 Nikita Shmatko <nash@altlinux.org> 4.3.27-alt1
- Initial build for Sisyphus.
