%define mname collective
%define oname %mname.testcaselayer

%def_disable check

Name: python-module-%oname
Version: 1.6.1
Release: alt1.dev0.git20140826
Summary: Use test cases as zope.testing layers
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.testcaselayer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.testcaselayer.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-zLOG
BuildPreReq: python-module-zope.testing python-module-initgroups
BuildPreReq: python-module-collective.monkeypatcher python-module-openid
BuildPreReq: python-module-Plone python-module-unittest2
BuildPreReq: python-module-argparse python-module-Zope2-tests
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-Products.PloneTestCase

%py_provides %oname
%py_requires %mname zope.testing collective.monkeypatcher
Requires: python-module-Zope2-tests
%py_requires Plone zope.component.testing zope.security.testing
%py_requires Products.PloneTestCase

%description
The support for layers provided by zope.testing helps to lessen the
amount of time consumed during test driven development by sharing
expensive test fixtures, such as is often requires for functional test.
This package provides several well tested facilities to make writing and
using layers faster and easier.

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

%changelog
* Mon Nov 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.6.1-alt1.dev0.git20140826
- Initial build for Sisyphus

