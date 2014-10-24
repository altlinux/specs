%define oname plone.app.theming

Name: python-module-%oname
Version: 1.2.2.dev0
Release: alt1.dev0.git20141023
Summary: Integrates the Diazo theming engine with Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.theming/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.theming.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-diazo python-module-docutils
BuildPreReq: python-module-roman python-module-lxml
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.subrequest
BuildPreReq: python-module-plone.transformchain
BuildPreReq: python-module-plone.resource
BuildPreReq: python-module-plone.resourceeditor
BuildPreReq: python-module-repoze.xmliter
BuildPreReq: python-module-five.globalrequest
BuildPreReq: python-module-zope.traversing
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFPlone

%py_provides %oname
%py_requires plone.app.registry plone.subrequest plone.transformchain
%py_requires plone.resource plone.resourceeditor repoze.xmliter
%py_requires five.globalrequest zope.traversing
%py_requires Products.CMFPlone

%description
This package offers a simple way to develop and deploy Plone themes
using the Diazo theming engine.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
This package offers a simple way to develop and deploy Plone themes
using the Diazo theming engine.

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
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Fri Oct 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2.dev0-alt1.dev0.git20141023
- Version 1.2.2.dev0

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt2.dev0.git20141009
- Added necessary requirements
- Enabled testing

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.1-alt1.dev0.git20141009
- Initial build for Sisyphus

