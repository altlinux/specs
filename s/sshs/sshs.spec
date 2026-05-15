%define _unpackaged_files_terminate_build 1
%def_with check

Name: sshs
Version: 4.7.2
Release: alt1

Summary: Terminal user interface for SSH
License: MIT
Group: Development/Other
Url: https://github.com/quantumsheep/sshs
VCS: https://github.com/quantumsheep/sshs

Requires: openssh-clients

# Source-url: https://github.com/quantumsheep/%name/archive/refs/tags/%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
%summary

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
* Fri May 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 4.7.2-alt1
- initial build for ALT Linux
