%define oname jsonform

Name: python3-module-%oname
Version: 0.0.2
Release: alt2

Summary: Form validation for JSON-like data (i.e. document) in Python
License: MIT
Group: Development/Python3
Url: https://github.com/RussellLuo/jsonform
BuildArch: noarch

# https://github.com/RussellLuo/jsonform.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-jsonschema python3-module-nose
BuildPreReq: python-tools-2to3

%py3_provides %oname


%description
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test
nosetests3

%files
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*


%changelog
* Fri Nov 29 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.0.2-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.git20150116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150116.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150116
- Version 0.0.2

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140831
- Initial build for Sisyphus

