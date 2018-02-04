%define oname pytest-expect

%def_with python3

Name: python-module-%oname
Version: 0.9.1
Release: alt1.git20150720.1.1
Summary: A py.test plugin that stores test expectations by saving the set of failing tests
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-expect/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/gsnedders/pytest-expect.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_expect
%py_requires pytest

%description
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them in
future. The tests expectations are stored such that they can be
distributed alongside the tests. However, note that test expectations
can only be reliably shared between Python 2 and Python 3 if they only
use ASCII characters in their node ids: this likely isn't a limitation
if tests are using the normal Python format, as Python 2 only allows
ASCII characters in identifiers.

%if_with python3
%package -n python3-module-%oname
Summary: A py.test plugin that stores test expectations by saving the set of failing tests
Group: Development/Python3
%py3_provides pytest_expect
%py3_requires pytest

%description -n python3-module-%oname
A py.test plugin that stores test expectations by saving the set of
failing tests, allowing them to be marked as xfail when running them in
future. The tests expectations are stored such that they can be
distributed alongside the tests. However, note that test expectations
can only be reliably shared between Python 2 and Python 3 if they only
use ASCII characters in their node ids: this likely isn't a limitation
if tests are using the normal Python format, as Python 2 only allows
ASCII characters in identifiers.
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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.9.1-alt1.git20150720.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9.1-alt1.git20150720.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 28 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.1-alt1.git20150720
- Initial build for Sisyphus

