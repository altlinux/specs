%define _unpackaged_files_terminate_build 1

Name: wasm-component-ld
Version: 0.5.22
Release: alt1

Summary: Command line linker for creating WebAssembly components
License: Apache-2.0 WITH LLVM-exception OR Apache-2.0 OR MIT
Group: Development/Tools
Url: https://github.com/bytecodealliance/wasm-component-ld

Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-build-rust
# For tests
BuildRequires: /usr/bin/wasm-ld

Requires: /usr/bin/wasm-ld

%description
wasm-component-ld is a linker driver for creating WebAssembly components.
It invokes LLVM wasm-ld to produce a core WebAssembly module and then
wraps that module as a WebAssembly component.

The tool is used by Clang and Rust toolchains for the wasm32-wasip2
target.

%prep
%setup -a 1
%rust_prep

%build
%rust_build

%install
%rust_install

%check
%rust_test --lib

%files
%_bindir/%name
%doc README.md LICENSE-APACHE LICENSE-Apache-2.0_WITH_LLVM-exception LICENSE-MIT

%changelog
* Fri May 22 2026 Artyom Sinyugin <writers@altlinux.org> 0.5.22-alt1
- Initial build.
