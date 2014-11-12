%define mname collective
%define oname %mname.leadmedia
Name: python-module-%oname
Version: 0.0.1
Release: alt1.git20141112
Summary: Adds a slideshow to any dexterity folderish type
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.leadmedia/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/intk/collective.leadmedia.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-PasteScript
BuildPreReq: python-module-Zope2-tests python-module-unittest2
BuildPreReq: python-module-argparse
BuildPreReq: python-module-collective.folderishtypes
BuildPreReq: python-module-collective.slickslideshow
BuildPreReq: python-module-collective.flowplayer
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-plone.supermodel
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.autoform
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.app.contenttypes
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.theme
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.folderishtypes collective.slickslideshow
%py_requires collective.flowplayer Products.CMFCore Products.CMFPlone
%py_requires plone.app.layout plone.supermodel plone.dexterity
%py_requires plone.autoform plone.namedfile plone.app.contenttypes
%py_requires plone.indexer plone.theme zope.interface zope.component
%py_requires zope.schema zope.annotation

%description
Adds a slideshow to any dexterity folderish type.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires Products.PloneTestCase

%description tests
Adds a slideshow to any dexterity folderish type.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests.*

%files tests
%python_sitelibdir/%mname/*/tests.*

%changelog
* Wed Nov 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20141112
- Initial build for Sisyphus

