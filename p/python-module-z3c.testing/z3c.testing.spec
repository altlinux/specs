%define oname z3c.testing
Name: python-module-%oname
Version: 0.3.2
Release: alt2.1
Summary: High-level Testing Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testing/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ZODB3 zope.app.appsetup zope.app.publication
%py_requires zope.app.testing zope.container zope.site zope.component
%py_requires zope.configuration zope.interface zope.testing

%py_requires zope.app.rotterdam zope.browserpage zope.browserresource
%py_requires zope.principalregistry zope.publisher zope.securitypolicy
%py_requires zope.testbrowser

%description
This package provides a collection of high-level test setups for unit
and functional testing. In particular, it provides a testing layer that
can use an existing, pre-populated database as a starting point, which
speeds up the test setup phase for large testing data sets.

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

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.2-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1
- Initial build for Sisyphus

