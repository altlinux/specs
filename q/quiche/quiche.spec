%define _unpackaged_files_terminate_build 1
%define abiversion 0

Name: quiche
Version: 0.30.1
Release: alt1

Summary: QUIC and HTTP/3 protocol implementation and tools
License: BSD-2-Clause AND BSD-3-Clause AND MIT AND Apache-2.0 AND ISC AND MPL-2.0 AND Unicode-3.0 AND Zlib
Group: Networking/Other
URL: https://quiche.tech/
VCS: https://github.com/cloudflare/quiche.git

Source: %name-%version.tar
Source1: quiche.pc

Requires: %name-common

BuildRequires(pre): rpm-build-rust
BuildRequires: gcc-c++
BuildRequires: cmake
BuildRequires: clang
BuildRequires: libclang21
BuildRequires: git-core
BuildRequires: perl
BuildRequires: pkg-config
BuildRequires: fontconfig-devel
BuildRequires: libfreetype-devel
BuildRequires: libexpat-devel
BuildRequires: libzstd-devel

%description
Quiche implements the QUIC transport protocol and HTTP/3. This package
contains its client, server, interactive HTTP/3 tool and qlog analysis tool.

%package common
Summary: Shared license notices for Quiche
Group: Documentation
BuildArch: noarch

%description common
Original license notices for the Quiche libraries, programs and their
embedded dependencies.

%package -n lib%name%abiversion
Summary: QUIC and HTTP/3 shared library
Group: System/Libraries
Requires: %name-common

%description -n lib%name%abiversion
The native C interface to Quiche's QUIC and HTTP/3 implementation.

%package -n lib%name-devel
Summary: Development files for Quiche
Group: Development/C
Requires: lib%name%abiversion = %version-%release

%description -n lib%name-devel
C headers and pkg-config metadata for developing applications with Quiche.

%package -n lib%name-devel-static
Summary: Static Quiche library
Group: Development/C
Requires: lib%name-devel = %version-%release

%description -n lib%name-devel-static
The static library for applications that require static linking to Quiche.

%prep
%setup

%build
export ZSTD_SYS_USE_PKG_CONFIG=1
export CFLAGS="%optflags -ffat-lto-objects"
export CXXFLAGS="%optflags -ffat-lto-objects"
%rust_build --locked --workspace --features async,ffi,qlog,rpk
%cargo build --release --offline --locked -p quiche --lib \
    --features ffi,qlog,pkg-config-meta

%install
%rust_install quiche-client quiche-server h3i qlog-dancer
install -Dm755 target/release/libquiche.so \
    %buildroot%_libdir/libquiche.so.%abiversion
ln -s libquiche.so.%abiversion %buildroot%_libdir/libquiche.so
install -Dm644 target/release/libquiche.a %buildroot%_libdir/libquiche.a
install -Dm644 quiche/include/quiche.h %buildroot%_includedir/quiche.h
install -d %buildroot%_libdir/pkgconfig
sed -e 's|@LIBDIR@|%_libdir|g' -e 's|@VERSION@|%version|g' \
    %SOURCE1 > %buildroot%_libdir/pkgconfig/quiche.pc
mkdir -p vendor-notices
find vendor -type f \( -iname 'license*' -o -iname 'copying*' \
    -o -iname 'notice*' \) -print0 | \
    while IFS= read -r -d '' notice; do
        install -Dm644 "$notice" "vendor-notices/$notice"
    done

%check
%rust_test --locked --workspace --all-targets --features async,ffi,qlog,rpk
%rust_test --locked --workspace --doc --features async,ffi,qlog,rpk

%files
%_bindir/quiche-client
%_bindir/quiche-server
%_bindir/h3i
%_bindir/qlog-dancer

%files common
%doc COPYING vendor-notices

%files -n lib%name%abiversion
%_libdir/libquiche.so.%abiversion

%files -n lib%name-devel
%_includedir/quiche.h
%_libdir/libquiche.so
%_libdir/pkgconfig/quiche.pc

%files -n lib%name-devel-static
%_libdir/libquiche.a

%changelog
* Sat Nov 21 2026 Ivan Khanas <xeno@altlinux.org> 0.30.1-alt1
- New version.
- Fix the C layout of peer transport parameters.
- Fix log isolation in the 0-RTT timeout test.
- Use ephemeral ports in migration tests.

* Sun Nov 15 2026 Ivan Khanas <xeno@altlinux.org> 0.30.0-alt1
- Initial build for ALT.
