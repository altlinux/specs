%define _unpackaged_files_terminate_build 1
%define oname pytest-regtest

%def_with python3

Name: python-module-%oname
Version: 0.15.0
Release: alt1.1
Summary: py.test plugin for regression tests
License: GPLv3
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-regtest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# http://sissource.ethz.ch/uweschmitt/pytest-regtest.git
Source0: https://pypi.python.org/packages/88/80/ea05c590891d7c107adfa5be2262dbfaaf628be4fc8b37852c6126fff244/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BUildPreReq: python-tools-2to3
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_regtest

%description
This pytest-plugin allows capturing of output of test functions which
can be compared to the captured output from former runs. This is a
common technique to start TDD if you have to refactor legacy code which
ships without tests.

%package -n python3-module-%oname
Summary: py.test plugin for regression tests
Group: Development/Python3
%py3_provides pytest_regtest

%description -n python3-module-%oname
This pytest-plugin allows capturing of output of test functions which
can be compared to the captured output from former runs. This is a
common technique to start TDD if you have to refactor legacy code which
ships without tests.

%prep
%setup -q -n %{oname}-%{version}

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
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.15.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 0.15.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.1-alt1.git20141120.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Nov 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1.git20141120
- Version 0.4.1

* Wed Nov 19 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.0-alt1.git20141114
- Initial build for Sisyphus

