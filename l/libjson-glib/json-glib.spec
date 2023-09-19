%def_disable snapshot
%define _libexecdir %_prefix/libexec

%define _name json-glib
%define ver_major 1.8
%define api_ver 1.0
%def_disable symbol_versioning
%def_enable gtk_doc
%def_enable man
%def_enable introspection
%def_enable check

Name: lib%_name
Version: %ver_major.0
Release: alt1

Summary: GLib-based JSON manipulation library
Group: System/Libraries
License: LGPLv2.1
Url: https://wiki.gnome.org/Projects/JsonGlib

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
Patch: json-glib-1.6.6-alt-doc_build.patch
# https://gitlab.gnome.org/GNOME/json-glib/-/issues/33
# --default-symver breaks set-versioned dependencies, revert it
Patch1: json-glib-1.6.4-alt-remove_symbol_versioning.patch

%define glib_ver 2.54
%define gi_ver 0.10.5

BuildRequires(pre): rpm-macros-meson
BuildRequires: meson glib2-devel >= %glib_ver
%{?_enable_static:BuildRequires: glibc-devel-static}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= %gi_ver}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}
%{?_enable_man:BuildRequires: xsltproc docbook-dtds docbook-style-xsl}

%description
JSON-GLib implements a full JSON parser using GLib and GObject. Use
JSON-GLib it is possible to parse and generate valid JSON data
structures, using a DOM-like API. JSON-GLib also offers GObject
integration, providing the ability to serialize and deserialize GObject
instances to and from JSON data types.

%package devel
Summary: Development files for %_name
Group: Development/C
Requires: %name = %EVR

%description devel
The %name-devel package contains libraries and header files for
developing applications that use %name.

%package gir
Summary: GObject introspection data for the JSON-GLib library
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the JSON-GLib library

%package gir-devel
Summary: GObject introspection devel data for the JSON-GLib library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the JSON-GLib library

%package devel-doc
Summary: Development package for JSON-GLib
Group: Development/Documentation
BuildArch: noarch
Conflicts: lib%name < %version

%description devel-doc
This package contains developer documentation for the JSON-GLib library.

%package tests
Summary: Tests for the %_name package
Group: Development/Other
Requires: %name = %EVR

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed %_name library.

%prep
%setup -n %_name-%version
%patch -b .doc
%{?_disable_symbol_versioning:%patch1 -p1 -b .symver}

%build
%meson %{?_disable_introspection:-Dintrospection=disabled} \
    %{?_disable_gtk_doc:-Dgtk_doc=disabled} \
    %{?_enable_man:-Dman=true}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%_name.lang %_name-%api_ver

%check
%__meson_test

%files -f %_name.lang
%_bindir/%_name-format
%_bindir/%_name-validate
%_libdir/*.so.*
%if_enabled man
%_man1dir/%_name-format.1.*
%_man1dir/%_name-validate.1.*
%endif
%doc NEWS README.md

%files devel
%_libdir/*.so
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Json-%api_ver.typelib

%files gir-devel
%_girdir/Json-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver
%endif

%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/

%changelog
* Sat Sep 16 2023 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Mon May 09 2022 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- updated to 1.6.6-20-g23ae2f5
- made symbol versioning introduced in 1.5.2 optional (disabled by default)

* Tue Aug 17 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Feb 09 2021 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Fri Sep 11 2020 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0
- new devel-doc subpackage

* Tue Sep 18 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Tue May 08 2018 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1.1
- rebuilt for e2kv4

* Tue Sep 12 2017 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Sat Mar 18 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.8-alt1
- 1.2.8

* Mon Mar 13 2017 Yuri N. Sedunov <aris@altlinux.org> 1.2.6-alt1
- 1.2.6

* Fri Jul 29 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.2-alt1
- 1.2.2

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Wed Mar 02 2016 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Sun Jan 24 2016 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt2
- fixed build with glib >= 2.46

* Mon Mar 16 2015 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Sun Jun 01 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.2-alt1
- 1.0.2

* Tue Mar 25 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Tue Mar 18 2014 Yuri N. Sedunov <aris@altlinux.org> 0.99.2-alt1
- 0.99.2

* Sat Sep 21 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.2-alt1
- 0.16.2

* Tue Apr 16 2013 Yuri N. Sedunov <aris@altlinux.org> 0.16.0-alt1
- 0.16.0

* Wed Sep 19 2012 Yuri N. Sedunov <aris@altlinux.org> 0.15.2-alt1
- 0.15.2

* Thu Nov 03 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.2-alt1
- 0.14.2

* Mon Sep 19 2011 Yuri N. Sedunov <aris@altlinux.org> 0.14.0-alt1
- 0.14.0

* Wed Jun 15 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.6-alt1
- 0.12.6

* Tue Apr 12 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.4-alt1
- 0.12.4

* Sun Jan 16 2011 Yuri N. Sedunov <aris@altlinux.org> 0.12.2-alt1
- 0.12.2

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 0.12.0-alt1
- 0.12.0

* Wed Mar 31 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt2
- rebuild with new rpm-build-gir (0.2-alt1)

* Fri Mar 19 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.4-alt1
- 0.10.4

* Mon Mar 08 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt2
- rebuild using rpm-build-gir

* Fri Feb 26 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.2-alt1
- 0.10.2

* Fri Jan 08 2010 Yuri N. Sedunov <aris@altlinux.org> 0.10.0-alt1
- 0.10.0
- new -gir{,-devel} subpackages
- %%check section

* Mon Jun 22 2009 Yuri N. Sedunov <aris@altlinux.org> 0.7.2-alt1
- 0.7.2

* Tue Nov 11 2008 Yuri N. Sedunov <aris@altlinux.org> 0.6.2-alt1
- adapted for Sisyphus

* Sat May 31 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.2-1
- Update to 0.6.2.
- Enable tests.

* Mon May 19 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.6.0-1
- Update 0.6.0.
- Disable tests for now.
- Add requires on gtk-doc.

* Sun Apr 20 2008 Brian Pepple <bpepple@fedoraproject.org> - 0.4.0-1
- Initial Fedora spec.

