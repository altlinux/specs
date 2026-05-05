%define _unpackaged_files_terminate_build 1

# Set textrel=relaxed for i586, i686 
%ifarch %ix86
%set_verify_elf_method textrel=relaxed
%endif

Name: wasmtime
Version: 43.0.0
Release: alt1
Summary: Wasmtime is a standalone runtime for WebAssembly, WASI, and the Component Model by the Bytecode Alliance.
License: Apache-2.0
Group: Development/Tools
Url: https://wasmtime.dev/
Vcs: https://github.com/bytecodealliance/wasmtime

BuildRequires: /proc
BuildRequires: rust-cargo
BuildRequires: elfutils
BuildRequires(pre): rpm-build-cmake

Source0: %name-%version.tar

%description
Wasmtime is a standalone runtime for WebAssembly, WASI, and the Component Model by the Bytecode
Alliance. It allows you to run WebAssembly code in a sandboxed environment, which is important for security.

%package examples
Summary: Wasmtime examples
Group: Development/Documentation

%description examples
This package contains examples of how to use the Wasmtime API to
create applications. The examples are organized by topic, such as
WASM, WASI, and Component Model.

%package -n libwasmtime
Summary: Shared library to develop with Wasmtime.
Group: System/Libraries
%description -n libwasmtime
The libwasmtime package contains the Wasmtime runtime library,
which provides WebAssembly run time support for the Component Model,
the WASI API, and the Wasmtime API. The library can be used to
embed Wasmtime's runtime in a program.

%package -n libwasmtime-devel
Summary: Includes and docs to develop with Wasmtime.
Group: Development/C
%description -n libwasmtime-devel
The libwasmtime-devel package contains the header files and
documentation to develop with the Wasmtime API. The Wasmtime API
provides a way to embed Wasmtime's runtime in a program and to
create applications that take advantage of the Component Model,
the WASI API, and the Wasmtime API.

%package -n libwasmtime-devel-static
Summary: Static library to develop with Wasmtime.
Group: Development/C

%description -n libwasmtime-devel-static
The libwasmtime-devel-static package contains the static library
libwasmtime.a, which can be used to embed Wasmtime's runtime in a
program. The static library provides all the symbols that are
needed to use the Wasmtime API.

%prep
%setup -q
mkdir -p .cargo/ && cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "$PWD/vendor"

[term]
verbose = true
quiet = false

[install]
root = "%buildroot%_prefix"

[profile.release]
strip = false
EOF

mkdir -p crates/c-api/.cargo && 
cp ./.cargo/config.toml crates/c-api/.cargo/config.toml

mkdir -p crates/c-api-macros/.cargo &&
cp ./.cargo/config.toml crates/c-api-macros/.cargo/config.toml

%build
export RUSTFLAGS="-Clink-args=-fPIC -Cdebuginfo=1 --cfg=rustix_use_libc -Crelocation-model=pic"
export CFLAGS="-O3 -DPIC -fPIC"
export RUST_MIN_STACK=16777216
cargo build %_smp_mflags --offline --release
cargo build %_smp_mflags --offline --release -p wasmtime-c-api
%cmake -S crates/c-api -DCMAKE_POSITION_INDEPENDENT_CODE=ON
%cmake_build

## Tests are disabled due to the lack of a packaged `wasm-unknown-unknown` target for rustc
#%check
#cargo test %_smp_mflags --release --no-fail-fast

%install
mkdir -p %buildroot{%_includedir,%_libdir}
install -Dp target/release/%name -t %buildroot%_bindir
install -Dm644 target/release/libwasmtime.so -t "%buildroot%_libdir"
install -Dm644 target/release/libwasmtime.a -t "%buildroot%_libdir"
cp -r %_target_platform/include/* "%buildroot%_includedir"
mkdir -p %buildroot%_datadir/%name/
cp -a examples %buildroot%_datadir/%name/

%files
%_bindir/wasmtime
%doc docs/*

%files examples
%dir %_datadir/%name
%_datadir/%name/examples/

%files -n libwasmtime
%_libdir/libwasmtime.so

%files -n libwasmtime-devel
%_includedir/*
%dir %_includedir/%name

%files -n libwasmtime-devel-static
%_libdir/libwasmtime.a

%changelog
* Sat Apr 04 2026 Vitaly Lipatov <lav@altlinux.ru> 43.0.0-alt1
- new version 43.0.0
- (GHSA-hc7m-r6v8-hg9q, CVE-2025-64345) SECURITY: fix in versions 36-38
- (GHSA-4h67-722j-5pmc, CVE-2025-62711) SECURITY: fix in v38.0.3
- (GHSA-xjhv-v822-pf94) SECURITY: fix in v40.0.4/v41.0.4
- (GHSA-852m-cvvp-9p4w) SECURITY: fix in v42.0.0
- (GHSA-243v-98vx-264h) SECURITY: fix in v42.0.0

* Mon Jul 28 2025 Korney Gedert <kiper@altlinux.org> 35.0.0-alt1
- New version 35.0.0.
- fix: wasmtime-examples=34.0.1-alt1 post-install unowned files

* Mon Jun 30 2025 Korney Gedert <kiper@altlinux.org> 34.0.1-alt1
- Initial release
