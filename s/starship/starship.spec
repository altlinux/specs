Name: starship
Version: 1.11.0
Release: alt1
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell
License: ISC
Group: Shells
Url: https://github.com/starship/starship
Source: %name-%version.tar

BuildRequires: rust-cargo
BuildRequires: cmake

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
* Sun Nov 20 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.0-alt1
- Initial build for ALT

