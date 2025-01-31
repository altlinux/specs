Name: eww
Version: 0.6.0
Release: alt2
License: MIT

Summary: ElKowars wacky widgets

Group: Graphical desktop/Other

Url: https://github.com/elkowar/eww?tab=readme-ov-file

Source: %name-%version.tar
Source1: %name-development-%version.tar

Patch0: lockfile.patch

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: libdbusmenu-gtk3-devel
BuildRequires: libgtk-layer-shell-devel
BuildRequires: libgtk+3-devel

%description
Elkowars Wacky Widgets is a standalone widget system 
made in Rust that allows you to implement your own, 
custom widgets in any window manager.

%prep
%setup -a1
%patch0 -p1

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
%doc README.md LICENSE CHANGELOG.md examples/eww-bar
%_bindir/%name

%changelog
* Thu Jan 23 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.6.0-alt2
- drop manual dependencies
- move examples/eww-bar to doc

* Tue Sep 24 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.6.0-alt1
- Initial build
