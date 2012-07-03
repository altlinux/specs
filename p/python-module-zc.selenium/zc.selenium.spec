%define oname zc.selenium
Name: python-module-%oname
Version: 1.2.1
Release: alt2.1
Summary: Selenium integration for Zope 3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.selenium/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zope.interface zope.component zope.publisher
%py_requires z3c.zrtresource

%description
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

%package tests
Summary: Tests for Selenium integration for Zope 3
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides an easy way to use Selenium tests for Zope 3
applications. It provides Selenium itself as a resource directory, and
it provides a test suite listing generated from registered views,
allowing different packages to provide tests without a central list of
tests to be maintained.

This package contains tests for Selenium integration for Zope 3.

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
%exclude %python_sitelibdir/*/*/*test.py*
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*test.py*
%python_sitelibdir/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.2.1-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1
- Initial build for Sisyphus

