Name: maturin
Version: 0.12.11
Release: alt1

Summary: Build and publish rust crates as python packages

License: MIT or Apache v2.0
Group: Development/Python3
Url: https://github.com/PyO3/maturin

# Source-url: https://github.com/PyO3/maturin/archive/v%version/%name-%version.tar.gz
Source: %name-%version.tar

# auto predownloaded node modules during update version with rpmgs from etersoft-build-utils
# ask me about description using: lav@etersoft.ru
Source1: %name-development-%version.tar

# error: failed to run custom build command for `ring v0.16.20`
ExcludeArch: ppc64le

BuildRequires: rust-cargo
BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-macros-rust
BuildRequires: rust /proc
BuildRequires: rpm-build-rust

# https://bugzilla.altlinux.org/40901
Requires: /proc
Requires: rust-cargo

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep
%setup -a1

mkdir -p .cargo
cat >.cargo/config <<EOF
[source.crates-io]
registry = 'https://github.com/rust-lang/crates.io-index'
replace-with = 'vendored-sources'

[source.vendored-sources]
directory = 'vendor'
EOF


%build
%rust_build

%install
%rust_install

%files

%doc Changelog.md Readme.md
%attr(755,root,root) %_bindir/maturin

%changelog
* Sun Apr 03 2022 Vitaly Lipatov <lav@altlinux.ru> 0.12.11-alt1
- new version 0.12.11 (with rpmrb script)

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.11.3-alt1
- new version 0.11.3 (with rpmrb script)
- add requires: rust-cargo, rust

* Mon Sep 13 2021 Vitaly Lipatov <lav@altlinux.ru> 0.10.3-alt1
- initial build for ALT Sisyphus

* Wed Apr 14 2021 PLD Linux Team <feedback@pld-linux.org>
- For complete changelog see: http://git.pld-linux.org/?p=packages/maturin.git;a=log;h=master

* Wed Apr 14 2021 Jan Palus <atler@pld-linux.org> 531002c
- new

