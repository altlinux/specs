%define oname fido

%def_with python3

Name: python-module-%oname
Version: 4.2.2
Release: alt1.1
Summary: Intelligent asynchronous HTTP client
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/fido
BuildArch: noarch

# https://github.com/Yelp/fido.git
Source: %name-%version.tar

BuildRequires: python-dev python-module-setuptools
BuildRequires: python-module-twisted-core python-module-crochet
BuildRequires: python-module-service-identity python-module-OpenSSL
BuildRequires: python-module-coverage python-module-flake8
BuildRequires: python-module-mock python-module-twisted-web
BuildRequires: python-module-futures
BuildRequires: python-module-pytest
BuildRequires: python2.7(yelp_bytes) python2.7(constantly)
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev python3-module-setuptools
BuildRequires: python3-module-twisted-core python3-module-crochet
BuildRequires: python3-module-service-identity python3-module-OpenSSL
BuildRequires: python3-module-coverage python3-module-flake8
BuildRequires: python3-module-mock python3-module-twisted-web
BuildRequires: python3(yelp_bytes) python3(constantly)
BuildRequires: python3-module-pytest
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
# remove remote tests
rm -f tests/0_import_reactor_test.py
rm -f tests/acceptance/fetch_test.py
py.test
%if_with python3
pushd ../python3
# remove remote tests
rm -f tests/0_import_reactor_test.py
rm -f tests/acceptance/fetch_test.py
py.test3
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 4.2.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Oct 18 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.2.2-alt1
- Updated to upstream version 4.2.2.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.1.1-alt1.git20150807.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 2.1.1-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1.git20150807
- Initial build for Sisyphus

