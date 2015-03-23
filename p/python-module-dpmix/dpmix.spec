%define oname dpmix

%def_with python3

Name: python-module-%oname
Version: 0.3
Release: alt1.git20150301
Summary: Optimized (and optionally gpu enhaced) fitting of Gaussian Mixture Models
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/dpmix/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/andrewcron/dpmix.git
Source: %name-%version.tar

BuildPreReq: gcc-c++ libarmadillo-devel libgomp-devel libhdf5-devel
BuildPreReq: python-devel python-module-setuptools-tests xvfb-run
BuildPreReq: python-module-Cython libnumpy-devel /proc
BuildPreReq: python-module-scipy python-module-matplotlib
BuildPreReq: python-module-cyarma python-module-cyrand
BuildPreReq: python-module-pymc
BuildPreReq: python-modules-multiprocessing
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython libnumpy-py3-devel
BuildPreReq: python3-module-scipy python3-module-matplotlib
BuildPreReq: python3-module-cyarma python3-module-cyrand
BuildPreReq: python3-module-pymc
%endif

%py_provides %oname
%py_requires numpy scipy matplotlib cyarma cyrand multiprocessing pymc
%add_python_req_skip gpustats pycuda

%description
dpmix is a library for understanding posterior distributions for
Dirichlet and heirarchical Dirichlet mixtures of normal distributions
represented by truncated stick breaking.

%if_with python3
%package -n python3-module-%oname
Summary: Optimized (and optionally gpu enhaced) fitting of Gaussian Mixture Models
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy matplotlib cyarma cyrand multiprocessing pymc
%add_python3_req_skip gpustats pycuda

%description -n python3-module-%oname
dpmix is a library for understanding posterior distributions for
Dirichlet and heirarchical Dirichlet mixtures of normal distributions
represented by truncated stick breaking.
%endif

%prep
%setup

# we not have Cuda
rm -f src/gpuworker.py src/multigpu.py tests/test_multigpu.py

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
export PYTHONPATH=%buildroot%python_sitelibdir
pushd tests
xvfb-run nosetests -v %oname
popd
%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
pushd tests
xvfb-run nosetests3 -v %oname
popd
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
* Mon Mar 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20150301
- Initial build for Sisyphus

