%def_disable snapshot

%define _name libpeas
%define ver_major 2.0
%define api_ver 2

%def_enable gjs
# not ready for lua-5.3
%def_disable lua
%def_enable introspection
%def_disable vala
%def_enable gtk_doc
%def_enable check
# no demo
%def_disable demo

Name: %_name%api_ver
Version: %ver_major.0
Release: alt1

Summary: A gobject-based plugins engine
Group: System/Libraries
License: LGPL-2.1-or-later
Url: https://wiki.gnome.org/Projects/Libpeas

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

BuildRequires(pre): rpm-macros-meson rpm-build-gir
BuildRequires: meson gnome-common
BuildRequires: libgio-devel >= 2.74.0
# for python3 support
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-pygobject3-devel >= 3.2.0
%{?_enable_introspection:BuildRequires: gobject-introspection-devel >= 1.39}
%{?_enable_gjs:BuildRequires: libgjs-devel >= 1.77.1 libmozjs115-devel gcc-c++}
%{?_enable_lua:BuildRequires: liblua5-devel luajit libluajit-devel lgi >= 0.9.0}
%{?_enable_vala:BuildRequires: vala-tools >= 0.14}
%{?_enable_gtk_doc:BuildRequires: gi-docgen}

%description
%name is a convenience library making adding plug-ins support
to GTK/GNOME and glib-based applications.

%package python3-loader
Summary: Python3 loader for %name
Group: System/Libraries
Requires: %name = %EVR

%description python3-loader
This package provides Python3 loader for %name.

%package gjs-loader
Summary: Javascript loader for %name
Group: System/Libraries
Requires: %name = %EVR

%description gjs-loader
This package provides GJS Javascript loader for %name.

%package lua-loader
Summary: LUA loader for %name
Group: System/Libraries
Requires: %name = %EVR

%description lua-loader
This package provides LUA-5.1 loader for %name.

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %EVR

%description devel
This package contains development libraries and header files
that are needed to write applications that use %name.

%package devel-doc
Summary: Development documentation for the %name
Group: Development/Documentation
Conflicts: %name < %version-%release
BuildArch: noarch

%description devel-doc
%name is a convenience library making adding plug-ins support
to GTK/GNOME and glib-based applications.

This package contains development documentation for the %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %EVR

%description gir
GObject introspection data for the %name.

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/Other
BuildArch: noarch
Requires: %name-devel = %EVR
Requires: %name-gir = %EVR

%description gir-devel
GObject introspection devel data for the %name.

%package demo
Summary: %name demonstration program
Group: Development/C
Requires: %name = %EVR
Requires: %name-gir = %EVR

%description demo
%name is a convenience library making adding plug-ins support
to GTK/GNOME and glib-based applications.

This package contains %name demonstration programs.

%prep
%setup -n %_name-%version

%build
%meson \
    %{?_enable_gtk_doc:-Dgtk_doc=true} \
    %{?_disable_gjs:-Dgjs=false} \
    %{?_disable_lua:-Dlua51=false} \
    %{?_enable_vala:-Dvapi=true} \
    %{?_disable_introspection:-Dintrospection=false}
%nil
%meson_build

%install
%meson_install
%find_lang --output=%name.lang %_name-%api_ver

%check
#xvfb-run
%__meson_test


%files -f %name.lang
%_libdir/%{_name}*-%api_ver.so.*
%dir %_libdir/%_name-%api_ver/loaders
#%_datadir/icons/hicolor/*/*/*
%doc README*

%files python3-loader
%_libdir/%_name-%api_ver/loaders/libpythonloader.so

%if_enabled gjs
%files gjs-loader
%_libdir/%_name-%api_ver/loaders/libgjsloader.so
%endif

%if_enabled lua
%files lua-loader
%_libdir/%_name-%api_ver/loaders/liblua*loader.so
%endif

%files devel
%_libdir/%{_name}*-%api_ver.so
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc

%if_enabled gtk_doc
%files devel-doc
%_datadir/doc/%_name-%api_ver
%endif

%if_enabled introspection
%files gir
%_typelibdir/Peas-%api_ver.typelib

%files gir-devel
%_girdir/Peas-%api_ver.gir
%endif

%if_enabled demo
%files demo
%_bindir/peas-demo
%add_python3_path %_libdir/peas-demo
%_libdir/peas-demo/
%endif


%changelog
* Sun Sep 17 2023 Yuri N. Sedunov <aris@altlinux.org> 2.0.0-alt1
- 2.0.0

