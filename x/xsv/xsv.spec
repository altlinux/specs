Name:    xsv
Version: 0.13.0
Release: alt1

Summary: A fast CSV command line toolkit written in Rust
License: MIT
Group:   Other
Url:     https://github.com/BurntSushi/xsv

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source:   %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
xsv is a command line program for indexing, slicing, analyzing, splitting and
joining CSV files. Commands should be simple, fast and composable:
1. Simple tasks should be easy.
2. Performance trade offs should be exposed in the CLI interface.
3. Composition should not come at the expense of performance.

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
%rust_install

%check
%rust_test

%files
%_bindir/*
%doc *.md

%changelog
* Sun Sep 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus
