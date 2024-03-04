%def_disable snapshot

%define _name gom
%define ver_major 0.5
%define api_ver 1.0
%def_enable introspection
%def_enable gtk_doc
%def_enable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A GObject to SQLite object mapper
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/Gom
Vcs: https://gitlab.gnome.org/GNOME/gom.git

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

%define glib_ver 2.38
%define sqlite_ver 3.7

BuildRequires(pre): rpm-macros-meson rpm-build-gir rpm-build-python3
BuildRequires: meson
BuildRequires: libgio-devel >= %glib_ver libsqlite3-devel >= %sqlite_ver
%{?_enable_introspection:BuildRequires: gobject-introspection-devel python3-module-pygobject3-devel}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_check:BuildRequires: libgdk-pixbuf-devel}

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex
queries upon that data.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains libraries and header files needed for
development using %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the Gom library.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %EVR
Requires: %name-devel = %EVR

%description gir-devel
GObject introspection devel data for the Gom library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version

%description devel-doc
This package contains development documentation for the Gom library.

%prep
%setup -n %_name-%version

%build
%meson %{?_enable_gtk_doc:-Denable-gtk-doc=true} \
	%{?_enable_introspection:-Denable-introspection=true}
%meson_build

%install
%meson_install

%check
%__meson_test

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Gom-%api_ver.typelib
%python3_sitelibdir/gi/overrides/Gom.py
%python3_sitelibdir/gi/overrides/__pycache__/*

%files gir-devel
%_girdir/Gom-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver/
%endif

%changelog
* Mon Mar 04 2024 Yuri N. Sedunov <aris@altlinux.org> 0.5.0-alt1
- 0.5.0

* Mon Mar 16 2020 Yuri N. Sedunov <aris@altlinux.org> 0.4-alt1
- 0.4
- enabled %%check

* Wed Jun 21 2017 Yuri N. Sedunov <aris@altlinux.org> 0.3.3-alt1
- 0.3.3

* Sat Dec 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Wed Apr 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus



