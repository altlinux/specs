%define oname pytest-flakes

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20140206.1
Summary: pytest plugin to check source code with pyflakes
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-flakes/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fschulze/pytest-flakes.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests pyflakes
BuildPreReq: python-module-pytest-cache python-module-pytest
BuildPreReq: python-module-pytest-pep8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pytest-cache python3-module-pytest
BuildPreReq: python3-pyflakes python3-module-pytest-pep8
%endif

%description
py.test plugin for efficiently checking python source with pyflakes.

%package -n python3-module-%oname
Summary: pytest plugin to check source code with pyflakes
Group: Development/Python3

%description -n python3-module-%oname
py.test plugin for efficiently checking python source with pyflakes.

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
export PYTHONPATH=$PWD
py.test
%if_with python3
pushd ../python3
export PYTHONPATH=$PWD
py.test-%_python3_version
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2-alt1.git20140206.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20140206
- Initial build for Sisyphus

