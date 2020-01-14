%define oname schemabuilder

Name: python3-module-%oname
Version: 0.3.0
Release: alt3

Summary: Helper to build json schema definitions
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/schemabuilder/
BuildArch: noarch

# https://github.com/dinoboff/schemabuilder.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-jsonschema python3-module-coverage
BuildRequires: python-tools-2to3

%py3_provides %oname
%py3_requires jsonschema


%description
Helpers to build you define JSON schema for either validation or
publication.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Helpers to build you define JSON schema for either validation or
publication.

This package contains tests for %oname.

%prep
%setup

find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Jan 14 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.3.0-alt3
- porting on python3

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2.git20150105.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.git20150105
- Fixed build

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150105
- Initial build for Sisyphus

