%define oname scs

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1
Summary: scs: splittling cone solver
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/scs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel
%endif

%description
Solves convex cone programs via operator splitting. Can solve: linear
programs (LPs) second-order cone programs (SOCPs), semidefinite programs
(SDPs), and exponential cone programs (EXPs).

%package -n python3-module-%oname
Summary: scs: splittling cone solver
Group: Development/Python3

%description -n python3-module-%oname
Solves convex cone programs via operator splitting. Can solve: linear
programs (LPs) second-order cone programs (SOCPs), semidefinite programs
(SDPs), and exponential cone programs (EXPs).

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
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus

