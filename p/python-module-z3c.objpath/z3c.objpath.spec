%define oname z3c.objpath
Name: python-module-%oname
Version: 1.0
Release: alt2.1
Summary: Generate and resolve paths to to objects
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.objpath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface

%description
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

%package tests
Summary: Tests for z3c.objpath
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package contains two things:

* the z3c.objpath.interfaces.IObjectPath interface.
* some helper functions to construct (relative) object paths, in
  z3c.objpath.path.

The idea is that a particular application can implement a utility that
fulfills the IObjectPath interface, so that it is possible to construct
paths to objects in a uniform way. The implementation may be done with
zope.traversing, but in some cases you want application-specific object
paths. In this case, the functions in z3c.objpath.path might be useful.

This package contains tests for z3c.objpath.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/__init__.*
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

