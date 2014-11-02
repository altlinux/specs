%define oname Products.ATVocabularyManager
Name: python-module-%oname
Version: 1.6.7
Release: alt1.dev0.git20140314
Summary: Vocabulary library Plone. Central, Pluggable, TTW, with IMS VDEX Support
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Products.ATVocabularyManager/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/Products.ATVocabularyManager.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-imsvdex python-module-interlude
BuildPreReq: python-module-Pillow python-module-unittest2
BuildPreReq: python-module-argparse
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-Products.LinguaPlone
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests

%py_provides %oname
Requires: python-module-Zope2
%py_requires ZODB3 plone.app.layout plone.app.registry plone.app.uuid
%py_requires plone.app.z3cform plone.indexer plone.registry zope.event
%py_requires plone.z3cform zope.annotation zope.component zope.container
%py_requires zope.i18nmessageid zope.interface zope.lifecycleevent
%py_requires zope.site

%description
ATVocabularyManager: a vocabulary managing portal tool for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.LinguaPlone zope.component.testing
%py_requires zope.security.testing

%description tests
ATVocabularyManager: a vocabulary managing portal tool for Plone.

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
rm -fR build
py.test

%files
%doc *.txt *.rst docs/*
%python_sitelibdir/Products/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/Products/*/tests

%files tests
%python_sitelibdir/Products/*/tests

%changelog
* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.7-alt1.dev0.git20140314
- Initial build for Sisyphus

