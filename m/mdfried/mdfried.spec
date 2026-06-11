%def_without check
# test result: ok. 33 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.05s

Name:    mdfried
Version: 0.22.1
Release: alt1

Summary: A markdown viewer for the terminal that renders images and Big Headers
License: GPL-3.0-or-later
Group:   File tools
Url:     https://crates.io/crates/mdfried
Vcs:     https://github.com/benjajaja/mdfried.git

Source0: %name-%version.tar
Source1: vendor.tar

ExcludeArch: %ix86

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc
BuildRequires: pkgconfig(chafa)

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

%check
%rust_test

%files
%doc *.md
%_bindir/%name

%changelog
* Tue Jun 09 2026 Sergey Gvozdetskiy <serjigva@altlinux.org> 0.22.1-alt1
- Initial build for Sisyphus.
