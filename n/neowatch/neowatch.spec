Name: neowatch
Version: 0.2.1
Release: alt1
Summary: A modern alternative to watch command
License: LGPL-2.1
Group: Monitoring
Url: https://github.com/kilpkonn/neowatch
Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
%summary.

%prep
%setup -a 1
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

%files
%_bindir/%name

%changelog
* Sun Dec 24 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.2.1-alt1
- Initial build for ALT.

