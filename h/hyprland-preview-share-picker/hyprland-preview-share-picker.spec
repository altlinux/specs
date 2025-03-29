Name: hyprland-preview-share-picker
Version: 0.2.0
Release: alt1
License: MIT

Summary: An alternative share picker for hyprland

Group: Graphical desktop/Other

Url: https://github.com/WhySoBad/hyprland-preview-share-picker
Vcs: https://github.com/WhySoBad/hyprland-preview-share-picker.git

Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: %name-postsubmodules-%version.tar
Source3: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(graphene-gobject-1.0)
BuildRequires: pkgconfig(gdk-pixbuf-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)

BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(pango)

BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(gtk4)

%description
An alternative share picker for hyprland with
window and monitor previews written in rust

%prep
%setup -a1 -a2
install -vD %SOURCE3 .cargo/config.toml

%build
%rust_build

%install
%rust_install

%files
%_bindir/%name

%changelog
* Sat Mar 29 2025 Kirill Unitsaev <fiersik@altlinux.org> 0.2.0-alt1
- Initial build
