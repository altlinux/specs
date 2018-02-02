%define oname jsonform

%def_with python3

Name: python-module-%oname
Version: 0.0.2
Release: alt1.git20150116.1.1
Summary: Form validation for JSON-like data (i.e. document) in Python
License: MIT
Group: Development/Python
Url: https://github.com/RussellLuo/jsonform
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/RussellLuo/jsonform.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-jsonschema python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-jsonschema python3-module-nose
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname

%description
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Form validation for JSON-like data (i.e. document) in Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
JsonForm is mainly based on jsonschema, which is an implementation of
JSON Schema for Python.

Unlike the other validation libraries in Python, JsonForm is dedicated
to validating JSON-like data, which means it's a document-oriented
validation library.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
nosetests3
popd
%endif

%files
%doc *.md
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.md
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.0.2-alt1.git20150116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.2-alt1.git20150116.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.2-alt1.git20150116
- Version 0.0.2

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.1-alt1.git20140831
- Initial build for Sisyphus

