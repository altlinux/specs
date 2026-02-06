%define _unpackaged_files_terminate_build 1

Name: tgt-client
Version: 1.0.0
Release: alt1

Summary: A simple TUI for Telegram
License: Apache-2.0 and MIT
Group: Networking/Instant messaging
Url: https://github.com/FedericoBruzzone/tgt
VCS: https://github.com/FedericoBruzzone/tgt

Requires: tdlib-devel

# Source-url: https://github.com/FedericoBruzzone/tgt/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: libssl-devel
BuildRequires: rust-cargo
BuildRequires: tdlib-devel

%description
TUI for Telegram written in Rust.

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build --no-default-features

%install
%rust_install -- tgt

%files
%doc README.md CHANGELOG.md
%_bindir/tgt

%changelog
* Fri Feb 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux
