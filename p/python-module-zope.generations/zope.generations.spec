%define oname zope.generations
Name: python-module-%oname
Version: 3.7.1
Release: alt1
Summary: Zope application schema generations
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.generations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope transaction zope.component zope.interface
%py_requires zope.processlifetime

%description
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

%package tests
Summary: Tests and demos of zope.generations
Group: Development/Python
Requires: %name = %version-%release
%py_requires ZODB3 zope.app.publication zope.site zope.testing

%description tests
Generations are a way of updating objects in the database when the
application schema changes. An application schema is essentially the
structure of data, the structure of classes in the case of ZODB or the
table descriptions in the case of a relational database.

This package contains tests and demos of zope.generations.

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
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/demo*

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/demo*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.1-alt1
- Version 3.7.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun May 22 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.0-alt1
- Initial build for Sisyphus

