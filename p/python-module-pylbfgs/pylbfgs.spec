%define oname pylbfgs

%def_with python3

Name: python-module-%oname
Version: 0.2.0.2
Release: alt1
Summary: LBFGS and OWL-QN optimization algorithms
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/PyLBFGS
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-nose libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-nose libnumpy-py3-devel
%endif

%py_provides %oname lbfgs
%py_requires numpy

%description
This is a Python wrapper around Naoaki Okazaki (chokkan)'s liblbfgs
library of quasi-Newton optimization routines (limited memory BFGS and
OWL-QN).

This package aims to provide a cleaner interface to the LBFGS algorithm
than is currently available in SciPy, and to provide the OWL-QN
algorithm to Python users.

%if_with python3
%package -n python3-module-%oname
Summary: LBFGS and OWL-QN optimization algorithms
Group: Development/Python3
%py3_provides %oname lbfgs
%py3_requires numpy

%description -n python3-module-%oname
This is a Python wrapper around Naoaki Okazaki (chokkan)'s liblbfgs
library of quasi-Newton optimization routines (limited memory BFGS and
OWL-QN).

This package aims to provide a cleaner interface to the LBFGS algorithm
than is currently available in SciPy, and to provide the OWL-QN
algorithm to Python users.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

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

cp liblbfgs/README README.libLBFGS

%check
python setup.py test -v
python setup.py build_ext -i
nosetests -vv lbfgs
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
nosetests3 -vv lbfgs
popd
%endif

%files
%doc *.rst README.libLBFGS
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst README.libLBFGS
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0.2-alt1
- Initial build for Sisyphus

