%def_with check

Name: starship
Version: 1.12.0
Release: alt1
Summary: The minimal, blazing-fast, and infinitely customizable prompt for any shell
License: ISC
Group: Shells
Url: https://github.com/starship/starship
Source: %name-%version.tar

BuildRequires: rust-cargo
BuildRequires: cmake

%if_with check
BuildRequires: git
%endif

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

%check
%buildroot%_bindir/%name print-config > %name.toml
export STARSHIP_CONFIG=%name.toml
export TERM=xterm
cargo test

%files
%_bindir/%name

%changelog
* Sun Dec 18 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.12.0-alt1
- Updated to version 1.12.0
- Enabled check

* Sun Nov 20 2022 Alexander Makeenkov <amakeenk@altlinux.org> 1.11.0-alt1
- Initial build for ALT

