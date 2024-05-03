%define oname gtk-session-lock

Name: lib%oname
Version: 0.2.0
Release: alt1.git.4.gb9ddb27
Summary: Library to use GTK 3 to build Wayland screen lockers using the secure ext-session-lock-v1
License: GPL3
Group: System/Libraries
Url: https://github.com/Cu3PO42/gtk-session-lock/

Source: https://github.com/Cu3PO42/gtk-session-lock/archive/refs/tags/v%version.tar.gz#/%oname-%version.tar
Source44: %oname.watch

# Automatically added by buildreq on Tue Apr 30 2024
# optimized out: at-spi2-atk bashrc dconf glib-networking glib2-devel glibc-kernheaders-generic glibc-kernheaders-x86 gobject-introspection-devel libat-spi2-core libatk-devel libatk-gir-devel libcairo-devel libcairo-gobject libcairo-gobject-devel libgdk-pixbuf libgdk-pixbuf-devel libgdk-pixbuf-gir-devel libgio-devel libgpg-error libgtk+3-devel libharfbuzz-devel libharfbuzz-gir-devel libpango-devel libpango-gir-devel libwayland-client libwayland-client-devel libwayland-cursor libwayland-egl ninja-build pkg-config python3 python3-base python3-dev python3-module-pkg_resources sh5 vala wayland-devel xz zlib-devel
BuildRequires: libgirepository1.0-devel libgtk+3-gir-devel meson python3-module-setuptools vala-tools wayland-protocols

%description
This is a library to use [GTK 3](https://www.gtk.org/) to build screen lockers
using the secure [ext-session-lock-v1](https://wayland.app/protocols/ext-session-lock-v1)
protocol. This Library is compatible with C, C++ and any language that supports
GObject introspection files (Python, Vala, etc, see using the library below).

This library is a fork of the incredible [gtk-layer-shell](https://github.com/wmww/gtk-layer-shell),
which has laid all the groundwork necessary to make this happen.

%package devel
Summary: Development files for %oname
Group: Development/C

%description devel
Development files for %oname

%prep
%setup -n %oname-%version

%build
%meson
%meson_build

%install
%meson_install

%files
%doc CHANGELOG* LICENSE* README* compatibility.md
%_libdir/*.so.*
%_libdir/girepository-1.0/*.typelib

%files devel
%_includedir/%oname
%_libdir/*.so
%_pkgconfigdir/*.pc
%_vapidir/%oname-0.deps
%_vapidir/%oname-0.vapi
%_datadir/gir-1.0/*.gir

%changelog
* Tue Apr 30 2024 Ildar Mulyukov <ildar@altlinux.ru> 0.2.0-alt1.git.4.gb9ddb27
- initial build for Sisyphus
