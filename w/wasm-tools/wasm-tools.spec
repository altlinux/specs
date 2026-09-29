%define _unpackaged_files_terminate_build 1
%define _stripped_files_terminate_build 1

Name: wasm-tools
Version: 1.259.0
Release: alt1
Summary: CLI and Rust libraries for low-level manipulation of WebAssembly modules
License: Apache-2.0 and Apache-2.0 with LLVM-exception and MIT
Group: Development/Other
Url: https://github.com/bytecodealliance/wasm-tools
Vcs: https://github.com/bytecodealliance/wasm-tools.git

Source: %name-%version.tar
%{!?_enable_rust_vendoring:
Source1: vendor.tar
}

BuildRequires(pre): rpm-build-rust
%{?_enable_rust_vendoring:
BuildRequires: cargo-vendor-filterer
}

%description
%summary.

%prep
%setup %{!?_enable_rust_vendoring:-a1}
%rust_prep

%build
%rust_build

%install
%rust_install

%files
%_bindir/wasm-tools

%changelog
* Tue Sep 29 2026 Sergey Zhidkih <rx1513@altlinux.org> 1.259.0-alt1
- Initial build.
