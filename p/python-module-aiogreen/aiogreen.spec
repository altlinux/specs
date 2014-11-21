%define oname aiogreen

%def_with python3

Name: python-module-%oname
Version: 0.2
Release: alt1
Summary: asyncio event loop scheduling callbacks in eventlet
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiogreen
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-eventlet python-module-futures
BuildPreReq: python-module-trollius python-module-greenlet
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-eventlet python3-module-greenlet
BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires trollius

%description
asyncio event loop scheduling callbacks in eventlet.

%package -n python3-module-%oname
Summary: asyncio event loop scheduling callbacks in eventlet
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
asyncio event loop scheduling callbacks in eventlet.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

