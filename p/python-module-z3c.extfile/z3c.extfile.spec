%define oname z3c.extfile
Name: python-module-%oname
Version: 0.3.0b2
Release: alt2.1
Summary: Large file handling for zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.extfile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.filetype zope.app.component zope.app.appsetup
%py_requires zope.app.file zope.app.form zope.app.wsgi
%py_requires zope.cachedescriptors zope.contenttype zope.datetime
%py_requires zope.formlib zope.i18nmessageid zope.publisher zope.schema
%py_requires zope.security zope.traversing

%description
Large file handling for zope3.

%package tests
Summary: Tests for Large file handling for zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing paste paste.deploy

%description tests
Large file handling for zope3.

This package contains tests for Large file handling for zope3.

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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/test*
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.0b2-alt2.1
- Rebuild with Python-2.7

* Fri Jul 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0b2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0b2-alt1
- Initial build for Sisyphus

