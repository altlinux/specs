%define _unpackaged_files_terminate_build 1

Name: procs
Version: 0.14.3
Release: alt1

Summary: procs is a replacement for ps written in Rust
License: MIT
Group: Monitoring
Url: https://crates.io/crates/procs
Vcs: https://github.com/dalance/procs

Source0: %name-%version.tar
Source1: vendor.tar
Source2: .cargo/config.toml
BuildRequires(pre): rpm-build-rust
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc

%description
procs is a replacement for ps written in Rust

%prep
%setup -a 1

install -D %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc README.md LICENSE

%changelog
* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.3-alt1
- Updated to 0.14.3

* Mon Sep 04 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.0-alt1
- Initial build for ALT

