%define oname pytest-services

%def_with python3

Name: python-module-%oname
Version: 1.0.4
Release: alt1.git20150120
Summary: Services plugin for pytest testing framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-services/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pytest-dev/pytest-services.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: libmemcached-devel libmysqlclient-devel
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-subprocess32
BuildPreReq: python-module-tox python-module-mock
BuildPreReq: python-module-mysqlclient python-module-pylibmc
BuildPreReq: python-module-pytest-cov python-module-pytest-pep8
BuildPreReq: python-module-psutil
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests
BuildPreReq: python3-module-tox python3-module-mock
BuildPreReq: python3-module-mysqlclient python3-module-pylibmc
BuildPreReq: python3-module-pytest-cov python3-module-pytest-pep8
BuildPreReq: python3-module-psutil
%endif

%py_provides pytest_services
%py_requires requests psutil subprocess32

%description
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

%package -n python3-module-%oname
Summary: Services plugin for pytest testing framework
Group: Development/Python3
%py3_provides pytest_services
%py3_requires requests psutil

%description -n python3-module-%oname
The plugin provides a set of fixtures and utility functions to start
service processes for your tests with pytest.

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
py.test -vv --fixtures tests
%if_with python3
pushd ../python3
py.test-%_python3_version -vv --fixtures tests
popd
%endif

%files
%doc *.rst docs/*.rst docs/api
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst docs/api
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.4-alt1.git20150120
- Version 1.0.4

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150120
- Initial build for Sisyphus

