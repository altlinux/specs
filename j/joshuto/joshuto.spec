Name:    joshuto
Version: 0.9.8
Release: alt1

Summary: ranger-like terminal file manager written in Rust
License: LGPL-3.0
Group:   Other
Url:     https://github.com/kamiyaa/joshuto

Packager: Mikhail Gordeev <obirvalger@altlinux.org>

Source: %name-%version.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: /proc

%description
%summary

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
%rust_test

%files
%doc *.md
%doc docs
%doc config
%_bindir/*

%changelog
* Wed Jun 05 2024 Mikhail Gordeev <obirvalger@altlinux.org> 0.9.8-alt1
- Initial build for Sisyphus
