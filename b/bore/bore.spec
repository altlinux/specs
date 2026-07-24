%define _unpackaged_files_terminate_build 1

Name: bore
Version: 0.6.0
Release: alt1

Summary: bore is a simple CLI tool for making tunnels to localhost
License: MIT
Group: Networking/Remote access
Url: https://github.com/ekzhang/bore
Vcs: https://github.com/ekzhang/bore

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust

%description
A modern, simple TCP tunnel in Rust that exposes local ports to a remote server,
bypassing standard NAT connection firewalls.

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
%doc README.md
%_bindir/bore

%changelog
* Fri Jul 24 2026 Pavel Petrykin <silverducks@altlinux.org> 0.6.0-alt1
- Initial build for Alt Linux.
