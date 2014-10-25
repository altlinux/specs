%define mname ploneintranet
%define oname %mname.invitations
Name: python-module-%oname
Version: 0.2
Release: alt1.dev0.git20141015
Summary: Generic invitation framework for use with ploneintranet
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/ploneintranet.invitations/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/ploneintranet/ploneintranet.invitations.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.api
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zest.releaser
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-openid

%py_provides %oname
Requires: python-module-%mname = %EVR
%py_requires plone.api zest.releaser

%description
Generic invitation framework for use with ploneintranet.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing

%description tests
Generic invitation framework for use with ploneintranet.

This package contains tests for %oname.

%description tests
Generic invitation framework for use with ploneintranet.

This package contains pickles for %oname

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Generic invitation framework for use with ploneintranet.

This package contains pickles for %oname

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Generic invitation framework for use with ploneintranet.

This package contains documentation for %oname

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname

%description -n python-module-%mname
Core files of %mname.

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

install -p -m644 src/ploneintranet/__init__.py \
	%buildroot%python_sitelibdir/ploneintranet/

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
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*
%exclude %python_sitelibdir/%mname/__init__.py*

%files tests
%python_sitelibdir/%mname/*/test*

%files pickles
%python_sitelibdir/%oname

%files docs
%doc docs/build/html/*

%files -n python-module-%mname
%dir %python_sitelibdir/%mname
%python_sitelibdir/%mname/__init__.py*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.dev0.git20141015
- Initial build for Sisyphus

