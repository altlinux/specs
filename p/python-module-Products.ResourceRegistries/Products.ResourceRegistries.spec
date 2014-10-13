%define oname Products.ResourceRegistries

%def_disable check

Name: python-module-%oname
Version: 3.0.1
Release: alt1.dev0.git20141009
Summary: Registry for managing CSS and JS
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ResourceRegistries/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/Products.ResourceRegistries.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.viewlet
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-zope.contentprovider
#BuildPreReq: python-module-plone.app.registry
#BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.component zope.interface zope.viewlet Products.CMFCore
%py_requires plone.protect Products.GenericSetup ZODB3
#py_requires plone.app.registry

%description
Provides a registry for linked Stylesheet and Javascript files.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.contentprovider
#py_requires Products.PloneTestCase

%description tests
Provides a registry for linked Stylesheet and Javascript files.

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
%doc *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Mon Oct 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.1-alt1.dev0.git20141009
- Initial build for Sisyphus

