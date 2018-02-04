%define _unpackaged_files_terminate_build 1
%define oname sql

%def_with python3

Name: python-module-%oname
Version: 0.8
Release: alt1.1
Summary: Library to write SQL queries
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/python-sql/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/Tyba/python-sql.git
Source0: https://pypi.python.org/packages/c5/4b/c8c15049bc683428c8248eb37a0f22e9ad20e7853f8215ca8deb023ed689/python-%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
python-sql is a library to write SQL queries in a pythonic way.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
python-sql is a library to write SQL queries in a pythonic way.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Library to write SQL queries
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
python-sql is a library to write SQL queries in a pythonic way.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
python-sql is a library to write SQL queries in a pythonic way.

This package contains tests for %oname.

%prep
%setup -q -n python-%{oname}-%{version}

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
%doc CHANGELOG README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20140911
- Initial build for Sisyphus

