%define _unpackaged_files_terminate_build 1

Name: oxker
Version: 0.12.0
Release: alt1

Summary: A simple tui to view and control docker containers
License: MIT
Group: System/Configuration/Other
Url: https://github.com/mrjackwills/oxker
VCS: https://github.com/mrjackwills/oxker

# Source-url: https://github.com/mrjackwills/%name/archive/refs/tags/v%version.tar.gz
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
* Tue Feb 17 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.12.0-alt1
- initial build for ALT Linux
