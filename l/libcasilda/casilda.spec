%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name casilda
%define namespace Casilda
%define ver_major 1.2
%define api_ver_major 1
%define api_ver 1.0
%define sover 0

%def_enable introspection
%def_enable vala
%def_enable doc
%def_enable examples
%def_enable check

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: Wayland compositor widget for GTK4
Group: System/Libraries
License: LGPL-2.1
Url: https://gitlab.gnome.org/jpu/casilda.git

Vcs: https://gitlab.gnome.org/jpu/casilda.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/jpu/casilda/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define gtk_ver 4.14
%define epoxy_ver 1.5
%define wlr_api_ver 0.20
%define wp_ver 1.22
%define xkb_ver 1.5

BuildRequires(pre): rpm-macros-meson rpm-build-gir %{?_enable_examples:rpm-build-python3} %{?_enable_vala:rpm-build-vala}
BuildRequires: meson
BuildRequires: pkgconfig(gtk4) >= %gtk_ver
BuildRequires: pkgconfig(epoxy) >= %epoxy_ver
BuildRequires: pkgconfig(wlroots-%wlr_api_ver)
BuildRequires: pkgconfig(wayland-protocols) >= %wp_ver
BuildRequires: pkgconfig(xkbcommon-x11) >= %xkb_ver
BuildRequires: pkgconfig(x11-xcb)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Gtk) = 4.0}
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_doc:BuildRequires: gi-docgen}

%description
A simple Wayland compositor widget for GTK4 which can be used to embed
other processes windows in GTK4 applications.

This package provides shared %_name library.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package provides development files for %_name library.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %_name library.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %_name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name library.

%package -n %_name-examples
Summary: simple applications from %_name package
Group: Development/Other
Requires: %name = %EVR
Requires: gtk4-demo
Requires: /usr/bin/gjs typelib(%namespace) = %api_ver
Requires: python3-module-pygobject3
Requires: lib%_name-gir = %EVR

%add_python3_path %_libexecdir/%_name

%description -n %_name-examples
This package provides example programs that can be used to chek
the functionality of the %_name library.

%prep
%setup -n %_name-%version

%build
%meson \
    %{subst_enable_meson_bool vala vapi} \
    %{subst_enable_meson_bool doc documentation}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name-%api_ver

mkdir -p %buildroot%_libexecdir/%_name
# %__builddir/examples/{compositor,nested} segfaults
install -pD -m755  %__sourcedir/examples/*.{py,js} \
    %buildroot%_libexecdir/%_name

%check
%__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver.so.*
%doc CHANGELOG* README*

%files devel
%_includedir/%_name
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.*}

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled doc
%files devel-doc
%_datadir/doc/%_name/
%endif

%if_enabled examples
%files -n %_name-examples
%_libexecdir/%_name/
%endif

%changelog
* Sat Apr 11 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.3-alt1
- 1.2.3

* Sat Apr 04 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Fri Mar 20 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.1-alt1
- 1.2.1

* Sat Mar 07 2026 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0 (ported to wlroots-0.19)

* Sat Oct 25 2025 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Mon Sep 15 2025 Yuri N. Sedunov <aris@altlinux.org> 0.9.2-alt1
- first build for sisyphus (0.9.2-10-gf26d2c6)

