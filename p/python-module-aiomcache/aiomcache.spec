%define oname aiomcache

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.1
Release: alt1.git20140713.1
Summary: memcached client for asyncio
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiomcache/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiomcache.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-asyncio python-module-nose
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-asyncio python3-module-nose
%endif

%py_provides %oname
%py_requires asyncio

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python3 python3-base python3-module-setuptools
BuildRequires: python3-module-nose python3-module-pytest rpm-build-python3

%description
asyncio (PEP 3156) library to work with memcached.

%package -n python3-module-%oname
Summary: memcached client for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio

%description -n python3-module-%oname
asyncio (PEP 3156) library to work with memcached.

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
python runtests.py -v
python examples/simple.py
%endif
%if_with python3
pushd ../python3
python3 setup.py test
python3 runtests.py -v
python3 examples/simple.py
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples
%python_sitelibdir/*
%exclude %python_sitelibdir/tests
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.1-alt1.git20140713.1
- NMU: Use buildreq for BR.

* Thu Jan 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20140713
- Initial build for Sisyphus

