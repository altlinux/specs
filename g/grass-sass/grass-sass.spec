%define oname grass

Name: grass-sass
Version: 0.13.4
Release: alt1
Summary: Sass compiler written purely in Rust
License: MIT
Group: Text tools
Url: https://github.com/connorskees/grass
Source: https://github.com/connorskees/grass/archive/refs/tags/0.13.4.tar.gz#/%oname-%version.tar.gz
Source1: vendor.tar
ExcludeArch: i586 armh

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

BuildRequires: /proc

%description
This crate aims to provide a high level interface for compiling Sass into plain
CSS. It offers a very limited API, currently exposing only 2 functions.

In addition to a library, this crate also includes a binary that is intended to
act as an invisible replacement to the Sass commandline executable.

This crate aims to achieve complete feature parity with the dart-sass reference
implementation. A deviation from the dart-sass implementation can be considered
a bug except for in the case of error messages and error spans.

%prep
%setup -n%oname-%version
tar xf %SOURCE1

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
%rust_install %oname
%find_lang --with-gnome %name

%check
%rust_test

%files -f %name.lang
%doc *.md LICENSE
%_bindir/*

%changelog
* Sun Mar 16 2025 Ildar Mulyukov <ildar@altlinux.ru> 0.13.4-alt1
- Initial build for Sisyphus
