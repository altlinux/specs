Name: hyprdim
Version: 3.0.0
Release: alt1
License: GPL-3.0

Summary: Automatically dim windows in Hyprland when switching between them

Group: Graphical desktop/Other

Url: https://github.com/donovanglover/hyprdim

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch1: min-version.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

%description
%summary.

%prep
%setup -a1
%patch1 -p1

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
* Sun Dec 08 2024 Kirill Unitsaev <fiersik@altlinux.org> 3.0.0-alt1
- Initial build
