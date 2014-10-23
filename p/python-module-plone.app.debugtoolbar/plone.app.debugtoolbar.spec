%define oname plone.app.debugtoolbar
Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20140813
Summary: Debug toolbar for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.debugtoolbar/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.debugtoolbar.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-paste
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires plone.app Products.CMFPlone zope.annotation
%py_requires plone.transformchain

%description
plone.app.debugtoolbar provides a wealth of debug information about a
running Plone site at your fingertips. Simply install it in your build
(e.g. by adding it to the eggs list in your Buildout and re-running
buildout) and install it into your Plone site.

You should now see a Debug link at the top of your site. Click it to
open the debug drawer. Click on a panel to view relevant information.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.debugtoolbar provides a wealth of debug information about a
running Plone site at your fingertips. Simply install it in your build
(e.g. by adding it to the eggs list in your Buildout and re-running
buildout) and install it into your Plone site.

You should now see a Debug link at the top of your site. Click it to
open the debug drawer. Click on a panel to view relevant information.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20140813
- Initial build for Sisyphus

