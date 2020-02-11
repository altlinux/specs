%define _unpackaged_files_terminate_build 1

%define oname sql

Name: python3-module-%oname
Version: 0.8
Release: alt2

Summary: Library to write SQL queries
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/python-sql/
BuildArch: noarch

# https://github.com/Tyba/python-sql.git
Source0: https://pypi.python.org/packages/c5/4b/c8c15049bc683428c8248eb37a0f22e9ad20e7853f8215ca8deb023ed689/python-%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3
%py3_provides %oname


%description
python-sql is a library to write SQL queries in a pythonic way.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
python-sql is a library to write SQL queries in a pythonic way.

This package contains tests for %oname.

%prep
%setup -q -n python-%{oname}-%{version}

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc CHANGELOG README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Tue Feb 11 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.8-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.1-alt1.git20140911.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.1-alt1.git20140911
- Initial build for Sisyphus

