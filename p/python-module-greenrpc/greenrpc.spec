%define oname greenrpc

%def_without python3

Name: python-module-%oname
Version: 0.1.4
Release: alt2.git20141101.1
Summary: TCP & HTTP RPC Servers built on msgpack and gevent
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/greenrpc/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/brettlangdon/greenrpc.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-gevent python-module-msgpack
BuildPreReq: python-module-requests python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-gevent python3-module-msgpack
BuildPreReq: python3-module-requests
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires gevent msgpack requests json

%description
TCP & HTTP RPC Servers written with msgpack and gevent.

%if_with python3
%package -n python3-module-%oname
Summary: TCP & HTTP RPC Servers built on msgpack and gevent
Group: Development/Python3
%py3_provides %oname
%py3_requires gevent msgpack requests

%description -n python3-module-%oname
TCP & HTTP RPC Servers written with msgpack and gevent.
%endif

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
%if_with python3
pushd ../python3
%python3_install
popd
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.md
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.4-alt2.git20141101.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt2.git20141101
- Fixed build

* Tue Jan 27 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.4-alt1.git20141101
- Initial build for Sisyphus

