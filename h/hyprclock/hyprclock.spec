Name: hyprclock
Version: 0.1.0
Release: alt1
License: GPL-3.0

Summary: A sleek and customizable clock widget for hyprland

Group: Graphical desktop/Other

Url: https://github.com/cvusmo/hyprclock

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(pango)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(graphene-gobject-1.0)

%description
Hyprclock is a modern, highly customizable clock application
designed for use with the Hyprland window manager on Linux. 
It offers real-time updates, animated effects, and easy theming
options, making it a perfect fit for your Hyprland setup.

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
* Mon Oct 28 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.0-alt1
- Initial build
