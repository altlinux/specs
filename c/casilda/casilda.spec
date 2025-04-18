Name: casilda
Version: 0.2.0
Release: alt1

Summary: Wayland compositor for GTK4
# The entire source is LGPL-2.1-only, except src/casilda.h and
# src/casilda-version.h.in, which are LGPL-2.1-or-later.
# https://gitlab.gnome.org/jpu/casilda/-/merge_requests/3
License: LGPL-2.1-only AND LGPL-2.1-or-later
Group: Development/GNOME and GTK+
Url: https://gitlab.gnome.org/jpu/casilda

Source0: %name-%version.tar
Patch1: soname.patch

BuildRequires:  gcc
BuildRequires:  meson

BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(gtk4)
BuildRequires:  pkgconfig(pixman-1)
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-scanner)
BuildRequires:  pkgconfig(wayland-server)
BuildRequires:  pkgconfig(wlroots-0.18)
BuildRequires:  pkgconfig(x11-xcb)
BuildRequires:  pkgconfig(xkbcommon)
BuildRequires:  pkgconfig(xkbcommon-x11)
BuildRequires:  gobject-introspection-devel
BuildRequires:  libgtk4-gir-devel

%description
A simple Wayland compositor widget for Gtk 4 which can be used to embed other
processes windows in your Gtk 4 application.
It was originally created for Cambalache's workspace using wlroots,
a modular library to create Wayland compositors.
Following Wayland tradition, this library is named after my hometown in
Santa Fe, Argentina.

%package devel
Group: Development/GNOME and GTK+
Summary: Wayland compositor for GTK4
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
Development files for Casilda.

%prep
%setup -n %name-%version
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%check

%files
%doc README.md
%dir %_libdir/girepository-1.0
%_libdir/girepository-1.0/Casilda-0.1.typelib
%_libdir/libcasilda-0.1.so.0.1
%_libdir/libcasilda-0.1.so.0

%files devel
%dir %_includedir/casilda
%_includedir/casilda/*.h
%_libdir/libcasilda-0.1.so
%_libdir/pkgconfig/casilda-0.1.pc
%dir %_datadir/gir-1.0
%_datadir/gir-1.0/Casilda-0.1.gir

%changelog
* Wed Apr 09 2025 Maria Alexeeva <alxvmr@altlinux.org> 0.2.0-alt1
- First build
