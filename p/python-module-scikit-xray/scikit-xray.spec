%define oname scikit-xray

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.0.3
Release: alt1.git20141209
Summary: Data analysis tools for X-ray science
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/scikit-xray
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Nikea/scikit-xray.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock libnumpy-devel
BuildPreReq: python-module-six python-module-scipy
BuildPreReq: python-module-xraylib python-module-nose
BuildPreReq: python-module-netCDF4 python-module-lmfit
BuildPreReq: python-module-scikit-image python-module-coverage
BuildPreReq: python-module-sphinx-devel python-module-numpydoc
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock libnumpy-py3-devel
BuildPreReq: python3-module-six python3-module-scipy
BuildPreReq: python3-module-xraylib python3-module-nose
BuildPreReq: python3-module-netCDF4 python3-module-scikit-image
BuildPreReq: python3-module-coverage
%endif

%py_provides skxray
%py_requires netCDF4 xraylib lmfit

%description
Data analysis tools for X-ray science.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Data analysis tools for X-ray science.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Data analysis tools for X-ray science
Group: Development/Python3
%py3_provides skxray
%py3_requires netCDF4 xraylib
%add_python3_req_skip lmfit

%description -n python3-module-%oname
Data analysis tools for X-ray science.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Data analysis tools for X-ray science.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
Data analysis tools for X-ray science.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Data analysis tools for X-ray science.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install
cp -fR skxray/constants/data \
	%buildroot%python_sitelibdir/skxray/constants/

%if_with python3
pushd ../python3
%python3_install
cp -fR skxray/constants/data \
	%buildroot%python3_sitelibdir/skxray/constants/
popd
rm -f %buildroot%python3_sitelibdir/ctrans.*.so
%endif

%make -C doc pickle
%make -C doc html

install -d %buildroot%python_sitelibdir/%oname
cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
py.test
python run_tests.py
#if_with python3
%if 0
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
py.test-%_python3_version
python3 run_tests.py
popd
%endif

%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/testing

%files tests
%python_sitelibdir/*/testing

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/testing

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/testing
%endif

%changelog
* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141209
- New snapshot

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.3-alt1.git20141114
- Initial build for Sisyphus

