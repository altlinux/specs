Name: cursor-clip
Version: 1.0.3
Release: alt1
License: GPL-3.0-only

Summary: GTK4 clipboard manager for Wayland

Group: Graphical desktop/Other

Url: https://github.com/Sirulex/cursor-clip
Vcs: https://github.com/Sirulex/cursor-clip.git

ExcludeArch: %ix86

# Source-url: https://github.com/Sirulex/cursor-clip.git
Source: %name-%version.tar
Source1: %name-development-%version.tar
Source2: config.toml

BuildRequires(pre): rpm-macros-rust
BuildRequires: rpm-build-rust
BuildRequires: /proc

BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: pkgconfig(libadwaita-1) >= 1.5

%description
Cursor Clip is a GTK4 clipboard manager for Wayland compositors. It keeps
clipboard history and displays it in a searchable overlay positioned near
the mouse pointer.

%prep
%setup -a1
install -vD %SOURCE2 .cargo/config.toml

%build
%rust_build

%install
%makeinstall_std PREFIX=%prefix BUILD_DIR=target/release

%files
%doc README.md LICENSE
%_bindir/%name
%_bindir/%name-toggle
%_desktopdir/io.github.sirulex.cursor-clip.desktop
%_iconsdir/hicolor/scalable/apps/io.github.sirulex.cursor-clip.svg

%changelog
* Thu Oct 15 2026 Kirill Unitsaev <fiersik@altlinux.org> 1.0.3-alt1
- Initial build

