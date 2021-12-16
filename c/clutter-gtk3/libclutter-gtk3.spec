%def_disable snapshot
%define _name clutter-gtk
%define ver_major 1.8
%define api_ver 1.0
%def_enable introspection
%def_enable docs

Name: %{_name}3
Version: %ver_major.4
Release: alt1.1

Summary: Library integrating clutter with GTK+3
License: LGPL-2.1-or-later
Group: System/Libraries
Url: https://wiki.gnome.org/Projects/Clutter

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif
BuildRequires(pre): rpm-macros-meson
BuildRequires: meson libgtk+3-devel >= 3.21.0 libclutter-devel >= 1.24
%{?_enable_docs:BuildRequires: gtk-doc}
%{?_enable_introspection:BuildRequires(pre): rpm-build-gir
BuildRequires: libjson-glib-gir-devel libcogl-gir-devel libclutter-gir-devel libgtk+3-gir-devel}

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
%setup -n %_name-%version
touch AUTHORS

%build
%meson \
    %{?_enable_docs:-Denable_docs=true}
%nil
%meson_build

%install
%meson_install

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
* Thu Dec 16 2021 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1.1
- fixed meson options
- fixed License tag

* Mon Aug 14 2017 Yuri N. Sedunov <aris@altlinux.org> 1.8.4-alt1
- 1.8.4

* Sun Sep 18 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.2-alt1
- 1.8.2

* Mon Mar 28 2016 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Oct 13 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.6-alt1
- 1.6.6

* Tue Sep 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.4-alt1
- 1.6.4

* Tue Jun 30 2015 Yuri N. Sedunov <aris@altlinux.org> 1.6.2-alt1
- 1.6.2

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0

* Fri Aug 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.4-alt1
- 1.5.4

* Wed Feb 19 2014 Yuri N. Sedunov <aris@altlinux.org> 1.5.2-alt1
- 1.5.2

* Wed Feb 05 2014 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt3
- rebuilt against libcogl.so.19

* Mon Aug 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt2
- rebuilt against libcogl.so.15

* Tue Mar 19 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4.4-alt1
- 1.4.4

* Fri Feb 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt2
- rebuilt against libcogl.so.12

* Mon Dec 17 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.2-alt1
- 1.4.2

* Thu Oct 18 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.0-alt1
- 1.4.0

* Sat Sep 08 2012 Yuri N. Sedunov <aris@altlinux.org> 1.3.2-alt1
- 1.3.2

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

