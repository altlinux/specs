%define mname plone.app
%define oname %mname.deco
Name: python-module-%oname
Version: 1.0
Release: alt1.git20130310
Summary: Drag-and-drop layout composition system for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.deco/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.deco.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-interlude
BuildPreReq: python-module-unittest2 python-module-robotsuite
BuildPreReq: python-module-decorator python-module-coverage
BuildPreReq: python-module-robotframework-selenium2library
BuildPreReq: python-module-nose
BuildPreReq: python-module-plone.app.jquery
BuildPreReq: python-module-plone.app.blocks
BuildPreReq: python-module-plone.app.tiles
BuildPreReq: python-module-plone.app.toolbar
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.app.layoutpage
BuildPreReq: python-module-plone.app.texttile
BuildPreReq: python-module-plone.app.imagetile
BuildPreReq: python-module-z3c.form-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.act

%py_provides %oname
%py_requires %mname plone.app.jquery plone.app.blocks plone.app.tiles
%py_requires plone.app.toolbar plone.app.registry plone.app.layoutpage
%py_requires plone.app.texttile plone.app.imagetile

%description
Deco is a graphical editor for Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires z3c.form.testing plone.app.testing plone.act

%description tests
Deco is a graphical editor for Plone.

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
%doc *.txt *.rst
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*
%exclude %python_sitelibdir/plone/app/*/*/tests

%files tests
%python_sitelibdir/plone/app/*/test*
%python_sitelibdir/plone/app/*/*/tests

%changelog
* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20130310
- Initial build for Sisyphus

