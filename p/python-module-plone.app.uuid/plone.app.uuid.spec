%define oname plone.app.uuid
Name: python-module-%oname
Version: 1.1.1
Release: alt2.dev0.git20140823
Summary: Plone integration for the basic plone.uuid package
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.uuid/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.uuid.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.uuid
BuildPreReq: python-module-plone.indexer
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.Archetypes

%py_provides %oname
%py_requires plone.app plone.uuid plone.indexer zope.publisher
%py_requires zope.interface

%description
This package integrates the low-level plone.uuid into Plone-the-
application.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.dexterity plone.app.testing
%py_requires Products.Archetypes

%description tests
This package integrates the low-level plone.uuid into Plone-the-
application.

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
* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt2.dev0.git20140823
- Added necessary requirements

* Tue Oct 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20140823
- Initial build for Sisyphus

