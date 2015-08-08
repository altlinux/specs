%define oname fido

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt1.git20150807
Summary: Intelligent asynchronous HTTP client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/fido
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Yelp/fido.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-twisted-core python-module-crochet
BuildPreReq: python-module-service-identity python-module-OpenSSL
BuildPreReq: python-module-coverage python-module-flake8
BuildPreReq: python-module-mock python-module-twisted-web
BuildPreReq: python-module-futures
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-twisted-core python3-module-crochet
BuildPreReq: python3-module-service-identity python3-module-OpenSSL
BuildPreReq: python3-module-coverage python3-module-flake8
BuildPreReq: python3-module-mock python3-module-twisted-web
%endif

%py_provides %oname
%py_requires twisted.internet crochet service_identity OpenSSL
%py_requires twisted.web concurrent.futures

%description
Fido is a simple, asynchronous HTTP client built on top of Crochet,
Twisted and concurrent.futures. It is intended to be used in
environments where there is no event loop, and where you cannot afford
to spin up lots of threads (otherwise you could just use a
ThreadPoolExecutor).

%if_with python3
%package -n python3-module-%oname
Summary: Intelligent asynchronous HTTP client
Group: Development/Python3
%py3_provides %oname
%py3_requires twisted.internet crochet service_identity OpenSSL
%py3_requires twisted.web

%description -n python3-module-%oname
Fido is a simple, asynchronous HTTP client built on top of Crochet,
Twisted and concurrent.futures. It is intended to be used in
environments where there is no event loop, and where you cannot afford
to spin up lots of threads (otherwise you could just use a
ThreadPoolExecutor).
%endif

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
python setup.py test -v
#if_with python3
%if 0
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150807
- Initial build for Sisyphus

