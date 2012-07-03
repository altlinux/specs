%define oname z3c.flashmessage
Name: python-module-%oname
Version: 1.3
Release: alt2.1
Summary: A package for sending `flash messages` to users
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.flashmessage/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.interface zope.schema zope.session

%description
Components to display small messages to users.

%package tests
Summary: Tests for z3c.flashmessage
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.publisher zope.component zope.security zope.app.wsgi

%description tests
Components to display small messages to users.

This package contains tests for z3c.flashmessage.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Initial build for Sisyphus

