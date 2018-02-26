%define major 2.28
%define oname pygobject
%define gtk_api_ver 2.0
%def_disable introspection

Name: python-module-pygobject
Version: %major.6
Release: alt3

Summary: Python bindings for GObject

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/%oname/%major/%oname-%version.tar

%setup_python_module pygobject

%add_python_lib_path  %python_sitelibdir/gtk-%gtk_api_ver
%add_findprov_lib_path %python_sitelibdir/gtk-%gtk_api_ver/gtk
%{?_enable_introspection:%add_findprov_lib_path %python_sitelibdir/gtk-%gtk_api_ver/gi}
%{?_enable_introspection:Requires: python-module-pygi = %version-%release}

Conflicts: python-module-pygtk <= 2.8.2-alt2.1

%define glib_ver 2.28.0

BuildPreReq: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildRequires: python-devel python-modules-encodings python-module-pycairo-devel
%{?_enable_introspection:BuildPreReq: gobject-introspection-devel >= 0.10.2}
# for tests
# BuildRequires: libcairo-gobject-devel dbus-tools-gui libgtk+3-gir-devel

%description
This package provides Python bindings for the GLib, GObject and GIO,
to be used in Python. It is a fairly complete set of bindings,
it's already rather useful, and is usable to write moderately
complex programs.  (see the examples directory for some examples
of the simpler programs you could write).

%package devel
Summary: Development files for %oname
Group: Development/Python
Requires: %name = %version-%release
Conflicts: python-module-pygtk-devel <= 2.8.2-alt2.1

%description devel
Development files for %oname.

%package devel-doc
Summary: Development documentation for %oname
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
Development documentation for %oname.

%package -n python-module-pygi
Summary: Python dynamic bindings based on GObject-Introspection
Group: Development/Python
%{?_enable_introspection:%setup_python_module pygi}
Requires: %name = %version-%release

%description -n python-module-pygi
PyGI is a module which aims to utilize GObject Introspection to
facilitate the creation of Python bindings.

%prep
%setup -q -n %oname-%version

%build
%autoreconf
%configure --with-pic --disable-static \
	%{subst_enable introspection}

%make_build

%check
#%%make check

%install
%make_install install DESTDIR=%buildroot
mkdir -p %buildroot%_includedir/python%__python_version
mv %buildroot%_includedir/pygtk-%gtk_api_ver %buildroot%_includedir/python%__python_version/pygtk
%__subst "s|\${includedir}/pygtk-%gtk_api_ver|\${includedir}/python%__python_version/pygtk|g" %buildroot/%_pkgconfigdir/*.pc

# hack to avoid verify-elf errors
export LD_PRELOAD=%_libdir/libpython%__python_version.so

%files
%_libdir/libpyglib-2.0-python.so.*
%python_sitelibdir/pygtk.*
%python_sitelibdir/gobject
%python_sitelibdir/glib
%dir %python_sitelibdir/gtk-%gtk_api_ver
%python_sitelibdir/gtk-%gtk_api_ver/gio

%files devel
%_bindir/pygobject-codegen-2.0
%_libdir/libpyglib-2.0-python.so
%_includedir/python%__python_version/pygtk
%python_sitelibdir/gtk-%gtk_api_ver/dsextras.*
%_datadir/pygobject/2.0
%_datadir/pygobject/xsl
%_pkgconfigdir/pygobject-2.0.pc
%doc README AUTHORS NEWS examples

%exclude %python_sitelibdir/*/*.la

%files devel-doc
%_datadir/gtk-doc/html/pygobject/

