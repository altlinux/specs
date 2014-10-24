%define mname collective
%define oname %mname.documentviewer
Name: python-module-%oname
Version: 3.0.2
Release: alt1.git20140531
Summary: Document cloud's document viewer integration into plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.documentviewer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.documentviewer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.browserresource
BuildPreReq: python-module-repoze.catalog
BuildPreReq: python-module-plone.app.z3cform
BuildPreReq: python-module-collective.monkeypatcher
BuildPreReq: python-module-plone.app.testing

%py_provides %oname
%py_requires %mname Products.CMFPlone zope.browserresource
%py_requires repoze.catalog plone.app.z3cform collective.monkeypatcher

%description
This package integrates documentcloud's viewer and pdf processing into
plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package integrates documentcloud's viewer and pdf processing into
plone.

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.0.2-alt1.git20140531
- Initial build for Sisyphus

