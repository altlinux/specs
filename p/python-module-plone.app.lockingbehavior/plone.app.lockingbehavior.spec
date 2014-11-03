%define mname plone.app
%define oname %mname.lockingbehavior
Name: python-module-%oname
Version: 1.1
Release: alt1.dev.git20130223
Summary: Locking integration for dexterity content objects
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.lockingbehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.lockingbehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.locking
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.configuration

%py_provides %oname
%py_requires %mname plone.behavior plone.dexterity plone.locking
%py_requires zope.component

%description
The plone.app.lockingbehavior package provides a plone.locking
integration for dexterity.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing zope.configuration

%description tests
The plone.app.lockingbehavior package provides a plone.locking
integration for dexterity.

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
rm -fR build
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.dev.git20130223
- Initial build for Sisyphus

