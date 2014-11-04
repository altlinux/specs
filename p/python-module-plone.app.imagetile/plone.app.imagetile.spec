%define mname plone.app
%define oname %mname.imagetile
Name: python-module-%oname
Version: 1.0
Release: alt1.git20121010
Summary: Image tile for deco UI
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.imagetile/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.imagetile.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-interlude
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-plone.directives.form
BuildPreReq: python-module-plone.tiles
BuildPreReq: python-module-plone.app.tiles
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.formwidget.namedfile
BuildPreReq: python-module-plone.testing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname zope.schema zope.i18nmessageid plone.directives.form
%py_requires plone.tiles plone.app.tiles plone.namedfile
%py_requires plone.formwidget.namedfile

%description
Image tile, to be used with Deco Layout Editor.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.testing plone.app.testing zope.configuration

%description tests
Image tile, to be used with Deco Layout Editor.

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
%doc *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20121010
- Initial build for Sisyphus

