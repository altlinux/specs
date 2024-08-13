Name: nwg-dock-hyprland
Version: 0.2.1
Release: alt1
License: MIT

Summary: GTK3-based dock for Hyprland

Group: Graphical desktop/Other

Url: https://github.com/nwg-piotr/nwg-dock-hyprland

Source: %name-%version.tar
Source1: %name-development-%version.tar

BuildRequires(pre): rpm-macros-golang

BuildRequires: golang
BuildRequires: rpm-build-golang

BuildRequires: pkgconfig(gtk-layer-shell-0)
BuildRequires: pkgconfig(cairo-gobject)
BuildRequires: pkgconfig(cairo)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gdk-3.0)

Requires: libgtk-layer-shell libgtk+3

%description
Configurable (w/ command line arguments and css) dock, written in Go,
aimed exclusively at the Hyprland Wayland compositor.
It features pinned buttons, client buttons and the launcher button.

%prep
%setup -a1

%build
export GOROOT="%_libexecdir/golang"
%gobuild -mod=vendor

%install
install -Dpm755 %name %buildroot%_bindir/%name

mkdir -p %buildroot%_datadir/%name
cp config/* %buildroot%_datadir/%name

%files
%_bindir/%name
%_datadir/%name/

%changelog
* Mon Aug 12 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.2.1-alt1
- new version (0.2.1)

* Fri Jul 26 2024 Kirill Unitsaev <fiersik@altlinux.org> 0.1.9-alt1
- Initial build
