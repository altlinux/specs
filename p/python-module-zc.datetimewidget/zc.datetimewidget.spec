%define oname zc.datetimewidget
Name: python-module-%oname
Version: 0.7.0
Release: alt1
Summary: Javascript-based widgets for date and datetime fields
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.datetimewidget/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc pytz zc.i18n zc.resourcelibrary zope.app.form
%py_requires zope.component zope.datetime zope.interface zope.publisher
%py_requires zope.schema

%description
There are two types of widgets provided by this package, a date widget
and a datetime widget.

%package tests
Summary: Tests for zc.datetimewidget
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.zcmlfiles zope.app.securitypolicy
%py_requires zope.app.authentication zope.app.server zope.app.testing
%py_requires zope.securitypolicy zope.testbrowser zope.testing

%description tests
There are two types of widgets provided by this package, a date widget
and a datetime widget.

This package contains tests for zc.datetimewidget.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*
%python_sitelibdir/*/*/*/tests.*

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Version 0.7.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.6.4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.6.4-alt1
- Initial build for Sisyphus

