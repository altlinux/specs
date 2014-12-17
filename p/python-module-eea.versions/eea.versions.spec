%define mname eea
%define oname %mname.versions
Name: python-module-%oname
Version: 7.5
Release: alt1.dev.git20141215
Summary: Versioning system for Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/eea.versions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.versions.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFEditions
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.discussion
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Products.ZCatalog Products.CMFCore Products.CMFPlone
%py_requires Products.CMFEditions Products.Archetypes plone.theme
%py_requires Products.ATContentTypes plone.app.layout plone.memoize
%py_requires plone.app.discussion plone.indexer zope.interface
%py_requires zope.component zope.annotation zope.event
%py_requires zope.globalrequest

%description
EEA Versions is a versioning system based on a version ID to group
certains objects and EffectiveDate to determine version number.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
EEA Versions is a versioning system based on a version ID to group
certains objects and EffectiveDate to determine version number.

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

pushd %mname/versions
cp -fR *.txt *.zcml *.pt docs documentation locales profiles skins \
	%buildroot%python_sitelibdir/%mname/versions/
install -p -m644 browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/versions/browser/
install -p -m644 upgrades/*.zcml \
	%buildroot%python_sitelibdir/%mname/versions/upgrades/
popd

%check
python setup.py test

%files
%doc *.md *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.5-alt1.dev.git20141215
- Initial build for Sisyphus

