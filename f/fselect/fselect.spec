%def_without check
# Check passed with 0 fails
# test result:
# ok.
# 625 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.02s

Name:    fselect
Version: 0.10.0
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
* Thu May 07 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.10.0-alt1
- New version.

* Wed Mar 04 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.3-alt1
- New version.

* Thu Dec 11 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.2-alt1
- New version.

* Wed Nov 19 2025 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.9.1-alt1
- Initial build for Sisyphus.
