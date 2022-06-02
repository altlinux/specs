Name: ouch
Version: 0.3.1
Release: alt1
Summary: Painless compression and decompression for your terminal
License: MIT
Group: Archiving/Compression
Url: https://github.com/ouch-org/ouch
Source: %name-%version.tar

BuildRequires: rust-cargo
BuildRequires: /proc

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
install -D -m755 target/release/%name %buildroot%_bindir/%name

%files
%_bindir/%name
%doc LICENSE README.md

%changelog
* Thu Jun 02 2022 Alexander Makeenkov <amakeenk@altlinux.org> 0.3.1-alt1
- Initial build for ALT
