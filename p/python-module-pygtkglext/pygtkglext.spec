%define qname gtk

Name: python-module-pygtkglext
Version: 1.1.0
Release: alt5.1

Summary: Python bindings for GtkGLExt
License: LGPLv2+
Group: Development/Python
Url: http://sourceforge.net/projects/gtkglext/
Packager: Igor Zubkov <icesik@altlinux.org>

Source: pygtkglext-%version.tar

# Automatically added by buildreq on Sun Jul 27 2008
BuildRequires: gcc-c++ libgtkglext-devel python-module-pygtk-devel

%description
PyGtkGLExt is Python language bindings for GtkGLExt, OpenGL Extension to GTK.
It enables Python programmers to write OpenGL applications with PyGTK2.

%package devel
Summary: Development files for %name
Group: Development/Python
Requires: %name = %version-%release
Requires: python-module-pygtk-devel

%description devel
This package contains libraries and header files for
developing applications that use %name.

%prep
%setup -q -n pygtkglext-%version

%build
%autoreconf
%configure
%make_build

%install
%make_install DESTDIR=%buildroot install

%ifarch x86_64
mv %buildroot%python_sitelibdir_noarch/gtk-2.0/%qname/gdkgl/* \
	%buildroot%python_sitelibdir/gtk-2.0/%qname/gdkgl/
mv %buildroot%python_sitelibdir_noarch/gtk-2.0/%qname/gtkgl/* \
	%buildroot%python_sitelibdir/gtk-2.0/%qname/gtkgl/
%endif

%files
%doc AUTHORS ChangeLog* README
%python_sitelibdir/gtk-2.0/gtk/gdkgl
%python_sitelibdir/gtk-2.0/gtk/gtkgl

%files devel
%_pkgconfigdir/*
%_datadir/pygtk/2.0/defs/*

%changelog
* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt5.1
- Rebuild with Python-2.7

* Sun Mar 13 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt5
- Rebuilt for debuginfo

* Mon Nov 16 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt4.1
- Rebuilt with python 2.6

* Mon Feb 16 2009 Dmitry V. Levin <ldv@altlinux.org> 1.1.0-alt4
- Moved development files to -devel subpackage.

* Sun Jul 27 2008 Igor Zubkov <icesik@altlinux.org> 1.1.0-alt3
- don't use obsolete macros
- buildreq

* Mon Feb 11 2008 Grigory Batalov <bga@altlinux.ru> 1.1.0-alt2.1
- Rebuilt with python-2.5.

* Thu Jan 03 2008 Igor Zubkov <icesik@altlinux.org> 1.1.0-alt2
- fix build

* Sat Sep 22 2007 Igor Zubkov <icesik@altlinux.org> 1.1.0-alt1
- build for Sisyphus

* Sun Aug 31 2003 Naofumi Yasufuku <naofumi@users.sourceforge.net>
- Updated source URL.

* Sun May 11 2003 Naofumi Yasufuku <naofumi@users.sourceforge.net>
- Initial build.

