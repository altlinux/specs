%define rname tlottie
# upstream sets no soname for the cdylib, this one is ALT-specific:
# bump it when the C API in include/tlottie.h breaks ABI
%define sover 1

Name: libtlottie
Version: 1.0.6
Release: alt2

Summary: Rust Lottie renderer with a C API

License: MIT
Group: System/Libraries
Url: https://github.com/dkaraush/tlottie

# Telegram Desktop pins an older snapshot and applies
# desktop-app/patches/tlottie.patch to it. Both behaviour fixes of that patch
# (empty tangent arrays in optimized .tgs and the rlottie order of the `d`
# field) are already implemented upstream in 1.0.6, so no patch is needed here.
# Source-url: https://github.com/dkaraush/tlottie.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

%description
tlottie is a Rust library which renders Lottie animations and Telegram
animated stickers (TGS). It provides a C API and is used by Telegram
Desktop 7.2 and newer instead of the previous rlottie backend.

%package -n %name%sover
Summary: Rust Lottie renderer with a C API
Group: System/Libraries

%description -n %name%sover
tlottie is a Rust library which renders Lottie animations and Telegram
animated stickers (TGS). It provides a C API and is used by Telegram
Desktop 7.2 and newer instead of the previous rlottie backend.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name%sover = %EVR
Obsoletes: %name-devel-static < %EVR

%description devel
tlottie is a Rust library which renders Lottie animations and Telegram
animated stickers (TGS). It provides a C API and is used by Telegram
Desktop 7.2 and newer instead of the previous rlottie backend.

This package contains the header and the link library needed to build
applications with tlottie.

%prep
%setup -a1

install -vD %SOURCE2 .cargo/config.toml

%build
export CARGO_HOME="$PWD/.cargo"
# rustc does not set a soname for a cdylib, so pass it explicitly
cargo rustc --offline --locked --lib --release --features c-api \
    --crate-type cdylib -- -C link-arg=-Wl,-soname,libtlottie.so.%sover

%check
export CARGO_HOME="$PWD/.cargo"
# the dos:: and budget:: tests assert exact allocation sizes, so they depend on
# the allocator behaviour and the pointer width of the build host
cargo test --offline --locked -- --skip dos:: --skip renderer::frame::budget::

%install
install -pD -m755 target/release/libtlottie.so %buildroot%_libdir/libtlottie.so.%version
ln -s libtlottie.so.%version %buildroot%_libdir/libtlottie.so.%sover
ln -s libtlottie.so.%sover %buildroot%_libdir/libtlottie.so

install -pD -m644 include/tlottie.h %buildroot%_includedir/%rname/tlottie.h

cat > tlottie.pc <<EOF
prefix=%prefix
exec_prefix=%prefix
libdir=%_libdir
includedir=%_includedir

Name: tlottie
Description: Rust Lottie renderer with a C API
Version: %version
Libs: -L\${libdir} -ltlottie
Cflags: -I\${includedir}/%rname
EOF
install -pD -m644 tlottie.pc %buildroot%_pkgconfigdir/tlottie.pc

%files -n %name%sover
%doc README.md LICENSE
%_libdir/libtlottie.so.%sover
%_libdir/libtlottie.so.%version

%files devel
%_libdir/libtlottie.so
%_includedir/%rname/
%_pkgconfigdir/tlottie.pc

%changelog
* Thu Oct 08 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt2
- build shared library libtlottie.so.1 instead of the static one

* Sun Sep 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for Sisyphus
