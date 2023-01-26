%def_with check

Name: bottom
Version: 0.8.0
Release: alt1
Summary: Yet another cross-platform graphical process/system monitor
License: MIT
Group: Monitoring
Url: https://clementtsang.github.io/bottom
Vcs: https://github.com/ClementTsang/bottom
Source: %name-%version.tar

BuildRequires: rust-cargo

%description
A customizable cross-platform graphical process/system monitor for the terminal.

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

%check
cargo test

%files
%_bindir/btm

%changelog
* Thu Jan 26 2023 Alexander Makeenkov <amakeenk@altlinux.org> 0.8.0-alt1
- Initial build for ALT

