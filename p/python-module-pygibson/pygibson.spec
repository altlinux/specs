%define oname pygibson

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20131001
Summary: Python client for gibson cache server
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pygibson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/bak1an/pygibson.git
Source: %name-%version.tar

BuildPreReq: libgibsonclient-devel
BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Python client for gibson cache server.

%package -n python3-module-%oname
Summary: Python client for gibson cache server
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python client for gibson cache server.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
python -m tests.run
%if_with python3
pushd ../python3
python3 -m tests.run
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
* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20131001
- Initial build for Sisyphus

