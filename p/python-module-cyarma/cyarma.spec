%define oname cyarma

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140620
Summary: A set of cython bindings for using armadillo in cython
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/cyarma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andrewcron/cy_armadillo.git
Source: %name-%version.tar
Source1: setup.py

BuildPreReq: gcc-c++ libarmadillo-devel libhdf5-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-Cython libnumpy-devel
BuildPreReq: python-module-scipy python-module-matplotlib
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-matplotlib
%endif

%py_provides %oname
%py_requires numpy scipy matplotlib

%description
This is simply a set of cython definitions for the Armadillo C++
library. It also includes conversion utilities to and from numpy arrays.
For now, the best working model is to inline them using the "include"
cython statement. "Installing" the package only stores the definitions
in site_packages so that distutils can find it later.

%if_with python3
%package -n python3-module-%oname
Summary: A set of cython bindings for using armadillo in cython
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy matplotlib

%description -n python3-module-%oname
This is simply a set of cython definitions for the Armadillo C++
library. It also includes conversion utilities to and from numpy arrays.
For now, the best working model is to inline them using the "include"
cython statement. "Installing" the package only stores the definitions
in site_packages so that distutils can find it later.
%endif

%prep
%setup

rm -f setup.py
install -m644 %SOURCE1 ./
sed -i 's|@VERSION@|%version|' setup.py

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst example
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140620
- Initial build for Sisyphus

