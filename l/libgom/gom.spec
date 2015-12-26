%define _name gom
%define ver_major 0.3
%define api_ver 1.0
%def_enable introspection
%def_enable gtk_doc

Name: lib%_name
Version: %ver_major.2
Release: alt1

Summary: A GObject to SQLite object mapper
Group: System/Libraries
License: LGPLv2.1+
Url: https://wiki.gnome.org/Projects/Gom

Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
#Source: %name-%version.tar

%define glib_ver 2.36
%define sqlite_ver 3.7

BuildPreReq: libgio-devel >= %glib_ver libsqlite3-devel >= %sqlite_ver
BuildRequires: gnome-common intltool gtk-doc
%{?_enable_introspection:BuildRequires: gobject-introspection-devel}
# for check
BuildRequires: libgdk-pixbuf-devel

%description
Gom provides an object mapper from GObjects to SQLite. It helps you write
applications that need to store structured data as well as make complex
queries upon that data.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

%description devel
This package contains libraries and header files needed for
development using %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the Gom library.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-gir = %version-%release
Requires: %name-devel = %version-%release

%description gir-devel
GObject introspection devel data for the Gom library.

%package devel-doc
Summary: Development documentation for %name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name < %version-%release

%description devel-doc
This package contains development documentation for the Gom library.

%prep
%setup -n %_name-%version

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc} \
	--disable-static
%make_build

%install
%makeinstall_std

%find_lang %_name

%check
%make check

%files -f %_name.lang
%_libdir/%name-%api_ver.so.*
%doc NEWS README

%files devel
%_includedir/%_name-%api_ver/
%_libdir/%name-%api_ver.so
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled introspection
%files gir
%_typelibdir/Gom-%api_ver.typelib

%files gir-devel
%_girdir/Gom-%api_ver.gir
%endif

%if_enabled gtk_doc
%files devel-doc
%_datadir/gtk-doc/html/*
%endif

%changelog
* Sat Dec 26 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.2-alt1
- 0.3.2

* Wed Apr 29 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.1-alt1
- 0.3.1

* Tue Feb 24 2015 Yuri N. Sedunov <aris@altlinux.org> 0.3.0-alt1
- first build for Sisyphus



