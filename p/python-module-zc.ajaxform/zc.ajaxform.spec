%define oname zc.ajaxform
Name: python-module-%oname
Version: 0.7.0
Release: alt3.1
Summary: Ajax Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.ajaxform/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires ClientForm rwproperty simplejson zc.form
%py_requires zope.html zope.testbrowser

%description
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

%package tests
Summary: Tests for zc.ajaxform
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
The zc.ajaxform package provides framework to support:

- A single-class application model

- Nested-application support

- Integration with zope.formlib

This package contains tests for zc.ajaxform.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt3.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt3
- Removed setuptools from requirements

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

