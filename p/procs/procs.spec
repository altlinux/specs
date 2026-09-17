%define _unpackaged_files_terminate_build 1

Name: procs
Version: 0.14.12
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
%doc README.md CHANGELOG.md
%_bindir/%name

%changelog
* Thu Sep 17 2026 Vladislav Glinkin <smasher@altlinux.org> 0.14.12-alt1
- New version 0.14.12.
- Removed obsolete nix 0.26.4 loongarch64 patch (fixed upstream in newer nix).

* Wed Apr 01 2026 Vladislav Glinkin <smasher@altlinux.org> 0.14.11-alt1
- New version 0.14.11.

* Mon Aug 11 2025 Ilya Sorochan <k0tran@altlinux.org> 0.14.10-alt1
- New version 0.14.10.

* Tue Dec 03 2024 Ilya Sorochan <k0tran@altlinux.org> 0.14.8-alt2
- Add patch that fixes build for nix crate on loongarch64.

* Wed Oct 30 2024 Vladislav Glinkin <smasher@altlinux.org> 0.14.8-alt1
- New version 0.14.8.

* Tue Oct 01 2024 Vladislav Glinkin <smasher@altlinux.org> 0.14.6-alt1
- New version 0.14.6.

* Sun Mar 24 2024 Vladislav Glinkin <smasher@altlinux.org> 0.14.5-alt1
- New version 0.14.5.

* Sun Nov 05 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.3-alt1
- New version 0.14.3.

* Mon Sep 04 2023 Vladislav Glinkin <smasher@altlinux.org> 0.14.0-alt1
- Initial build for ALT.
