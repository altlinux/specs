%def_disable snapshot

%define _libexecdir %_prefix/libexec
%define _name jsonrpc-glib
# probably meson bug
%define libname libjsonrpc-glib
%define ver_major 3.44
%define api_ver 1.0

%def_enable introspection
%def_enable gtk_doc
%def_enable vala
%def_disable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A JSON-RPC library for GLib
Group: System/Libraries
License: LGPLv2.1
Url: https://wiki.gnome.org/Apps/Builder

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson >= 0.49.2 vala-tools
BuildRequires: libgio-devel libjson-glib-devel
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: gobject-introspection-devel libjson-glib-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_vala:BuildRequires(pre):rpm-build-vala
BuildRequires: vala-tools}

%description
Jsonrpc-GLib is a JSON-RPC library for GLib. It includes support for
communicating as both a JSON-RPC client and server. Additionally, it
supports upgrating connections to use GVariant for less runtime overhead.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_gtk_doc:-Denable_gtk_doc=true} \
    %{?_disable_vala:-Dwith_vapi=false}
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%libname-%api_ver.so.*
%doc README.md NEWS AUTHORS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%{?_enable_vala:%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi}

%if_enabled introspection
%files gir
%_typelibdir/Jsonrpc-%api_ver.typelib

%files gir-devel
%_girdir/Jsonrpc-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name/
%endif

%changelog
* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 3.44.0-alt1
- 3.44.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 3.42.0-alt1
- 3.42.0

* Thu Sep 23 2021 Yuri N. Sedunov <aris@altlinux.org> 3.40.0-alt1
- 3.40.0

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 3.38.0-alt1
- 3.38.0

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 3.34.0-alt1
- 3.34.0

* Wed Mar 13 2019 Yuri N. Sedunov <aris@altlinux.org> 3.32.0-alt1
- 3.32.0

* Thu Oct 11 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.1-alt1
- 3.30.1

* Wed Sep 05 2018 Yuri N. Sedunov <aris@altlinux.org> 3.30.0-alt1
- 3.30.0

* Tue Jun 19 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.1-alt1
- 3.28.1

* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Jun 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.2-alt1
- first build for Sisyphus

