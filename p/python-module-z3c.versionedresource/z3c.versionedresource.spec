%define oname z3c.versionedresource
Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: Versioned Resources
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.versionedresource/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.component zope.configuration zope.interface
%py_requires zope.security zope.publisher zope.app.publisher

%description
Versioned Resources insert a version number in the URL of a resource, so
that cache behavior can be customized.

%package tests
Summary: Tests for Versioned Resources
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing z3c.coverage

%description tests
Versioned Resources insert a version number in the URL of a resource, so
that cache behavior can be customized.

This package contains tests for Versioned Resources.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Thu Jun 02 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

