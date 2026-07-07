%def_disable snapshot

%define _name libipuz
%define ver_major 0.5
%define api_ver 1.0
%define namespace Ipuz

%def_enable introspection
%def_enable docs
%def_enable check
%def_enable installed_tests

%def_disable bootstrap
# if "sandboxed" CARGO_HOME=cargo
%def_enable sandboxed

Name: %_name
Version: %ver_major.5
Release: alt1

Summary: Library for parsing and writing .ipuz puzzle files
License: LGPL-2.1 or MIT
Group: System/Libraries
Url: https://gitlab.gnome.org/jrb/libipuz

Vcs: https://gitlab.gnome.org/jrb/libipuz.git

%if_disabled snapshot
Source: https://gitlab.gnome.org/jrb/libipuz/-/archive/%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif
Source1: %name-%version-cargo.tar

BuildRequires(pre): rpm-macros-meson rpm-build-rust %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson rust-cargo
BuildRequires: pkgconfig(json-glib-1.0)
%{?_enable_docs:BuildRequires: gi-docgen}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel gir(Json) = 1.0}

%description
%summary

%package devel
Summary: Header and development libraries for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains header and development libraries for %name

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library.

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %name library.

%package tests
Summary: Tests for the %_name
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name.

%prep
%setup -n %_name-%version %{?_disable_bootstrap:-a1}
%{?_enable_bootstrap:
pushd %_name/rust
mkdir cargo
cargo vendor | sed 's/^directory = ".*"/directory = "vendor"/g' > cargo/config.toml
tar -cf %_sourcedir/%name-%version-cargo.tar cargo vendor
popd}

%build
%meson \
    %{subst_enable_meson_feature introspection introspection} \
    %{subst_enable_meson_feature docs documentation} \
    %{subst_enable_meson_bool sandboxed sandboxed}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name-%api_ver

%check
%__meson_test


%files -f %_name.lang
%_libdir/lib%_name-%ver_major.so
%doc NEWS* README*

%files devel
%_includedir/%_name/
#%_libdir/*.so
%_pkgconfigdir/%_name-%ver_major.pc

%if_enabled docs
%files devel-doc
%_datadir/doc/%_name-%api_ver
%endif

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Tue Jul 07 2026 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Dec 31 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Wed Oct 22 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- 0.5.3

* Mon Jun 02 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.2-alt1
- updated to 0.5.2-2-g03293f2

* Sat Jan 25 2025 Yuri N. Sedunov <aris@altlinux.org> 0.5.1-alt1
- first build for Sisyphus (0.5.1-11-g1ee3f0f)

