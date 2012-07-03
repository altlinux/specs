%define oname repoze.tm
Name: python-module-%oname
Version: 1.0a5
Release: alt3.1
Summary: Zope-like transaction manager via WSGI middleware
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.tm/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze ZODB3
Conflicts: python-module-repoze.tm2

%description
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

%package tests
Summary: Tests for repoze.tm
Group: Development/Python
Requires: %name = %version-%release
Conflicts: python-module-repoze.tm2-tests

%description tests
Middleware which uses the ZODB transaction manager to wrap a call to its
pipeline children inside a transaction.

This package contains tests for repoze.tm.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0a5-alt3.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt3
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt2
- Added explicit conflict with python-module-repoze.tm2

* Thu Jun 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0a5-alt1
- Initial build for Sisyphus

