%define oname z3c.boston
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: A version of the zope.app.boston skin which support pagelets
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.boston/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.boston z3c.pagelet z3c.formui z3c.layer
%py_requires jquery.layer z3c.template z3c.viewlet z3c.form z3c.formjs
%py_requires z3c.zrtresource jquery.javascript jquery.layer

%description
This skin is a derivative of the zope.app.boston.Boston skin, which
supports pagelets, forms and javascript forms.

%package tests
Summary: Tests for z3c.boston
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testbrowser zope.app.dtmlpage
%py_requires zope.app.onlinehelp zope.app.securitypolicy
%py_requires zope.app.zcmlfiles

%description tests
This skin is a derivative of the zope.app.boston.Boston skin, which
supports pagelets, forms and javascript forms.

This package contains tests for z3c.boston.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

