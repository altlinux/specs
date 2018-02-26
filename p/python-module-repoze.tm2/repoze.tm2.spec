%define oname repoze.tm2
Name: python-module-%oname
Version: 1.0b2
Release: alt1.git20110718
Summary: WSGI middleware: commit / abort transactions
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.tm2
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.tm2.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides repoze.tm2
%py_requires repoze transaction

%description
Middleware which uses the ZODB transaction manager to wrap a call to
its pipeline children inside a transaction.  This is a fork of the
``repoze.tm`` package which depends only on the ``transaction``
package rather than the entirety of ZODB (for users who don't rely on
ZODB).

%package tests
Summary: Tests for repoze.tm2
Group: Development/Python
Requires: %name = %version-%release

%description tests
Middleware which uses the ZODB transaction manager to wrap a call to
its pipeline children inside a transaction.  This is a fork of the
``repoze.tm`` package which depends only on the ``transaction``
package rather than the entirety of ZODB (for users who don't rely on
ZODB).

This package contains tests for repoze.tm2.

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
* Tue Dec 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b2-alt1.git20110718
- Version 1.0b2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0b1-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0b1-alt1.git20110225
- Initial build for Sisyphus

