%define oname plone.api
Name: python-module-%oname
Version: 1.3.3
Release: alt1.dev0.git20141118
Summary: Elegant and simple API, built for humans wishing to develop with Plone
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.api/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/plone/plone.api.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-decorator
BuildPreReq: python-module-Plone
BuildPreReq: python-module-coverage
BuildPreReq: python-module-flake8
BuildPreReq: python-module-jarn.mkrelease
BuildPreReq: python-module-manuel
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-mock
BuildPreReq: python-module-plone.app.dexterity
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-openid

%py_provides %oname
%py_requires plone Plone jarn.mkrelease zest.releaser
# for tests:
%py_requires plone.app.dexterity plone.app.testing

%description
The plone.api is an elegant and simple API, built for humans wishing to
develop with Plone.

It comes with cookbook-like documentation and step-by-step instructions
for doing common development tasks in Plone. Recipes try to assume the
user does not have extensive knowledge about Plone internals.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The plone.api is an elegant and simple API, built for humans wishing to
develop with Plone.

It comes with cookbook-like documentation and step-by-step instructions
for doing common development tasks in Plone. Recipes try to assume the
user does not have extensive knowledge about Plone internals.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
The plone.api is an elegant and simple API, built for humans wishing to
develop with Plone.

It comes with cookbook-like documentation and step-by-step instructions
for doing common development tasks in Plone. Recipes try to assume the
user does not have extensive knowledge about Plone internals.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
The plone.api is an elegant and simple API, built for humans wishing to
develop with Plone.

It comes with cookbook-like documentation and step-by-step instructions
for doing common development tasks in Plone. Recipes try to assume the
user does not have extensive knowledge about Plone internals.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

export PYTHONPATH=$PWD/src
pushd docs
sphinx-build -b pickle -d build/doctrees . build/pickle
sphinx-build -b html -d build/doctrees . build/html
popd

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/plone/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/plone/*/tests
%exclude %python_sitelibdir/plone/*/*/test*

%files tests
%python_sitelibdir/plone/*/tests
%python_sitelibdir/plone/*/*/test*

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*

%changelog
* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.3-alt1.dev0.git20141118
- Version 1.3.3.dev0

* Thu Oct 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.dev.git20140813
- Initial build for Sisyphus

