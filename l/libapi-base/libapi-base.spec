%define _unpackaged_files_terminate_build 1

%define apiver 1
%define namever %name-%apiver

Name: libapi-base
Version: 1.6
Release: alt1

Summary: Base objects for API libraries on Vala
License: GPL-3.0-or-later
Group: Development/Other
Url: https://gitlab.gnome.org/Rirusha/libapi-base
VCS: https://gitlab.gnome.org/Rirusha/libapi-base

Source0: %name-%version.tar
Patch0: %name-%version-alt.patch

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: gobject-introspection-devel
BuildRequires: libjson-glib-gir-devel
BuildRequires: libgee0.8-gir-devel
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(libsoup-3.0)
BuildRequires: pkgconfig(json-glib-1.0)

%description
%summary.

%package -n %namever
Summary: %{summary %name}
Group: System/Libraries

%description -n %namever
%{description %name}.

%package -n %namever-devel
Group: Development/Other
Summary: Headers files and library symbolic links for %name
Requires: %namever = %EVR

%description -n %namever-devel
%summary.
This package contains headers and libs
required for building programs with %name.

%package -n %namever-gir
Summary: GObject introspection data for libapi-base
Group: System/Libraries
Requires: %namever = %EVR

%description -n %namever-gir
%{summary %namever-gir}.

%package -n %namever-gir-devel
Summary: GObject introspection devel data for libapi-base
Group: System/Libraries
BuildArch: noarch
Requires: %namever-gir = %EVR
Requires: %namever-devel = %EVR

%description -n %namever-gir-devel
%{summary %namever-gir-devel}.

%prep
%setup
%autopatch -p1

%build
%meson
%meson_build

%install
%meson_install
%find_lang %name

%files -n %namever
%_libdir/libapi-base-%apiver.so.*

%files -n %namever-devel
%_includedir/libapi-base-%apiver.h
%_libdir/libapi-base-%apiver.so
%_pkgconfigdir/libapi-base-%apiver.pc
%_datadir/vala/vapi/libapi-base-%apiver.deps
%_datadir/vala/vapi/libapi-base-%apiver.vapi

%files -n %namever-gir
%_typelibdir/ApiBase-%apiver.typelib

%files -n %namever-gir-devel
%_girdir/ApiBase-%apiver.gir

%changelog
* Sat Dec 14 2024 Alexey Volkov <qualimock@altlinux.org> 1.6-alt1
- Initial build for ALT
