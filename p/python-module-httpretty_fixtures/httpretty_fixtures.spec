%define oname httpretty_fixtures

%def_with python3

Name: python-module-%oname
Version: 2.0.1
Release: alt1.git20150714.1.1
Summary: Fixture manager for httpretty
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/httpretty_fixtures
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/underdogio/httpretty-fixtures.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-httpretty python-module-nose
BuildPreReq: python-module-requests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-httpretty python3-module-nose
BuildPreReq: python3-module-requests
%endif

%py_provides %oname
%py_requires httpretty

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

%if_with python3
%package -n python3-module-%oname
Summary: Fixture manager for httpretty
Group: Development/Python3
%py3_provides %oname
%py3_requires httpretty

%description -n python3-module-%oname
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
python setup.py test
nosetests httpretty_fixtures/test/*.py -v
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3 httpretty_fixtures/test/*.py -v
popd
%endif

%files
%doc *.rst docs/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1.git20150714.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.0.1-alt1.git20150714.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.1-alt1.git20150714
- Initial build for Sisyphus

