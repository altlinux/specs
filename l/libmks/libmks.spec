%def_disable snapshot
%define _name mks
%define ver_major 0.1
%define api_ver 1

%def_enable introspection
%def_enable vala
%def_enable docs
%def_enable check

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: Mouse, Keyboard, and Screen to QEMU
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://gitlab.gnome.org/GNOME/libmks

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Vcs: https://gitlab.gnome.org/GNOME/libmks.git
Source: %name-%version.tar
%endif

%define glib_ver 2.75
%define gtk_ver 4.11

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson glib2-devel >= %glib_ver
BuildRequires: libepoxy-devel libpixman-devel
BuildRequires: libgtk4-devel >= %gtk_ver
BuildRequires: gobject-introspection-devel libgtk4-gir-devel
%{?_enable_vala:BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gi-docgen}

%description
This library provides a "Mouse, Keyboard, and Screen" to QEMU using the
D-Bus device support in QEMU and GTK 4.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This library provides a "Mouse, Keyboard, and Screen" to QEMU using the
D-Bus device support in QEMU and GTK 4.

This package contains files needed to develop applications using %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
Conflicts: %name < %version
BuildArch: noarch

%description devel-doc
This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for %name

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for %name.

%prep
%setup

%build
%meson \
    %{?_enable_introspection:-Dintrospection=enabled} \
    %{?_disable_vala:-Dvapi=false} \
    %{?_enable_docs:-Ddocs=true}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%{?_enable_vala:
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi}

%if_enabled docs
%files devel-doc
%_datadir/doc/%{name}%api_ver/
%endif

%files gir
%_typelibdir/Mks-%api_ver.typelib

%files gir-devel
%_girdir/Mks-%api_ver.gir

%changelog
* Fri Sep 08 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Thu Aug 31 2023 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

