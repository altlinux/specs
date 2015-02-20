%define oname decorated

%def_with python3

Name: python-module-%oname
Version: 1.5.2
Release: alt1.git20150220
Summary: Decorator framework and common decorators for python
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/decorated/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/CooledCoffee/decorated.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-six python-module-fixtures2
BuildPreReq: python-module-pylru
BuildPreReq: python-modules-logging
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-six python3-module-fixtures2
BuildPreReq: python3-module-pylru
%endif

%py_provides %oname
%py_requires six logging pylru

%description
Decorator framework and common decorators for python.

%package -n python3-module-%oname
Summary: Decorator framework and common decorators for python
Group: Development/Python3
%py3_provides %oname
%py3_requires six logging pylru

%description -n python3-module-%oname
Decorator framework and common decorators for python.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
pushd src
%python_build_debug
popd

%if_with python3
pushd ../python3/src
%python3_build_debug
popd
%endif

%install
pushd src
%python_install
popd

%if_with python3
pushd ../python3/src
%python3_install
popd
%endif

%check
export PYTHONPATH=$PWD/src
py.test -vv
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD/src
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.2-alt1.git20150220
- Initial build for Sisyphus

