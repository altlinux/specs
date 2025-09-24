Name: countryfetch
Version: 0.2.0
Release: alt1

Summary: A Command-line tool similar to Neofetch for obtaining information about your country
License: MIT
Group: Other
Url: https://github.com/nik-rev/countryfetch
Vcs: https://github.com/nik-rev/countryfetch.git

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: libssl-devel
BuildRequires: /proc

%description
Countryfetch is a neofetch-like tool for fetching information about your country.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

#use the system-provided openssl
sed -i 's/openssl = { version = "0.10", features = \["vendored"\] }//' Cargo.toml

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc README.* LICENSE-MIT
%_bindir/%name

%changelog
* Wed Sep 24 2025 Anton Kurachenko <srebrov@altlinux.org> 0.2.0-alt1
- Initial build for ALT.
