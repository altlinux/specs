%define oname zantedeschia

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt1.git20150208.1
Summary: ZeroMQ sockets integrated with the AsyncIO event loop
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/Zantedeschia/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/takluyver/Zantedeschia.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-zmq python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-zmq python3-module-asyncio
%endif

%py_provides %oname
%py_requires zmq asyncio

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-cffi python3-module-greenlet python3-module-pluggy python3-module-py python3-module-pycparser python3-module-setuptools xz
BuildRequires: python3-module-asyncio python3-module-pytest python3-module-zmq rpm-build-python3 time

%description
Zantedeschia is an experimental alternative integration between asyncio
and ZeroMQ sockets.

%package -n python3-module-%oname
Summary: ZeroMQ sockets integrated with the AsyncIO event loop
Group: Development/Python3
%py3_provides %oname
%py3_requires zmq asyncio

%description -n python3-module-%oname
Zantedeschia is an experimental alternative integration between asyncio
and ZeroMQ sockets.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%check
%if_with python2
py.test -vv
%endif
%if_with python3
pushd ../python3
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20150208.1
- NMU: Use buildreq for BR.

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20150208
- Initial build for Sisyphus

