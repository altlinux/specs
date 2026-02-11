%define _unpackaged_files_terminate_build 1

Name: rustscan
Version: 2.4.1
Release: alt1

Summary: The Modern Port Scanner
License: GPL-3.0-or-later
Group: Other
Url: https://github.com/RustScan/RustScan
Vcs: https://github.com/RustScan/RustScan

Source: %name-%version.tar
Source1: vendor.tar

Patch: rustscan-2.4.1-alt-ignore-hosts-tests.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
%{?!_without_check:%{?!_disable_check:BuildRequires: python3}}

%description
The Modern Port Scanner. Find ports quickly (3 seconds at its fastest).
Run scripts through our scripting engine (Python, Lua, Shell supported).

%prep
%setup -a 1
%autopatch -p1
mkdir -p .cargo
cat >> .cargo/config.toml << '_EOF_'
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
_EOF_

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.md LICENSE
%_bindir/rustscan

%changelog
* Tue Feb 10 2026 Evgeny Shesteperov <alimektor@altlinux.org> 2.4.1-alt1
- Initial build for Sisyphus.
