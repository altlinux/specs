%define oname schemabuilder

%def_without python3

Name: python-module-%oname
Version: 0.3.0
Release: alt2.git20150105.1
Summary: Helper to build json schema definitions
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/schemabuilder/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/dinoboff/schemabuilder.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-jsonschema python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-jsonschema python3-module-coverage
%endif

%py_provides %oname
%py_requires jsonschema

%description
Helpers to build you define JSON schema for either validation or
publication.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Helpers to build you define JSON schema for either validation or
publication.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Helper to build json schema definitions
Group: Development/Python3
%py3_provides %oname
%py3_requires jsonschema

%description -n python3-module-%oname
Helpers to build you define JSON schema for either validation or
publication.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Helpers to build you define JSON schema for either validation or
publication.

This package contains tests for %oname.
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
%make test py=python
%if_with python3
pushd ../python3
python3 setup.py test
%make test py=python3
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt2.git20150105.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Fri Mar 06 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt2.git20150105
- Fixed build

* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1.git20150105
- Initial build for Sisyphus

