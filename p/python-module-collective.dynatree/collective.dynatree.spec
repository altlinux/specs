%define mname collective
%define oname %mname.dynatree
Name: python-module-%oname
Version: 2.1
Release: alt1.dev0.git20141030
Summary: Dynatree (JQuery Javascript) integration for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.dynatree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.dynatree.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-zope.schema python-module-openid
BuildPreReq: python-module-Plone python-module-unittest2
BuildPreReq: python-module-plone.behavior python-module-argparse
BuildPreReq: python-module-nose
BuildPreReq: python-module-collective.js.jqueryui
BuildPreReq: python-module-collective.js.backbone
BuildPreReq: python-module-Products.ATVocabularyManager
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-collective.vdexvocabulary
BuildPreReq: python-module-ipdb python-module-interlude
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-zope.dottedname
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.publisher

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.schema Plone plone.behavior Products.Archetypes
%py_requires collective.js.jqueryui collective.js.backbone
%py_requires plone.dexterity plone.supermodel plone.autoform zope.i18n
%py_requires zope.component zope.interface zope.dottedname
%py_requires zope.i18nmessageid zope.publisher

%description
collective.dynatree provides the basic integration of the jQuery plugin
jquery.dynatree.js (at google-code).

Optional it also provides a full-featured Archetypes Widget with full
ATVocabularyManager support, including hierachical VDEX-vocabularies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
collective.dynatree provides the basic integration of the jQuery plugin
jquery.dynatree.js (at google-code).

Optional it also provides a full-featured Archetypes Widget with full
ATVocabularyManager support, including hierachical VDEX-vocabularies.

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
nosetests

%files
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1-alt1.dev0.git20141030
- Initial build for Sisyphus

