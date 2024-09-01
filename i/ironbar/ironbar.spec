Name: ironbar
Version: 0.16.0
Release: alt1
License: MIT

Summary: Customisable Wayland gtk bar

Group: Graphical desktop/Other

Url: https://github.com/JakeStanger/ironbar

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(dbus-1)
BuildRequires: pkgconfig(openssl)
BuildRequires: pkgconfig(luajit)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(atk)
BuildRequires: pkgconfig(gdk-3.0)
BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(libpulse)

%description
A customisable and feature-rich GTK bar for wlroots 
compositors, written in Rust. Ironbar is designed to support 
anything from a lightweight bar to a full desktop panel with ease.

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
* Sun Sep 01 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.16.0-alt1
- Initial build
