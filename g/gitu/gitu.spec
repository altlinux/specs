%define _unpackaged_files_terminate_build 1

Name: gitu
Version: 0.35.0
Release: alt2

Summary: A terminal user interface for Git
License: MIT
Group: Development/Tools
Url: https://crates.io/crates/gitu
Vcs: https://github.com/altsem/gitu

Source0: %name-%version.tar
Source1: vendor.tar
Source2: config.toml

Patch1: vendored-nix-loongarch64-support.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: rust
BuildRequires: rust-cargo

%description
%summary. Inspired by Magit, and launched straight from the terminal.

%prep
%setup -a 1
install -D %SOURCE2 .cargo/config.toml

%autopatch -p1

# allow patching vendored rust code
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/nix-0.26.4/.cargo-checksum.json

%build
%rust_build

%install
%rust_install

%files
%doc README.md CHANGELOG.md
%_bindir/%name

%changelog
* Thu Sep 11 2025 Ivan A. Melnikov <iv@altlinux.org> 0.35.0-alt2
- NMU: fix FTBFS on loongarch64

* Mon Sep 08 2025 Vladislav Glinkin <smasher@altlinux.org> 0.35.0-alt1
- 0.34.0 -> 0.35.0

* Tue Aug 19 2025 Vladislav Glinkin <smasher@altlinux.org> 0.34.0-alt1
- 0.29.0 -> 0.34.0

* Tue Mar 11 2025 Vladislav Glinkin <smasher@altlinux.org> 0.29.0-alt1
- 0.26.0 -> 0.29.0

* Wed Oct 30 2024 Vladislav Glinkin <smasher@altlinux.org> 0.26.0-alt1
- Initial build for ALT

