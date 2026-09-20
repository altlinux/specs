%define rname tlottie

Name: libtlottie
Version: 1.0.6
Release: alt1

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

Only a static library is built: upstream links it statically.

%package devel-static
Summary: Development files for %name
Group: Development/C
Provides: %name-devel = %EVR

%description devel-static
tlottie is a Rust library which renders Lottie animations and Telegram
animated stickers (TGS). It provides a C API and is used by Telegram
Desktop 7.2 and newer instead of the previous rlottie backend.

This package contains the static library and the header needed to build
applications with tlottie.

%prep
%setup -a1

install -vD %SOURCE2 .cargo/config.toml

%build
export CARGO_HOME="$PWD/.cargo"
cargo rustc --offline --locked --lib --release --features c-api --crate-type staticlib

%check
export CARGO_HOME="$PWD/.cargo"
# the dos:: and budget:: tests assert exact allocation sizes, so they depend on
# the allocator behaviour and the pointer width of the build host
cargo test --offline --locked -- --skip dos:: --skip renderer::frame::budget::

%install
install -pD -m644 target/release/libtlottie.a %buildroot%_libdir/libtlottie.a
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
Libs.private: -lm -lpthread -ldl -lgcc_s
Cflags: -I\${includedir}/%rname
EOF
install -pD -m644 tlottie.pc %buildroot%_pkgconfigdir/tlottie.pc

%files devel-static
%doc README.md LICENSE
%_libdir/libtlottie.a
%_includedir/%rname/
%_pkgconfigdir/tlottie.pc

%changelog
* Sun Sep 20 2026 Vitaly Lipatov <lav@altlinux.ru> 1.0.6-alt1
- initial build for Sisyphus

