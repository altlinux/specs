%define oname plone.app.hud
Name: python-module-%oname
Version: 1.0
Release: alt1.a2.git20130921
Summary: Plone Heads Up Display Panels
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.hud/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.hud.git 
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow python-module-mock
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-coverage
BuildPreReq: python-module-flake8
BuildPreReq: python-module-Plone
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.hud
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Clouseau
BuildPreReq: python-module-Products.DocFinderTab
BuildPreReq: python-module-Products.PDBDebugMode
BuildPreReq: python-module-Products.PrintingMailHost
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-jarn.mkrelease
BuildPreReq: python-module-niteoweb.loginas
BuildPreReq: python-module-plone.app.debugtoolbar
BuildPreReq: python-module-plone.reload
BuildPreReq: python-module-zest.pocompile
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-zptlint
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires plone.app Plone plone.api plone.hud

%description
This Plone add-on contains several HUD Panels:

* Best Practices - Plone best practices panel.
* Content Browser - browse through catalog.
* Security Advisories - RSS reader for securiry advisories directly
  inside Plone.
* Users - basic users information.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This Plone add-on contains several HUD Panels:

* Best Practices - Plone best practices panel.
* Content Browser - browse through catalog.
* Security Advisories - RSS reader for securiry advisories directly
  inside Plone.
* Users - basic users information.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This Plone add-on contains several HUD Panels:

* Best Practices - Plone best practices panel.
* Content Browser - browse through catalog.
* Security Advisories - RSS reader for securiry advisories directly
  inside Plone.
* Users - basic users information.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This Plone add-on contains several HUD Panels:

* Best Practices - Plone best practices panel.
* Content Browser - browse through catalog.
* Security Advisories - RSS reader for securiry advisories directly
  inside Plone.
* Users - basic users information.

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

export PYTHONPATH=$PWD/src
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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%files pickles
%python_sitelibdir/%oname

%files docs
%doc docs/build/html/*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2.git20130921
- Initial build for Sisyphus

