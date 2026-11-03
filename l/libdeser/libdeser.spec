# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libdeser to altlinux branch

%define _unpackaged_files_terminate_build 1

%define api_version 0.1
%define gir_name Deser

%define sname libsession
%define gir_sname Session

Name: libdeser
Version: %api_version.0
Release: alt1

Summary: Serialization and HTTP session libraries for Vala
License: GPL-3.0-or-later
Group: System/Libraries
URL: https://altlinux.space/rirusha/libdeser
VCS: https://altlinux.space/rirusha/libdeser.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(yyjson)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: gir(Soup) = 3.0
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: pkgconfig(libtoml)
BuildRequires: gobject-introspection-devel

%description
%summary.

%package -n %name%api_version
Summary: JSON, YAML and TOML serialization for Vala
Group: Development/C

%description -n %name%api_version
%summary.

%package devel
Summary: Development files for %name
Group: Development/C

Requires: %name%api_version = %EVR

%description devel
%summary.

%package -n %sname%api_version
Summary: HTTP session helpers for Vala
Group: Development/C

%description -n %sname%api_version
%summary.

%package -n %sname-devel
Summary: Development files for %sname
Group: Development/C

Requires: %sname%api_version = %EVR

%description -n %sname-devel
%summary.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %name%api_version
%_libdir/%name-%api_version.so.*
%_typelibdir/%gir_name-%api_version.typelib
%doc README.md

%files devel
%_libdir/%name-%api_version.so
%_includedir/%name-%api_version.h
%_pkgconfigdir/%name-%api_version.pc
%_vapidir/%name-%api_version.vapi
%_vapidir/%name-%api_version.deps
%doc README.md
%_girdir/%gir_name-%api_version.gir

%files -n %sname%api_version
%_libdir/%sname-%api_version.so.*
%_typelibdir/%gir_sname-%api_version.typelib

%files -n %sname-devel
%_libdir/%sname-%api_version.so
%_includedir/%sname-%api_version.h
%_pkgconfigdir/%sname-%api_version.pc
%_vapidir/%sname-%api_version.vapi
%_vapidir/%sname-%api_version.deps
%_girdir/%gir_sname-%api_version.gir

%changelog
* Tue Nov 03 2026 Vladimir Romanov <rirusha@altlinux.org> 0.1.0-alt1
- Initail build.