%if_enabled introspection
%files -n python-module-pygi
%python_sitelibdir/gi/
%exclude %python_sitelibdir/gi/*.la
%endif

%changelog
* Fri Apr 13 2012 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt3
- updated to latest pygobject-2-28 (42d01f0)
- no more libpython dependencies

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.28.6-alt2.1
- Rebuild with Python-2.7

* Sun Sep 11 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt2
- disabled introspection support

* Tue Jun 14 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.6-alt1
- 2.28.6

* Mon Apr 18 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.4-alt1
- 2.28.4

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.3-alt1
- 2.28.3

* Wed Mar 23 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.2-alt1
- 2.28.2

* Mon Mar 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.1-alt1
- 2.28.1
- fixed link

* Tue Mar 08 2011 Yuri N. Sedunov <aris@altlinux.org> 2.28.0-alt1
- 2.28.0

* Tue Mar 01 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.91-alt1
- 2.27.91

* Sat Feb 12 2011 Yuri N. Sedunov <aris@altlinux.org> 2.27.90-alt1
- 2.27.90
- removed useless link patch

* Wed Dec 15 2010 Yuri N. Sedunov <aris@altlinux.org> 2.27.0-alt1
- 2.27.0

* Thu Nov 04 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt2
- rebuild for update dependencies

* Sun Oct 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.26.0-alt1
- 2.26.0

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.5-alt1
- 2.21.5

* Sun Aug 22 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt3
- build with libffi support

* Mon Jul 05 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt2
- requires python-module-pygi if introspection support enabled (closes
  #23720)

* Tue Jun 29 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.4-alt1
- 2.21.4

* Mon Jun 21 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.3-alt1
- 2.21.3

* Wed Jun 16 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.2-alt1
- 2.21.2

* Sun Jan 03 2010 Yuri N. Sedunov <aris@altlinux.org> 2.21.1-alt1
- new version
- introspection support temporarily disabled

* Fri Dec 25 2009 Yuri N. Sedunov <aris@altlinux.org> 2.21.0-alt1
- 2.21.0

* Wed Nov 11 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.20.0-alt2.1
- Rebuilt with python 2.6

* Tue Nov 10 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt2
- new gir{,-devel} packages

* Thu Sep 24 2009 Yuri N. Sedunov <aris@altlinux.org> 2.20.0-alt1
- 2.20.0

* Wed Aug 12 2009 Yuri N. Sedunov <aris@altlinux.org> 2.19.0-alt1
- 2.19.0
- new devel-doc noarch package

* Thu Jan 22 2009 Yuri N. Sedunov <aris@altlinux.org> 2.16.0-alt1
- 2.16.0

* Tue Sep 30 2008 Yuri N. Sedunov <aris@altlinux.org> 2.15.4-alt1
- 2.15.4
- updated buildreqs
- updated patch0

* Sun Jul 20 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.2-alt1
- new version 2.14.2 (with rpmrb script)

* Fri Mar 21 2008 Vitaly Lipatov <lav@altlinux.ru> 2.14.1-alt1
- new version 2.14.1 (with rpmrb script)

* Tue Oct 16 2007 Vitaly Lipatov <lav@altlinux.ru> 2.14.0-alt1
- new version 2.14.0 (with rpmrb script)

* Tue Aug 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.2-alt1
- new version 2.13.2 (with rpmrb script)

* Thu May 17 2007 Vitaly Lipatov <lav@altlinux.ru> 2.13.1-alt1
- new version 2.13.1 (with rpmrb script)

* Sat Apr 07 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.3-alt1
- new version 2.12.3 (with rpmrb script)

* Tue Feb 06 2007 Vitaly Lipatov <lav@altlinux.ru> 2.12.2-alt1
- fix linking, packing - applied patches from Valery Inozemtsev (fix bug #10771)

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.12.2-alt0.1
- new version 2.12.2 (with rpmrb script)

* Sun Sep 03 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.4-alt0.1
- new version 2.11.4 (with rpmrb script)

* Sun Jul 30 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt0.1
- new version
- remove broken TMPDIR definition from Makefile!

* Tue Jul 25 2006 Vitaly Lipatov <lav@altlinux.ru> 2.10.1-alt0.1
- new version 2.10.1 (with rpmrb script)

* Mon Jul 24 2006 Vitaly Lipatov <lav@altlinux.ru> 2.11.0-alt0.1
- new version 2.11.0 (with rpmrb script)

* Tue Mar 07 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt1
- add conflicts to old pygtk in -devel package

* Sat Mar 04 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.1-alt0.1
- new version (2.9.1)

* Sat Feb 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.9.0-alt0.1
- initial build for ALT Linux Sisyphus
