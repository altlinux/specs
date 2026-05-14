%define _unpackaged_files_terminate_build 1
%def_without check

Name: oxker
Version: 0.13.2
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
* Thu May 14 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.13.2-alt1
- new version

* Wed Mar 25 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.13.1-alt1
- new version

* Wed Mar 18 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.13.0-alt2
- disable tests

* Mon Mar 02 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.13.0-alt1
- new version

* Tue Feb 17 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 0.12.0-alt1
- initial build for ALT Linux
