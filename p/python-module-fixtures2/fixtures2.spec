%define oname fixtures2

%def_with python3

Name: python-module-%oname
Version: 0.1.2
Release: alt1.git20140528
Summary: Extension of the fixtures test framework
License: Free
Group: Development/Python
Url: https://pypi.python.org/pypi/fixtures2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/CooledCoffee/fixtures2.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mox python-module-fixtures
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mox python3-module-fixtures
%endif

%py_provides %oname
%py_requires mox fixtures

%description
Fixtures2 is an extension of the fixtures test framework.

%package -n python3-module-%oname
Summary: Extension of the fixtures test framework
Group: Development/Python3
%py3_provides %oname
%py3_requires mox fixtures

%description -n python3-module-%oname
Fixtures2 is an extension of the fixtures test framework.

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
* Fri Feb 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.git20140528
- Initial build for Sisyphus

