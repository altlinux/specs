%define _unpackaged_files_terminate_build 1
%define oname jsonquery

%def_with python3

Name: python-module-%oname
Version: 1.0.2
Release: alt2.1
Summary: Basic json -> sqlalchemy query builder
License: MIT
Group: Development/Python
BuildArch: noarch
Url: https://pypi.python.org/pypi/jsonquery/

# https://github.com/numberoverzero/jsonquery.git
Source: %{oname}-%{version}.tar.gz

BuildRequires: python-devel python-module-setuptools
BuildRequires: python-modules-json python-module-SQLAlchemy
BuildRequires: python-modules-sqlite3
BuildRequires: python-module-pytest
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-setuptools
BuildRequires: python3-module-SQLAlchemy
BuildRequires: python3-modules-sqlite3
BuildRequires: python3-module-pytest
%endif

%py_provides %oname
%py_requires json sqlalchemy

%description
Basic json -> sqlalchemy query builder.

%if_with python3
%package -n python3-module-%oname
Summary: Basic json -> sqlalchemy query builder
Group: Development/Python3
%py3_provides %oname
%py3_requires json sqlalchemy

%description -n python3-module-%oname
Basic json -> sqlalchemy query builder.
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
python setup.py test

%if_with python3
pushd ../python3
python3 setup.py test
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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.2-alt2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Tue Dec 19 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.2-alt2
- Fixed build.

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.0.2-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.1-alt1.git20150117.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20150117
- Initial build for Sisyphus

