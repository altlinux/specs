# If you want to suggest changes, please send PR on
# https://altlinux.space/rirusha/libapi-base to altlinux branch 

%define _unpackaged_files_terminate_build 1

%define api_version 7
%define minor_version 0
%define gir_name ApiBase

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

%prep
%setup

%build
%meson -Drun_net_tests=false
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
%doc README.md

%files -n %sname%api_version
%_libdir/%sname-%api_version.so.*

%files -n %sname-devel
%_libdir/%sname-%api_version.so
%_includedir/%sname-%api_version.h
%_pkgconfigdir/%sname-%api_version.pc
%_vapidir/%sname-%api_version.vapi
%_vapidir/%sname-%api_version.deps

%changelog
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
