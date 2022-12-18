Name: ouch
Version: 0.4.0
Release: alt1
Summary: Painless compression and decompression for your terminal
License: MIT
Group: Archiving/Compression
Url: https://github.com/ouch-org/ouch
Source: %name-%version.tar

BuildRequires: rust-cargo

%description
ouch stands for Obvious Unified Compression Helper and is a CLI tool
to help you compress and decompress files of several formats.

%prep
%setup
mkdir -p .cargo
cat >> .cargo/config <<EOF
[source.crates-io]
replace-with = "vendored-sources"

[source.vendored-sources]
directory = "vendor"
EOF

%build
cargo build --offline --release

%check
cargo test

%install
cargo install --path . --root %buildroot/%_usr

%files
%_bindir/%name
%doc README.md

%changelog
* Sat Dec 17 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.4.0-alt1
- Updated to version 0.4.0

* Thu Jun 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT
