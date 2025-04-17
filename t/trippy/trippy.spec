%define _unpackaged_files_terminate_build 1
%define bin_name trip

Name: trippy
Version: 0.12.2
Release: alt1
Summary: Interactive network diagnostic tool with route visualization

License: Apache-2.0
Group: Networking/WWW
Url: https://trippy.cli.rs
Vcs: https://github.com/fujiapple852/trippy.git
Source0: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
Trippy is a modern network diagnostic tool that combines the 
functionalities of traceroute and ping. It provides a visual 
representation of packet routes, facilitating the analysis of 
network issues. Trippy supports various protocols and offers 
a user-friendly interface for monitoring network connections.

%prep
%setup -a 1
mkdir -p .cargo
cat > .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
%rust_install -t %_sbindir %bin_name

%check
cargo test

%files
%doc README.md trippy-config-sample.toml
%_sbindir/%bin_name

%changelog
* Fri Apr 11 2025 Aleksandr A. Voyt <sobue@altlinux.org> 0.12.2-alt1
- Initial build
