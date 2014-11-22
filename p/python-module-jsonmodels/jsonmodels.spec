%define oname jsonmodels

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20141115
Summary: Make easier to deal with structures that are converted to, or read from JSON
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/jsonmodels/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/beregond/jsonmodels.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-dateutil python-module-six
BuildPreReq: python-module-jinja2 python-module-markupsafe
BuildPreReq: python-module-Pygments python-module-wheel
BuildPreReq: python-module-docutils python-module-flake8
BuildPreReq: python-module-invoke python-module-mccabe
BuildPreReq: python-module-mock python-tools-pep8
BuildPreReq: python-module-enchant pyflakes
BuildPreReq: python-module-pyhistory python-module-pytest-cov
BuildPreReq: python-module-tox python-module-virtualenv
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-spelling
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-dateutil python3-module-six
BuildPreReq: python3-module-jinja2 python3-module-markupsafe
BuildPreReq: python3-module-Pygments python3-module-wheel
BuildPreReq: python3-module-docutils python3-module-flake8
BuildPreReq: python3-module-invoke python3-module-mccabe
BuildPreReq: python3-module-mock python3-tools-pep8
BuildPreReq: python3-module-enchant python3-pyflakes
BuildPreReq: python3-module-pyhistory python3-module-pytest-cov
BuildPreReq: python3-module-tox python3-module-virtualenv
%endif

%py_provides %oname

%description
jsonmodels is library to make it easier for you to deal with structures
that are converted to, or read from JSON.

%package -n python3-module-%oname
Summary: Make easier to deal with structures that are converted to, or read from JSON
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
jsonmodels is library to make it easier for you to deal with structures
that are converted to, or read from JSON.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
jsonmodels is library to make it easier for you to deal with structures
that are converted to, or read from JSON.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
jsonmodels is library to make it easier for you to deal with structures
that are converted to, or read from JSON.

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

%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
flake8 jsonmodels tests
%if_with python3
pushd ../python3
python3 setup.py test
python3-flake8 jsonmodels tests
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20141115
- Initial build for Sisyphus

