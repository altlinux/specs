%define oname zope.app.testing
Name: python-module-%oname
Version: 3.9.0
Release: alt2.1
Summary: Zope Application Testing Support
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app zope.annotation zope.app.appsetup
%py_requires zope.processlifetime zope.app.debug zope.app.dependable
%py_requires zope.app.publication zope.component zope.container
%py_requires zope.i18n zope.interface zope.password zope.publisher
%py_requires zope.schema zope.security zope.site zope.testing
%py_requires zope.testbrowser zope.traversing

%py_requires ZODB3 zope.app.authentication zope.app.zcmlfiles zope.login
%py_requires zope.publisher zope.securitypolicy

%description
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

%package -n python-module-zope.app
Summary: Core files for zope.app
Group: Development/Python
Requires: python-module-zope
%py_provides zope.app

%description -n python-module-zope.app
This package provides testing support for Zope 3 applications. Besides
providing numerous setup convenience functions, it implements a testing
setup that allows the user to make calls to the publisher allowing to
write functional tests.

This package contains core files for zope.app.

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

touch %buildroot%python_sitelibdir/zope/app/__init__.py

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/zope/app/__init__.py*

%files -n python-module-zope.app
%python_sitelibdir/zope/app/__init__.py*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Initial build for Sisyphus

