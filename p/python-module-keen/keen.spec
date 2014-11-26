%define oname keen

%def_with python3

Name: python-module-%oname
Version: 0.3.5
Release: alt1.git20141125
Summary: Python Client for Keen IO
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/keen/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/keenlabs/KeenClient-Python.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-modules-json
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-requests python-module-pycrypto
BuildPreReq: python-module-Padding python-module-nose
BuildPreReq: python-module-urllib3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-requests python3-module-pycrypto
BuildPreReq: python3-module-Padding python3-module-nose
BuildPreReq: python3-module-urllib3
%endif

%py_provides %oname

%description
This is the official Python Client for the Keen IO API. The Keen IO API
lets developers build analytics features directly into their apps.

%package -n python3-module-%oname
Summary: Python Client for Keen IO
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This is the official Python Client for the Keen IO API. The Keen IO API
lets developers build analytics features directly into their apps.

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
%doc *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.5-alt1.git20141125
- Initial build for Sisyphus

