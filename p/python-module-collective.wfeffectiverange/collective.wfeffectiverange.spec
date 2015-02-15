%define mname collective
%define oname %mname.wfeffectiverange
Name: python-module-%oname
Version: 1.7
Release: alt1.dev0.git20150204
Summary: Workflowed effective range (Plone/Dexterity)
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.wfeffectiverange/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.wfeffectiverange.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-interlude python-module-ipdb
BuildPreReq: python-module-Plone python-module-openid
BuildPreReq: python-module-Products.cron4plone
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname Plone Products.cron4plone plone.api plone.autoform
%py_requires plone.app.vocabularies z3c.form plone.indexer zope.schema
%py_requires plone.dexterity plone.supermodel plone.app.dexterity
%py_requires zope.interface zope.i18nmessageid

%description
Once one of the effective range dates was reached an automatic workflow
transition is executed and changes the workflow state with its managed
permissions.

This is intended as an alternative implementation of the Dexterity
IPublication behavior.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.contenttypes plone.app.robotframework
%py_requires plone.app.testing

%description tests
Once one of the effective range dates was reached an automatic workflow
transition is executed and changes the workflow state with its managed
permissions.

This is intended as an alternative implementation of the Dexterity
IPublication behavior.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/profiles/testing

%files tests
%python_sitelibdir/%mname/*/profiles/testing

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.git20150204
- Version 1.7.dev0

* Fri Dec 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6-alt1.dev0.git20141218
- Initial build for Sisyphus

