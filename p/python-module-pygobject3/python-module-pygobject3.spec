%define _name pygobject
%define major 3.4
%define api_ver 3.0
%define gtk_api_ver 2.0
%def_disable devel_doc

Name: python-module-%{_name}3
Version: %major.3
Release: alt0.2

Summary: Python bindings for GObject

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Source: %_name-%version.tar
#Source: http://ftp.gnome.org/pub/GNOME/sources/%_name/%major/%_name-%version.tar.xz

%setup_python_module pygobject3

%add_findprov_lib_path %python_sitelibdir/gi
%add_findprov_lib_path %python_sitelibdir/gtk-%gtk_api_ver

%add_findprov_lib_path %python3_sitelibdir/gi
%add_findprov_lib_path %python3_sitelibdir/gtk-%gtk_api_ver

%define glib_ver 2.31.0
%define gi_ver 1.34.1.1

BuildPreReq: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildRequires: python-devel python-modules-encodings python-module-pycairo-devel libcairo-gobject-devel gtk-doc
BuildPreReq: gobject-introspection-devel >= %gi_ver
# python3
BuildRequires: rpm-build-python3 python3-devel python3-module-pycairo-devel
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

%package common-devel
Summary: Common development files for %_name
Group: Development/Python

%description common-devel
Common development files for %_name used for both python2 and python3.

%package devel
Summary: Development files for %name
Group: Development/Python
Requires: %name = %version-%release
Requires: %name-common-devel = %version-%release

%description devel
Development files for %name.

%package -n python3-module-%{_name}3
Summary: Python3 bindings for GObject
Group: Development/Python

%description -n python3-module-%{_name}3
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python3 programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package -n python3-module-%{_name}3-devel
Summary: Development files for python3-module-%{_name}3
Group: Development/Python
Requires: python3-module-%{_name}3 = %version-%release
Requires: %name-common-devel = %version-%release

%description -n python3-module-%{_name}3-devel
Development files for python3-module-%{_name}3.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Python
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
# hack to avoid verify-elf errors
export LD_PRELOAD=%_libdir/libpython%__python_version.so

pushd py3build
%makeinstall_std
# hack to avoid verify-elf errors
export LD_PRELOAD="${LD_PRELOAD:+"$LD_PRELOAD:"}%_libdir/libpython3.so"
popd

%check
xvfb-run %make check

# currently fails for python3
#pushd py3build
#xvfb-run %make check
#popd

%files
%_libdir/libpyglib-gi-2.0-python%__python_version.so.*
%python_sitelibdir/gi/
%python_sitelibdir/*.egg-info/

%exclude %python_sitelibdir/*/*.la

%files common-devel
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc
%doc README AUTHORS NEWS examples

%files devel
%_libdir/libpyglib-gi-2.0-python%__python_version.so

%files -n python3-module-%{_name}3
%_libdir/libpyglib-gi-2.0-python3.so.*
%python3_sitelibdir/gi/
%python3_sitelibdir/*.egg-info/

%files -n python3-module-%{_name}3-devel
%_libdir/libpyglib-gi-2.0-python3.so

%exclude %python3_sitelibdir/*/*.la

%if_enabled devel_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
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

