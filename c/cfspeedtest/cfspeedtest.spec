Name: cfspeedtest
Version: 2.2.2
Release: alt1

Summary: CLI for Cloudflare speed test

License: MIT
Group: Networking/Other
Url: https://github.com/code-inflation/cfspeedtest

# Source-url: https://github.com/code-inflation/cfspeedtest.git
Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust

%description
An unofficial CLI for speed.cloudflare.com. Measures internet speed
by conducting download and upload tests with various payload sizes.
Supports CSV and JSON output, IPv4/IPv6, verbose boxplots.

%prep
%setup
tar -xf %{SOURCE1} -C .
mkdir -p .cargo
cat >> .cargo/config <<'EOF'
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
%doc README.md LICENSE.txt
%_bindir/cfspeedtest

%changelog
* Mon Apr 06 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.2-alt1
- new version 2.2.2

* Sun Mar 08 2026 Vitaly Lipatov <lav@altlinux.ru> 2.2.0-alt1
- new version 2.2.0

* Fri Feb 14 2026 Vitaly Lipatov <lav@altlinux.ru> 2.1.0-alt1
- initial build for ALT Sisyphus
