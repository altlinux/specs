Name: wasm-pack
Version: 0.15.0
Release: alt1

Summary: Rust to WebAssembly workflow tool

License: MIT and Apache-2.0
Group: System/Configuration/Other
URL: https://github.com/wasm-bindgen/wasm-pack
# Source-url: https://github.com/wasm-bindgen/wasm-pack.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

%description
wasm-pack is a command line tool for building and working with Rust-generated
WebAssembly packages.

%prep
%setup -a1
%rust_prep
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/wasm-pack
%doc README.md

%changelog
* Sat Oct 24 2026 Vitaly Lipatov <lav@altlinux.ru> 0.15.0-alt1
- build wasm-pack from source with system Rust tooling.

