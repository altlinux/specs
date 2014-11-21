%define mname plone.app
%define oname %mname.multilingual
Name: python-module-%oname
Version: 2.0
Release: alt1.a4.dev0.git20141027
Summary: Plone multilingual content plugin (AT/DX)
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.multilingual/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.multilingual.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-decorator
BuildPreReq: python-module-z3c.relationfield
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-Products.PloneLanguageTool
BuildPreReq: python-module-archetypes.multilingual
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.contenttypes-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.browsermenu
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.app.intid
BuildPreReq: python-module-zope.pagetemplate
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zc.relation
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-plone.app.event-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.pagetemplate zope.globalrequest zc.relation
%py_requires zope.i18nmessageid zope.formlib zope.app.intid
%py_requires zope.browsermenu zope.traversing zope.publisher z3c.form
%py_requires zope.component zope.lifecycleevent zope.site zope.schema
%py_requires Products.Archetypes Products.LinguaPlone zope.interface
%py_requires Products.ATContentTypes Products.statusmessages zope.event
%py_requires %mname z3c.relationfield plone.behavior plone.dexterity
%py_requires plone.app.z3cform plone.app.registry Products.CMFPlone
%py_requires plone.formwidget.contenttree Products.PloneLanguageTool
%py_requires archetypes.multilingual Products.CMFCore Products.ZCatalog

%description
Multilingual Plone UI package, enables maintenance of translations for
both Dexterity types and Archetypes.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing plone.app.robotframework
%py_requires plone.app.contenttypes.testing zope.configuration
%py_requires plone.app.event.testing

%description tests
Multilingual Plone UI package, enables maintenance of translations for
both Dexterity types and Archetypes.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a4.dev0.git20141027
- Initial build for Sisyphus

