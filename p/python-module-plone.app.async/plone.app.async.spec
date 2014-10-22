%define oname plone.app.async

%def_disable check

Name: python-module-%oname
Version: 1.7
Release: alt1.dev0.git20130527
Summary: Integration package for zc.async allowing asynchronous operations in Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.app.async/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.app.async.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-rwproperty python-module-simplejson
BuildPreReq: python-module-zc.async-tests
BuildPreReq: python-module-zc.monitor
BuildPreReq: python-module-zc.z3monitor
BuildPreReq: python-module-five.intid
BuildPreReq: python-module-zope.keyreference
BuildPreReq: python-module-five.intid-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-mock
BuildPreReq: python-module-uuid

%py_provides %oname
%py_requires plone.app zc.async zc.monitor zc.z3monitor five.intid
%py_requires zope.keyreference

%description
Integration package for zc.async allowing asynchronous operations in
Plone 3 and 4.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires five.intid.tests plone.app.testing zc.async.testing

%description tests
Integration package for zc.async allowing asynchronous operations in
Plone 3 and 4.

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
py.test

%files
%doc *.rst docs/*
%python_sitelibdir/plone/app/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/app/*/test*

%files tests
%python_sitelibdir/plone/app/*/test*

%changelog
* Wed Oct 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7-alt1.dev0.git20130527
- Initial build for Sisyphus

