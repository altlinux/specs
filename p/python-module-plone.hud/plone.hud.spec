%define oname plone.hud
Name: python-module-%oname
Version: 1.0
Release: alt1.a1.git20130917
Summary: Plone Heads Up Display Framework
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.hud/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.hud.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Pillow
BuildPreReq: python-module-Plone
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-coverage
BuildPreReq: python-module-flake8
BuildPreReq: python-module-jarn.mkrelease
BuildPreReq: python-module-niteoweb.loginas
BuildPreReq: python-module-plone.app.debugtoolbar
BuildPreReq: python-module-plone.reload
BuildPreReq: python-module-Products.Clouseau
BuildPreReq: python-module-Products.DocFinderTab
BuildPreReq: python-module-Products.PDBDebugMode
BuildPreReq: python-module-Products.PrintingMailHost
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-zptlint
BuildPreReq: python-module-mock
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires plone Plone plone.api jarn.mkrelease niteoweb.loginas
%py_requires plone.app.debugtoolbar plone.reload Products.Clouseau
%py_requires Products.DocFinderTab Products.PDBDebugMode
%py_requires Products.PrintingMailHost zest.releaser

%description
plone.hud is framework for heads up display panels. It does not contain
any panels on it's own, this Plone add-on groups all the panels from
other add-ons (like plone.app.hud).

Framework looks for configlets in category HUD. Their browser views must
extend plone.hud.panel.HUDPanelView class and be registered for
Products.CMFPlone.interfaces.IPloneSiteRoot.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.hud is framework for heads up display panels. It does not contain
any panels on it's own, this Plone add-on groups all the panels from
other add-ons (like plone.app.hud).

Framework looks for configlets in category HUD. Their browser views must
extend plone.hud.panel.HUDPanelView class and be registered for
Products.CMFPlone.interfaces.IPloneSiteRoot.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
plone.hud is framework for heads up display panels. It does not contain
any panels on it's own, this Plone add-on groups all the panels from
other add-ons (like plone.app.hud).

Framework looks for configlets in category HUD. Their browser views must
extend plone.hud.panel.HUDPanelView class and be registered for
Products.CMFPlone.interfaces.IPloneSiteRoot.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
plone.hud is framework for heads up display panels. It does not contain
any panels on it's own, this Plone add-on groups all the panels from
other add-ons (like plone.app.hud).

Framework looks for configlets in category HUD. Their browser views must
extend plone.hud.panel.HUDPanelView class and be registered for
Products.CMFPlone.interfaces.IPloneSiteRoot.

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
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/*/test*

%files tests
%python_sitelibdir/plone/*/test*

%files pickles
%python_sitelibdir/%oname

%files docs
%doc docs/build/html/*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a1.git20130917
- Initial build for Sisyphus

