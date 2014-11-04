%define mname plone.app
%define oname %mname.texttile
Name: python-module-%oname
Version: 1.0
Release: alt1.git20121010
Summary: Text tile for Deco UI
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.texttile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.texttile.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-plone.app.tiles
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.contentprovider
BuildPreReq: python-module-plone.portlets
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-Products.CMFCore

%py_provides %oname
%py_requires %mname zope.schema zope.i18nmessageid plone.directives.form
%py_requires plone.tiles plone.app.z3cform plone.app.tiles

%description
Text tile, to be used with Deco Layout Editor.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing plone.app.testing zope.configuration
%py_requires zope.interface zope.component zope.publisher plone.portlets
%py_requires zope.contentprovider plone.dexterity Products.CMFCore

%description tests
Text tile, to be used with Deco Layout Editor.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20121010
- Initial build for Sisyphus

