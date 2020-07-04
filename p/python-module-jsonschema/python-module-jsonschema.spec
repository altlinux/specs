%define oname jsonschema

Name:		python-module-%oname
Version:	2.6.0
Release:	alt3
Summary:	An implementation of JSON Schema validation for Python

License:	MIT
Group:		Development/Python
URL:		http://pypi.python.org/pypi/jsonschema/
Source0:	%name-%version.tar.gz
BuildArch:	noarch

BuildRequires:	python-devel python-module-setuptools
BuildPreReq: python-modules-json python-module-nose python-module-mock
BuildPreReq: python-module-vcversioner python-module-functools32

%py_requires functools32

%description
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
jsonschema is JSON Schema validator currently based on
http://tools.ietf.org/html/draft-zyp-json-schema-03

This package contains tests for %oname.

%prep
%setup

%build
%python_build

%install
%python_install

%check
nosetests -v

%files
%doc *.rst COPYING
# Python 3 version provides jsonschema tool
%exclude %_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Sat Jul 04 2020 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt3
- (NMU) Don't pack jsonschema tool (closes: #38673)

* Fri Jul 03 2020 Vladimir Didenko <cow@altlinux.org> 2.6.0-alt1.2
- (NMU) Build Python 3 version in separate package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.6.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Aug 01 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 2.6.0-alt1
- Updated to upstream release 2.6.0.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.5.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5.1-alt1
- Version 2.5.1

* Fri Oct 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.4.0-alt1
- Version 2.4.0
- Added module for Python 3

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 0.2-alt1
- Initial release for Sisyphus (based on Fedora)
