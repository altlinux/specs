Name:    numbat
Version: 1.24.0
Release: alt1

Summary: A statically typed programming language for scientific computations with first class support for physical dimensions and units
License: Apache-2.0
Group:   Sciences/Mathematics
Url:     https://github.com/sharkdp/numbat

Source: %name-%version.tar

Patch1: numbat-1.24.0-alt-currency-url.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup
%patch1 -p1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc *.md book
%_bindir/*

%changelog
* Fri Oct 30 2026 Mikhail Gordeev <obirvalger@altlinux.org> 1.24.0-alt1
- Initial build for Sisyphus
