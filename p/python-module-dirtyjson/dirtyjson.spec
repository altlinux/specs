%define oname dirtyjson

%def_with python3

Name: python-module-%oname
Version: 1.0.3
Release: alt1.git20150108.1.1
Summary: Python JSON parser for reading JSON objects out of JS files
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/dirtyjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/codecobblers/dirtyjson.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Python JSON parser for reading JSON objects out of JS files
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
dirtyjson is a JSON decoder meant for extracting JSON-type data from .js
files. The returned data structure includes information about line and
column numbers, so you can output more useful error messages. The input
can also include single quotes, line comments, inline comments, dangling
commas, unquoted single-word keys, and hexadecimal and octal numbers.

This package contains tests for %oname.

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.3-alt1.git20150108.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.3-alt1.git20150108.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1.git20150108
- Initial build for Sisyphus

