%define oname pytest-localserver

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.3
Release: alt2
Summary: py.test plugin to test server connections locally
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-localserver/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-werkzeug python-module-OpenSSL
BuildPreReq: python-module-six python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-werkzeug python3-module-OpenSSL
BuildPreReq: python3-module-six python3-module-requests
%endif

%py_provides pytest_localserver

%description
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

%package -n python3-module-%oname
Summary: py.test plugin to test server connections locally
Group: Development/Python3
%py3_provides pytest_localserver

%description -n python3-module-%oname
pytest-localserver is a plugin for the pytest testing framework which
enables you to test server connections locally.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
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
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt2
- Fixed requirements

* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.3-alt1
- Initial build for Sisyphus

