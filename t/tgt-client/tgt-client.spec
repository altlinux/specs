%define _unpackaged_files_terminate_build 1
%define tdlib_ver 1.8.29
%define tdlib_installdir target/tdlib

Name: tgt-client
Version: 1.0.0
Release: alt3.gd1a0595

Summary: A simple TUI for Telegram
License: Apache-2.0 and MIT
Group: Networking/Instant messaging
Url: https://github.com/FedericoBruzzone/tgt
VCS: https://github.com/FedericoBruzzone/tgt

# Source-url: https://github.com/FedericoBruzzone/tgt/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rust-cargo
BuildRequires: cargo-vendor-checksum
BuildRequires: chafa-devel
BuildRequires: libalsa-devel
BuildRequires: libopus-devel
BuildRequires: tdlib-devel

%description
TUI for Telegram written in Rust.

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%ifarch %ix86
sed -i 's;\(lto =\).*;\1 "thin";' Cargo.toml
%endif

%build
%rust_build --no-default-features -F pkg-config,chafa-dyn,rodio,voice-message

%install
%rust_install -- tgt

%files
%doc README.md CHANGELOG.md
%_bindir/tgt

%changelog
* Mon Nov 23 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt3.gd1a0595
- update
- build with system TDLib (closes: 58115)

* Tue Mar 03 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt2
- fix a crash during authorization (closes: 58018)

* Fri Feb 06 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.0.0-alt1
- initial build for ALT Linux
