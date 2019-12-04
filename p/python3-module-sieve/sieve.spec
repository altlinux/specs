%define oname sieve

Name: python3-module-%oname
Version: 0.1.9
Release: alt2

Summary: XML Comparison Utils
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/sieve/
BuildArch: noarch

# https://github.com/ralphbean/sieve.git
# branch: develop
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-lxml python3-module-six
BuildRequires: python3-module-markupsafe python3-module-nose

%py3_provides %oname
%py3_requires lxml six markupsafe


%description
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR
%py3_requires nose

%description tests
XML Comparison Utils.

Ripped from FormEncode and strainer just to support Pythons 2 and 3.
Intended for use in your webapp test suites.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Dec 04 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.9-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.9-alt1.git20130911.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.9-alt1.git20130911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.9-alt1.git20130911
- Initial build for Sisyphus

