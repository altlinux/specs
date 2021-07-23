%define oname tldextract

%def_disable check

Name: python3-module-%oname
Version: 1.5.1
Release: alt1.git20141205.3
Summary: Accurately separate the TLD from the registered domain and subdomains of a URL
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/tldextract/

# https://github.com/john-kurkowski/tldextract.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires: python3-module-pytest

Conflicts: python-module-%oname
Obsoletes: python-module-%oname

%description
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
tldextract accurately separates the gTLD or ccTLD (generic or country
code top-level domain) from the registered domain and subdomains of a
URL, using the Public Suffix List.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc *.md tldextract_app
%_bindir/*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.5.1-alt1.git20141205.3
- Drop python2 support.

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 1.5.1-alt1.git20141205.1.2
- (NMU) rebuild with python3.6

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.5.1-alt1.git20141205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.5.1-alt1.git20141205.1
- NMU: Use buildreq for BR.

* Tue Jan 20 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1.git20141205
- Initial build for Sisyphus

