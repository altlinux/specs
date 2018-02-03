%define oname cerberus

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1.1
Summary: Extensible validation for Python dictionaries
License: ISCL
Group: Development/Python
Url: https://pypi.python.org/pypi/Cerberus/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/nicolaiarocci/cerberus.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides %oname

%description
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation. It has no dependancies and is thoroughly tested
under Python 2.6, Python 2.7, Python 3.3 and Python 3.4.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation. It has no dependancies and is thoroughly tested
under Python 2.6, Python 2.7, Python 3.3 and Python 3.4.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Extensible validation for Python dictionaries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation. It has no dependancies and is thoroughly tested
under Python 2.6, Python 2.7, Python 3.3 and Python 3.4.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Cerberus is an ISC Licensed validation tool for Python dictionaries.

Cerberus provides type checking and other base functionality out of the
box and is designed to be non-blocking and easily extensible, allowing
for custom validation. It has no dependancies and is thoroughly tested
under Python 2.6, Python 2.7, Python 3.3 and Python 3.4.

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
py.test -v %oname/tests

%if_with python3
pushd ../python3
py.test3 -v %oname/tests
popd
%endif

%files
%doc AUTHORS CHANGES LICENSE *.rst docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS CHANGES LICENSE *.rst docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue May 23 2017 Lenar Shakirov <snejok@altlinux.ru> 1.1-alt1
- New version

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8-alt1.git20141120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Nov 27 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8-alt1.git20141120
- Initial build for Sisyphus

