%define oname Products.CMFUid
Name: python-module-%oname
Version: 2.3.0
Release: alt1.beta
Summary: Uid product for the Zope Content Management Framework
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFUid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eggtestinfo
BuildPreReq: python-module-Products.CMFCore-tests
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-zope.testrunner
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.CMFCore Products.GenericSetup

%description
CMFUid introduces a simple unique id implementation.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing zope.traversing.testing zope.component.testing
%py_requires Products.CMFCore.testing zope.security.testing

%description tests
CMFUid introduces a simple unique id implementation.

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
%doc *.txt
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/test*

%files tests
%python_sitelibdir/Products/*/test*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3.0-alt1.beta
- Initial build for Sisyphus

