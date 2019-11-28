%define oname dirtyjson

Name: python3-module-%oname
Version: 1.0.3
Release: alt2

Summary: Python JSON parser for reading JSON objects out of JS files
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/dirtyjson/
BuildArch: noarch

# https://github.com/codecobblers/dirtyjson.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

This package contains tests for %oname.

%prep
%setup

sed -i 's|#!/usr/bin/env python|#!/usr/bin/env python3|' \
    $(find ./ -name '*.py')

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Thu Nov 28 2019 Andrey Bychkov <mrdrew@altlinux.org> 1.0.3-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.git20150108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20150108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150108
- Initial build for Sisyphus

