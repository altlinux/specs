%define _name clutter-gtk
%define ver_major 1.2
%define api_ver 1.0
%def_enable introspection

Name: %{_name}3
Version: %ver_major.0
Release: alt1

Summary: Library integrating clutter with GTK+3
License: LGPL v2+
Group: System/Libraries
Url: http://www.clutter-project.org/
Packager: GNOME Maintainers Team <gnome@packages.altlinux.org>

Source: http://source.clutter-project.org/sources/%_name/%ver_major/%_name-%version.tar.xz

BuildRequires: libgtk+3-devel >= 3.2.0 libclutter-devel >= 1.10.0
%{?_enable_introspection:BuildRequires: libjson-glib-gir-devel libclutter-gir-devel libgtk+3-gir-devel}

%description
Library integrating clutter with GTK+

%package -n lib%name
Summary: Library integrating clutter with GTK+
Group: System/Libraries

%description -n lib%name
Library integrating clutter with GTK+

%package -n lib%name-devel
Summary: Header files for clutter-gtk library
Group: Development/Other
Requires: lib%name = %version-%release

%description -n lib%name-devel
Header files for clutter-gtk library

%package -n lib%name-devel-doc
Summary: Documentation for clutter-gtk library
Group: Development/Other
BuildArch: noarch
Conflicts: lib%name-devel < %version

%description -n lib%name-devel-doc
Development documentation files for clutter-gtk library

%package -n lib%name-gir
Summary: GObject introspection data for the clutter-gtk library
Group: System/Libraries
Requires: lib%name = %version-%release
Requires: gir-repository libclutter-gir

%description -n lib%name-gir
GObject introspection data for the clutter-gtk library

%package -n lib%name-gir-devel
Summary: GObject introspection devel data for the clutter-gtk library
Group: System/Libraries
BuildArch: noarch
Requires: lib%name-gir = %version-%release
Requires: gir-repository-devel libclutter-gir-devel

%description -n lib%name-gir-devel
GObject introspection devel data for the clutter-gtk library

%prep
%setup -q -n %_name-%version
touch AUTHORS

%build
%configure \
	--disable-gtk-doc \
	%{subst_enable introspection} \
	--disable-static

%make_build

%install
%make DESTDIR=%buildroot install

%find_lang cluttergtk-%api_ver

%files -n lib%name -f cluttergtk-%api_ver.lang
%doc AUTHORS NEWS
%_libdir/lib%_name-*.so.*

%files -n lib%name-devel
%_includedir/%_name-*
%_libdir/lib%_name-*.so
%_pkgconfigdir/*.pc

%files -n lib%name-devel-doc
%_datadir/gtk-doc/html/*

%if_enabled introspection
%files -n lib%name-gir
%_typelibdir/*.typelib

%files -n lib%name-gir-devel
%_girdir/*.gir
%endif

%changelog
* Fri Mar 23 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Mar 06 2012 Yuri N. Sedunov <aris@altlinux.org> 1.1.2-alt1
- 1.1.2

* Tue Sep 27 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.4-alt1
- 1.0.4

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Fri Feb 25 2011 Yuri N. Sedunov <aris@altlinux.org> 0.91.8-alt1
- first build for Sisyphus

