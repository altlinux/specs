%define oname Products.ZopeVersionControl
Name: python-module-%oname
Version: 1.1.4
Release: alt1.dev.git20130313
Summary: Zope Version Control
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ZopeVersionControl/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/zopefoundation/Products.ZopeVersionControl.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction python-module-docutils

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.interface ZODB3

%description
Zope Version Control for the Zope application server.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Zope Version Control for the Zope application server.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.4-alt1.dev.git20130313
- Initial build for Sisyphus

