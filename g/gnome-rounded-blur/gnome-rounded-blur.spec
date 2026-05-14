%def_disable snapshot

%define _name gnome-rounded-blur
%define __name blur-effect
%define libname lib%__name
%define namespace Blur
%define ver_major 1.0
%define api_ver %ver_major

%def_enable check

Name: %_name
Version: %ver_major.1
Release: alt1

Summary: GNOME Rounded Blur
Group: System/Libraries
License: LGPL-3.0-or-later
Url: https://github.com/kancko/gnome-rounded-blur

Vcs: https://github.com/kancko/gnome-rounded-blur.git

%if_disabled snapshot
Source: https://github.com/kancko/gnome-rounded-blur/archive/v%version/%_name-%version.tar.gz
%else
Source: %_name-%version.tar
%endif

# mutter-50
%define mutter_api_ver 18

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson
BuildRequires: pkgconfig(libmutter-%mutter_api_ver)
BuildRequires: gobject-introspection-devel

%description
A standalone library providing `Blur.BlurEffect` with corner radius
support for GNOME Shell extensions. Basically it's just copy of
[ShellBlurEffect](https://gitlab.gnome.org/GNOME/gnome-shell/-/blob/main/src/shell-blur-effect.c)
with corner mask and different gir namespace (`Blur`).

%package -n %libname
Summary: %name shared library
Group: System/Libraries

%description -n %libname
This package provides shared %namespace library.

%package -n %libname-devel
Summary: Development files for %libname
Group: Development/C
Requires: %libname = %EVR

%description -n %libname-devel
The %libname-devel package provides libraries and header files for
developing applications that use %namespace library.

%package gir
Summary: GObject introspection data for %_name
Group: System/Libraries
Requires: %libname = %EVR

%description gir
GObject introspection data for %_name.

%package gir-devel
Summary: GObject introspection devel data for %_name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %libname-devel = %EVR

%description gir-devel
GObject introspection devel data for %_name.

%prep
%setup -n %_name-%version

%build
%meson
%meson_build

%install
%meson_install

%check
%__meson_test

%files -n %libname
%_libdir/%libname-%api_ver.so.*
%doc README*

%files -n %libname-devel
%_includedir/%__name-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%__name-%api_ver.pc

%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir

%changelog
* Thu May 14 2026 Yuri N. Sedunov <aris@altlinux.org> 1.0.1-alt1
- first build for sisyphus


