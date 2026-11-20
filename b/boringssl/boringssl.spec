%define _unpackaged_files_terminate_build 1
# Upstream has no stable ABI. Increment on snapshot updates unless compatibility is verified.
%define abiversion 1
%define libname libboringssl%abiversion

Name: boringssl
Version: 0.20261020.0
Release: alt2

Summary: Google's BoringSSL cryptographic library
License: Apache-2.0 and ISC
Group: System/Libraries
Url: https://boringssl.googlesource.com/boringssl
VCS: https://github.com/google/boringssl.git

Source0: boringssl-%version.tar
Patch0: boringssl-alt-package-layout.patch
Patch1: boringssl-alt-shared-abi.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%{?optflags_lto:%global optflags_lto %{optflags_lto} -ffat-lto-objects}

%description
BoringSSL is Google's fork of OpenSSL. It is designed for use by Google,
Chromium and other applications that need its APIs; it does not promise a
stable ABI. This package installs its command-line utility.

%package -n %libname
Summary: BoringSSL shared libraries
Group: System/Libraries

%description -n %libname
BoringSSL shared libraries with ABI-specific SONAMEs and symbol
prefixes for use alongside OpenSSL.

%package -n libboringssl-devel
Summary: Development files for shared BoringSSL
Group: Development/C
Requires: %libname = %EVR

%description -n libboringssl-devel
Headers, linker symlinks, pkg-config and CMake targets for shared BoringSSL.
BoringSSL::SSL and BoringSSL::Crypto propagate the symbol prefix to consumers.

%package -n libboringssl-devel-static
Summary: Static archives for BoringSSL
Group: Development/C
Requires: libboringssl-devel = %EVR
Provides: boringssl-devel = %EVR
Obsoletes: boringssl-devel < %EVR

%description -n libboringssl-devel-static
Unprefixed PIC archives and CMake metadata for static BoringSSL consumers.

%prep
%setup -q
%autopatch -p1

%build
# Baseline i586 does not guarantee SSE2; use the portable implementation.
%cmake \
%ifarch %ix86
    -DOPENSSL_NO_ASM=ON \
%endif
    -DBUILD_TESTING=OFF \
    -DCMAKE_POSITION_INDEPENDENT_CODE=ON \
    -DCMAKE_INSTALL_INCLUDEDIR=%_includedir/boringssl \
    -DCMAKE_INSTALL_LIBDIR=%_libdir/boringssl
%cmake_build

%cmake -B %_cmake__builddir-shared \
%ifarch %ix86
    -DOPENSSL_NO_ASM=ON \
%endif
    -DBUILD_TESTING=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DBORINGSSL_ALT_ABI=%abiversion \
    -DBORINGSSL_ALT_VERSION=%version \
    -DCMAKE_INSTALL_INCLUDEDIR=include/boringssl \
    -DCMAKE_INSTALL_LIBDIR=%_libdir
cmake --build %_cmake__builddir-shared --parallel "${NPROCS:-16}"

%install
%cmake_install
DESTDIR=%buildroot cmake --install %_cmake__builddir-shared

%files
%doc LICENSE
%doc README.md
%_bindir/bssl

%files -n %libname
%doc LICENSE
%_libdir/libboringssl-*.so.%abiversion

%files -n libboringssl-devel
%doc LICENSE
%_includedir/boringssl/
%_libdir/libboringssl-*.so
%_libdir/cmake/BoringSSL/
%_pkgconfigdir/boringssl.pc

%files -n libboringssl-devel-static
%doc LICENSE
%dir %_libdir/boringssl
%dir %_libdir/boringssl/cmake
%_libdir/boringssl/libcrypto.a
%_libdir/boringssl/libssl.a
%_libdir/boringssl/libdecrepit.a
%_libdir/boringssl/libpki.a
%_libdir/boringssl/cmake/BoringSSL/

%changelog
* Fri Nov 20 2026 Ivan Khanas <xeno@altlinux.org> 0.20261020.0-alt2
- Package versioned shared BoringSSL libraries with prefixed symbols.
- Move static archives to libboringssl-devel-static.

* Wed Oct 28 2026 Ivan Khanas <xeno@altlinux.org> 0.20261020.0-alt1
- Initial build for ALT.
