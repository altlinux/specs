%def_disable snapshot

%define ver_major 6.11
%define api_ver 6
%define namespace Tepl

%def_enable gtk_doc
%def_enable introspection
%def_enable check

Name: libgedit-tepl
Version: %ver_major.0
Release: alt1

Summary: Gedit Technology - Text editor product line
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.gnome.org/World/gedit/libgedit-tepl

Vcs: https://gitlab.gnome.org/World/gedit/libgedit-tepl.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

#Obsoletes: libtepl < 5.8.0-alt1
#Provides: libtepl = %EVR

%define meson_ver 0.64
%define glib_ver 2.64
%define gtk_doc_ver 1.0
%define gtk_ver 3.24
%define handy_ver 1.6
%define gtksource_ver 299.3.0
%define amtk_ver 5.9.0
%define gfls_ver 0.2.0

BuildRequires(pre): rpm-macros-meson rpm-build-gnome %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson >= %meson_ver
BuildRequires: glib2-devel >= %glib_ver
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: pkgconfig(libhandy-1) >= %handy_ver
BuildRequires: libgedit-gtksourceview-devel >= %gtksource_ver
BuildRequires: libxml2-devel libuchardet-devel gtk-doc >= %gtk_doc_ver
BuildRequires: pkgconfig(libgedit-amtk-5) >= %amtk_ver
BuildRequires: pkgconfig(libgedit-gfls-1) >= %gfls_ver
BuildRequires: pkgconfig(gsettings-desktop-schemas)
BuildRequires: vala-tools
BuildRequires: pkgconfig(sysprof-capture-4)
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel
BuildRequires: libgedit-gtksourceview-gir-devel libgedit-amtk-gir-devel}
%{?_enable_check:BuildRequires: xvfb-run}

%description
libgedit-tepl is part of Gedit Technology (https://gedit-technology.github.io/).
It is a library that eases the development of text editors and IDEs based on
GTK.

This package contains shared Tepl library.

%package devel
Summary: Files to compile applications that use %name
Group: Development/C
#Obsoletes: libtepl-devel < 5.8.0-alt1
#Provides: libtepl-devel = %EVR
Requires: %name = %EVR

%description devel
This package contains the files required to develop applications against
the Tepl library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %EVR
BuildArch: noarch
#Obsoletes: libtepl-devel-doc < 5.8.0-alt1
#Provides: libtepl-devel-doc = %EVR

%description devel-doc
libgedit-tepl is part of Gedit Technology (https://gedit-technology.net/).
It is a library that eases the development of text editors and IDEs based on
GTK.
This package provides development documentation for %name.

%package gir
Summary: GObject introspection data for the Tepl library
Group: System/Libraries
Requires: %name = %EVR
Conflicts: libtepl-gir
#Obsoletes: libtepl-gir < 5.8.0-alt1
#Provides: libtepl-gir = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the Tepl library
Group: Development/Other
BuildArch: noarch
Conflicts: libtepl-gir-devel
#Obsoletes: libtepl-gir-devel < 5.8.0-alt1
#Provides: libtepl-gir-devel = %EVR
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the %name library

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
%_gtk_docdir/*
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
* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 6.11.0-alt1
- first build for Sisyphus




