Name: hyprdim
Version: 3.0.1
Release: alt1
License: GPL-3.0

Summary: Automatically dim windows in Hyprland when switching between them

Group: Graphical desktop/Other

Url: https://github.com/donovanglover/hyprdim

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1

mkdir -p .cargo
cat <<EOF >> .cargo/config.toml
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
%_bindir/%name

%changelog
* Thu Feb 13 2025 Kirill Unitsaev <fiersik@altlinux.org> 3.0.1-alt1
- new version (3.0.1) with rpmgs script
- drop min-version.patch

* Sun Dec 08 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.0.0-alt1
- Initial build
