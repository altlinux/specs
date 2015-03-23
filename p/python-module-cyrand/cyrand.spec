%define oname cyrand

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3
Release: alt1.git20150228
Summary: Wrapper to Boost random numbers
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/cyrand/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andrewcron/cyrand.git
Source: %name-%version.tar

BuildPreReq: gcc-c++
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-matplotlib
BuildPreReq: boost-python-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-matplotlib
BuildPreReq: boost-python3-devel
%endif

%py_provides %oname
%py_requires numpy scipy matplotlib

%description
This is simply a set of cython definitions for the Boost TR1 Random
sampling library.

%if_with python3
%package -n python3-module-%oname
Summary: Wrapper to Boost random numbers
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy matplotlib

%description -n python3-module-%oname
This is simply a set of cython definitions for the Boost TR1 Random
sampling library.
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
sed -i 's|@IS3@|3|' ../python3/setup.py
%endif

sed -i 's|@IS3@||' setup.py

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif
exit 1

%files
%doc *.rst example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150228
- Initial build for Sisyphus

