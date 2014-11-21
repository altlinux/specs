%define oname plone.multilingual
Name: python-module-%oname
Version: 1.2.1
Release: alt1.git20141015
Summary: Multilingual extensions core package
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.multilingual/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.multilingual.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.app.uuid
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.intid
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-zope.container
BuildPreReq: python-module-zope.lifecycleevent
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-zope.configuration
#BuildPreReq: python-module-plone.multilingualbehavior
#BuildPreReq: python-module-archetypes.multilingual

%py_provides %oname
Requires: python-module-Zope2
%py_requires plone.uuid plone.app.uuid Products.CMFPlone plone.indexer
%py_requires Products.CMFCore plone.dexterity
%py_requires zope.interface zope.component zope.container
%py_requires zope.lifecycleevent
#py_requires archetypes.multilingual plone.multilingualbehavior

%description
This package contains the core functionality for the next generation
multilingual engine.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.intid Products.ATContentTypes
%py_requires zope.configuration

%description tests
This package contains the core functionality for the next generation
multilingual engine.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%changelog
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.git20141015
- Initial build for Sisyphus

