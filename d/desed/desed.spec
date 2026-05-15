%define _unpackaged_files_terminate_build 1

Name: desed
Version: 1.2.2
Release: alt1

Summary: Debugger for Sed
License: GPL-3.0-or-later
Group: Development/Other
Url: https://github.com/SoptikHa2/desed
VCS: https://github.com/SoptikHa2/desed

# Source-url: https://github.com/SoptikHa2/%name/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar
Source1: vendor-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: cargo-vendor-checksum
BuildRequires: rust-cargo

%description
Demystify and debug your sed scripts, from comfort of your terminal.

%prep
%setup -a1
%rust_prep
cargo-vendor-checksum --vendor vendor --all

%build
%rust_build

%install
%rust_install
install -Dpm 644 %name.1 %buildroot%_man1dir/%name.1

%files
%doc README.md
%_bindir/%name
%_man1dir/%name.1.xz

%changelog
* Fri May 15 2026 Dmitrii Fomchenkov <sirius@altlinux.org> 1.2.2-alt1
- initial build for ALT Linux
