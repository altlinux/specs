%define oname cHaversine

%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150527
Summary: Fast haversine calculation
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/cHaversine
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/doublemap/cHaversine.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython
%endif

%py_provides %oname

%description
Fast haversine calculation. Returns distance between two lat/lon pairs
in meters. Implemented using Cython.

%if_with python3
%package -n python3-module-%oname
Summary: Fast haversine calculation
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Fast haversine calculation. Returns distance between two lat/lon pairs
in meters. Implemented using Cython.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
cython %oname/%oname.pyx
%python_build_debug

%if_with python3
pushd ../python3
cython3 %oname/%oname.pyx
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
python setup.py test -v
python setup.py build_ext -i
python test_cHaversine.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 setup.py build_ext -i
python3 test_cHaversine.py -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150527
- Initial build for Sisyphus

