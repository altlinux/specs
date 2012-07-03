%define _name gtksourceview
%define api_ver 3.0
%define ver_major 3.4
%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: lib%{_name}3
Version: %ver_major.2
Release: alt1

Summary: GtkSourceView text widget library
License: LGPLv2+
Group: System/Libraries
Url: http://www.gnome.org
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

# From configure.ac
%define intltool_ver 0.40
%define gtk_ver 2.91.6
%define libxml2_ver 2.6.0

BuildPreReq: rpm-build-gnome

# From configure.ac
BuildPreReq: gnome-common
BuildPreReq: intltool >= %intltool_ver
BuildPreReq: gtk-doc >= 1.11
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver

BuildRequires: gcc-c++ perl-XML-Parser zlib-devel libgio-devel
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel}

%description
GtkSourceView is a text widget that extends the standard gtk+ 2.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package contains shared GtkSourceView library.

%package devel
Summary: Files to compile applications that use GtkSourceView
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains the files required to develop applications against
the GtkSourceView library.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
GtkSourceView is a text widget that extends the standard gtk+ 3.x text
widget GtkTextView. It improves GtkTextView by implementing syntax
highlighting and other features typical of a source editor.

This package provides development documentation for %_name.

%package gir
Summary: GObject introspection data for the GtkSourceView library
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the GtkSourceView library

%package gir-devel
Summary: GObject introspection devel data for the GtkSourceView library
Group: System/Libraries
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the GtkSourceView library

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -q -n %_name-%version

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection}

%make_build

%check
# display required
#%%make check

%install
%make_install DESTDIR=%buildroot install

%find_lang %_name-%api_ver

%files -f %_name-%api_ver.lang
%_libdir/*.so.*
%_datadir/%_name-%api_ver
%doc AUTHORS NEWS README

%files devel
%_includedir/*
%_libdir/*.so
%_pkgconfigdir/*
%doc HACKING MAINTAINERS

%files devel-doc
%_gtk_docdir/*

%if_enabled introspection
%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*
%endif

%changelog
* Tue May 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Tue Apr 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Mar 26 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Tue Nov 08 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.3-alt1
- 3.2.3

* Sun Oct 16 2011 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Fri Jul 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.5-alt1
- 3.0.5

* Mon Jun 20 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.4-alt1
- 3.0.4

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Wed May 25 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Tue Apr 26 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.0-alt1
- 3.0.0

* Tue Mar 22 2011 Yuri N. Sedunov <aris@altlinux.org> 2.91.9-alt1
- 2.91.9

* Sat Jun 26 2010 Yuri N. Sedunov <aris@altlinux.org> 2.90.3-alt1
- first build for Sisyphus.

