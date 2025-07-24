%global _unpackaged_files_terminate_build 1

Name: matugen
Version: 2.4.1
Release: alt1
Summary: A material you color generation tool 
License: GPL-2.0
Group: Other
Url: https://crates.io/crates/matugen
VCS: https://github.com/InioX/matugen

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
A material you color generation tool with templates.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF

[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"

[profile.release]
debug = true
strip = false
EOF

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name
%doc LICENSE

%changelog
* Thu Jul 24 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.4.1-alt1
- Initial build for ALT.
