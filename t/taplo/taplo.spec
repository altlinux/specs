%define _unpackaged_files_terminate_build 1

Name: taplo
Version: 0.9.3
Release: alt2

Summary: A TOML toolkit written in Rust
License: MIT
Group: File tools
Url: https://taplo.tamasfe.dev
Vcs: https://github.com/tamasfe/taplo

Source0: %name-%version.tar
Source1: vendor.tar

Patch0: taplo-0.9.3-alt-pprof-loongarch64.patch

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo
BuildRequires: /proc

ExcludeArch: i586 ppc64le

%description
Taplo CLI aims to be an one stop shop tool for working with TOML files
via the command line. The features include validation, formatting, and
querying TOML documents with a jq-like fashion.

%prep
%setup -a1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF
%patch0 -p2
sed -i -e 's/"files":{[^}]*}/"files":{}/' \
     ./vendor/pprof/.cargo-checksum.json

%build
%rust_build

%install
%rust_install

%check
%rust_test

%files
%doc LICENSE.md README.md
%_bindir/%name

%changelog
* Fri Nov 22 2024 Ilya Sorochan <k0tran@altlinux.org> 0.9.3-alt2
- Add patch for pprof crate to add support loongarch64.

* Wed Nov 20 2024 Michael Chernigin <chernigin@altlinux.org> 0.9.3-alt1
- Initial build for ALT Linux.

