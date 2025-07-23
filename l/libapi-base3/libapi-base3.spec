# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libapi-base to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define bare_name libapi-base
%define api_version 3
%define minor_version 0
%define gir_name ApiBase-%api_version
%define good_name %bare_name-%api_version

Name: %bare_name%api_version
Version: %api_version.%minor_version
Release: alt1

Summary: Base objects for API libraries
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.gnome.org/Rirusha/libapi-base
Vcs: https://gitlab.gnome.org/Rirusha/libapi-base.git

Source0: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson rpm-build-vala rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gir(Json) = 1.0
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: gir(Gee) = 0.8
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: gir(Soup) = 3.0
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: gobject-introspection-devel

%description
%summary.

%package devel
Summary: Development files for %name
Group: Development/C

Provides: %bare_name-devel = %EVR

Requires: %name = %EVR

%description devel
%summary.

%package devel-vala
Summary: Development vapi files for %name
Group: System/Libraries
BuildArch: noarch

Requires: %name-devel = %EVR

%description devel-vala
%summary.

%package gir
Summary: Typelib files for %name
Group: System/Libraries

Requires: %name = %EVR

%description gir
%summary.

%package gir-devel
Summary: Development gir files for %name for various bindings
Group: Development/Other
BuildArch: noarch

Requires: %name-gir = %EVR

%description gir-devel
%summary.

%prep
%setup

%build
%meson -Drun_net_tests=false
%meson_build

%install
%meson_install

%check
%meson_test

%files
%_libdir/%good_name.so.*
%doc README.md

%files devel
%_libdir/%good_name.so
%_includedir/%good_name.h
%_pkgconfigdir/%good_name.pc

%files devel-vala
%_vapidir/%good_name.vapi
%_vapidir/%good_name.deps

%files gir
%_typelibdir/%gir_name.typelib

%files gir-devel
%_girdir/%gir_name.gir

%changelog
* Wed Jul 23 2025 Vladimir Vaskov <rirusha@altlinux.org> 3.0-alt1
- Initial build
