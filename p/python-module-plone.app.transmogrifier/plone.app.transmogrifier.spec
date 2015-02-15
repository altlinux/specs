%define mname plone.app
%define oname %mname.transmogrifier
Name: python-module-%oname
Version: 1.3
Release: alt1
Summary: Plone blueprints for collective.transmogrifier pipelines
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.transmogrifier/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mjpieters/plone.app.transmogrifier.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-collective.transmogrifier-tests
BuildPreReq: python-module-Products.Archetypes
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.ATContentTypes
BuildPreReq: python-module-Products.CMFDynamicViewFTI
BuildPreReq: python-module-plone.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname collective.transmogrifier Products.Archetypes
%py_requires Products.CMFCore Products.ATContentTypes plone.i18n
%py_requires Products.CMFDynamicViewFTI zope.interface zope.event
%py_requires zope.annotation

%description
This package contains several blueprints for collective.transmogrifier
pipelines, commonly used to import content into a Plone site.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires collective.transmogrifier.tests zope.testing zope.component

%description tests
This package contains several blueprints for collective.transmogrifier
pipelines, commonly used to import content into a Plone site.

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
#py.test src/plone/app/transmogrifier/tests.py

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/tests.*

%files tests
%python_sitelibdir/plone/app/*/tests.*

%changelog
* Sun Feb 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1
- Version 1.3

* Sat Nov 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20120413
- Initial build for Sisyphus

