%define _name gtef
%define ver_major 2.0
%define api_ver 2
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: GTK+ Text Editor Framework
License: %lgpl2plus
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Gtef

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
Source1: pkg.m4

%define glib_ver 2.51.5
%define gtk_doc_ver 1.0
%define gtksource_ver 3.22

BuildPreReq: rpm-build-gnome rpm-build-licenses gnome-common
BuildPreReq: glib2-devel >= %glib_ver libgtksourceview3-devel >= %gtksource_ver
BuildPreReq: libxml2-devel libuchardet-devel gtk-doc >= %gtk_doc_ver
BuildRequires: vala-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel libgtksourceview3-gir-devel}

%description
Gtef is a library that eases the development of GtkSourceView-based
text editors and IDEs. Gtef is the acronym for "GTK+ Text Editor
Framework".

%package devel
Summary: Development environment for Gtef
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the necessary components to develop for Gtef,
GTK+ Text Editor Framework.

%package devel-doc
Summary: Development documentation for Gtef
Group: Development/C
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
Gtef is a library that eases the development of GtkSourceView-based
text editors and IDEs. Gtef is the acronym for "TK+ Text Editor
Framework"

This package contains development documentation for Gtef.

%package devel-static
Summary: Stuff for developing with Gtef
Group: Development/C
Requires: %name-devel = %version-%release

%description devel-static
This package contains the necessary components to develop statically
linked software for Gtef, GTK+ Text Editor Framework

%package gir
Summary: GObject introspection data for the Gtef library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gtef library

%package gir-devel
Summary: GObject introspection devel data for the Gtef library
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %version-%release
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the Gtef library

%prep
%setup -n %_name-%version
[ ! -d m4 ] && mkdir m4
cp -f %SOURCE1 m4/
# automake-1.15 required
rm -rf missing aclocal.m4 /m4/libtool.m4 m4/lt*.m4

%build
%autoreconf -I m4
%configure %{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%install
%makeinstall_std

%find_lang --output=%_name.lang %_name %{_name}-2

%files -f %_name.lang
%_libdir/*.so.*
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%_vapidir/*

%files devel-doc
%_datadir/gtk-doc/html/*

%if_enabled static
%files devel-static
%_libdir/*.a
%endif

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%changelog
* Fri Apr 21 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.1-alt1
- 2.0.1

* Sun Mar 19 2017 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- first build for Sisyphus

