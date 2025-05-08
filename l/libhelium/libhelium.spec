%define _unpackaged_files_terminate_build 1
%def_enable check
%def_enable snapshot
%define app_id com.fyralabs.desktop.appearance

%define tau_helium_ver 1.8.24

%define sover 1
%define api_ver 1
%define libhelium libhelium%sover
%define namespace He

Name: libhelium
Version: 1.8.24
Release: alt1

Summary: The elegant framework for building beautiful and useful apps
License: GPL-3.0-or-later
Group: System/Libraries

Url: https://github.com/tau-OS/libhelium
Vcs: https://github.com/tau-OS/libhelium
Source: %name-%version.tar

Patch0: libhelium-1.8.24-alt-gtk-3.0_func_work_with_sassc.patch
Patch1: libhelium-1.8.24-alt-gtk-4.0_func_work_with_sassc.patch
Patch2: libhelium-1.8.24-alt-gtk-4.0_meson_build_work_with_sassc.patch
Patch3: libhelium-1.8.24-alt-meson_build_work_with_sassc.patch
Patch4: libhelium-1.8.24-alt-fix_schema_build.patch

Source10: tau-helium-%tau_helium_ver.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: pkgconfig(libadwaita-1)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: sassc
BuildRequires: gobject-introspection-devel gir(Gtk) = 4.0
BuildRequires: blueprint-compiler
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
The Application Framework for tauOS apps.

%package -n %libhelium
Summary: The elegant framework for building beautiful and useful apps
Group: System/Libraries 
Requires: %name-data >= %EVR

%package data
Summary: GLib data for the %name
Group: System/Libraries
BuildArch: noarch
Conflicts: %libhelium < %EVR

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %libhelium = %EVR

%package devel
Summary: Development files for libhelium
Requires: %libhelium = %EVR
Group: System/Libraries

%description -n %libhelium
The Application Framework for tauOS apps.

%description data
GLib data for the %name.

%description gir
GObject introspection data for the %name.

%description devel
This package contains the libraries and header files that are needed
for writing applications with libhelium.

%prep
%setup %{?_enable_snapshot: -a10
mv tau-helium-%tau_helium_ver subprojects/tau-helium
}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%build
%meson \
    -Ddemo=false \
    -Dvaladoc=false
%meson_build

%install
%meson_install

rm -rf %{buildroot}%{_datadir}/themes/*

%check
%meson_test

%files -n %libhelium
%_libdir/libhelium-1.so.%sover
%doc README.md

%files data
%_datadir/glib-2.0/schemas/%app_id.gschema.xml

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files devel
%_libdir/libhelium-%api_ver.so
%_includedir/libhelium-%api_ver.h
%_libdir/pkgconfig/libhelium-%api_ver.pc
%_datadir/vala/vapi/libhelium-%api_ver.vapi
%_girdir/%namespace-%api_ver.gir

%changelog
* Mon Apr 21 2025 Semen Fomchenkov <armatik@altlinux.org> 1.8.24-alt1
- Initial build.
