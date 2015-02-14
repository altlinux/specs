%define oname Products.PloneGazette
Name: python-module-%oname
Version: 3.2.3
Release: alt1.dev0.git20150122
Summary: A complete Newsletter product for Plone
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PloneGazette/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.PloneGazette.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Plone python-module-elementtree
BuildPreReq: python-module-openid
BuildPreReq: python-module-Products.OrderableReferenceField
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-hexagonit.testing
BuildPreReq: python-module-Products.CMFPlone-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires Plone Products.OrderableReferenceField elementtree
%py_requires plone.directives.form zope.i18nmessageid

%description
A complete Newsletter product for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing hexagonit.testing Products.CMFPlone.tests

%description tests
A complete Newsletter product for Plone.

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
* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.2.3-alt1.dev0.git20150122
- Initial build for Sisyphus

