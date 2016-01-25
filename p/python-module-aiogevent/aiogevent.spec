%define oname aiogevent

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.2
Release: alt2
Summary: asyncio API (PEP 3156) implemented on top of gevent
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aiogevent
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-gevent python-module-trollius
BuildPreReq: python-module-mock python-module-futures
BuildPreReq: python-module-aiotest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-gevent python3-module-asyncio
BuildPreReq: python3-module-mock python3-module-aiotest
%endif

%py_provides %oname
%py_requires trollius

%description
aiogevent implements the asyncio API (PEP 3156) on top of gevent. It
makes possible to write asyncio code in a project currently written for
gevent.

aiogevent allows to use greenlets in asyncio coroutines, and to use
asyncio coroutines, tasks and futures in greenlets: see link_future()
and wrap_greenlet() functions.

%package -n python3-module-%oname
Summary: asyncio API (PEP 3156) implemented on top of gevent
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
aiogevent implements the asyncio API (PEP 3156) on top of gevent. It
makes possible to write asyncio code in a project currently written for
gevent.

aiogevent allows to use greenlets in asyncio coroutines, and to use
asyncio coroutines, tasks and futures in greenlets: see link_future()
and wrap_greenlet() functions.

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
python runtests.py
python run_aiotest.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py
python3 run_aiotest.py
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
* Mon Jan 25 2016 Sergey Alembekov <rt@altlinux.ru> 0.2-alt2
- rebuild without check

* Tue Jan 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Version 0.2

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

