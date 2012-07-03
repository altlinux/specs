%define oname z3c.rotterdam
Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: A version of the rotterdam skin which supports z3c.pagelet and z3c.form
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.rotterdam/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.app.rotterdam z3c.pagelet z3c.formui z3c.layer
%py_requires jquery.layer z3c.template zope.viewlet z3c.viewlet z3c.form
%py_requires z3c.formjs z3c.zrtresource jquery.javascript jquery.layer

%description
This skin is a derivative of the zope.app.rotterdam.Rotterdam skin, which
supports pagelets, forms and javascript forms.

%package tests
Summary: Tests for z3c.rotterdam
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing zope.testbrowser zope.app.dtmlpage
%py_requires zope.app.onlinehelp zope.app.securitypolicy
%py_requires zope.app.zcmlfiles

%description tests
This skin is a derivative of the zope.app.rotterdam.Rotterdam skin, which
supports pagelets, forms and javascript forms.

This package contains tests for z3c.rotterdam.

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

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1
- Initial build for Sisyphus

