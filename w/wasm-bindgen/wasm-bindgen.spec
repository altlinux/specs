Name: wasm-bindgen
Version: 0.2.128
Release: alt1
Summary: Interoperating JavaScript and Rust code

License: MIT OR Apache-2.0
Group: Development/Tools
URL: https://github.com/wasm-bindgen/wasm-bindgen
# Source-url: https://github.com/wasm-bindgen/wasm-bindgen.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust /proc

%description
The wasm-bindgen CLI generates JavaScript bindings for WebAssembly modules
produced by Rust. It must match the wasm-bindgen library version used to
compile a module.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build -p wasm-bindgen-cli --no-default-features --features rustls-tls

%install
%rust_install wasm-bindgen wasm-bindgen-test-runner wasm2es6js

%files
%_bindir/wasm-bindgen
%_bindir/wasm-bindgen-test-runner
%_bindir/wasm2es6js
%doc README.md
%doc LICENSE-MIT LICENSE-APACHE

%changelog
* Fri Oct 23 2026 Vitaly Lipatov <lav@altlinux.ru> 0.2.128-alt1
- initial build
