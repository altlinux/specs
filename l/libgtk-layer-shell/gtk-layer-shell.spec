%define rname gtk-layer-shell

Name: lib%rname
Version: 0.6.0
Release: alt1
Summary: Library to create components for Wayland using the Layer Shell
License: MIT
Group: System/Libraries
Url: https://github.com/wmww/gtk-layer-shell
Packager: Valery Inozemtsev <shrek@altlinux.ru>

Source: %rname-%version.tar
Patch: %rname-%version-%release.patch

BuildRequires: cmake meson gobject-introspection-devel libgtk+3-devel libgtk+3-gir-devel wayland-devel wayland-protocols libwayland-client-devel

%description
A library to write GTK applications that use Layer Shell. Layer Shell is a
Wayland protocol for desktop shell components, such as panels, notifications
and wallpapers. You can use it to anchor your windows to a corner or edge of
the output, or stretch them across the entire output. This library only makes
sense on Wayland compositors that support Layer Shell, and will not work on
X11. It supports all Layer Shell features including popups and popovers
(GTK popups Just Work). Please open issues for any bugs you come across.

%package devel
Summary: Development files for %rname
Group: Development/C

%description devel
Development files for %rname

%prep
%setup -q -n %rname-%version
%patch -p1

%build
%meson
%meson_build -v

%install
%meson_install

%files
%doc README.md
%_libdir/*.so.*
%_libdir/girepository-1.0/GtkLayerShell-*.typelib

%files devel
%_includedir/%rname
%_libdir/*.so
%_pkgconfigdir/*.pc
%_datadir/gir-1.0/GtkLayerShell-*.gir

%changelog
* Fri Aug 06 2021 Valery Inozemtsev <shrek@altlinux.ru> 0.6.0-alt1
- 0.6.0

* Fri Aug 14 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.3.0-alt1
- 0.3.0

* Wed Mar 04 2020 Valery Inozemtsev <shrek@altlinux.ru> 0.1.0-alt1
- initial release

