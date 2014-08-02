%define oname asa

%def_with python3

Name: python-module-%oname
Version: 0.4
Release: alt2
Summary: Python bindings for the ASA
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyasa/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-Cython libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-Cython libnumpy-py3-devel
%endif

%description
Python bindings for the Adaptive Simulated Annealing (ASA).

%package -n python3-module-%oname
Summary: Python bindings for the ASA
Group: Development/Python3

%description -n python3-module-%oname
Python bindings for the Adaptive Simulated Annealing (ASA).

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt2
- Added module for Python 3

* Thu Aug 16 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Initial build for Sisyphus

