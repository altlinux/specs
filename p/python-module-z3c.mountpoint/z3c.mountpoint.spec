%define oname z3c.mountpoint
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Very simple implementation of a mount point for an object in another ZODB connection
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.mountpoint/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.container zope.app.publication zope.component

%description
This package provides a very simple implementation of a mount point for
an object in another ZODB connection. If you have multiple connections
defined in your zope.conf configuration file or multiple databases
defined in your Python code, you can use this package to mount any
object from any database at any location of another database.

%package tests
Summary: Tests for z3c.mountpoint
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package provides a very simple implementation of a mount point for
an object in another ZODB connection. If you have multiple connections
defined in your zope.conf configuration file or multiple databases
defined in your Python code, you can use this package to mount any
object from any database at any location of another database.

This package contains tests for z3c.mountpoint.

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
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

