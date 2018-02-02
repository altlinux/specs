%define _unpackaged_files_terminate_build 1
%define oname sqlalchemy_monetdb

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 1.0.0
Release: alt1.1
Summary: SQLAlchemy dialect for MonetDB
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/sqlalchemy_monetdb/

Source: %oname-%version.tar

BuildRequires: python-devel python-module-setuptools python-module-pytest-runner
BuildRequires: python-module-monetdb python-module-SQLAlchemy-tests
BuildRequires: python-module-nose python-module-mock
BuildRequires: python-module-coverage python-module-pbr python-module-pytest python-module-unittest2
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools python3-module-pytest-runner
BuildRequires: python3-module-monetdb python3-module-SQLAlchemy-tests
BuildRequires: python3-module-nose python3-module-mock
BuildRequires: python3-module-coverage python3-module-html5lib python3-module-pbr python3-module-pytest python3-module-unittest2
%endif

%py_provides %oname
%py_requires pymonetdb sqlalchemy

%description
MonetDB dialect for SQLAlchemy.

%package -n python3-module-%oname
Summary: SQLAlchemy dialect for MonetDB
Group: Development/Python3
%py3_provides %oname
%py3_requires pymonetdb sqlalchemy

%description -n python3-module-%oname
MonetDB dialect for SQLAlchemy.

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
python setup.py test
python run_tests.py
%if_with python3
pushd ../python3
python3 setup.py test
python3 run_tests.py
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.0-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Jan 25 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.0-alt1
- Updated to upstream version 1.0.0.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.9.3-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.9-alt1.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9-alt1
- Initial build for Sisyphus

