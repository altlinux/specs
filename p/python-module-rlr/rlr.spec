%define oname rlr

%def_with python3

Name: python-module-%oname
Version: 1.0
Release: alt1.git20141119
Summary: Regularized Logistic Regression
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/rlr/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/datamade/rlr.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel python3-module-nose
%endif

%py_provides %oname
%py_requires numpy

%description
A Cython implementation of L2 regularized logistic regression.

%package -n python3-module-%oname
Summary: Regularized Logistic Regression
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy

%description -n python3-module-%oname
A Cython implementation of L2 regularized logistic regression.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
cython rlr/lr.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 rlr/lr.pyx
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

%check
python setup.py test build_ext -i
nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test build_ext -i
nosetests3 -v
popd
%endif

%files
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20141119
- Initial build for Sisyphus