* Fri Sep 01 2023 Yuri N. Sedunov <aris@altlinux.org> 1.99.1-alt1
- 1.99.1 (1.0 -> 2.0)

* Fri Mar 17 2023 Yuri N. Sedunov <aris@altlinux.org> 1.36.0-alt1
- 1.36.0

* Tue Sep 20 2022 Yuri N. Sedunov <aris@altlinux.org> 1.34.0-alt1
- 1.34.0

* Sat Mar 19 2022 Yuri N. Sedunov <aris@altlinux.org> 1.32.0-alt1
- 1.32.0

* Sat Mar 20 2021 Yuri N. Sedunov <aris@altlinux.org> 1.30.0-alt1
- 1.30.0

* Sat Sep 12 2020 Yuri N. Sedunov <aris@altlinux.org> 1.28.0-alt1
- 1.28.0

* Sat Mar 07 2020 Yuri N. Sedunov <aris@altlinux.org> 1.26.0-alt1
- 1.26.0

* Mon Dec 02 2019 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt2
- disabled python2 support

* Mon Oct 28 2019 Yuri N. Sedunov <aris@altlinux.org> 1.24.1-alt1
- 1.24.1

* Tue Sep 10 2019 Yuri N. Sedunov <aris@altlinux.org> 1.24.0-alt1
- 1.24.0 (ported to Meson build system)

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt3.1
- rebuilt with improved automake-1.16.1

* Tue Apr 09 2019 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt3
- updated to 1.22.0-9-g4eea771
- built with automake-1.14 (ALT #36568)

* Mon Jul 02 2018 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt2
- updated buildreqs

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.22.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Sun Sep 10 2017 Yuri N. Sedunov <aris@altlinux.org> 1.22.0-alt1
- 1.22.0

* Sun Oct 23 2016 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt2
- disabled lua loader (not ready for lua-5.3)

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 1.20.0-alt1.1
- 1.20.0

* Tue Mar 29 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.18.0-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Sun Mar 20 2016 Yuri N. Sedunov <aris@altlinux.org> 1.18.0-alt1
- 1.18.0

* Wed Jan 27 2016 Yuri N. Sedunov <aris@altlinux.org> 1.17.0-alt1
- 1.17.0

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 1.16.0-alt1
- 1.16.0

* Tue Jul 28 2015 Yuri N. Sedunov <aris@altlinux.org> 1.15.0-alt1
- 1.15.0

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 1.14.0-alt1
- 1.14.0

* Sun Feb 15 2015 Yuri N. Sedunov <aris@altlinux.org> 1.13.0-alt1
- 1.13.0

* Mon Sep 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.12.1-alt1
- 1.12.1

* Fri Aug 01 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.1-alt1
- 1.10.1

* Thu Apr 03 2014 Yuri N. Sedunov <aris@altlinux.org> 1.10.0-alt1
- 1.10.0

* Sun Mar 30 2014 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt2
- removed gjs-loader

* Mon Sep 30 2013 Yuri N. Sedunov <aris@altlinux.org> 1.9.0-alt1
- 1.9.0

* Sat Jun 22 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.1-alt1
- 1.8.1

* Tue Mar 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.8.0-alt1
- 1.8.0

* Tue Feb 26 2013 Yuri N. Sedunov <aris@altlinux.org> 1.7.0-alt1
- 1.7.0
- new python3-loader subpackage

* Tue Oct 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.1-alt1
- 1.6.1

* Tue Sep 25 2012 Yuri N. Sedunov <aris@altlinux.org> 1.6.0-alt1
- 1.6.0
- disabled seed loader (seed unmantained)

* Wed Apr 04 2012 Yuri N. Sedunov <aris@altlinux.org> 1.4.1-alt1
- 1.4.1 snapshot

* Mon Jan 16 2012 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt2
- used %%autoreconf to fix RPATH problem

* Mon Oct 31 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.0-alt1.1
- Rebuild with Python-2.7

* Wed Sep 28 2011 Yuri N. Sedunov <aris@altlinux.org> 1.2.0-alt1
- 1.2.0

* Tue Apr 05 2011 Yuri N. Sedunov <aris@altlinux.org> 1.0.0-alt1
- 1.0.0

* Thu Mar 10 2011 Yuri N. Sedunov <aris@altlinux.org> 0.7.4-alt1
- 0.7.4

* Mon Aug 23 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.5-alt1
- 0.5.5

* Wed Aug 04 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.4-alt1
- 0.5.4

* Tue Jul 27 2010 Yuri N. Sedunov <aris@altlinux.org> 0.5.3-alt1
- first build for sisyphus

