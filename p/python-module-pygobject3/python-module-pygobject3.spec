%define _name pygobject
%define major 3.2
%define api_ver 3.0
%define gtk_api_ver 2.0
%def_disable devel_doc

Name: python-module-%{_name}3
Version: %major.2
Release: alt1

Summary: Python bindings for GObject

License: LGPL
Group: Development/Python
Url: http://www.pygtk.org/

Source: http://ftp.gnome.org/pub/GNOME/sources/%_name/%major/%_name-%version.tar.xz

%setup_python_module pygobject3

%add_findprov_lib_path %python_sitelibdir/gi
%add_findprov_lib_path %python_sitelibdir/gtk-%gtk_api_ver

%define glib_ver 2.31.0

BuildPreReq: glib2-devel >= %glib_ver libgio-devel libffi-devel
BuildRequires: python-devel python-modules-encodings python-module-pycairo-devel
BuildPreReq: gobject-introspection-devel >= 1.29.0
# for tests
# BuildRequires: libcairo-gobject-devel dbus-tools-gui libgtk+3-gir-devel

%description
GObject is a object system used by GTK+, GStreamer and other libraries.

PyGObject provides a convenient wrapper for use in Python programs when
accessing GObject libraries.

PyGObject now dynamically accesses any GObject libraries that uses
GObject Introspection. It replaces the need for separate modules such as
PyGTK, GIO and python-gnome to build a full GNOME 3.0 application. Once
new functionality is added to gobject library it is instantly available
as a Python API without the need for intermediate Python glue.

%package devel
Summary: Development files for %_name
Group: Development/Python
Requires: %name = %version-%release

%description devel
Development files for %_name.

%package devel-doc
Summary: Development documentation for %_name
Group: Development/Python
BuildArch: noarch
Conflicts: %name-devel < %version-%release

%description devel-doc
Development documentation for %_name.

%prep
%setup -q -n %_name-%version

%build
%autoreconf
%configure --with-pic \
    --disable-static \
    --enable-cairo

%make_build

%check
#%%make check

%install
%makeinstall_std
# hack to avoid verify-elf errors
export LD_PRELOAD=%_libdir/libpython%__python_version.so

%files
%_libdir/libpyglib-gi-2.0-python.so.*
%python_sitelibdir/gi/

%files devel
%_libdir/libpyglib-gi-2.0-python.so
%_includedir/%_name-%api_ver/
%_pkgconfigdir/%_name-%api_ver.pc
%doc README AUTHORS NEWS examples

%exclude %python_sitelibdir/*/*.la

%if_enabled devel_doc
%files devel-doc
%_datadir/gtk-doc/html/%_name/
%endif

%changelog
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

