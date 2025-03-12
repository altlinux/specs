Name: mdbook-linkcheck
Version: 0.7.7
Release: alt1

Summary: A mdbook backend which will check all links in a document are valid

License: MIT
Group: Development/Documentation
Url: https://github.com/Michael-F-Bryan/mdbook-linkcheck

# Source-url: https://github.com/Michael-F-Bryan/mdbook-linkcheck/archive/refs/tags/v%version.tar.gz
Source: %name-%version.tar

Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust perl-Pod-Usage

Requires: mdbook

%description
%summary

%prep
%setup -a1

cat >.cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"
[source.vendored-sources]
directory = "vendor"
EOF

%build
%rust_build

%install
install -Dm 755 target/release/mdbook-linkcheck -t %buildroot%_bindir

%files
%_bindir/mdbook-linkcheck
%doc LICENSE README.md

%changelog
* Sun Mar 09 2025 Boris Yumankulov <boria138@altlinux.org> 0.7.7-alt1
- initial build for ALT Sisyphus



