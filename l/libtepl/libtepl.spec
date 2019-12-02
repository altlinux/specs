%define _libexecdir %_prefix/libexec

%define _name tepl
%define ver_major 4.2
%define api_ver 4

%def_disable static
%def_disable gtk_doc
%def_enable introspection
# display required
%def_disable check
%def_enable installed_tests

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: GTK+ Text Editor Framework
License: %lgpl2plus
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Tepl

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

%define glib_ver 2.52
%define gtk_doc_ver 1.0
%define gtk_ver 3.22
%define gtksource_ver 3.99.7
%define amtk_ver 5.0.0

BuildRequires(pre): rpm-build-gnome rpm-build-licenses rpm-build-gir
BuildRequires: glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libgtksourceview4-devel >= %gtksource_ver
BuildRequires: libxml2-devel libuchardet-devel gtk-doc >= %gtk_doc_ver
BuildRequires: libamtk-devel >= %amtk_ver
BuildRequires: vala-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel libgtksourceview4-gir-devel libamtk-gir-devel}

%description
Tepl is a library that eases the development of GtkSourceView-based
text editors and IDEs. Tepl is the acronym for "Text editor product
line".

%package devel
Summary: Development environment for Tepl
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop for Tepl,
GTK+ Text Editor Framework.

%package devel-doc
Summary: Development documentation for Tepl
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
Tepl is a library that eases the development of GtkSourceView-based
text editors and IDEs. Tepl is the acronym for "TK+ Text Editor
Framework"

This package contains development documentation for Tepl.

%package devel-static
Summary: Stuff for developing with Tepl
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the necessary components to develop statically
linked software for Tepl, GTK+ Text Editor Framework

%package gir
Summary: GObject introspection data for the Tepl library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Tepl library

%package gir-devel
Summary: GObject introspection devel data for the Tepl library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Tepl library

%package tests
Summary: Tests for the Tepl library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed Tepl library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{?_enable_installed_tests:--enable-installed-tests}

%make_build

%install
%makeinstall_std
%find_lang --output=%_name.lang %_name %{_name}-%api_ver

%check
%make check

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
#%_vapidir/*

%files devel-doc
%_datadir/gtk-doc/html/%_name-%{api_ver}.0/

%if_enabled static
%files devel-static
%_libdir/%name-%api_ver.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/Tepl-%api_ver.typelib

%files gir-devel
%_girdir/Tepl-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Mon Dec 02 2019 Yuri N. Sedunov <aris@altlinux.org> 4.2.1-alt1
- 4.2.1

* Mon Jul 16 2018 Yuri N. Sedunov <aris@altlinux.org> 4.2.0-alt1
- 4.2.0 (ALT #35073)

* Sun Apr 08 2018 Yuri N. Sedunov <aris@altlinux.org> 4.0.0-alt1
- 4.0.0

* Wed Feb 28 2018 Yuri N. Sedunov <aris@altlinux.org> 3.99.1-alt1
- 3.99.1

* Sat Sep 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Sun Aug 20 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.4-alt1
- 2.99.4

* Tue Jul 18 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.2-alt1
- 2.99.2

* Wed Jul 05 2017 Yuri N. Sedunov <aris@altlinux.org> 2.99.1-alt1
- first build for Sisyphus



