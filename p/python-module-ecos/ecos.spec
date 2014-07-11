%define oname ecos

%def_with python3

Name: python-module-%oname
Version: 1.0.4
Release: alt1
Summary: Embedded Conic Solver (ECOS)
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/ecos/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel
%endif

%description
A lightweight conic solver for second-order cone programming.

%package -n python3-module-%oname
Summary: Embedded Conic Solver (ECOS)
Group: Development/Python3

%description -n python3-module-%oname
A lightweight conic solver for second-order cone programming.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Jul 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1
- Initial build for Sisyphus

