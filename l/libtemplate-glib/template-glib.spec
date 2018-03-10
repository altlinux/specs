%def_disable snapshot

%define _name template-glib
# probably meson bug
%define libname libtemplate_glib
%define ver_major 3.28
%define api_ver 1.0

%def_enable introspection
%def_enable gtk_doc

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: A templating library for GLib
Group: System/Libraries
License: LGPLv2.1
Url: https://wiki.gnome.org/Projects/TemplateGlib

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %name-%version.tar
%endif

BuildRequires: meson >= 0.38.1 bison flex gtk-doc vala-tools
BuildRequires: libgio-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}

%description
Template-GLib is a templating library for GLib. It includes a simple
template format along with integration into GObject-Introspection for
properties and methods. It separates the parsing of templates and the
expansion of templates for faster expansion. You can also define scope,
custom functions, and more with the embedded expression language.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the %name library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name library

%package gir-devel
Summary: GObject introspection devel data for the %name library
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the %name library

%package devel-doc
Summary: Development documentation for %name
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name

%prep
%setup -n %_name-%version

%build
%meson %{?_enable_gtk_doc:-Denable_gtk_doc=true}
%meson_build

%install
%meson_install

%find_lang %_name

%check
%meson_test

%files -f %_name.lang
%_libdir/%libname-%api_ver.so.*
%doc README.md NEWS AUTHORS

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%libname-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi

%if_enabled introspection
%files gir
%_typelibdir/Template-%api_ver.typelib

%files gir-devel
%_girdir/Template-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
* Wed Mar 14 2018 Yuri N. Sedunov <aris@altlinux.org> 3.28.0-alt1
- 3.28.0

* Wed Oct 04 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.1-alt1
- 3.26.1

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 3.26.0-alt1
- 3.26.0

* Wed Jun 07 2017 Yuri N. Sedunov <aris@altlinux.org> 3.25.2-alt1
- first build for Sisyphus

