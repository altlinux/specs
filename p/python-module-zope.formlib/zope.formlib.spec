%define oname zope.formlib
Name: python-module-%oname
Version: 4.0.6
Release: alt1
Summary: Form generation and validation library for Zope
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.formlib
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope pytz zope.browser zope.browserpage zope.component
%py_requires zope.event zope.i18n zope.i18nmessageid zope.interface
%py_requires zope.lifecycleevent zope.publisher zope.schema
%py_requires zope.security zope.traversing zope.datetime

%description
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

%package tests
Summary: Tests for zope.formlib
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.configuration zope.testing

%description tests
Forms are web components that use widgets to display and input data.
Typically a template displays the widgets by accessing an attribute or
method on an underlying class.

This package contains sests for zope.formlib.

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

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.6-alt1
- Version 4.0.6

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 4.0.5-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.5-alt1
- Initial build for Sisyphus

