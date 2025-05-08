%define _unpackaged_files_terminate_build 1
%def_enable check
%def_enable snapshot

%define sover 1
%define api_ver 1
%define libbismuth libbismuth%sover
%define namespace Bis

Name: libbismuth
Version: 1.0.5
Release: alt1

Summary: Libadwaita's responsive widgets, without all the baggage
License: LGPL-2.1-or-later
Group: System/Libraries

Url: https://github.com/tau-OS/libbismuth
Vcs: https://github.com/tau-OS/libbismuth
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson
BuildRequires: vala
BuildRequires: vala-tools
BuildRequires: pkgconfig(gtk4)
BuildRequires: /usr/bin/glib-compile-schemas
BuildRequires: sassc
BuildRequires: pkgconfig(fribidi)
BuildRequires: gobject-introspection-devel gir(Gtk) = 4.0
BuildRequires: blueprint-compiler
%if_enabled check
BuildRequires: desktop-file-utils
BuildRequires: appstream
BuildRequires: libgio
%endif

%description
Libadwaita's responsive widgets, without all the baggage.

%package -n %libbismuth
Summary: Libadwaita's responsive widgets, without all the baggage
Group: System/Libraries

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %libbismuth = %EVR

%package devel
Summary: Development files for libbismuth
Requires: %libbismuth = %EVR
Group: System/Libraries

%description -n %libbismuth
Libadwaita's responsive widgets, without all the baggage.

%description gir
GObject introspection data for the %name.

%description devel
This package contains the libraries and header files that are needed
for writing applications with libbismuth.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n %libbismuth
%_libdir/libbismuth-%api_ver.so.%sover
%doc AUTHORS README.md

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files devel
%_libdir/libbismuth-%api_ver.so
%_includedir/libbismuth-%api_ver/*.h
%_libdir/pkgconfig/libbismuth-%api_ver.pc
%_datadir/vala/vapi/libbismuth-%api_ver.vapi
%_datadir/vala/vapi/libbismuth-%api_ver.deps
%_girdir/%namespace-%api_ver.gir

%changelog
* Mon Apr 21 2025 Semen Fomchenkov <armatik@altlinux.org> 1.0.5-alt1
- Initial build.
