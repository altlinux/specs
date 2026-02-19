# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libapi-base to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define api_version 5
%define minor_version 0
%define gir_name ApiBase
%define bare_name libapi-base

Name: %bare_name%api_version
Version: %api_version.%minor_version
Release: alt2

Summary: Base objects for API libraries on Vala
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://altlinux.space/rirusha/libapi-base
Vcs: https://altlinux.space/rirusha/libapi-base.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
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
Summary: Development files for %bare_name
Group: Development/C

Requires: %name = %EVR

%description devel
%summary.

%package gir
Summary: Typelib files for %bare_name
Group: System/Libraries

Requires: %name = %EVR

%description gir
%summary.

%package gir-devel
Summary: Development gir files for %bare_name for various bindings
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
%_libdir/%bare_name-%api_version.so.*

%files devel
%_libdir/%bare_name-%api_version.so
%_includedir/%bare_name-%api_version.h
%_pkgconfigdir/%bare_name-%api_version.pc
%_vapidir/%bare_name-%api_version.vapi
%_vapidir/%bare_name-%api_version.deps
%doc README.md

%files gir
%_typelibdir/%gir_name-%api_version.typelib

%files gir-devel
%_girdir/%gir_name-%api_version.gir

%changelog
* Thu Feb 19 2026 Vladimir Romanov <rirusha@altlinux.org> 5.0-alt2
- Changed source package name to libapi-base5.

* Mon Jan 12 2026 Vladimir Romanov <rirusha@altlinux.org> 5.0-alt1
- New version: 5.0.

* Fri Jan 09 2026 Vladimir Romanov <rirusha@altlinux.org> 4.4-alt1
- New version: 4.4.

* Fri Oct 24 2025 Vladimir Romanov <rirusha@altlinux.org> 4.3-alt1
- New version: 4.3.

* Mon Sep 22 2025 Vladimir Vaskov <rirusha@altlinux.org> 4.2-alt1
- New version: 4.2.

* Fri Sep 05 2025 Vladimir Vaskov <rirusha@altlinux.org> 4.1-alt1
- New version: 4.1.
- Changed VCS and URL.

* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 1.6-alt1
- Initial build for ALT
