%define oname profilehooks

%def_with python3

Name: python-module-%oname
Version: 1.7.1
Release: alt1.dev0.git20140926
Summary: Decorators for profiling/timing/tracing individual functions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/profilehooks/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mgedmin/profilehooks.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
It's a collection of decorators for profiling functions.

%package -n python3-module-%oname
Summary: Decorators for profiling/timing/tracing individual functions
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
It's a collection of decorators for profiling functions.

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

%check
%make test
%if_with python3
pushd ../python3
PYTHON=python3 make test
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
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.7.1-alt1.dev0.git20140926
- Initial build for Sisyphus

