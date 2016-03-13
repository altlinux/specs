%define oname brew

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20150323.1
Summary: BREW: Python Multiple Classifier System API
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/brew/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/viisar/brew.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-wheel python-module-scikit-learn
BuildPreReq: python-module-numpy python-module-scipy
BuildPreReq: python-module-coverage python-module-pytest-cov
BuildPreReq: python-module-sphinx-devel
BuildPreReq: python-module-sphinxcontrib-napoleon
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-wheel python3-module-scikit-learn
BuildPreReq: python3-module-numpy python3-module-scipy
BuildPreReq: python3-module-coverage python3-module-pytest-cov
%endif

%py_provides %oname
%py_requires sklearn numpy

%description
BREW: A Multiple Classifier Systems API.

The aim of this project is to provide a structure for Ensemble
Generation, Ensemble Pruning, and Static and Dynamic selection of
classifiers.

%if_with python3
%package -n python3-module-%oname
Summary: BREW: Python Multiple Classifier System API
Group: Development/Python3
%py3_provides %oname
%py3_requires sklearn numpy

%description -n python3-module-%oname
BREW: A Multiple Classifier Systems API.

The aim of this project is to provide a structure for Ensemble
Generation, Ensemble Pruning, and Static and Dynamic selection of
classifiers.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
BREW: A Multiple Classifier Systems API.

The aim of this project is to provide a structure for Ensemble
Generation, Ensemble Pruning, and Static and Dynamic selection of
classifiers.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
BREW: A Multiple Classifier Systems API.

The aim of this project is to provide a structure for Ensemble
Generation, Ensemble Pruning, and Static and Dynamic selection of
classifiers.

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

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
py.test -vv --cov-report html --cov brew/ test/
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv --cov-report html --cov brew/ test/
popd
%endif

%files
%doc *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.git20150323.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150323
- Initial build for Sisyphus

