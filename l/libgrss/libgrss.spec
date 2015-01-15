%define ver_major 0.6
%define api_ver %ver_major
%def_enable introspection
%def_enable gtk_doc

Name: libgrss
Version: %ver_major
Release: alt1

Summary: A Glib-based library to manage RSS and Atom feeds
Group: System/Libraries
License: LGPLv2+
Url: https://wiki.gnome.org/

Source: ftp://ftp.gnome.org/%name/%ver_major/%name-%version.tar.xz

%define glib_ver 2.42.1
%define soup_ver 2.48.0

BuildPreReq: libgio-devel >= %glib_ver libsoup-devel >= %soup_ver
BuildRequires: libxml2-devel gnome-common intltool gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel libsoup-gir-devel}

%description
libgrss is a Glib abstaction to handle feeds in RSS, Atom and other formats.
His code derives from the Liferea feeds reader: http://liferea.sourceforge.net/

%package devel
Summary: Development files for %name
Group: Development/C++
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using %name.

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
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for %name library.

%prep
%setup

# fix wrong {typelib,gir}dir
subst 's/\$(libdir)\/girepository-%api_ver/\$(INTROSPECTION_TYPELIBDIR)/
       s/\$(datadir)\/gir-%api_ver/\$(INTROSPECTION_GIRDIR)/' src/Makefile.am

%build
%autoreconf
%configure --disable-static \
	%{?_enable_gtk_doc:--enable-gtk-doc}
%make_build

%install
%makeinstall_std

%check
%make check

%files
%_libdir/%name-%api_ver.so.*
%doc NEWS README

%files devel
%_includedir/%name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Grss-%api_ver.typelib

%files gir-devel
%_girdir/Grss-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Thu Jan 15 2015 Yuri N. Sedunov <aris@altlinux.org> 0.6-alt1
- first build for Sisyphus

