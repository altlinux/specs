%define soversion 0
%define upstream gtk4-layer-shell

%def_enable introspection
%def_enable vala
%def_enable gtk_doc

Name: libgtk4-layer-shell
Version: 1.0.2
Release: alt1
License: MIT

Summary: Library to create components for Wayland using the Layer Shell and GTK4

Group: System/Libraries

Url: https://github.com/wmww/gtk4-layer-shell

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
%{?_enable_vala:BuildRequires(pre): rpm-build-vala vala-tools}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir gobject-introspection-devel}

BuildRequires: cmake meson libgtk4-devel libgtk4-gir-devel
BuildRequires: wayland-devel wayland-protocols libwayland-client-devel

%{?_enable_gtk_doc:BuildRequires: gi-docgen gtk-doc}

%description
A library for using the Layer Shell Wayland protocol with GTK4. With this library
you can build desktop shell components such as panels, notifications and wallpapers.
You can use it to anchor your windows to a corner or edge of the output,or stretch
them across the entire output.

This Library is compatible with C, C++ and any language that supports GObject
introspection files (Python, Vala, etc).

%package -n %name%soversion
Summary: GTK4 Layer Shell library
Group: System/Libraries

%description -n %name%soversion
%summary.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name%soversion = %EVR

%description gir
GObject introspection data for the %name library.

%package -n %name-devel
Summary: Development files for %name
Group: Development/Other
Requires: %name%soversion = %EVR

%description -n %name-devel
This package provides development files for %name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-devel < %EVR

%description devel-doc
The %name-devel-doc package contains documentation for
developing applications that use %name.

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library

%package vala
Summary: Vala language bindings for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR

%description vala
This package provides Vala language bindings for the %name library.

%prep
%setup

%build
%meson \
    -Ddocs=true \
    -Dintrospection=true \
    -Dvapi=true
%meson_build -v

%install
%meson_install

%files -n %name%soversion
%doc README.md
%_libdir/%name.so.%soversion
%_libdir/%name.so.*

%files -n %name-devel
%_includedir/%upstream/
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%upstream/
%endif

%if_enabled introspection
%files -n %name-gir
%_libdir/girepository-1.0/Gtk4LayerShell-*.typelib

%files -n %name-gir-devel
%_datadir/gir-1.0/Gtk4LayerShell-*.gir
%endif

%if_enabled vala
%files -n %name-vala
%_vapidir/%upstream-0.deps
%_vapidir/%upstream-0.vapi
%endif

%changelog
* Sun Jul 21 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.0.2-alt1
- Initial build
