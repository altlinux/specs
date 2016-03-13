%define oname asyncio_redis

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.14.1
Release: alt1.git20150808.1.1
Summary: PEP 3156 implementation of the redis protocol
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/asyncio_redis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jonathanslenders/asyncio-redis.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-hiredis python-module-asyncio-tests
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-hiredis python3-module-asyncio-tests
%endif

%py_provides %oname
%py_requires asyncio hiredis

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools
BuildRequires: python3-module-pytest rpm-build-python3

%description
Redis client for the PEP 3156 Python event loop.

This Redis library is a completely asynchronous, non-blocking client for
a Redis server.

%package -n python3-module-%oname
Summary: PEP 3156 implementation of the redis protocol
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio hiredis

%description -n python3-module-%oname
Redis client for the PEP 3156 Python event loop.

This Redis library is a completely asynchronous, non-blocking client for
a Redis server.

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
python tests.py -v
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 tests.py -v
popd
%endif

%if_with python2
%files
%doc CHANGELOG *.txt *.rst docs/*.rst docs/pages examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.txt *.rst docs/*.rst docs/pages examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.14.1-alt1.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.14.1-alt1.git20150808.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.14.1-alt1.git20150808
- Version 0.14.1

* Sat Jan 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.13.4-alt1.git20140818
- Initial build for Sisyphus

