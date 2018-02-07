%define _unpackaged_files_terminate_build 1
%define oname pytest-variables

%def_with python3

Name: python-module-%oname
Version: 1.4
Release: alt1.1
Summary: pytest plugin for providing variables to tests/fixtures
License: MPLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-variables/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/davehunt/pytest-variables.git
Source0: https://pypi.python.org/packages/ef/44/2f8207347c0ae3e8216feb4306be4ca575e184fda220d057095db9513b2f/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildRequires: python3-module-pytest
%endif

%py_provides pytest_variables
%py_requires pytest

%description
pytest-variables is a plugin for py.test that provides variables to
tests/fixtures as a dict via a JSON file specified on the command line.

%if_with python3
%package -n python3-module-%oname
Summary: pytest plugin for providing variables to tests/fixtures
Group: Development/Python3
%py3_provides pytest_variables
%py3_requires pytest

%description -n python3-module-%oname
pytest-variables is a plugin for py.test that provides variables to
tests/fixtures as a dict via a JSON file specified on the command line.
%endif

%prep
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.4-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1-alt1.git20150716.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 29 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.git20150716
- Initial build for Sisyphus

