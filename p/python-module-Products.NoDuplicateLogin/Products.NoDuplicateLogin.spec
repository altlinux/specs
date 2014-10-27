%define oname Products.NoDuplicateLogin
Name: python-module-%oname
Version: 1.0
Release: alt1.a2.svn20110218
Summary: This PAS plugin will reject multiple logins with the same user at the same time
License: ZPLv2.1
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.NoDuplicateLogin/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://svn.plone.org/svn/collective/PASPlugins/Products.NoDuplicateLogin/trunk/
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-zope.testing python-module-unittest2
BuildPreReq: python-module-Products.CMFPlone-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone

%description
This PAS plugin will reject multiple logins with the same user at the
same time. It ensures that only one browser may be logged with the same
userid at one time.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing Products.CMFPlone.tests

%description tests
This PAS plugin will reject multiple logins with the same user at the
same time. It ensures that only one browser may be logged with the same
userid at one time.

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
%doc *.txt docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests.*

%files tests
%python_sitelibdir/Products/*/tests.*

%changelog
* Mon Oct 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2.svn20110218
- Initial build for Sisyphus

