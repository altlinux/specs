%define soversion 0

%def_enable introspection
%def_enable vala
%def_enable gtk_doc
%def_enable examples

Name: gtk4-layer-shell
Version: 1.1.1
Release: alt1
License: MIT

Summary: Library to create components for Wayland using the Layer Shell and GTK4

Group: System/Libraries

Url: https://github.com/wmww/gtk4-layer-shell

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: cmake meson

%{?_enable_gtk_doc:BuildRequires: gi-docgen gtk-doc}
%{?_enable_vala:BuildRequires(pre): rpm-build-vala vala-tools}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir gobject-introspection-devel}

BuildRequires: gir(Gtk)
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(wayland-server)

BuildRequires: pkgconfig(wayland-server)
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(wayland-scanner)
BuildRequires: pkgconfig(wayland-protocols)

%description
A library for using the Layer Shell Wayland protocol with GTK4. With this library
you can build desktop shell components such as panels, notifications and wallpapers.
You can use it to anchor your windows to a corner or edge of the output,or stretch
them across the entire output.

This Library is compatible with C, C++ and any language that supports GObject
introspection files (Python, Vala, etc).

%package -n lib%name%soversion
Summary: GTK4 Layer Shell library
Group: System/Libraries

%description -n lib%name%soversion
%summary.

%package -n lib%name-devel
Summary: Development files for %name
Group: Development/Other
Requires: lib%name%soversion = %EVR

%description -n lib%name-devel
This package provides development files for lib%name library.

%if_enabled introspection
%package -n lib%name-gir
Summary: GObject introspection data for the lib%name library
Group: System/Libraries
Requires: lib%name%soversion = %EVR

%description -n lib%name-gir
GObject introspection data for the %name library.

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the lib%name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-gir = %EVR
Requires: lib%name-devel = %EVR

%description -n lib%name-gir-devel
GObject introspection devel data for the lib%name library
%endif

%if_enabled gtk_doc
%package -n lib%name-devel-doc
Summary: Development documentation for lib%name
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name-devel < %EVR

%description -n lib%name-devel-doc
The lib%name-devel-doc package contains documentation for
developing applications that use lib%name.
%endif

%if_enabled vala
%package -n lib%name-devel-vala
Summary: Vala language bindings for the lib%name library
Group: Development/Other
BuildArch: noarch
Requires: lib%name-devel = %EVR
Obsoletes: lib%name-vala < %EVR

%description -n lib%name-devel-vala
This package provides Vala language bindings for the lib%name library.
%endif

%if_enabled examples
%package -n %name-demo
Summary: Demo of GTK4 Layer Shell
Group: Development/GNOME and GTK+
Requires: lib%name%soversion = %EVR

%description -n %name-demo
%summary.
%endif

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool gtk_doc docs} \
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool vala vapi} \
    %{subst_enable_meson_bool examples examples}
%meson_build -v

%install
%meson_install

%files -n lib%name%soversion
%doc README.md
%_libdir/lib%name.so.%soversion
%_libdir/lib%name.so.%version

%files -n lib%name-devel
%_includedir/%name/
%_libdir/*.so
%_pkgconfigdir/*.pc

%if_enabled introspection
%files -n lib%name-gir
%_libdir/girepository-1.0/Gtk4LayerShell-*.typelib
%_libdir/girepository-1.0/Gtk4SessionLock-*.typelib

%files -n lib%name-gir-devel
%_datadir/gir-1.0/Gtk4LayerShell-*.gir
%_datadir/gir-1.0/Gtk4SessionLock-*.gir
%endif

%if_enabled gtk_doc
%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/%name/
%endif

%if_enabled vala
%files -n lib%name-devel-vala
%_vapidir/%name-0.deps
%_vapidir/%name-0.vapi
%endif

%if_enabled examples
%files -n %name-demo
%_bindir/gtk4-layer-demo
%endif

%changelog
* Sun Mar 30 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.1.1-alt1
- new version 1.1.1 (with rpmrb script)
- renamed source package to gtk4-layer-shell according upstream
- renamed vala package to libgtk4-layer-shell-devel-vala
- cleanup spec
- add demo package

* Sat Feb 08 2025 Kirill Unitsaev <fiersik@altlinux.org> 1.1.0-alt1
- new version 1.1.0 (with rpmrb script)

* Thu Nov 07 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.0.4-alt1
- new version 1.0.4 (with rpmrb script)

* Mon Sep 23 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.0.3-alt1
- new version 1.0.3 (with rpmrb script)

* Sun Jul 21 2024 Kirill Unitsaev <fiersik@altlinux.org> 1.0.2-alt1
- Initial build
