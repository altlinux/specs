%define _name gtksourceview
%define ver_major 3.99
%define api_ver 4

%def_disable static
%def_disable gtk_doc
%def_enable introspection
%def_enable vala
%def_enable installed_tests
%def_enable gspell

Name: lib%{_name}4
Version: %ver_major.7
Release: alt1

Summary: GtkSourceView text widget library
License: LGPLv2+
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/GtkSourceView

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz

# From configure.ac
%define gtk_ver 3.22.0
%define libxml2_ver 2.6.0
%define gspell_ver 1.2.0

BuildPreReq: rpm-build-gnome

# From configure.ac
BuildRequires: gcc-c++ autoconf-archive gtk-doc itstool
BuildPreReq: libgtk+3-devel >= %gtk_ver
BuildPreReq: libxml2-devel >= %libxml2_ver
BuildRequires: perl-XML-Parser zlib-devel
%{?_enable_gspell:BuildRequires: libgspell-devel >= %gspell_ver}
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.9.5 libgtk+3-gir-devel}
%{?_enable_vala:BuildRequires: vala-tools libvala-devel}
# for check
BuildRequires: xvfb-run valgrind

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
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the GtkSourceView library

%package tests
Summary: Tests for the GtkSourceView library
Group: Development/Other
Requires: %name = %version-%release

%description tests
This package provides tests programs that can be used to verify
the functionality of the installed GtkSourceView library.

%define _gtk_docdir %_datadir/gtk-doc/html

%prep
%setup -n %_name-%version

%build
%configure \
	%{subst_enable static} \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	%{subst_enable introspection} \
	%{?_enable_installed_tests:--enable-installed-tests}

%make_build

%install
%makeinstall_std
%find_lang %_name-%api_ver

%check
xvfb-run %make check

%files -f %_name-%api_ver.lang
%_libdir/lib%_name-%api_ver.so.*
%_datadir/%_name-%api_ver/
%doc AUTHORS NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/lib%_name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc
%if_enabled vala
%_vapidir/%_name-%api_ver.deps
%_vapidir/%_name-%api_ver.vapi
%endif
%doc HACKING

%files devel-doc
%_gtk_docdir/*

%if_enabled introspection
%files gir
%_typelibdir/GtkSource-%api_ver.typelib

%files gir-devel
%_girdir/GtkSource-%api_ver.gir
%endif

%if_enabled installed_tests
%files tests
%_libexecdir/installed-tests/%_name-%api_ver/
%_datadir/installed-tests/%_name-%api_ver/
%endif


%changelog
* Sat Dec 09 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.7-alt1
- 3.99.7

* Tue Oct 17 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.6-alt1
- 3.99.6

* Wed Sep 06 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.5-alt1
- 3.99.5

* Sun Apr 23 2017 Yuri N. Sedunov <aris@altlinux.org> 3.99.4-alt1
- 3.99.4

* Wed Nov 16 2016 Yuri N. Sedunov <aris@altlinux.org> 3.99.2-alt1
- first build for Sisyphus




