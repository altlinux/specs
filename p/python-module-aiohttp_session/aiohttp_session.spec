%define oname aiohttp_session

%def_without python2
%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.20150211
Release: alt1.git20150211
Summary: Provide sessions for aiohttp.web
License: ASLv2.0
Group: Development/Python
Url: https://github.com/aio-libs/aiohttp_session
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/aio-libs/aiohttp_session.git
Source: %name-%version.tar
BuildArch: noarch

%if_with python2
BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-aiohttp python-module-jinja2
BuildPreReq: python-module-pycrypto python-module-aioredis
BuildPreReq: python-module-nose python-module-flake8
BuildPreReq: python-module-coverage
%endif
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-aiohttp python3-module-jinja2
BuildPreReq: python3-module-pycrypto python3-module-aioredis
BuildPreReq: python3-module-nose python3-module-flake8
BuildPreReq: python3-module-coverage
%endif

%py_provides %oname
%py_requires aiohttp jinja2 Crypto aioredis

%description
Provide sessions for aiohttp.web.

%package -n python3-module-%oname
Summary: Provide sessions for aiohttp.web
Group: Development/Python3
%py3_provides %oname
%py3_requires aiohttp jinja2 Crypto aioredis

%description -n python3-module-%oname
Provide sessions for aiohttp.web.

%prep
%setup

sed -i 's|@VERSION@|%version|' setup.py

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
%doc CHANGES.txt *.rst
%python_sitelibdir/*
%endif

%if_with python3
%files -n python3-module-%oname
%doc CHANGES.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.20150211-alt1.git20150211
- Initial build for Sisyphus

