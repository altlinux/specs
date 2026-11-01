%define _unpackaged_files_terminate_build 1

Name: boringssl
Version: 0.20261020.0
Release: alt1

Summary: Google's BoringSSL cryptographic library
License: Apache-2.0 and ISC
Group: System/Libraries
Url: https://boringssl.googlesource.com/boringssl
VCS: https://github.com/google/boringssl.git

Source0: boringssl-%version.tar
Patch0: boringssl-alt-package-layout.patch

BuildRequires(pre): rpm-macros-cmake
BuildRequires: cmake
BuildRequires: gcc-c++
BuildRequires: make

%{?optflags_lto:%global optflags_lto %{optflags_lto} -ffat-lto-objects}

%description
BoringSSL is Google's fork of OpenSSL. It is designed for use by Google,
Chromium and other applications that need its APIs; it does not promise a
stable ABI. This package installs its command-line utility.

%package devel
Summary: Headers and static libraries for BoringSSL
Group: Development/C

%description devel
Headers, static libraries and CMake package metadata for applications that
embed BoringSSL. The files use a private prefix to avoid collisions with
OpenSSL; no shared libraries or stable ABI are provided.

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

%install
%cmake_install

%files
%doc LICENSE
%doc README.md
%_bindir/bssl

%files devel
%doc LICENSE
%_includedir/boringssl/
%_libdir/boringssl/libcrypto.a
%_libdir/boringssl/libssl.a
%_libdir/boringssl/libdecrepit.a
%_libdir/boringssl/libpki.a
%_libdir/boringssl/cmake/BoringSSL/

%changelog
* Wed Oct 28 2026 Ivan Khanas <xeno@altlinux.org> 0.20261020.0-alt1
- Initial build for ALT.
