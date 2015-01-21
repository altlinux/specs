%define oname wsrpc-tornado

%def_with python3

Name: python-module-%oname
Version: 0.1.1
Release: alt1.git20150119
Summary: WSRPC is WebSocket Remote procedure call for tornado and javascript
License: LGPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/wsrpc-tornado/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/mosquito/wsrpc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-tornado
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-tornado
BuildPreReq: python-tools-2to3
%endif

%py_provides wsrpc
%py_requires tornado

%description
Remote Procedure call through WebSocket between browser and tornado.

%package -n python3-module-%oname
Summary: WSRPC is WebSocket Remote procedure call for tornado and javascript
Group: Development/Python3
%py3_provides wsrpc
%py3_requires tornado

%description -n python3-module-%oname
Remote Procedure call through WebSocket between browser and tornado.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
cp -fR wsrpc/static %buildroot%python_sitelibdir/wsrpc/

%if_with python3
pushd ../python3
%python3_install
cp -fR wsrpc/static %buildroot%python3_sitelibdir/wsrpc/
popd
%endif

%files
%doc *.rst auth.py example
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst auth.py example
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.git20150119
- Initial build for Sisyphus

