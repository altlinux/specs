%define oname zope.app.generations
Name: python-module-%oname
Version: 3.7.0
Release: alt2.1
Summary: ZMI UI for zope.generations
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.generations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.publication zope.app.renderer
%py_requires zope.applicationcontrol zope.generations zope.interface
%py_requires zope.processlifetime

%description
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package only contains the ZMI user interface for zope.generations

%package tests
Summary: Tests for zope.app.generations
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.securitypolicy zope.testing

%description tests
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package contains tests for zope.app.generations.

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
%exclude %python_sitelibdir/*/*/*/test*
%exclude %python_sitelibdir/*/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*
%python_sitelibdir/*/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

