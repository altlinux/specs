%define oname fastcluster

%def_with python3

Name: python-module-%oname
Version: 1.1.13
Release: alt1
Summary: Fast hierarchical clustering routines for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/fastcluster/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests gcc-c++
BuildPreReq: libnumpy-devel python-module-scipy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests gcc-c++
BuildPreReq: libnumpy-py3-devel python3-module-scipy
%endif

%py_provides %oname
%py_requires numpy scipy

%description
This library provides Python functions for hierarchical clustering. It
generates hierarchical clusters from distance matrices or from vector
data.

%package -n python3-module-%oname
Summary: Fast hierarchical clustering routines for Python
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy

%description -n python3-module-%oname
This library provides Python functions for hierarchical clustering. It
generates hierarchical clusters from distance matrices or from vector
data.

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

%files
%doc *.txt docs/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.13-alt1
- Initial build for Sisyphus

