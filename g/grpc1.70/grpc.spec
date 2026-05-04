%define _unpackaged_files_terminate_build 0

# ABI/SONAME versions from CMakeLists.txt of grpc 1.70.1
# (gRPC_CORE_SOVERSION / gRPC_CPP_SOVERSION).
%define _sover_c   45
%define _sover_cxx 1.70

Name: grpc1.70
Version: 1.70.1
Release: alt2

Summary: gRPC 1.70 legacy runtime libraries
License: Apache-2.0
Group: System/Libraries
Url: https://www.grpc.io
Vcs: https://github.com/grpc/grpc.git

Source0: %name-%version.tar
Source11: envoy-api.tar
Source12: opencensus-proto.tar
Source13: xds.tar

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake ninja-build
BuildRequires: gcc-c++ libstdc++-devel
BuildRequires: libprotobuf-devel
BuildRequires: protobuf-compiler
BuildRequires: openssl-devel libssl-devel
BuildRequires: pkgconfig(zlib)
BuildRequires: libcares-devel
BuildRequires: libabseil-cpp-devel
BuildRequires: libre2-devel
BuildRequires: libxxhash-devel
BuildRequires: chrpath
BuildRequires: libopentelemetry-devel

Patch0: grpc1.70-1.70.1-alt.patch
Patch1: grpc-0001-enforce-system-crypto-policies.patch

%description
Legacy runtime shared libraries from gRPC 1.70.1, kept in Sisyphus alongside
the current grpc package so that consumers built against the previous
SOVERSIONs (C %_sover_c, C++ %_sover_cxx) keep working. This package ships
only the .so.* files; headers, pkgconfig, cmake helpers and language bindings
live in the main grpc package.

%package -n libgrpc
Summary: C runtime library for gRPC 1.70 (legacy)
Group: System/Libraries

%description -n libgrpc
Legacy C runtime shared libraries from gRPC 1.70.1 (SOVERSION %_sover_c).
For headers and development files use the current grpc-devel package.

%package -n libgrpc++
Summary: C++ runtime library for gRPC 1.70 (legacy)
Group: System/Libraries

%description -n libgrpc++
Legacy C++ runtime shared libraries from gRPC 1.70.1 (SOVERSION %_sover_cxx).
For headers and development files use the current grpc-devel package.

%prep
%setup
tar -xf %SOURCE11 -C third_party/envoy-api
tar -xf %SOURCE12 -C third_party/opencensus-proto
tar -xf %SOURCE13 -C third_party/xds
%autopatch -p1
rm -rvf third_party/googletest
rm -rvf third_party/xxhash
rm -rfv \
    src/boringssl/boringssl_prefix_symbols.h \
    third_party/cares/ares_build.h \
    third_party/upb/third_party/lunit
rm -rvf examples/android src/android
rm -vf examples/node/package-lock.json

%build
rm -f Makefile
rm -f BUILD

# Prevent -Werror=return-type in switch/case blocks:
%add_optflags -Wno-error=return-type

%cmake \
    -DBUILD_SHARED_LIBS:BOOL=ON \
    -DCMAKE_SKIP_INSTALL_RPATH:BOOL=OFF \
    -DgRPC_INSTALL_LIBDIR="$(relative %_libdir/ %prefix/)" \
    -DgRPC_INSTALL_PKGCONFIGDIR="$(relative %_pkgconfigdir/ %prefix/)" \
    -DgRPC_ZLIB_PROVIDER="package" \
    -DgRPC_CARES_PROVIDER="package" \
    -DgRPC_RE2_PROVIDER="package" \
    -DgRPC_SSL_PROVIDER="package" \
    -DgRPC_PROTOBUF_PROVIDER="package" \
    -DgRPC_PROTOBUF_PACKAGE_TYPE:STRING='MODULE' \
    -DgRPC_USE_PROTO_LITE:BOOL=OFF \
    -DgRPC_BENCHMARK_PROVIDER="package" \
    -DgRPC_ABSL_PROVIDER="package" \
    -DgRPC_BUILD_GRPC_CSHARP_PLUGIN:BOOL=OFF \
    -DgRPC_BUILD_GRPC_NODE_PLUGIN:BOOL=OFF \
    -DgRPC_BUILD_GRPC_OBJECTIVE_C_PLUGIN:BOOL=OFF \
    -DgRPC_BUILD_GRPC_PHP_PLUGIN:BOOL=OFF \
    -DgRPC_BUILD_GRPC_PYTHON_PLUGIN:BOOL=OFF \
    -DgRPC_BUILD_GRPC_RUBY_PLUGIN:BOOL=OFF \
    -DCMAKE_CXX_STANDARD=17 \
    -GNinja

%cmake_build

%ifarch %e2k
# error: cpio archive too big - 5000M
strip --strip-debug %_cmake__builddir/libgrpc{,_*}.so.*
%endif

%install
%cmake_install

%files -n libgrpc
%doc README.md LICENSE
%_libdir/libgpr.so.%{_sover_c}*
%_libdir/libgrpc.so.%{_sover_c}*
%_libdir/libgrpc_unsecure.so.%{_sover_c}*
%dir %_libdir/grpc
%_libdir/grpc/*.so.%{_sover_c}*

%files -n libgrpc++
%doc README.md LICENSE
%_libdir/libgrpc++.so.%{_sover_cxx}*
%_libdir/libgrpc++_alts.so.%{_sover_cxx}*
%_libdir/libgrpc++_error_details.so.%{_sover_cxx}*
%_libdir/libgrpc++_reflection.so.%{_sover_cxx}*
%_libdir/libgrpc++_unsecure.so.%{_sover_cxx}*
%_libdir/libgrpcpp_channelz.so.%{_sover_cxx}*
%_libdir/libgrpc_authorization_provider.so.%{_sover_cxx}*
%_libdir/libgrpc_plugin_support.so.%{_sover_cxx}*

%changelog
* Sun Apr 26 2026 Anton Farygin <rider@altlinux.org> 1.70.1-alt2
- built as legacy package grpc1.70 (runtime libraries only)

* Mon Jul 07 2025 Ilya Kurdyukov <ilyakurdyukov@altlinux.org> 1.70.1-alt1.1
- e2k build fix

* Fri Feb 21 2025 Paul Wolneykien <manowar@altlinux.org> 1.70.1-alt1
- NMU: Update to v1.70.1.
- NMU: Install third-party libraries to %_libdir/grpc.

* Mon Apr 10 2023 Alexey Shabalin <shaba@altlinux.org> 1.53.0-alt1
- 1.53.0

* Sat Jul 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1.2
- ! closes gem build requires with check condition

* Sat Jul 24 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1.1
- + ruby packages

* Tue Jun 01 2021 Pavel Skrylev <majioa@altlinux.org> 1.38.0-alt1
- ^ 1.35.0 -> 1.38.0

* Mon May 31 2021 Arseny Maslennikov <arseny@altlinux.org> 1.35.0-alt3
- spec: Fixed FTBFS.

* Tue May 11 2021 Slava Aseev <ptrnine@altlinux.org> 1.35.0-alt2
- Fix build with libabseil (-DCMAKE_CXX_STANDARD=17)

* Wed Jan 27 2021 Arseny Maslennikov <arseny@altlinux.org> 1.35.0-alt1
- Initial build for ALT Sisyphus.
