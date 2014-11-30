%define mname ftw
%define oname %mname.topics
Name: python-module-%oname
Version: 1.1.3
Release: alt1.dev0.git20141127
Summary: Create subject trees in Plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.topics/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.topics.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2 python-module-mocker
BuildPreReq: python-module-pyquery python-module-transaction
BuildPreReq: python-module-simplelayout.base
BuildPreReq: python-module-ftw.contentpage
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-archetypes.referencebrowserwidget
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.browserlayer
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-Products.GenericSetup
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.formwidget.contenttree
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-collective.dexteritytextindexer
BuildPreReq: python-module-plone.app.referenceablebehavior
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-z3c.autoinclude
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.inflator

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname simplelayout.base ftw.contentpage zope.schema
%py_requires Products.Archetypes archetypes.schemaextender ftw.upgrade
%py_requires archetypes.referencebrowserwidget zope.interface
%py_requires zope.component zope.i18nmessageid plone.app.layout
%py_requires plone.browserlayer plone.memoize Products.GenericSetup
%py_requires Products.CMFCore Products.CMFPlone plone.autoform
%py_requires plone.formwidget.contenttree plone.behavior plone.dexterity
%py_requires plone.app.dexterity collective.dexteritytextindexer
%py_requires plone.app.referenceablebehavior plone.directives.form

%description
This package integrates a subject tree into Plone.

Features:

* Dexterity based content types "Topic Tree" and "Topic" for creating a
  topic tree (subject tree).
* Archetypes schema extender, adding a reference field "topics" to all
  objects prividing ITopicSupport for assigning content to a topic.
* The topic-view lists all content referenced the topic.
* Simplelayout support for topics, so that additional content can be
  added to the topic view.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing ftw.testbrowser ftw.builder.testing zope.i18n
%py_requires z3c.autoinclude zope.traversing zope.configuration
%py_requires plone.uuid plone.testing plone.app.testing ftw.inflator

%description tests
This package integrates a subject tree into Plone.

Features:

* Dexterity based content types "Topic Tree" and "Topic" for creating a
  topic tree (subject tree).
* Archetypes schema extender, adding a reference field "topics" to all
  objects prividing ITopicSupport for assigning content to a topic.
* The topic-view lists all content referenced the topic.
* Simplelayout support for topics, so that additional content can be
  added to the topic view.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sun Nov 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.3-alt1.dev0.git20141127
- Initial build for Sisyphus

