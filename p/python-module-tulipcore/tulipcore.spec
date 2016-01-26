%define oname tulipcore

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1.0
Release: alt2.a2.git20140503
Summary: An alternative Gevent core loop implementation with asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/tulipcore/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/decentfox/tulipcore.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-gevent
BuildPreReq: python-module-greenlet
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-gevent
#BuildPreReq: python3-module-greenlet
BuildRequires: python3-module-cffi python3-module-greenlet python3-module-pytest
%endif

%py_provides %oname
#%py_requires asyncio gevent greenlet

%description
tulipcore is an alternative gevent core loop. It is based on asyncio
a.k.a. tulip, the async library for Python 3. With tulipcore, you can
run gevent code on top of asyncio.

%package -n python3-module-%oname
Summary: An alternative Gevent core loop implementation with asyncio
Group: Development/Python3
%py3_provides %oname
#%py3_requires asyncio gevent greenlet

%description -n python3-module-%oname
tulipcore is an alternative gevent core loop. It is based on asyncio
a.k.a. tulip, the async library for Python 3. With tulipcore, you can
run gevent code on top of asyncio.

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
python setup.py test
%endif
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%if_with python2
%files
%doc AUTHORS *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 0.1.0-alt2.a2.git20140503
- Rebuild with "def_disable check"
- Cleanup buildreq

* Sun Jan 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.0-alt1.a2.git20140503
- Initial build for Sisyphus

