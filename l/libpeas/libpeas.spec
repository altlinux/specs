%define ver_major 1.20
%define api_ver 1.0
%define gtk_api_ver 3.0

%def_disable js
# removed since 1.10.0
%def_disable gjs
# not ready for lua-5.3
%def_disable lua
%def_enable vala
%def_enable gtk_doc

Name: libpeas
Version: %ver_major.0
Release: alt2

Summary: A gobject-based plugins engine
Group: System/Libraries
License: LGPLv2+
Url: ftp://ftp.gnome.org/pub/gnome/sources/%name/

Source: ftp://ftp.gnome.org/pub/gnome/sources/%name/%ver_major/%name-%version.tar.xz
#Source: %name-%version.tar
# our python3 --ldflags break build
Patch: libpeas-1.8.0-alt-python3_build.patch

BuildRequires: gnome-common intltool gtk-doc
BuildRequires: libgio-devel >= 2.32.0 libgtk+3-devel >= 3.0.0
BuildRequires: gobject-introspection-devel >= 1.31.10 libgtk+3-gir-devel
# for python support
BuildRequires: python-module-pygobject3-devel >= 3.1.1
# for python3 support
BuildRequires: python3-devel python3-module-pygobject3-devel >= 3.1.1

# for Javascript support
%{?_enable_js:BuildRequires: libseed-devel >= 3.2.0}
%{?_enable_gjs:BuildRequires: libgjs-devel >= 1.37.1}
%{?_enable_lua:BuildRequires: liblua5-devel luajit libluajit-devel lgi >= 0.9.0}
%{?_enable_vala:BuildRequires: vala-tools >= 0.14}

%description
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

%package python-loader
Summary: Python loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description python-loader
This package provides Python loader for %name

%package python3-loader
Summary: Python3 loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description python3-loader
This package provides Python3 loader for %name

%package js-loader
Summary: Javascript loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description js-loader
This package provides WebKit Javascript loader for %name

%package gjs-loader
Summary: Javascript loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description gjs-loader
This package provides MozJS Javascript loader for %name

%package lua-loader
Summary: LUA loader for %name
Group: System/Libraries
Requires: %name = %version-%release

%description lua-loader
This package provides LUA-5.1 loader for %name

%package devel
Summary: Development files for %name
Group: Development/C
Requires: %name = %version-%release

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
to GTK+ and glib-based applications.

This package contains development documentation for the %name.

%package gir
Summary: GObject introspection data for the %name
Group: System/Libraries
Requires: %name = %version-%release

%description gir
GObject introspection data for the %name

%package gir-devel
Summary: GObject introspection devel data for the %name
Group: Development/C
BuildArch: noarch
Requires: %name-gir = %version-%release

%description gir-devel
GObject introspection devel data for the %name

%package demo
Summary: %name demonstration program
Group: Development/C
Requires: %name = %version-%release
Requires: %name-gir = %version-%release

%description demo
%name is a convenience library making adding plug-ins support
to GTK+ and glib-based applications.

This package contains %name demonstration programs

%prep
%setup
%patch

%build
%autoreconf
%configure \
	%{?_enable_gtk_doc:--enable-gtk-doc}

%make_build

%install
%makeinstall_std

%find_lang %name

%files -f %name.lang
%_libdir/%{name}*-%api_ver.so.*
%dir %_libdir/%name-%api_ver/loaders
#%_libdir/%name-%api_ver/loaders/libcloader.so
%_datadir/icons/hicolor/*/*/*
%doc AUTHORS README

%files python-loader
%_libdir/%name-%api_ver/loaders/libpythonloader.so

%files python3-loader
%_libdir/%name-%api_ver/loaders/libpython3loader.so

%if_enabled js
%files js-loader
%_libdir/%name-%api_ver/loaders/libseedloader.so
%endif

%if_enabled gjs
%files gjs-loader
%_libdir/%name-%api_ver/loaders/libgjsloader.so
%endif

%if_enabled lua
%files lua-loader
%_libdir/%name-%api_ver/loaders/liblua*loader.so
%endif

%files devel
%_libdir/%{name}*-%api_ver.so
%_includedir/%name-%api_ver/
%_libdir/pkgconfig/*.pc

%files devel-doc
%_datadir/gtk-doc/html/*

%files demo
%_bindir/peas-demo
%_libdir/peas-demo/

%files gir
%_typelibdir/*

%files gir-devel
%_girdir/*

%exclude %_libdir/%name-%api_ver/loaders/*.la


%changelog
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

