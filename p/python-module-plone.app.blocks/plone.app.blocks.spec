%define mname plone.app
%define oname %mname.blocks
Name: python-module-%oname
Version: 1.2
Release: alt1.git20131122
Summary: Implements the in-Plone blocks rendering process
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.blocks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.blocks.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-lxml python-module-zope.publisher
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.site
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-repoze.xmliter
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.subrequest
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-plone.memoize
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-plone.registry
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-transaction
BuildPreReq: python-module-Products.BTreeFolder2

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.interface zope.component zope.publisher
%py_requires zope.schema zope.site zope.i18nmessageid repoze.xmliter
%py_requires plone.tiles plone.behavior plone.subrequest plone.resource
%py_requires plone.memoize plone.transformchain plone.registry
%py_requires plone.app.registry Products.CMFCore

%description
This package implements the 'blocks' rendering model, by providing
several transform stages that hook into plone.transformchain.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing plone.app.testing zope.configuration
%py_requires Products.BTreeFolder2

%description tests
This package implements the 'blocks' rendering model, by providing
several transform stages that hook into plone.transformchain.

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
%doc *.txt *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20131122
- Initial build for Sisyphus

