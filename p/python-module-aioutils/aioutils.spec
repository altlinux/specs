%define oname aioutils

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.2.0
Release: alt1.git20150226.1.1
Summary: Python3 Asyncio Utils
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/aioutils/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/observerss/aioutils.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-pluggy python3-module-py python3-module-pytest python3-module-setuptools xz
BuildRequires: python3-module-asyncio python3-module-setuptools-tests rpm-build-python3 time

%description
Python3 Asyncio implements an event loop, but in quite low level, it
misses some basic helpers that can make our life a lot easier.

This package enhances asyncio.wait and asyncio.as_completed, provides
more user friendly interfaces through the following primitives.

* Group: a gevent.pool.Group alike object, allows you to spawn
  coroutines and join them later
* Pool: a gevent.poo.Pool alike object, allows setting concurrency level
* Bag: a helper to write generator with coroutines
* OrderedBag: a helper to write generator with coroutines, and keep
  yielding order the same as spawning order

%package -n python3-module-%oname
Summary: Python3 Asyncio Utils
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
Python3 Asyncio implements an event loop, but in quite low level, it
misses some basic helpers that can make our life a lot easier.

This package enhances asyncio.wait and asyncio.as_completed, provides
more user friendly interfaces through the following primitives.

* Group: a gevent.pool.Group alike object, allows you to spawn
  coroutines and join them later
* Pool: a gevent.poo.Pool alike object, allows setting concurrency level
* Bag: a helper to write generator with coroutines
* OrderedBag: a helper to write generator with coroutines, and keep
  yielding order the same as spawning order

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
export PYTHONPATH=$PWD
py.test -vv
%endif
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%if_with python2
%files
%doc *.md
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150226.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150226
- Initial build for Sisyphus

