%define oname aiorest

%def_without python2
%def_with python3

Name: python-module-%oname
Version: 0.4.0
Release: alt1.git20150118.1
Summary: REST interface for server based on aiohttp
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/aiorest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiorest.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-asyncio python-module-aiohttp
BuildPreReq: python-module-aioredis python-module-wheel
BuildPreReq: python-module-ipdb pyflakes python-tools-pep8
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-asyncio python3-module-aiohttp
BuildPreReq: python3-module-aioredis python3-module-wheel
BuildPreReq: python3-module-ipdb python3-pyflakes python3-tools-pep8
%endif

%py_provides %oname
%py_requires asyncio aiohttp aioredis

%description
JSON REST framework based on aiohttp (an asyncio (PEP 3156) http
server).

%package -n python3-module-%oname
Summary: REST interface for server based on aiohttp
Group: Development/Python3
%py3_provides %oname
%py3_requires asyncio aiohttp aioredis

%description -n python3-module-%oname
JSON REST framework based on aiohttp (an asyncio (PEP 3156) http
server).

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

rm -f requirements.txt

%check
%if_with python2
python setup.py test
#python runtests.py -v
%make pep
%endif
%if_with python3
pushd ../python3
python3 setup.py test
#python3 runtests.py -v
#make pep FLAKE=python3-pyflakes PEP=python3-pep8
popd
%endif

%if_with python2
%files
%doc *.txt *.rst docs/*.rst examples
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst docs/*.rst examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.0-alt1.git20150118.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20150118
- Version 0.4.0

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141223
- Initial build for Sisyphus

