%define mname collective
%define oname %mname.instancebehavior
Name: python-module-%oname
Version: 0.3
Release: alt1.git20141202
Summary: Enable per instance behaviors on dexterity content 
License: BSD / GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.instancebehavior/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.instancebehavior.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-openid
BuildPreReq: python-module-simplejson python-module-Plone
BuildPreReq: python-module-plone.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.behavior
BuildPreReq: python-module-zope.interface
BuildPreReq: python-module-zope.component
BuildPreReq: python-module-zope.annotation

%py_provides %oname
%py_requires %mname Plone plone.dexterity plone.behavior zope.interface
%py_requires zope.component zope.annotation

%description
Enable behaviors per content type instance.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
Enable behaviors per content type instance.

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
%doc *.rst
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Fri Dec 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20141202
- Initial build for Sisyphus

