%def_enable snapshot

%define ver_major 299
%define api_ver 300
%define namespace GtkSource

%def_enable gtk_doc
%def_enable introspection
%def_enable check

Name: libgedit-gtksourceview
Version: %ver_major.7.1
Release: alt1

Summary: Gedit Technology - Source code editing widget
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://gitlab.gnome.org/World/gedit/libgedit-gtksourceview

Vcs: https://gitlab.gnome.org/World/gedit/libgedit-gtksourceview.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define gtk_ver 3.24
%define libxml2_ver 2.6.0
%define gfls_ver 0.4.0
%define amtk_ver 5.10

BuildRequires(pre): rpm-macros-meson %{?_enable_introspection:rpm-build-gir}
BuildRequires: meson
BuildRequires: libgtk+3-devel >= %gtk_ver
BuildRequires: libxml2-devel >= %libxml2_ver
BuildRequires: pkgconfig(libgedit-gfls-1) >= %gfls_ver
BuildRequires: pkgconfig(libgedit-amtk-5) >= %amtk_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libgtk+3-gir-devel}
%{?_enable_gtk_doc:BuildRequires: gtk-doc}
%{?_enable_check:BuildRequires: xvfb-run xmllint
BuildRequires: fonts-ttf-roboto fonts-ttf-google-noto-sans-vf}

%description
libgedit-gtksourceview is part of
[Gedit Technology](https://gedit-technology.net/).

libgedit-gtksourceview is a library that extends GtkTextView, the
standard GTK widget for multiline text editing. This library adds support
for syntax highlighting, undo/redo, file loading and saving, search and
replace, a completion system, printing, displaying line numbers, and
other features typical of a source code editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
Conflicts: %name < %EVR
BuildArch: noarch

%description devel-doc
libgedit-gtksourceview is part of
[Gedit Technology](https://gedit-technology.net/).

libgedit-gtksourceview is a library that extends GtkTextView, the
standard GTK widget for multiline text editing. This library adds support
for syntax highlighting, undo/redo, file loading and saving, search and
replace, a completion system, printing, displaying line numbers, and
other features typical of a source code editor.

This package provides development documentation for %name.

%package gir
Summary: GObject introspection data for the GtkSourceView library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: Development/Other
BuildArch: noarch
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
%_datadir/%name-%api_ver/
%doc NEWS README*

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc
%if_enabled vala
%_vapidir/%name-%api_ver.deps
%_vapidir/%name-%api_ver.vapi
%endif
%doc CONTRIBUTING

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
* Sat Jun 27 2026 Yuri N. Sedunov <aris@altlinux.org> 299.7.1-alt1
- 299.7.1

* Mon Mar 30 2026 Yuri N. Sedunov <aris@altlinux.org> 299.7.0-alt1
- 299.7.0

* Sun Jan 04 2026 Yuri N. Sedunov <aris@altlinux.org> 299.6.0-alt1
- 299.6.0

* Tue Apr 08 2025 Yuri N. Sedunov <aris@altlinux.org> 299.5.0-alt1
- 299.5.0

* Sun Dec 08 2024 Yuri N. Sedunov <aris@altlinux.org> 299.4.0-alt1
- 299.4.0

* Mon Sep 16 2024 Yuri N. Sedunov <aris@altlinux.org> 299.3.0-alt1
- 299.3.0

* Fri Feb 16 2024 Yuri N. Sedunov <aris@altlinux.org> 299.1.0-alt1
- 299.1.0

* Thu Dec 07 2023 Yuri N. Sedunov <aris@altlinux.org> 299.0.5-alt1
- 299.0.5

* Sat Jul 29 2023 Yuri N. Sedunov <aris@altlinux.org> 299.0.4-alt1
- 299.0.4

* Fri Jun 23 2023 Yuri N. Sedunov <aris@altlinux.org> 299.0.3-alt1
- first build for Sisyphus




