%def_disable snapshot

%define ver_major 0.2
%define api_ver 1
%define namespace Gfls

%def_enable gtk_doc
%def_enable introspection
%def_enable check

Name: libgedit-gfls
Version: %ver_major.0
Release: alt1

Summary: Gedit Technology - File loading and saving library
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://gitlab.gnome.org/World/gedit/libgedit-gfls

Vcs: https://gitlab.gnome.org/World/gedit/libgedit-gfls.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.78
%define gtk_ver 3.22

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: xvfb-run}

%description
libgedit-gfls is part of
[Gedit Technology](https://gedit-technology.net/).

It is a module dedicated to file loading and saving for the needs of gedit and
other similar text editors.

This package contains shared gfls library.

%package devel
Summary: Files to compile applications that use %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the files required to develop applications against
the %name library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %EVR
BuildArch: noarch

%description devel-doc
libgedit-gfls is part of
[Gedit Technology](https://gedit-technology.net/).

This package provides development documentation for %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library.

%package tests
Summary: Tests for the %name library
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %name library.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup

%build
%meson \
    %{subst_enable_meson_bool gtk_doc gtk_doc} \
    %{subst_enable_meson_bool introspection gobject_introspection}
%nil
%meson_build

%install
%meson_install
%find_lang %name-%api_ver

%check
xvfb-run %__meson_test

%files -f %name-%api_ver.lang
%_libdir/%name-%api_ver.so.*
%doc NEWS README*

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%if_enabled vala
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi
%endif

%if_enabled gtk_doc
%files devel-doc
%_gtk_docdir/%name-%api_ver/
%endif

%if_enabled introspection
%files gir
%_typelibdir/%namespace-%api_ver.typelib

%files gir-devel
%_girdir/%namespace-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%name-%api_ver/
%_datadir/installed-tests/%name-%api_ver/
%endif

%changelog
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 0.2.0-alt1
- first build for Sisyphus




