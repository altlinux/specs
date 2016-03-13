%define oname fido

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt1.git20150807.1.1
Summary: Intelligent asynchronous HTTP client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/fido
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Yelp/fido.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-twisted-core python-module-crochet
#BuildPreReq: python-module-service-identity python-module-OpenSSL
#BuildPreReq: python-module-coverage python-module-flake8
#BuildPreReq: python-module-mock python-module-twisted-web
#BuildPreReq: python-module-futures
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-twisted-core python3-module-crochet
#BuildPreReq: python3-module-service-identity python3-module-OpenSSL
#BuildPreReq: python3-module-coverage python3-module-flake8
#BuildPreReq: python3-module-mock python3-module-twisted-web
%endif

%py_provides %oname
%py_requires twisted.internet crochet service_identity OpenSSL
%py_requires twisted.web concurrent.futures

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: pyflakes python-base python-devel python-module-OpenSSL python-module-cffi python-module-cryptography python-module-enum34 python-module-mccabe python-module-pyasn1 python-module-pyasn1-modules python-module-pytest python-module-serial python-module-setuptools python-module-twisted-core python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-unittest python-tools-2to3 python-tools-pep8 python3 python3-base python3-module-cffi python3-module-cryptography python3-module-cssselect python3-module-enum34 python3-module-genshi python3-module-mccabe python3-module-ntlm python3-module-pip python3-module-pycparser python3-module-pytest python3-module-setuptools python3-module-zope.interface python3-pyflakes python3-tools-pep8
BuildRequires: python-module-coverage python-module-crochet python-module-flake8 python-module-pbr python-module-service-identity python-module-setuptools-tests python-module-unittest2 python3-module-coverage python3-module-flake8 python3-module-html5lib python3-module-pbr python3-module-pygobject3 python3-module-serial python3-module-unittest2 python3-module-zope rpm-build-python3 time

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150807
- Initial build for Sisyphus

