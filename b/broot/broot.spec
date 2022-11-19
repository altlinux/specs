Name: broot
Version: 1.16.2
Release: alt1
Summary: A new way to see and navigate directory trees
License: MIT
Group: File tools
Url: https://dystroy.org/broot
Source: %name-%version.tar

BuildRequires: rust-cargo

%description
%summary.

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

%install
cargo install --path . --root %buildroot/%_usr

%files
%_bindir/%name
%doc LICENSE

%changelog
* Sat Nov 19 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.2-alt1
- Updated to version 1.16.2

* Sun Oct 30 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.16.1-alt1
- Initial build for ALT

