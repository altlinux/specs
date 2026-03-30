%def_enable snapshot

%define ver_major 5.10
%define api_ver 5
%define namespace Amtk

%def_enable gtk_doc
%def_enable introspection
%def_enable check

Name: libgedit-amtk
Version: %ver_major.0
Release: alt1

Summary: Gedit Technology - Actions, Menus and Toolbars Kit for GTK3 applications
License: LGPL-3.0-or-later
Group: System/Libraries
Url: https://gitlab.gnome.org/World/gedit/libgedit-amtk

Vcs: https://gitlab.gnome.org/World/gedit/libgedit-amtk.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

#Obsoletes: libamtk < 5.8.0-alt1
#Provides: libamtk = %EVR

%define gtk_ver 3.22

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson
BuildRequires: libgtk+3-devel >= %gtk_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: xvfb-run xmllint
BuildRequires: fonts-ttf-roboto fonts-ttf-google-noto-sans-vf}

%description
libgedit-amtk is part of [Gedit Technology](https://gedit-technology.net/).

Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

This package contains shared Amtk library.

%package devel
Summary: Files to compile applications that use %name
Group: Development/C
#Obsoletes: libamtk-devel < 5.8.0-alt1
#Provides: libamtk-devel = %EVR
Requires: %name = %EVR

%description devel
This package contains the files required to develop applications against
the Amtk library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %EVR
BuildArch: noarch
#Obsoletes: libamtk-devel-doc < 5.8.0-alt1
#Provides: libamtk-devel-doc = %EVR

%description devel-doc
libgedit-amtk is part of [Gedit Technology](https://gedit-technology.net/).

Amtk is the acronym for "Actions, Menus and Toolbars Kit". It is a basic
GtkUIManager replacement based on GAction. It is suitable for both a
traditional UI or a modern UI with a GtkHeaderBar.

This package provides development documentation for %name.

%package gir
Summary: GObject introspection data for the Amtk library
Group: System/Libraries
Requires: %name = %EVR
Conflicts: libamtk-gir
#Obsoletes: libamtk-gir < 5.8.0-alt1
#Provides: libamtk-gir = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the Amtk library
Group: Development/Other
BuildArch: noarch
Conflicts: libamtk-gir-devel
#Obsoletes: libamtk-gir-devel < 5.8.0-alt1
#Provides: libamtk-gir-devel = %EVR
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
* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 5.10.0-alt1
- 5.10.0

* Tue Nov 18 2025 Yuri N. Sedunov <aris@altlinux.org> 5.9.2-alt1
- 5.9.2

* Tue Apr 08 2025 Yuri N. Sedunov <aris@altlinux.org> 5.9.1-alt1
- 5.9.1

* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 5.9.0-alt1
- 5.9.0

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 5.8.0-alt1
- first build for Sisyphus




