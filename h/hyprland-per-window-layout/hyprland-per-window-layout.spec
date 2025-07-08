Name: hyprland-per-window-layout
Version: 2.13
Release: alt1
Summary: Hyprland per window layout
License: MIT
Group: Graphical desktop/Other
Url: https://aur.archlinux.org/packages/hyprland-per-window-layout

Source: %name-%version.tar
Source1: vendor.tar

BuildRequires(pre): rpm-build-rust
BuildRequires: rust-cargo

%description
Per window keyboard layout (language) for Hyprland wayland compositor.

%prep
%setup -a 1
mkdir -p .cargo
cat >> .cargo/config.toml <<EOF
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
%doc LICENSE

%changelog
* Mon Jul 07 2025 Alexander Makeenkov <amakeenk@altlinux.org> 2.13-alt1
- Initial build for ALT.
