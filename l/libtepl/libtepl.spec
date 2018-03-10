%define _name tepl
%define ver_major 3.99
%define api_ver 4

%def_disable static
%def_disable gtk_doc
%def_enable introspection

Name: lib%_name
Version: %ver_major.1
Release: alt1

Summary: GTK+ Text Editor Framework
License: %lgpl2plus
Group: System/Libraries
Url:  https://wiki.gnome.org/Projects/Tepl

Source: %gnome_ftp/%_name/%ver_major/%_name-%version.tar.xz
Source1: pkg.m4

%define glib_ver 2.52
%define gtk_doc_ver 1.0
%define gtk_ver 3.22
%define gtksource_ver 3.99.7

BuildPreReq: rpm-build-gnome rpm-build-licenses
BuildPreReq: glib2-devel >= %glib_ver libgtk+3-devel >= %gtk_ver libgtksourceview4-devel >= %gtksource_ver
BuildPreReq: libxml2-devel libuchardet-devel gtk-doc >= %gtk_doc_ver
BuildRequires: vala-tools
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 0.6.7 libgtk+3-gir-devel libgtksourceview4-gir-devel}

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

%package -n libamtk
Summary: Actions, Menus and Toolbars Kit
Group: System/Libraries

%description -n libamtk
Amtk is a library that eases the development of GtkSourceView-based text
editors and IDEs.

%package -n libamtk-devel
Summary: Development environment for Amtk
Group: Development/C
Requires: libamtk = %version-%release

%description -n libamtk-devel
This package contains the necessary components to develop for Amtk,
Actions, Menus and Toolbars Kit.

%package -n libamtk-devel-doc
Summary: Development documentation for Amtk
Group: Development/C
BuildArch: noarch
Conflicts: libamtk < %version-%release

%description -n libamtk-devel-doc
Amtk is a library that eases the development of GtkSourceView-based
text editors and IDEs.

This package contains development documentation for Amtk.

%package -n libamtk-devel-static
Summary: Stuff for developing with Amtk
Group: Development/C
Requires: libamtk-devel = %version-%release

%description -n libamtk-devel-static
This package contains the necessary components to develop statically
linked software for Amtk, Actions, Menus and Toolbars Kit

%package -n libamtk-gir
Summary: GObject introspection data for the Amtk library
Group: System/Libraries
Requires: libamtk = %version-%release

%description -n libamtk-gir
GObject introspection data for the Amtk library

%package -n libamtk-gir-devel
Summary: GObject introspection devel data for the Amtk library
Group: Development/Other
BuildArch: noarch
Requires: libamtk-devel = %version-%release
Requires: libamtk-gir = %version-%release

%description -n libamtk-gir-devel
GObject introspection devel data for the Amtk library


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

%find_lang --output=%_name.lang %_name %{_name}-%api_ver

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

%files -n libamtk
%_libdir/libamtk-%api_ver.so.*
%doc AUTHORS NEWS README

%files -n libamtk-devel
%_includedir/amtk-%api_ver/
%_libdir/libamtk-%api_ver.so
%_pkgconfigdir/amtk-%api_ver.pc
#%_vapidir/*

%files -n libamtk-devel-doc
#%_datadir/gtk-doc/html/amtk-%api_ver/

%if_enabled static
%files -n libamtk-devel-static
%_libdir/%name.a
%endif

%if_enabled introspection
%files -n libamtk-gir
%_typelibdir/Amtk-%api_ver.typelib

%files -n libamtk-gir-devel
%_girdir/Amtk-%api_ver.gir
%endif


%changelog
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



