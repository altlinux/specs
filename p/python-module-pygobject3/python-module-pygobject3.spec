%def_disable snapshot

%define _name pygobject
%define ver_major 3.22
%define api_ver 3.0
%define gtk_api_ver 2.0
%def_disable devel_doc

Name: python-module-%{_name}3
Version: %ver_major.0
Release: alt2

Summary: Python bindings for GObject
Group: Development/Python
License: LGPL
Url: http://www.pygtk.org/

%if_disabled snapshot
Source: ftp://ftp.gnome.org/pub/gnome/sources/%_name/%ver_major/%_name-%version.tar.xz
%else
Source: %_name-%version.tar
%endif

%setup_python_module pygobject3

%add_findprov_lib_path %python_sitelibdir/gi
%add_findprov_lib_path %python_sitelibdir/gtk-%gtk_api_ver

%add_findprov_lib_path %python3_sitelibdir/gi
%add_findprov_lib_path %python3_sitelibdir/gtk-%gtk_api_ver

%add_typelib_req_skiplist typelib(Foo)
%filter_from_requires /Gst.*/d

%define glib_ver 2.46.0
%define gi_ver 1.46.0

BuildRequires: gnome-common
BuildRequires(pre): rpm-build-gir
BuildPreReq: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildPreReq: python-devel  python-modules-encodings python-module-pycairo-devel libcairo-gobject-devel gtk-doc
BuildPreReq: gobject-introspection-devel >= %gi_ver
# python3
BuildPreReq: rpm-build-python3  python3-devel python3-module-pycairo-devel
# for tests
BuildRequires: dbus-tools-gui libgtk+3-gir-devel xvfb-run
BuildRequires: glibc-i18ndata

%description
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package pygtkcompat
Summary: PyGTK compatibility layer for PyGObject
Group: Development/Python
Requires: %name = %version-%release

%description pygtkcompat
PyGTK compatibility layer.
It is recommended to not depend on this layer, but only use it as an
intermediate step when porting your application to PyGI. Compatibility
might never be 100%%, but the aim is to make it possible to run a well
behaved PyGTK application mostly unmodified on top of PyGI.

%package common-devel
Summary: Common development files for %_name
Group: Development/Python

%description common-devel
Common development files for %_name used for both python2 and python3.

%package devel
Summary: Development files for %name
Group: Development/Python
BuildArch: noarch
Requires: %name = %version-%release
Requires: %name-common-devel = %version-%release

%description devel
Development files for %name.

%package -n python3-module-%{_name}3
Summary: Python3 bindings for GObject
Group: Development/Python3

%description -n python3-module-%{_name}3
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python3 programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package -n python3-module-%{_name}3-pygtkcompat
Summary: PyGTK compatibility layer for PyGObject
Group: Development/Python3
Requires: python3-module-%{_name}3 = %version-%release

%description -n python3-module-%{_name}3-pygtkcompat
PyGTK compatibility layer.
It is recommended to not depend on this layer, but only use it as an
intermediate step when porting your application to PyGI. Compatibility
might never be 100%%, but the aim is to make it possible to run a well
behaved PyGTK application mostly unmodified on top of PyGI.

%package -n python3-module-%{_name}3-devel
Summary: Development files for python3-module-%{_name}3
Group: Development/Python3
BuildArch: noarch
Requires: python3-module-%{_name}3 = %version-%release
Requires: %name-common-devel = %version-%release

%description -n python3-module-%{_name}3-devel
Development files for python3-module-%{_name}3.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Documentation
BuildArch: noarch
Conflicts: %name-common-devel < %version-%release

%description devel-doc
Development documentation for %_name.

%prep
%setup -n %_name-%version
%setup -D -c -n %_name-%version
mv %_name-%version py3build

%build
%define opts --with-pic --disable-static --enable-cairo
export PYTHON=%__python
%autoreconf
%configure %opts
%make_build

pushd py3build
export PYTHON=python3
%autoreconf
%configure %opts
%make_build
popd

%install
%makeinstall_std

pushd py3build
%makeinstall_std
popd

%check
#xvfb-run %make check

#pushd py3build
#xvfb-run %make check
#popd

%files
%python_sitelibdir/gi/
%exclude %python_sitelibdir/gi/pygtkcompat.py*
%python_sitelibdir/*.egg-info/

%exclude %python_sitelibdir/*/*.la

