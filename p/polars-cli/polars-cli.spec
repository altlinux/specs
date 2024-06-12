Name:    polars-cli
Version: 0.8.0
Release: alt1

Summary: CLI interface for running SQL queries with Polars as backend
License: MIT
Group:   Other
Url:     https://github.com/pola-rs/polars-cli

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

ExcludeArch: %ix86

%description
%summary

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install polars

%check
%rust_test

%files
%doc *.md
%_bindir/*

%changelog
* Wed Jun 05 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.8.0-alt1
- Initial build for Sisyphus
