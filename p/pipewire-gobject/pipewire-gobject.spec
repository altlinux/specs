%def_disable snapshot

%define _name pipewire-gobject
%define __name pwg
%define libname lib%__name
%define namespace Pwg
%define ver_major 0.3
%define api_ver 0.1

%def_enable tests
%def_enable check

Name: %_name
Version: %ver_major.9
Release: alt1

Summary: Experimental GObject/GObject-Introspection binding layer for PipeWire
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://github.com/bhack/pipewire-gobject

Vcs: https://github.com/bhack/pipewire-gobject.git

%if_disabled snapshot
Source: https://github.com/bhack/pipewire-gobject/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

%define pw_api_ver 0.3

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gi-docgen
BuildRequires: pkgconfig(libpipewire-%pw_api_ver)
BuildRequires: gobject-introspection-devel
%{?_enable_check:BuildRequires: python3-module-pygobject3}

%description
This project is a prototype for exposing a safe, high-level, app-facing
PipeWire API to Python, GJS, Vala, and other GI consumers. It is not a
complete PipeWire binding yet, and it is not a mechanical one-to-one
binding of the C API.

%package -n %libname
Summary: %name shared library
Group: System/Libraries

%description -n %libname
This package provides shared %namespace library.

%package -n %libname-devel
Summary: Development files for %libname
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
The %libname-devel package provides libraries and header files for
developing applications that use %namespace library.

%package gir
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %libname = %EVR

%description gir
GObject introspection data for %_name.

%package gir-devel
Summary: GObject introspection devel data for %_name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %libname-devel = %EVR

%description gir-devel
GObject introspection devel data for %_name.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %libname < %version-%release
BuildArch: noarch

%description devel-doc
This package contains development documentation for %_name.

%package examples
Summary: simple applications from %_name package
Group: Development/Other
Requires: %name-gir = %EVR

%description examples
This package provides example programs that can be used to chek
the functionality of the %_name library.

%package tests
Summary: Tests for %name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.

%prep
%setup -n %_name-%version

%build
%meson \
    %{subst_enable_meson_bool tests tests}
%nil
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n %libname
%_libdir/%libname-%api_ver.so.*
%doc AGENTS* CHANGELOG* README*

%files -n %libname-devel
%_includedir/%__name-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%__name-%api_ver.pc

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%if_enabled doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%changelog
* Wed May 20 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.9-alt1
- 0.3.9

* Tue May 19 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.8-alt1
- 0.3.8

* Tue May 12 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.7-alt1
- 0.3.7

* Mon May 11 2026 Yuri N. Sedunov <aris@altlinux.org> 0.3.6-alt1
- first build for sisyphus


