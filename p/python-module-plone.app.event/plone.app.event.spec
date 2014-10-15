%define oname plone.app.event

Name: python-module-%oname
Version: 2.0
Release: alt1.a5.dev0.git20141014
Summary: The Plone calendar framework
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.event/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.event.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-pytz python-module-transaction
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.DateRecurringIndex
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.ZCatalog
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-collective.elephantvocabulary
BuildPreReq: python-module-icalendar
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.portlets
BuildPreReq: python-module-plone.app.querystring
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.textfield
BuildPreReq: python-module-plone.app.widgets
BuildPreReq: python-module-plone.app.vocabularies
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.event
BuildPreReq: python-module-plone.folder
BuildPreReq: python-module-plone.formwidget.recurrence
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-plone.app.robotframework
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-mock python-module-robotsuite
BuildPreReq: python-module-transaction python-module-unittest2
BuildPreReq: python-module-zExceptions
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.app.collection
BuildPreReq: python-module-plone.app.contentlisting
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.controlpanel

%py_provides %oname
Requires: python-module-Zope2
%py_requires zope.lifecycleevent zope.publisher
%py_requires zope.i18n zope.interface zope.i18nmessageid zope.schema
%py_requires zope.contentprovider zope.event zope.globalrequest
%py_requires z3c.form zope.annotation zope.component zope.container
%py_requires plone.registry plone.supermodel plone.uuid plone.z3cform
%py_requires plone.indexer plone.memoize plone.namedfile plone.portlets
%py_requires plone.event plone.folder plone.formwidget.recurrence
%py_requires plone.behavior plone.browserlayer plone.dexterity
%py_requires plone.app.vocabularies plone.app.z3cform plone.autoform
%py_requires plone.app.registry plone.app.textfield plone.app.widgets
%py_requires plone.app.layout plone.app.portlets plone.app.querystring
%py_requires Products.statusmessages collective.elephantvocabulary
%py_requires Products.GenericSetup Products.ZCatalog plone.app.dexterity
%py_requires plone.app Products.CMFCore Products.DateRecurringIndex
%py_requires Products.CMFPlone plone.app.contentlisting

%description
Plone.app.event is the calendaring framework for Plone. It provides
Dexterity behaviors and an Archetypes type, Timezone support, RFC5545
icalendar export, Recurrence support, event views and a lot more.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing plone.testing
%py_requires plone.app.collection plone.app.contenttypes

%description tests
Plone.app.event is the calendaring framework for Plone. It provides
Dexterity behaviors and an Archetypes type, Timezone support, RFC5545
icalendar export, Recurrence support, event views and a lot more.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Plone.app.event is the calendaring framework for Plone. It provides
Dexterity behaviors and an Archetypes type, Timezone support, RFC5545
icalendar export, Recurrence support, event views and a lot more.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Plone.app.event is the calendaring framework for Plone. It provides
Dexterity behaviors and an Archetypes type, Timezone support, RFC5545
icalendar export, Recurrence support, event views and a lot more.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst
%dir %python_sitelibdir/%oname
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*
%exclude %python_sitelibdir/plone/app/*/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*
%python_sitelibdir/plone/app/*/*/test*

%files pickles
%python_sitelibdir/%oname/pickle

%files docs
%doc docs/build/html/*

%changelog
* Wed Oct 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a5.dev0.git20141014
- New snapshot
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1.a5.dev0.git20141009
- Initial build for Sisyphus

