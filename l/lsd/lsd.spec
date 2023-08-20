%define cargo_prep %nil
%define cargo_build %rust_build
%define cargo_install %rust_install
%define cargo_test %rust_test

Name:           lsd
Version:        0.23.1
Release:        alt1

Summary:        Ls command with a lot of pretty colors and some other stuff

License:        Apache-2.0
Group: File tools
URL:            https://crates.io/crates/lsd

# Source-url: https://github.com/lsd-rs/lsd/archive/refs/tags/%version.tar.gz
Source:         %name-%version.tar

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
* Sun Aug 20 2023 Vitaly Lipatov <lav@altlinux.ru> 0.23.1-alt1
- initial build for ALT Sisyphus

