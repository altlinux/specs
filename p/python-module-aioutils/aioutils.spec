%define oname aioutils

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.3.10
Release: alt1.1
Summary: Python3 Asyncio Utils
License: ASLv2.0
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/aioutils/

# https://github.com/observerss/aioutils.git
Source: %name-%version.tar

%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python2.7(asyncio)
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3(asyncio) python3(nose)
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires asyncio

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
py.test3 -vv
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.10-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Dec 04 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.3.10-alt1
- Updated to upstream version 0.3.10.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.0-alt1.git20150226.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.2.0-alt1.git20150226.1
- NMU: Use buildreq for BR.

* Thu Feb 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1.git20150226
- Initial build for Sisyphus

