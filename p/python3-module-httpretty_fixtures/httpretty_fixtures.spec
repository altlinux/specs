%define oname httpretty_fixtures

Name:       python3-module-%oname
Version:    2.0.1
Release:    alt2

Summary:    Fixture manager for httpretty
License:    MIT
Group:      Development/Python
Url:        https://pypi.python.org/pypi/httpretty_fixtures

BuildArch:  noarch

# https://github.com/underdogio/httpretty-fixtures.git
Source:     %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-httpretty python3-module-nose
BuildRequires: python3-module-requests

%py3_provides %oname
%py3_requires httpretty


%description
This was written to solve communicating to an Elasticsearch during
tests. For our usage, mock didn't scale well and placing httpretty
fixtures on our base test case was impratical. To solve this, we wrote
a fixture manager, httpretty-fixtures.

Features:
* Reuse responses across tests
* Allows maintaining state between requests
  - See the Examples section for a demonstration
* Access past request information
  - On per-fixture basis
  - Across all fixtures

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3 httpretty_fixtures/test/*.py -v

%files
%doc *.rst docs/*
%python3_sitelibdir/*


%changelog
* Fri Jan 31 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.git20150714.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.git20150714.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20150714
- Initial build for Sisyphus

