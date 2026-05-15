%define _unpackaged_files_terminate_build 1
%def_with check

Name: flamelens
Version: 0.4.0
Release: alt1

Summary: Flamegraph viewer in the terminal
License: MIT
Group: Development/Other
Url: https://github.com/YS-L/flamelens
VCS: https://github.com/YS-L/flamelens

# Source-url: https://github.com/YS-L/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
%name is an interactive flamegraph viewer in the terminal.

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md
%_bindir/%name

%changelog
* Fri May 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.4.0-alt1
- initial build for ALT Linux
