# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libapi-base to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define api_version 7
%define minor_version 8
%define gir_name ApiBase

%define yaml_api_version 0.1
%define yaml_name yaml
%define yaml_gir_name Yaml

%define sname libserialize
%define gir_sname Serialize

Name: libapi-base
Version: %api_version.%minor_version
Release: alt1

Summary: Base objects for API libraries on Vala
License: GPL-3.0-or-later
Group: System/Libraries
URL: https://altlinux.space/rirusha/libapi-base
VCS: https://altlinux.space/rirusha/libapi-base.git

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
BuildRequires: pkgconfig(yaml-0.1)
BuildRequires: gobject-introspection-devel

%description
%summary.

%package -n %name%api_version
Summary: Base objects for API libraries
Group: Development/C

%description -n %name%api_version
%summary.

%package devel
Summary: Development files for %name
Group: Development/C

Requires: %name%api_version = %EVR

%description devel
%summary.

%package -n %name%api_version-gir
Summary: Typelib files for %name
Group: System/Libraries

Requires: %name%api_version = %EVR

%description -n %name%api_version-gir
%summary.

%package gir-devel
Summary: Development gir files for %name for various bindings
Group: Development/Other
BuildArch: noarch

Requires: %name%api_version-gir = %EVR

%description gir-devel
%summary.

%package -n %sname%api_version
Summary: Serialization/Deserialoztion tools for vala
Group: Development/C

%description -n %sname%api_version
%summary.

%package -n %sname-devel
Summary: Development files for %sname
Group: Development/C

Requires: %sname%api_version = %EVR

%description -n %sname-devel
%summary.

%package -n %sname%api_version-gir
Summary: Typelib files for %sname
Group: System/Libraries

Requires: %sname%api_version = %EVR

%description -n %sname%api_version-gir
%summary.

%package -n %sname-gir-devel
Summary: Development gir files for %sname for various bindings
Group: Development/Other
BuildArch: noarch

Requires: %sname%api_version-gir = %EVR

%description -n %sname-gir-devel
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

%files devel
%_libdir/%name-%api_version.so
%_includedir/%name-%api_version.h
%_pkgconfigdir/%name-%api_version.pc
%_vapidir/%name-%api_version.vapi
%_vapidir/%name-%api_version.deps
%_vapidir/%yaml_name-%yaml_api_version.vapi
%_vapidir/%yaml_name-%yaml_api_version.deps
%doc README.md

%files -n %name%api_version-gir
%_typelibdir/%gir_name-%api_version.typelib

%files gir-devel
%_girdir/%gir_name-%api_version.gir
%_girdir/%yaml_gir_name-%yaml_api_version.gir

%files -n %sname%api_version
%_libdir/%sname-%api_version.so.*

%files -n %sname-devel
%_libdir/%sname-%api_version.so
%_includedir/%sname-%api_version.h
%_pkgconfigdir/%sname-%api_version.pc
%_vapidir/%sname-%api_version.vapi
%_vapidir/%sname-%api_version.deps

%files -n %sname%api_version-gir
%_typelibdir/%gir_sname-%api_version.typelib

%files -n %sname-gir-devel
%_girdir/%gir_sname-%api_version.gir

%changelog
* Sat Jun 13 2026 Vladimir Romanov <rirusha@altlinux.org> 7.8-alt1
- Added yaml support.
- Class TypeFamily now JsonTypeFamily for json and YamlTypeFamily for yaml.
- Full release notes:
  https://altlinux.space/rirusha/libapi-base/releases/tag/v7.8

* Tue Jun 09 2026 Vladimir Romanov <rirusha@altlinux.org> 7.7-alt1
- Added comments to generated vapi file.
- Full release notes:
  https://altlinux.space/rirusha/libapi-base/releases/tag/v7.7

* Thu Jun 04 2026 Vladimir Romanov <rirusha@altlinux.org> 7.6-alt1
- New version: 7.6.
- Fixed build soversion.
- Full release notes:
  https://altlinux.space/rirusha/libapi-base/releases/tag/v7.6

* Mon May 18 2026 Vladimir Romanov <rirusha@altlinux.org> 7.5-alt1
- New version: 7.5.
- Added INI format support in Serialize.
- Added supported PascalCase.
- Deprecate `Serialize.Jsoner`, `Serialize.JsonWorker` should be used instead.
- Deprecate `Serialize.JsonError`, `Serialize.Error` should be used instead.
- Full release notes:
  https://altlinux.space/rirusha/libapi-base/releases/tag/v7.5

* Mon Apr 20 2026 Vladimir Romanov <rirusha@altlinux.org> 7.4-alt1
- New version: 7.4.
- New `send` API in `Session` with `Soup.Session` compatibility.
- Added managing multiple base URLs with automatic failover.
- Improved serialization: case-insensitive enum parsing, UTC timezone
  for DateTime, INT64 -> DateTime conversion.
- Full release notes:
  https://altlinux.space/rirusha/libapi-base/releases/tag/v7.4

* Sun Mar 29 2026 Vladimir Romanov <rirusha@altlinux.org> 7.3-alt1
- New version: 7.3.
- Removed assert on wrong request type in `add_content`.
- Fixed Critical on `HasFallback` serialization.

* Mon Mar 23 2026 Vladimir Romanov <rirusha@altlinux.org> 7.2-alt1
- New version: 7.2.
- Returned building typelib and gir.
- Added API_BASE_UNKNOWN_PROPS for detection unused props.
- Added string[] type property support.

* Thu Feb 26 2026 Vladimir Romanov <rirusha@altlinux.org> 7.0-alt1
- New version: 7.0.

* Thu Feb 19 2026 Vladimir Romanov <rirusha@altlinux.org> 6.1-alt1
- New version: 6.1.

* Thu Feb 19 2026 Vladimir Romanov <rirusha@altlinux.org> 6.0-alt1
- New version: 6.0.

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
