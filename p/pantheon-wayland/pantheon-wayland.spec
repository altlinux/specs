%define _unpackaged_files_terminate_build 1

Name: pantheon-wayland
Version: 1.0.0
Release: alt1

Summary: Wayland integration library to the Pantheon Desktop
License: LGPL-3.0-or-later
Group: Graphical desktop/Other
Url: https://github.com/elementary/pantheon-wayland

Source: %name-%version.tar

BuildRequires(pre): rpm-macros-meson
BuildRequires(pre): rpm-macros-cmake
BuildRequires(pre): rpm-build-vala

BuildRequires: meson
BuildRequires: cmake
BuildRequires: vala-tools
BuildRequires: pkgconfig(wayland-client)
BuildRequires: pkgconfig(gtk4)
BuildRequires: /usr/bin/g-ir-compiler
BuildRequires: libgtk4-gir-devel

%description
%summary

%package -n lib%{name}
Group: Development/Other
Summary: Pantheon shell utilities for Wayland

%description -n lib%{name}
A collection of utilities for Pantheon shell specific
features such as sticky and centered windows

%package -n lib%{name}-devel
Group: Development/Other
Summary: Pantheon shell utilities for Wayland
Requires: lib%{name} = %{version}-%{release}

%description -n lib%{name}-devel
A collection of utilities for Pantheon shell specific
features such as sticky and centered windows

This package contains the development files used for %name.

%prep
%setup

%build
%meson
%meson_build

%install
%meson_install

%check
%meson_test

%files -n lib%{name}
%doc COPYING README.md
%_libdir/libpantheon-wayland.so.1
%_libdir/libpantheon-wayland.so.1.0.0
%_libdir/girepository-1.0/PantheonWayland-1.typelib

%files -n lib%{name}-devel
%dir %_includedir/pantheon-wayland-1
%_includedir/pantheon-wayland-1/pantheon-wayland.h
%_libdir/libpantheon-wayland.so
%_pkgconfigdir/pantheon-wayland-1.pc
%_datadir/gir-1.0/PantheonWayland-1.gir
%_vapidir/pantheon-wayland-1.deps
%_vapidir/pantheon-wayland-1.vapi

%changelog
* Sat Sep 20 2025 Nikolay Strelkov <snk@altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus
