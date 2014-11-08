%define oname httmock

%def_with python3

Name: python-module-%oname
Version: 1.2.2
Release: alt1.git20141017
Summary: A mocking library for requests
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/httmock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/patrys/httmock.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests
%endif

%py_provides %oname

%description
A mocking library for requests.

%package -n python3-module-%oname
Summary: A mocking library for requests
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A mocking library for requests.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sat Nov 08 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.2-alt1.git20141017
- Initial build for Sisyphus

