%define oname z3c.preference
Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: UI for zope.preference using z3c.pagelet and z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.preference/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.form z3c.formui z3c.pagelet zope.preference

%description
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

%package tests
Summary: Tests for z3c.preference
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.wsgi zope.browserresource zope.login
%py_requires zope.principalregistry zope.app.principalannotation
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
This packages provides a user interface for zope.preference using
z3c.pagelet and z3c.form.

This package contains tests for z3c.preference.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

