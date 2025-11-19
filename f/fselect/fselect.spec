%def_without check
# Check passed with 0 fails
# test result:
# ok.
# 203 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.01s

Name:    fselect
Version: 0.9.1
Release: alt1

Summary: Find files with SQL-like queries
License: Apache-2.0 and MIT
Group:   File tools
Url:     https://fselect.rocks
Vcs:     https://github.com/jhspetersson/fselect.git

Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
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
install -d %buildroot%_man1dir
install -Dm 0644 docs/%name.1 %buildroot%_man1dir

%check
%rust_test --workspace

%files
%doc *.md LICENSE-*
%_bindir/*
%_man1dir/%name.1.*

%changelog
* Wed Nov 19 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus.
