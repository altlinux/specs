%define _unpackaged_files_terminate_build 1

Name: procs
Version: 0.14.6
Release: alt1

Summary: A replacement for ps written in Rust
License: MIT
Group: Monitoring
Url: https://crates.io/crates/procs
Vcs: https://github.com/dalance/procs

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml
BuildRequires(pre): rpm-build-rust
BuildRequires: rust
BuildRequires: rust-cargo
BuildRequires: /proc

%description
%summary.

%prep
%setup -a 1

install -Dm 644 %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc README.md CHANGELOG.md

%changelog
* Tue Oct 01 2024 Vladislav Glinkin <smasher@altlinux.org> 0.14.6-alt1
- Update to 0.14.6

* Sun Mar 24 2024 Vladislav Glinkin <smasher@altlinux.org> 0.14.5-alt1
- Update to 0.14.5

* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.3-alt1
- Updated to 0.14.3

* Mon Sep 04 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.0-alt1
- Initial build for ALT

