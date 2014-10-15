%define oname Products.PlonePAS

Name: python-module-%oname
Version: 5.0.1
Release: alt1.dev0.git20140405
Summary: PlonePAS adapts the PluggableAuthService for use by Plone
License: ZPL
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.PlonePAS/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.PluggableAuthService
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.LDAPMultiPlugins
BuildPreReq: python-module-Products.LDAPUserFolder
BuildPreReq: python-module-Products.BTreeFolder2
BuildPreReq: python-module-Products.PluginRegistry
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-unidecode
BuildPreReq: python-module-zope.ramcache
BuildPreReq: python-module-repoze.xmliter
BuildPreReq: python-module-future
BuildPreReq: python-module-Products.Archetypes-tests
BuildPreReq: python-module-plone.session
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires Products.PluggableAuthService Products.CMFCore
%py_requires Products.LDAPMultiPlugins Products.LDAPUserFolder
%py_requires Products.Five plone.memoize unidecode zope.ramcache
%py_requires Products.BTreeFolder2 repoze.xmliter Products.Archetypes
%py_requires plone.session plone.i18n Products.GenericSetup

%description
This product adapts the "PluggableAuthService" for use by Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PluginRegistry plone.app.testing plone.testing
%py_requires Products.Archetypes.tests

%description tests
This product adapts the "PluggableAuthService" for use by Plone.

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
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0.1-alt1.dev0.git20140405
- Version 5.0.1.dev0
- Enabled testing

* Sat Oct 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.4-alt1
- Initial build for Sisyphus

