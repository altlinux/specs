%define oname corbeau

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1.git20130925
Summary: A Sentry client based on Raven that verifies SSL certs
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/corbeau/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/kilink/corbeau.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-raven python-module-requests
BuildPreReq: python-module-mock python-module-urllib3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-raven python3-module-requests
BuildPreReq: python3-module-mock python3-module-urllib3
%endif

%py_provides %oname
%py_requires raven requests

%description
Corbeau is an extension to Raven which adds a cert-verifying HTTPS
transport.

%package -n python3-module-%oname
Summary: A Sentry client based on Raven that verifies SSL certs
Group: Development/Python3
%py3_provides %oname
%py3_requires raven requests

%description -n python3-module-%oname
Corbeau is an extension to Raven which adds a cert-verifying HTTPS
transport.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1.git20130925
- Initial build for Sisyphus

