%define oname aioredis

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.1.5
Release: alt1.git20150225.1
Summary: asyncio (PEP 3156) Redis support
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aioredis/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aioredis.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-hiredis python-module-asyncio
BuildPreReq: pyflakes python-tools-pep8
%endif
BuildPreReq: python-module-sphinx-devel redis
BuildPreReq: python3-module-sphinx
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-hiredis python3-module-asyncio
BuildPreReq: python3-pyflakes python3-tools-pep8
%endif

%py_provides %oname
%py_requires hiredis asyncio

%description
The library is intended to provide simple and clear interface to Redis
based on asyncio.

Features:

* Connections pool
* Low-level & high-level API
* hiredis parser

%package -n python3-module-%oname
Summary: asyncio (PEP 3156) Redis support
Group: Development/Python3
%py3_provides %oname
%py3_requires hiredis asyncio

%description -n python3-module-%oname
The library is intended to provide simple and clear interface to Redis
based on asyncio.

Features:

* Connections pool
* Low-level & high-level API
* hiredis parser

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv docs/

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

%make -C docs html

%check
%if_with python2
python setup.py test
%make flake
%endif
%if_with python3
pushd ../python3
python3 setup.py test
%make flake FLAKE=python3-pyflakes PEP=python3-pep8
popd
%endif

%if_with python2
%files
%doc *.txt *.rst examples docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20150225
- New snapshot

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141217
- Initial build for Sisyphus

