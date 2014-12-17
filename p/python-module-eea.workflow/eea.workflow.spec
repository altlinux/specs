%define mname eea
%define oname %mname.workflow
Name: python-module-%oname
Version: 7.9
Release: alt1.dev.git20141015
Summary: Enhancements for the default Plone/CMF workflow system
License: GPLv2+
Group: Development/Python
Url: http://eggrepo.eea.europa.eu/d/eea.workflow/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/eea/eea.workflow.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-eea.versions
BuildPreReq: python-module-eea.jquery
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-plone.protect
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-z3c.caching
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname eea.versions eea.jquery collective.monkeypatcher
%py_requires plone.protect Products.ATVocabularyManager Products.CMFCore
%py_requires Products.Archetypes Products.statusmessages plone.portlets
%py_requires Products.CMFPlone plone.app.layout plone.app.portlets
%py_requires plone.app.contentrules plone.contentrules zope.interface
%py_requires zope.component zope.formlib zope.event zope.schema
%py_requires zope.annotation zope.i18nmessageid z3c.caching

%description
Enhancements for the default Plone/CMF workflow system.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Enhancements for the default Plone/CMF workflow system.

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

pushd %mname/workflow
cp -fR *.txt *.zcml Extensions documentation profiles skins \
	%buildroot%python_sitelibdir/%mname/workflow/
install -p -m644 browser/*.pt browser/*.js browser/*.zcml \
	%buildroot%python_sitelibdir/%mname/workflow/browser/
install -p -m644 portlets/*.zcml portlets/*.pt \
	%buildroot%python_sitelibdir/%mname/workflow/portlets/
install -p -m644 rules/*.zcml \
	%buildroot%python_sitelibdir/%mname/workflow/rules/
install -p -m644 upgrades/*.zcml \
	%buildroot%python_sitelibdir/%mname/workflow/upgrades/
install -p -m644 tests/*.txt \
	%buildroot%python_sitelibdir/%mname/workflow/tests/
popd

%check
python setup.py test

%files
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Wed Dec 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 7.9-alt1.dev.git20141015
- Initial build for Sisyphus

