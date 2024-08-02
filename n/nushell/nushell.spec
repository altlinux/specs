%define bin_name nu
%def_with check

Name: nushell
Version: 0.96.1
Release: alt1

Summary: A new type of shell
License: MIT
Group: Terminals
Url: www.nushell.sh/
Vcs: https://github.com/nushell/nushell.git
Source: %name-%version.tar
Source1: vendor.tar
# Not supported by upstream
ExcludeArch: %ix86

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: openssl-devel

%description
Nushell (or Nu for short) is a new type of shell that supports structured and typed data.

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
%rust_install %bin_name

#according to the upstream documentation
%check
cargo test --workspace

%files
%_bindir/%bin_name
%doc README.md CONTRIBUTING.md CODE_OF_CONDUCT.md

%changelog
* Wed Jul 31 2024 Elena Dyatlenko <lenka@altlinux.org> 0.96.1-alt1
- Updated to upstream version 0.96.1

* Mon Jul 08 2024 Elena Dyatlenko <lenka@altlinux.org> 0.95.0-alt1
- Initial build for Sisyphus

