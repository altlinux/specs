%define oname zope.mimetype
Name: python-module-%oname
Version: 1.3.1
Release: alt2.1
Summary: A simple package for working with MIME content types
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.mimetype/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.browser zope.browserresource zope.component
%py_requires zope.configuration zope.contenttype zope.event zope.formlib
%py_requires zope.i18n zope.i18nmessageid zope.interface zope.publisher
%py_requires zope.schema zope.security

%description
This package provides a way to work with MIME content types. There are
several interfaces defined here, many of which are used primarily to
look things up based on different bits of information.

%package tests
Summary: Tests for zope.mimetype
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component

%description tests
This package provides a way to work with MIME content types. There are
several interfaces defined here, many of which are used primarily to
look things up based on different bits of information.

This package contains tests for zope.mimetype.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.3.1-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Initial build for Sisyphus

