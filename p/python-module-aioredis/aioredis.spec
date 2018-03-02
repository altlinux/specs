%define oname aioredis

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 1.1.0
Release: alt1
Summary: asyncio (PEP 3156) Redis support
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/aioredis/

# https://github.com/aio-libs/aioredis.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires: redis
%if_with python2
BuildRequires: python-devel python-module-setuptools
BuildRequires: python-module-hiredis python2.7(asyncio)
BuildRequires: pyflakes python-tools-pep8
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-hiredis python3(asyncio)
BuildRequires: python3-pyflakes python3-tools-pep8
BuildRequires: python3(async_timeout)
BuildRequires: python3-module-sphinx-devel python3-module-sphinx python3(sphinxcontrib.asyncio)
BuildRequires: python3(sphinxcontrib.spelling) python3(enchant) libenchant
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

%if_with python3
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
%endif

%prep
%setup
%patch1 -p1

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
export LC_ALL=en_US.UTF-8
%if_with python2
%python_build_debug
%endif

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%if_with python2
%python_install
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%make -C docs html SPHINXBUILD=py3_sphinx-build

%check
export LC_ALL=en_US.UTF-8
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
%doc *.txt *.rst examples docs/_build/html
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst examples docs/_build/html
%python3_sitelibdir/*
%endif

%changelog
* Fri Mar 02 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1
- Updated to upstream version 1.1.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.5-alt1.git20150225.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Mar 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20150225
- New snapshot

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.5-alt1.git20141217
- Initial build for Sisyphus

