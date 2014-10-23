%define oname plone.app.cmsui
Name: python-module-%oname
Version: 1.0
Release: alt1.a2.git20111220
Summary: CMS user interface for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.cmsui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.cmsui.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-plone.app.toolbar
BuildPreReq: python-module-plone.namedfile
BuildPreReq: python-module-plone.formwidget.namedfile
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires plone.app plone.app.registry Products.CMFPlone
%py_requires plone.app.toolbar plone.namedfile zope.browserresource
%py_requires plone.formwidget.namedfile

%description
plone.app.cmsui installs a new content management user interface for
Plone. For the moment, it is an experiment only, but hopefully one that
will point the way towards Plone's future.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
plone.app.cmsui installs a new content management user interface for
Plone. For the moment, it is an experiment only, but hopefully one that
will point the way towards Plone's future.

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
* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.a2.git20111220
- Initial build for Sisyphus

