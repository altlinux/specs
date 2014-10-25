%define mname collective
%define oname %mname.workspace
Name: python-module-%oname
Version: 1.2
Release: alt1.dev0.git20140927
Summary: Restricted workspaces for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.workspace/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.workspace.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-plone.app.robotframework-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.api

%py_provides %oname
%py_requires %mname plone.app.dexterity plone.formwidget.autocomplete
%py_requires zest.releaser

%description
collective.workspace package for providing 'membership' in specific
areas of a Plone Site.

It allows you to grant people access to areas of content using a
membership group rather than local roles for each user, and to delegate
control over that group to people who don't have access to the site-wide
user/group control panel.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.robotframework plone.app.testing plone.api
%py_requires plone.app.robotframework.testing

%description tests
collective.workspace package for providing 'membership' in specific
areas of a Plone Site.

It allows you to grant people access to areas of content using a
membership group rather than local roles for each user, and to delegate
control over that group to people who don't have access to the site-wide
user/group control panel.

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
%doc *.txt *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.dev0.git20140927
- Initial build for Sisyphus

