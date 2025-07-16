Name: neowatch
Version: 0.3.0
Release: alt1
Summary: A modern alternative to watch command
License: LGPL-2.1
Group: Monitoring
Url: https://crates.io/crates/neowatch
VCS: https://github.com/kilpkonn/neowatch

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
%summary.

%prep
%setup -a 1
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

%files
%_bindir/%name
%doc LICENSE

%changelog
* Wed Jul 16 2025 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.0-alt1
- Updated to version 0.3.0.

* Sun Dec 24 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.1-alt1
- Initial build for ALT.

