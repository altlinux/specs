%define oname Products.CMFEditions
Name: python-module-%oname
Version: 2.2.11
Release: alt1.dev0.git20141007
Summary: Versioning for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.CMFEditions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.CMFEditions.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-transaction
BuildPreReq: python-module-zope.copy
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFDiffTool
BuildPreReq: python-module-Products.CMFUid
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.ZopeVersionControl
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-plone.app.blob-tests
#BuildPreReq: python-module-Products.CMFPlone
#BuildPreReq: python-module-Products.Archetypes
#BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.copy zope.dottedname zope.i18nmessageid zope.interface
%py_requires Products.CMFCore Products.CMFDiffTool Products.CMFUid
%py_requires Products.GenericSetup Products.ZopeVersionControl ZODB3

%description
CMFEditions provides versioning in Plone.

* It works out of the box.
* It's higly extensible for specific use cases.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
Requires: python-module-plone.app.blob-tests
%py_requires zope.testing Products.CMFDynamicViewFTI
#py_requires Products.CMFPlone Products.Archetypes
#py_requires Products.PloneTestCase

%description tests
CMFEditions provides versioning in Plone.

* It works out of the box.
* It's higly extensible for specific use cases.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
CMFEditions provides versioning in Plone.

* It works out of the box.
* It's higly extensible for specific use cases.

This package contains documentation for %oname.

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

%files docs
%doc doc/*

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.2.11-alt1.dev0.git20141007
- Initial build for Sisyphus

