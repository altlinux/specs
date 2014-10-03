%define oname django-registration

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.hg20130617
Summary: An extensible user-registration application for Django
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/django-registration/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# hg clone https://bitbucket.org/ubernostrum/django-registration
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-sphinx-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: An extensible user-registration application for Django
Group: Development/Python3

%description -n python3-module-%oname
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a fairly simple user-registration application for Django,
designed to make allowing user signups as painless as possible. It
requires a functional installation of Django 1.4 or newer, but has no
other dependencies.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

export PYTHONPATH=%buildroot%python_sitelibdir
%make -C docs pickle
%make -C docs html

install -d %buildroot%python_sitelibdir/%oname
cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%files
%doc AUTHORS CHANGELOG README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGELOG README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Oct 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.hg20130617
- Initial build for Sisyphus

