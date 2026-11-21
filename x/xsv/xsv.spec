Name:    xsv
Version: 0.13.0
Release: alt3

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
export __CARGO_TEMPORARY_BUILD_DIR_NEW_LAYOUT_OPT_OUT=1
%rust_test

%files
%_bindir/*
%doc *.md

%changelog
* Sat Nov 21 2026 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt3
- Fix FTBFS with cargo 1.100.0

* Tue Jan 16 2024 Alexey Sheplyakov <asheplyakov@altlinux.org> 0.13.0-alt2
- NMU: fixed FTBFS on LoongArch (updated libc crate).

* Sun Sep 12 2021 Mikhail Gordeev <obirvalger@altlinux.org> 0.13.0-alt1
- Initial build for Sisyphus
