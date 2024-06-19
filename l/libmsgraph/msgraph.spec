%def_disable snapshot

%def_enable introspection
%def_enable gtk_doc
%def_disable check
%def_disable tests
%def_disable installed_tests

%define _name msgraph
%define ver_major 0.2
%define api_ver_major 0
%define api_ver 0.1

Name: lib%_name
Version: %ver_major.3
Release: alt1

Summary: GObject wrapper for the Microsoft Graph API
Group: System/Libraries
License: LGPL-3.0-or-later
Url: https://gitlab.com/tabos/msgraph

Vcs: https://gitlab.com/tabos/msgraph.git
%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(rest-1.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(goa-1.0)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel
BuildRequires: gir(Goa) = 1.0 gir(Json) = 1.0 gir(Soup) = 3.0 gir(Rest) = 1.0}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: pkgconfig(libuhttpmock-1.0)}

%description
libmsgraph is a GLib-based library for accessing online service APIs
using MS Graph protocol.

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
    %{subst_enable_meson_bool introspection introspection} \
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool tests tests}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name-%api_ver

%check
%__meson_test

%files -f %name.lang
%_libdir/%name-%api_ver_major.so.*
%doc NEWS README*

%files devel
%_includedir/msg/
%_libdir/%name-%api_ver_major.so
%_pkgconfigdir/%_name-%api_ver.pc

%files gir
%_typelibdir/Msg-%api_ver_major.typelib

%files gir-devel
%_girdir/Msg-%api_ver_major.gir

%files devel-doc
%_datadir/doc/%_name-%api_ver_major/

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Wed Jun 19 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.3-alt1
- 0.2.3

* Wed May 22 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.2-alt1
- 0.2.2

* Tue Mar 05 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.1-alt1
- 0.2.1

* Sat Mar 02 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for sisyphus (0.2.0-1-g11e0670)

