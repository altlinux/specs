%define _unpackaged_files_terminate_build 1
%def_without python3_bindings

Name: grpc
Version: 1.35.0
Release: alt1

Summary: Modern, open source, high-performance remote procedure call (RPC) framework

License: Apache-2.0
Group: Networking/Other
URL: https://www.grpc.io

Source0: %name-%version.tar
# VCS0: git://github.com/grpc/grpc.git

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: openssl-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: libcares-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libre2-devel
#BuildRequires: gflags-devel
#BuildRequires: gtest-devel
#BuildRequires: gperftools-devel

Patch1: grpc-0001-enforce-system-crypto-policies.patch
Patch2: 0001-CMakeLists.txt-introduce-a-cache-variable-for-pkg-config.patch

%description
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package plugins
Summary: gRPC protocol buffers compiler plugins
Group: Networking/Other
Requires: protobuf-compiler

%description plugins
Plugins to the protocol buffers compiler to generate gRPC sources.

# %%package cli
# Summary: gRPC protocol buffers cli
# Group: Networking/Other

# %%description cli
# Plugins to the protocol buffers compiler to generate gRPC sources.

%package -n libgrpc
Summary: C API for gRPC
Group: System/Libraries

%description -n libgrpc
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package -n libgrpc++
Summary: C++ API for gRPC
Group: System/Libraries

%description -n libgrpc++
gRPC is a modern open source high performance RPC framework that can run in any
environment. It can efficiently connect services in and across data centers
with pluggable support for load balancing, tracing, health checking and
authentication. It is also applicable in last mile of distributed computing to
connect devices, mobile applications and browsers to backend services.

The main usage scenarios:

* Efficiently connecting polyglot services in microservices style architecture
* Connecting mobile devices, browser clients to backend services
* Generating efficient client libraries

Core Features that make it awesome:

* Idiomatic client libraries in 10 languages
* Highly efficient on wire and with a simple service definition framework
* Bi-directional streaming with http/2 based transport
* Pluggable auth, tracing, load balancing and health checking

%package -n libgrpc-devel
Summary: gRPC library development files: C libraries
Group: Development/C

%description -n libgrpc-devel
Development headers and files for gRPC libraries.

%package -n libgrpc++-devel
Summary: gRPC library development files: C++ libraries
Group: Development/C++

%description -n libgrpc++-devel
Development headers and files for gRPC libraries.

%if_with python3_bindings
%package -n python3-module-grpcio
Summary: Python language bindings for gRPC
Group: Development/Python3
Requires: %name = %EVR

%description -n python3-module-grpcio
Python3 bindings for gRPC library.
%endif

%prep
%setup
%patch1 -p1
%patch2 -p1

%build
rm -f Makefile
%define _cmake_builddir %_target_platform
rm -f BUILD
srcdir=..
%cmake -S "$srcdir" -B "$srcdir/%_cmake_builddir" \
    -DBUILD_SHARED_LIBS:BOOL=on \
    -DgRPC_INSTALL_LIBDIR="$(relative %_libdir/ %_prefix/)" \
    -DgRPC_INSTALL_PKGCONFIGDIR="$(relative %_pkgconfigdir/ %_prefix/)" \
    -DgRPC_ZLIB_PROVIDER="package" \
    -DgRPC_CARES_PROVIDER="package" \
    -DgRPC_RE2_PROVIDER="package" \
    -DgRPC_SSL_PROVIDER="package" \
    -DgRPC_PROTOBUF_PROVIDER="package" \
    -DgRPC_BENCHMARK_PROVIDER="package" \
    -DgRPC_ABSL_PROVIDER="package" \
#

LD_LIBRARY_PATH="%_cmake_builddir" \
    cmake --build "%_cmake_builddir" --verbose -j%__nprocs

%if_with python3_bindings
# build python module
export GRPC_PYTHON_BUILD_WITH_CYTHON=True
export GRPC_PYTHON_BUILD_SYSTEM_OPENSSL=True
export GRPC_PYTHON_BUILD_SYSTEM_ZLIB=True
export GRPC_PYTHON_BUILD_SYSTEM_CARES=True
export CFLAGS="%optflags"
%py3_build
%endif

%install
DESTDIR=%buildroot cmake --install "%_cmake_builddir" --verbose

%if_with python3_bindings
%py3_install
%endif

%files -n libgrpc
%doc README.md LICENSE
%_libdir/libaddress_sorting.so.*
%_libdir/libgpr.so.*
%_libdir/libgrpc.so.*
%_libdir/libgrpc_plugin_support.so.*
%_libdir/libgrpc_unsecure.so.*
%_datadir/grpc

%files -n libgrpc++
%doc README.md LICENSE
%_libdir/libgrpc++.so.*
%_libdir/libgrpc++_alts.so.*
%_libdir/libgrpc++_error_details.so.*
%_libdir/libgrpc++_reflection.so.*
%_libdir/libgrpc++_unsecure.so.*
%_libdir/libgrpcpp_channelz.so.*
%_libdir/libupb.so.*

# %%files cli
# %%_bindir/grpc_cli

%files plugins
%doc README.md LICENSE
%_bindir/grpc_*_plugin

%files -n libgrpc-devel
%_libdir/libaddress_sorting.so
%_libdir/libgpr.so
%_libdir/libgrpc.so
%_libdir/libgrpc_plugin_support.so
%_libdir/libgrpc_unsecure.so
%_pkgconfigdir/gpr.pc
%_pkgconfigdir/grpc.pc
%_pkgconfigdir/grpc_unsecure.pc
%_includedir/grpc
%_prefix/lib/cmake/grpc

%files -n libgrpc++-devel
%_libdir/libgrpc++.so
%_libdir/libgrpc++_alts.so
%_libdir/libgrpc++_error_details.so
%_libdir/libgrpc++_reflection.so
%_libdir/libgrpc++_unsecure.so
%_libdir/libgrpcpp_channelz.so
%_libdir/libupb.so
%_pkgconfigdir/grpc++.pc
%_pkgconfigdir/grpc++_unsecure.pc
%_includedir/grpc++
%_includedir/grpcpp

%if_with python3-bindings
%files -n python3-grpcio
%doc LICENSE
%{python3_sitearch}/grpc
%{python3_sitearch}/grpcio-%{version}-py%{python3_version}.egg-info
%endif

%changelog
* Wed Jan 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.35.0-alt1
- Initial build for ALT Sisyphus.
