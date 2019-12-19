%define oname fido

Name: python3-module-%oname
Version: 4.2.2
Release: alt2

Summary: Intelligent asynchronous HTTP client
License: ASLv2.0
Group: Development/Python3
Url: https://pypi.python.org/pypi/fido
BuildArch: noarch

# https://github.com/Yelp/fido.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-twisted-core python3-module-crochet
BuildRequires: python3-module-service-identity python3-module-OpenSSL
BuildRequires: python3-module-coverage python3-module-flake8
BuildRequires: python3-module-mock python3-module-twisted-web
BuildRequires: python3(yelp_bytes) python3(constantly)
BuildRequires: python3-module-pytest

%py3_provides %oname
%py3_requires twisted.internet crochet service_identity OpenSSL
%py3_requires twisted.web concurrent.futures


%description
Fido is a simple, asynchronous HTTP client built on top of Crochet,
Twisted and concurrent.futures. It is intended to be used in
environments where there is no event loop, and where you cannot afford
to spin up lots of threads (otherwise you could just use a
ThreadPoolExecutor).

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
rm -f tests/0_import_reactor_test.py
rm -f tests/acceptance/fetch_test.py
py.test3

%files
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*


%changelog
* Thu Dec 19 2019 Andrey Bychkov <mrdrew@altlinux.org> 4.2.2-alt2
- build for python2 disabled

* Sun Oct 14 2018 Igor Vlasenko <viy@altlinux.ru> 4.2.2-alt1.1.qa1
- NMU: applied repocop patch

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

