%define _unpackaged_files_terminate_build 1

%define api_version 1
%define gir_name AltRepo

Name: libalt-repo
Version: 1.21.1
Release: alt1

Summary: ALT Repo API library on Vala
License: GPL-3.0-or-later
Group: System/Libraries
Url: https://altlinux.space/alt-gnome/libalt-repo
Vcs: https://altlinux.space/alt-gnome/libalt-repo.git

Source: %name-%version.tar
Patch: %name-%version-%release.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: rpm-build-vala
BuildRequires: rpm-build-gir
BuildRequires: meson
BuildRequires: vala
BuildRequires: gobject-introspection-devel
BuildRequires: gir(Gee) = 0.8
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libapi-base-4)
BuildRequires: gir(ApiBase) = 4

%description
%summary.

%package -n %name%api_version
Summary: %{summary %name}
Group: Development/C

Obsoletes: libalt-repo-vala-1 <= 1.19.20
Provides: libalt-repo-vala-1 = %EVR

%description -n %name%api_version
%summary.

%package devel
Summary: Development files for %name
Group: Development/C

Obsoletes: libalt-repo-vala-1-devel <= 1.19.20
Provides: libalt-repo-vala-1-devel = %EVR

Requires: %name%api_version = %EVR

%description devel
%summary.

%package -n %name%api_version-gir
Summary: Typelib files for %name
Group: System/Libraries
Requires: %name%api_version = %EVR

Obsoletes: libalt-repo-vala-1-gir <= 1.19.20
Provides: libalt-repo-vala-1-gir = %EVR

%description -n %name%api_version-gir
%{description %name}.

%package gir-devel
Summary: GObject introspection devel data for %name
Group: Development/Other
BuildArch: noarch

Obsoletes: libalt-repo-vala-1-gir-devel <= 1.19.20
Provides: libalt-repo-vala-1-gir-devel = %EVR

Requires: %name%api_version-gir = %EVR

%description gir-devel
%{summary %api_version-gir-devel}.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -n %name%api_version
%_libdir/%name-%api_version.so.*

%files devel
%_libdir/%name-%api_version.so
%_includedir/%name-%api_version.h
%_pkgconfigdir/%name-%api_version.pc
%_vapidir/%name-%api_version.vapi
%_vapidir/%name-%api_version.deps
%doc README.md

%files -n %name%api_version-gir
%_typelibdir/%gir_name-%api_version.typelib

%files gir-devel
%_girdir/%gir_name-%api_version.gir

%changelog
* Fri Sep 05 2025 Vladimir Vaskov <rirusha@altlinux.org> 1.21.1-alt1
- New Version 1.21.1.
- Changed URL and VCS.
- Corrected package names according to Shared Libs Policy.
- Corrected packages groups.

* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 1.19.20-alt1
- Initial build for ALT
