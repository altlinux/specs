%define _unpackaged_files_terminate_build 1

# require libpulseaudio-devel directly
%filter_from_requires /vapi(libpulse)/d
%filter_from_requires /vapi(libpulse-mainloop-glib)/d

# FIXME?
%filter_from_requires /vapi(upower-glib)/d

%def_with check

Name: libsingularity
Version: 0.1.0
Release: alt1

Summary: GTK4 application and widget framework for the Singularity Desktop Environment
License: LGPL-2.1-only
Group: System/Libraries
Url: https://github.com/singularityos-lab/libsingularity

Source: %name-%version.tar

BuildRequires(pre): meson
BuildRequires(pre): rpm-build-vala

BuildRequires: vala-tools
BuildRequires: cmake
BuildRequires: pkgconfig(gtk4)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(libpeas-2)
BuildRequires: pkgconfig(gtksourceview-5)
BuildRequires: pkgconfig(gobject-introspection-1.0)
BuildRequires: pkgconfig(gtk4-layer-shell-0)
BuildRequires: /usr/bin/g-ir-compiler
BuildRequires: pkgconfig(libpulse)
BuildRequires: pkgconfig(gudev-1.0)
BuildRequires: pkgconfig(upower-glib)
BuildRequires: pkgconfig(libnm)
BuildRequires: /usr/bin/sassc
BuildRequires: vapi(gtk4-layer-shell-0)
BuildRequires: libgtk4-gir-devel
BuildRequires: libgee0.8-gir-devel
BuildRequires: libgtksourceview5-gir-devel

%description
A %summary.

%package devel
Summary: Development files for %name
Group: Development/Other
Requires: %name = %{version}-%{release}
Requires: libpulseaudio-devel

%description devel
Development files for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files
%doc CONTRIBUTING.md LICENSE README.md
%dir %_datadir/themes/Singularity
%_datadir/themes/Singularity/*
%_libdir/girepository-1.0/Singularity-1.0.typelib
%_libdir/libsingularity.so.0*
%_libdir/libsingularity-system.so.0*
%dir %_datadir/singularity
%_datadir/singularity/*

%files devel
%_includedir/singularity.h
%_includedir/singularity-system.h
%_libdir/libsingularity.so
%_libdir/libsingularity-system.so
%_libdir/pkgconfig/singularity-1.0.pc
%_libdir/pkgconfig/singularity-system-1.0.pc
%_datadir/gir-1.0/Singularity-1.0.gir
%_vapidir/singularity-1.0.deps
%_vapidir/singularity-1.0.vapi
%_vapidir/singularity-system-1.0.deps
%_vapidir/singularity-system-1.0.vapi

%changelog
* Sat Sep 05 2026 Nikolay Strelkov <snk@altlinux.org> 0.1.0-alt1
- Initial build for Sisyphus
