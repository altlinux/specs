%define _unpackaged_files_terminate_build 1
%define _name varlink-glib
%define soversion 1

%def_enable introspection
%def_disable vapi
%def_disable docs
%def_disable sysprof

Name:          lib%_name
Version:       1.0.alpha
Release:       alt1
Group:         System/Libraries
Summary:       Varlink client/server library for GLib
License:       LGPL-2.1-or-later
Url:           https://gitlab.gnome.org/chergert/varlink-glib
Vcs:           https://gitlab.gnome.org/chergert/varlink-glib.git

Source:        %name-%version.tar
BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson >= 1.1.0
BuildRequires: glib2-devel >= 2.82
BuildRequires: libdex-devel >= 1.2
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libdex-gir-devel}
%{?_enable_vapi:BuildRequires: vala-tools}
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_sysprof:BuildRequires: pkgconfig(sysprof-capture-4)}

%description
Varlink GLib is a library for building Varlink clients and services
based on GLib/GIO, with typed C code generation support.

%package gir
Group: System/Libraries
Summary: GObject introspection data for the Varlink GLib library
Requires: %name = %EVR

%description gir
This package provides GObject introspection data for the Varlink
GLib client/server library.

%package gir-devel
Group: Development/Other
Summary: GObject introspection devel data for the Varlink GLib library
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
This package provides GObject introspection devel data for the
Varlink GLib client/server library.

%package       devel
Group:         Development/C
Summary:       Development files for libvarlink-glib
Requires:      %name = %EVR
Requires:      glib2-devel >= 2.82
Requires:      libdex-devel >= 1.2

%description   devel
Development files for the Varlink GLib client/server library.

%prep
%setup -q

%build
%meson \
    --wrap-mode=nodownload \
    %{subst_enable_meson_feature introspection introspection} \
    %{subst_enable_meson_feature sysprof sysprof} \
    %{subst_enable_meson_bool vapi vapi} \
    %{subst_enable_meson_bool docs docs}
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc README.md LICENSE
%_libdir/%name-%soversion.so.%{soversion}*

%files gir
%_typelibdir/Varlink-%soversion.typelib

%files gir-devel
%_girdir/Varlink-%soversion.gir

%files         devel
%_bindir/varlink-codegen
%_includedir/%_name-%soversion/
%_libdir/%name-%soversion.so
%_pkgconfigdir/%_name-%soversion.pc
%{?_enable_vapi:%_vapidir/%_name-%soversion.vapi}

%changelog
* Thu Nov 05 2026 Alexey Saprunov <sav@altlinux.org> 1.0.alpha-alt1
- Initial build for ALT Linux.
