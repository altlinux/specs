%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install
%define cargo_test %rust_test

Name: lsd
Version: 1.0.0
Release: alt2

Summary: Ls command with a lot of pretty colors and some other stuff

License: Apache-2.0
Group: File tools
Url: https://crates.io/crates/lsd

# Source-url: https://github.com/lsd-rs/lsd/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

# Cargo modules for build rust code
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
An ls command with a lot of pretty colors and some other stuff.

%prep
%setup -a1
%cargo_prep
mkdir -p .cargo
cat <<EOF >> .cargo/config
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%cargo_build

%install
%cargo_install

%files
%doc LICENSE
%doc CHANGELOG.md
%doc README.md
%_bindir/lsd

%changelog
* Fri Mar 08 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 1.0.0-alt2
- NMU: fixed FTBFS on LoongArch

* Wed Feb 28 2024 Vitaly Lipatov <lav@altlinux.ru> 1.0.0-alt1
- new version 1.0.0
- cleanup spec, fix source url

* Sun Aug 20 2023 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- initial build for ALT Sisyphus