%files pygtkcompat
%python_sitelibdir/pygtkcompat/
%python_sitelibdir/gi/pygtkcompat.py*

%files common-devel
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc
%doc README AUTHORS NEWS examples

%files devel

%files -n python3-module-%{_name}3
%python3_sitelibdir/gi/
%exclude %python3_sitelibdir/gi/pygtkcompat.py*
%python3_sitelibdir/*.egg-info/

%files -n python3-module-%{_name}3-pygtkcompat
%python3_sitelibdir/pygtkcompat/
%python3_sitelibdir/gi/pygtkcompat.py*

%files -n python3-module-%{_name}3-devel

%exclude %python3_sitelibdir/*/*.la

%if_enabled devel_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
* Wed Mar 01 2017 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt2
- removed dependencies on old GStreamer (ALT #33183)

* Mon Sep 19 2016 Yuri N. Sedunov <aris@altlinux.org> 3.22.0-alt1
- 3.22.0

* Mon Apr 25 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.1-alt1
- 3.20.1

* Fri Apr 01 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.20.0-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 3.20.0-alt2
- NMU LD_PRELOAD changes for Python 3.5

* Tue Mar 22 2016 Yuri N. Sedunov <aris@altlinux.org> 3.20.0-alt1
- 3.20.0

* Sat Oct 24 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.2-alt1
- 3.18.2

* Tue Sep 22 2015 Yuri N. Sedunov <aris@altlinux.org> 3.18.0-alt1
- 3.18.0

* Sun Jun 21 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.2-alt1
- 3.16.2

* Tue Apr 14 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.1-alt1
- 3.16.1

* Wed Mar 25 2015 Yuri N. Sedunov <aris@altlinux.org> 3.16.0-alt1
- 3.16.0

* Tue Sep 23 2014 Yuri N. Sedunov <aris@altlinux.org> 3.14.0-alt1
- 3.14.0

* Mon May 26 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.2-alt1
- 3.12.2

* Tue Apr 15 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.1-alt1
- 3.12.1

* Mon Mar 24 2014 Yuri N. Sedunov <aris@altlinux.org> 3.12.0-alt1
- 3.12.0

* Mon Nov 11 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.2-alt1
- 3.10.2

* Mon Oct 14 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.1-alt1
- 3.10.1

* Mon Sep 23 2013 Yuri N. Sedunov <aris@altlinux.org> 3.10.0-alt1
- 3.10.0

* Fri Jul 05 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.3-alt1
- 3.8.3

* Mon May 13 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.2-alt1
- 3.8.2

* Mon Apr 15 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.1-alt1
- 3.8.1

* Thu Apr 04 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt2
- moved pygtkcompat to separate subpackages (ALT #28787)

* Mon Mar 25 2013 Yuri N. Sedunov <aris@altlinux.org> 3.8.0-alt1
- 3.8.0

* Sun Mar 17 2013 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.3
- rebuilt with python-3.3

* Mon Dec 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.2
- built python3 module too (new python3-module-, -common-devel subpackages)

* Sat Dec 08 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.3-alt0.1
- 3.4.3 snapshot (c36e1236)
- enabled %%check again using xvfb-run

* Mon Nov 12 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.2-alt1
- 3.4.2

* Wed Oct 17 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1.1-alt1
- 3.4.1.1

* Mon Oct 15 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.1-alt1
- 3.4.1

* Mon Sep 24 2012 Yuri N. Sedunov <aris@altlinux.org> 3.4.0-alt1
- 3.4.0

* Mon May 14 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.2-alt1
- 3.2.2

* Thu May 10 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.1-alt1
- 3.2.1

* Fri Apr 13 2012 Yuri N. Sedunov <aris@altlinux.org> 3.2.0-alt1
- 3.2.0
- no more libpython dependencies

* Thu Mar 22 2012 Yuri N. Sedunov <aris@altlinux.org> 3.1.93-alt1
- 3.1.93

* Mon Dec 12 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.3-alt1
- 3.0.3

* Sun Oct 30 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.0.2-alt1.1
- Rebuild with Python-2.7

* Sat Oct 22 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.2-alt1
- 3.0.2

* Sat Oct 01 2011 Yuri N. Sedunov <aris@altlinux.org> 3.0.1-alt1
- 3.0.1

* Sun Aug 21 2011 Yuri N. Sedunov <aris@altlinux.org> 2.90.2-alt1
- first build for Sisyphus

